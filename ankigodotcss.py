style = """
:root {
  --main-bg-color: rgba(50, 70, 100);
	--secondary-color:  rgba(50, 100, 100);
	--blended-color: calc(var(--main-bg-color) + var(--secondary-color));
}

code {
	background-color: dark-grey;
}

.headerlink {
 background-color: var(--secondary-color);
}

.card {
    font-family: arial;
    font-size: 20px;
    // text-align: center;
    color: black;
    background-color: white;
}

#top-id {
 	background-color: rgba(30, 80, 80);
	padding: 20px;
	font-weight: bold;
	border-radius: 10px;
	box-shadow: inset 0 0 20px rgba(0,0,0);
	text-align: center;
}

#main {
	background-color: var(--main-bg-color);
}

img {
	
	border-color: green;
	border-solid: 5px solid;
	border-radius: 20px;
	box-shadow: inset 0 0 20px #0c0;

}

section {
    background-color: var(--secondary-color);
    color: white;
    //rgb(200, 100,200);
    padding: 10px;
    font-weight: bold;
    border-radius: 10px;
    box-shadow: inset 0 0 15px rgba(0,0,0);
    text-stroke: ;
    //text-shadow: rgb(0, 0, 0) 3px 0px 0px, rgb(0, 0, 0) 2.83487px 0.981584px 0px, rgb(0, 0, 0) 2.35766px 1.85511px 0px, rgb(0, 0, 0) 1.62091px 2.52441px 0px, rgb(0, 0, 0) 0.705713px 2.91581px 0px, rgb(0, 0, 0) -0.287171px 2.98622px 0px, rgb(0, 0, 0) -1.24844px 2.72789px 0px, rgb(0, 0, 0) -2.07227px 2.16926px 0px, rgb(0, 0, 0) -2.66798px 1.37182px 0px, rgb(0, 0, 0) -2.96998px 0.42336px 0px, rgb(0, 0, 0) -2.94502px -0.571704px 0px, rgb(0, 0, 0) -2.59586px -1.50383px 0px, rgb(0, 0, 0) -1.96093px -2.27041px 0px, rgb(0, 0, 0) -1.11013px -2.78704px 0px, rgb(0, 0, 0) -0.137119px -2.99686px 0px, rgb(0, 0, 0) 0.850987px -2.87677px 0px, rgb(0, 0, 0) 1.74541px -2.43999px 0px, rgb(0, 0, 0) 2.44769px -1.73459px 0px, rgb(0, 0, 0) 2.88051px -0.838247px 0px;
    //text-shadow: 1px 2px 15px black, 1px -1px 0 #000, -2px 1px 0 #000, 1px 1px 0, -3px -1px 0 #000, 2px 1px 0 #000, 3px //1px 0 #000;

    text-stroke: 6px 5px yellow;
}


pre{
	inline-size: 150;
 	white-space: pre-wrap;
	padding: 15px 25px 0px 25px;
	font-weight: bold;
	color: rgb(200,180,200);
	background-color: rgba(50, 50, 100);
	border-radius: 20px;
	text-stroke: 5px red;

	box-shadow: inset 0 0 20px #0c0;
}

.cloze {
	font-weight: bold
	color: blue;
	width: 500px;
 	height: 300px;
		 
}
.nightMode {
	color: black;
	height: 100px;	
	overflow: auto;

	text-stroke: 0 0 0 black; 
}

.nightMode .cloze {
    //position: absolute;
    color: rgb(10,10,70);
    font-size: 2em;
    font-weight: bold;
    //animation: shift 5s infinite;
    background-color: rgba(255, 255, 255, .25);
    //width: 500px;
    //height: 300px;
    border: 5px solid;
    padding: 1px 1px 4px 3px;
    border-radius: 15px;
    box-shadow: inset 0 0 20px yellow;

}


.nightMode .cloze a {
    color: blue;
    font-weight: bold;
    //animation: shift 5s infinite;
    background-color: rgba(255, 255, 255, .25);
    width: 500px;
    height: 300px;
}

@keyframes shift {
  0%, 100% {
    clip-path: polygon(0% 47%, 10% 48%, 33% 54%, 54% 60%, 70% 61%, 84% 59%, 100% 52%, 100% 100%, 0% 100%);
  }
}
"""
