---
comments: False
layout: default
title: Computer Science Principles Create Performance Task - Matrix Calculator
permalink: student/matrix/
---

<html lang="en">
<head>
<title>Matrix Calculator</title>
    <!-- Styles for the webpage -->
    <style>
        /* header {
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
        } */
        #upper {
            margin-left: auto;
            margin-right: auto;
            display: flex;
            flex-flow: row wrap;
            width: 40em;
            height: 35em;
            /* background: #FAFAFA; */
            align-items: center;
            justify-content: center;
        }
        #matrix1, #matrix2, #matrix3{
            order: 1;
            width: 12em;
            height: 40%;
        }
        #operations {
            order: 1;
            width: 5em;
            height: 40%;
            display: flex;
            flex-flow: row wrap;
            align-items: center;
            justify-content: center;
        }
        .operation {
            width: 5em;
            height: 10%
        }
        .parent {
            display: flex;
            flex-flow: row wrap;
            width: 12em;
            background: #FAFAFA;
            align-items: center;
            justify-content: center;
        }
        .title {
            order: 1;
            font-family: "Times New Roman", serif;
            width: 9em;
            height: 10%;
            text-align: center;
        }
        .m1r1, .m2r1, .m3r1 {
            order: 2;
            width: 3em;
            height: 10%;
            text-align: center;
        }
        .m1r2, .m2r2, .m3r2 {
            order: 3;
            width: 3em;
            height: 10%;
            text-align: center;
        }
        .m1r3, .m2r3, .m3r3 {
            order: 4;
            width: 3em;
            height: 10%;
            text-align: center;
        }
        .functions {
            order: 5;
            width: 9em;
            height: 40%;
            display: flex;
            flex-flow: row wrap;
            align-items: center;
            justify-content: center;
        }
        .function {
            width: 8em;
            height: 10%;
            border-radius: 2em;
        }
        #console {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 40%;
            height: 50%;
        }
    </style>
</head>
<body>
	<div id="upper">
		<div id="matrix1" class="parent">
			<h1 class="title">Matrix A</h1>
			<input class="m1r1" id="1.1.1" type="text" value="1"/>
			<input class="m1r1" id="1.1.2" type="text" value="2"/>
			<input class="m1r1" id="1.1.3" type="text" value="3"/>
			<input class="m1r2" id="1.2.1" type="text" value="4"/>
			<input class="m1r2" id="1.2.2" type="text" value="5"/>
			<input class="m1r2" id="1.2.3" type="text" value="6"/>
			<input class="m1r3" id="1.3.1" type="text" value="7"/>
			<input class="m1r3" id="1.3.2" type="text" value="8"/>
			<input class="m1r3" id="1.3.3" type="text" value="9"/>	
		</div>
		<div id="operations">
			<input class="operation" type="button" value="A x B" onclick="getvalues()"/>
			<input class="operation" type="button" value="A + B" onclick="addmatrix()"/>
			<input class="operation" type="button" value="A - B" onclick="getvalues()"/>
		</div>
		<div id="matrix2" class="parent">
			<h1 class="title">Matrix B</h1>
			<input class="m2r1" id="2.1.1" type="text" value="9"/>
			<input class="m2r1" id="2.1.2" type="text" value="8"/>
			<input class="m2r1" id="2.1.3" type="text" value="7"/>
			<input class="m2r2" id="2.2.1" type="text" value="6"/>
			<input class="m2r2" id="2.2.2" type="text" value="5"/>
			<input class="m2r2" id="2.2.3" type="text" value="4"/>
			<input class="m2r3" id="2.3.1" type="text" value="3"/>
			<input class="m2r3" id="2.3.2" type="text" value="2"/>
			<input class="m2r3" id="2.3.3" type="text" value="1"/>
		</div>
        <div id="matrix3" class="parent">
			<h1 class="title">Result</h1>
			<input class="m3r1" id="3.1.1" type="text" value="0"/>
			<input class="m3r1" id="3.1.2" type="text" value="0"/>
			<input class="m3r1" id="3.1.3" type="text" value="0"/>
			<input class="m3r2" id="3.2.1" type="text" value="0"/>
			<input class="m3r2" id="3.2.2" type="text" value="0"/>
			<input class="m3r2" id="3.2.3" type="text" value="0"/>
			<input class="m3r3" id="3.3.1" type="text" value="0"/>
			<input class="m3r3" id="3.3.2" type="text" value="0"/>
			<input class="m3r3" id="3.3.3" type="text" value="0"/>
		</div>
	</div>
<script>
var matrix1
var matrix2
var matrix3
function getvalues() {
    // console.log("getting values")
    var matrix1 = []
    var matrix2 = []
    var matrix3 = []
    var temp
    var temp2
    for (let i = 1; i < 4; i++) {
        for (let j = 1; j < 4; j++) {
            var temp1 = []
            for (let k = 1; k < 4; k++) {
                temp = document.getElementById(""+i+"."+j+"."+k+"").value
                temp1.push(temp)
            }
            if (i==1) {
                matrix1.push(temp1)
            }
            else if (i==2) {
                matrix2.push(temp1)
            }
            else if (i==3) {
                matrix3.push(temp1)
            }
        }
    }
    // console.log("got values")
    // console.log(matrix3)
    return matrix3
}
function addmatrix() {
    var temp3
    console.log("adding")
    console.log(getvalues())
}
getvalues()

</script>
</body>