import json
import requests
import os
import re
from bs4 import BeautifulSoup as bs
from ankigodotcss import *

def invoke(action, **params):
    request_json = json.dumps({
        'action': action,
        'version': 6,
        'params': params
    })
    response = requests.post('http://localhost:8765', data=request_json)
    print(response.text)
    return json.loads(response.text)

def create_deck(deck_name):
    return invoke('createDeck', deck=deck_name)

def add_note(deck_name: str, model_name: str, fields: dict, styling: str = None):
    note = {
        'deckName': deck_name,
        'modelName': model_name,
        'fields': fields,
        'options': {
            'allowDuplicate': False
        },
        "styling": styling,
        'tags': ["Godot", "Godot Docs"]
    }
    return invoke('addNote', note=note)

def get_id_html(text, id="description"):
    output = ""
    for i, line, in enumerate(text.splitlines()):
        if f'id="{id}"' in line:
            j = i + 1
            output += "{{c1::" + text.splitlines()[j] + "}}" + "\n" 
            j += 1
            while text.splitlines()[j] != "</section>" and j < len(text.splitlines()):
                output += text.splitlines()[j] + "\n"
                j += 1
    return output  


def get_file_name(file, text=None):
    cleaned = file.split("_")[1].split(".")[0]
    if text is None:
        return cleaned

    for i, line, in enumerate(text.splitlines()):
        if cleaned in line.lower():
            pattern = re.compile(rf"{cleaned}", re.IGNORECASE)
            match = re.search(pattern, line)

            return match.group()

all_ids = ['description', 'constants', 'annotations', 'method-descriptions', 'properties', 'enumerations', 'property-descriptions', 'constructor-descriptions', 'operator-descriptions', 'signals', 'theme-property-descriptions']
godot_url = "https://docs.godotengine.org/en/stable/"


def load_soup(path):
    # soup = bs(open(path), 'html.parser')
    soup = bs(requests.get(url=path).text, "html.parser")
    return soup

def get_content(soup):
    content = soup.find("div", {"itemprop": "articleBody"})
    return content
    
def get_sections(content):
    sections = content.section
    return sections

def get_new_name(sections):
    new_name = sections.h1.text[:-1]
    return new_name

def clean_section(section):
    text = (repr(section).replace("¶", ""))
    text = text.splitlines()
    cleaned = ""
    for line in text:
        cleaned += line.replace("../..", godot_url).replace("class_%40", godot_url + "classes/class_%40")
    return bs(cleaned, "html.parser")

def make_single_godot_card(all_content_sections, deck_name):
    for section in all_content_sections:
        if section.get("id") in all_ids:
            section_copy = section
            header = section_copy.find("h2")
            header["id"] = "top-id"
            header_copy = repr(header).replace("¶", "")
            header.decompose()  
            cleaned = clean_section(section_copy)
            # field_header = f"<h2>{header.text}</h2>"
            field = {"Front" :  f"{header_copy}" + "\n" + repr(cleaned)}
            # add_note(deck_name, 'Basic', fields=field, styling=style)


def make_godot_cards(files, path, deck_name):  
    sections = get_sections(
        content= get_content(
            soup= load_soup(
                path="https://docs.godotengine.org/en/stable/tutorials/2d/2d_meshes.html"
            )
        )
    )

    cleaned = clean_section(sections)
    all_content_sections = cleaned.find_all("section")
    # temporary until I get around to making this more automatic
    deck_name = "Technology::GodotTutorials::" + "Rendering" + "::" + "2D meshes"
    create_deck(deck_name)
    for section in all_content_sections:
        section_copy = section
        header = section_copy.find("h2")
        if header:
            header["id"] = "top-id"
            header_copy = repr(header).replace("¶", "")
    content = ""
    for item in all_content_sections:
        content += repr(item) + "\n"
    # print(content)
    field = {"Front" :  f"{content}"}
    add_note(deck_name, "Basic", fields=field, styling=style)


    return 
    for i, file in enumerate(files):
        new_path = os.path.join(path, file)
        sections = get_sections(
            content= get_content(
                soup= load_soup(
                    path=new_path
                )
            )
        )
        new_name = get_new_name(sections)
        print(new_name)
        all_content_sections = sections.find_all("section")
        new_deck = f"{deck_name}::{new_name}"
        create_deck(new_deck)
        make_single_godot_card(all_content_sections, new_deck)

def main():
    
    deck_name = "Technology::Godot_Docs"
    path = "/home/brad/Documents/godot-docs-html-master/classes"

    files = sorted(os.listdir(path))
    make_godot_cards(files,path, deck_name)

if __name__ == "__main__":
    main()
