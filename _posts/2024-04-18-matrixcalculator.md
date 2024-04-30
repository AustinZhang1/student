---
layout: default
title: Matrix Calculator
permalink: matrix/
---
<html lang="en">
<head>
<title>Matrix Calculator</title>
    <style>
        body {
            width: 100%;
            height: 100%;
            background-image: linear-gradient(#020e21,#0d473e);
        }
        .header {
            margin-top: 2em;
            margin-bottom: auto;
            margin-left: auto;
            margin-right: auto;
            font-family: Courier, monospace;
            text-align: center;
            font-size: 5em;
            color: blue;
        }
        #upper {
            border-radius: 25px;
            margin-left: auto;
            margin-right: auto;
            margin-top: 4%;
            margin-bottom: auto;
            display: flex;
            flex-flow: row wrap;
            width: 35%;
            height: 35em;
            align-items: center;
            justify-content: center;
        }
        #matrix1, #matrix2, #matrix3{
            order: 1;
            width: 12em;
            height: 40%;
            background: linear-gradient(#c4c4c4,#d6d6d6);
        }
        #operations {
            margin-top: 3%;
            order: 1;
            width: 15em;
            height: 40%;
            display: flex;
            flex-flow: row wrap;
            align-items: center;
            justify-content: center;
        }
        .operation {
            width: 7em;
            height: 12%;
            font-family: Courier, monospace;
            font-size: 1.3em;
            font-weight: bold;
        }
        .parent {
            margin-bottom: 2%;
            display: flex;
            flex-flow: row wrap;
            width: 18em;
            background: #FAFAFA;
            align-items: center;
            justify-content: center;
            border-radius: 6px;
        }
        .title {
            order: 1;
            font-family: Courier, monospace;
            width: 9em;
            height: 10%;
            text-align: center;
        }
        .m1r1, .m2r1, .m3r1 {
            order: 2;
            width: 3em;
            height: 10%;
            border-radius: 5px;
            text-align: center;
            font-family: Courier, monospace;
            font-weight: bold;
        }
        .m1r2, .m2r2, .m3r2 {
            order: 3;
            width: 3em;
            height: 10%;
            border-radius: 5px;
            text-align: center;
            font-family: Courier, monospace;
            font-weight: bold;
        }
        .m1r3, .m2r3, .m3r3 {
            order: 4;
            width: 3em;
            height: 10%;
            border-radius: 5px;
            text-align: center;
            font-family: Courier, monospace;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div>
        <h1 class="header">3x3 Matrix Calculator</h1>
    </div>
    <div id="upper">
        <div id="matrix1" class="parent">
            <h1 class="title">MATRIX A</h1>
            <input class="m1r1" id="1.1.1" type="number" value="0"/>
            <input class="m1r1" id="1.1.2" type="number" value="0"/>
            <input class="m1r1" id="1.1.3" type="number" value="0"/>
            <input class="m1r2" id="1.2.1" type="number" value="0"/>
            <input class="m1r2" id="1.2.2" type="number" value="0"/>
            <input class="m1r2" id="1.2.3" type="number" value="0"/>
            <input class="m1r3" id="1.3.1" type="number" value="0"/>
            <input class="m1r3" id="1.3.2" type="number" value="0"/>
            <input class="m1r3" id="1.3.3" type="number" value="0"/>
        </div>
        <div id="operations">
            <input class="operation" type="button" value="A x B" onclick="operations('multiply')"/>
            <input class="operation" type="button" value="A + B" onclick="operations('add')"/>
            <input class="operation" type="button" value="A - B" onclick="operations('subtract')"/>
            <input class="operation" type="button" value="RESET" onclick="reset()"/>
        </div>
        <div id="matrix2" class="parent">
            <h1 class="title">MATRIX B</h1>
            <input class="m2r1" id="2.1.1" type="number" value="0"/>
            <input class="m2r1" id="2.1.2" type="number" value="0"/>
            <input class="m2r1" id="2.1.3" type="number" value="0"/>
            <input class="m2r2" id="2.2.1" type="number" value="0"/>
            <input class="m2r2" id="2.2.2" type="number" value="0"/>
            <input class="m2r2" id="2.2.3" type="number" value="0"/>
            <input class="m2r3" id="2.3.1" type="number" value="0"/>
            <input class="m2r3" id="2.3.2" type="number" value="0"/>
            <input class="m2r3" id="2.3.3" type="number" value="0"/>
        </div>
        <div id="matrix3" class="parent">
            <h1 class="title">RESULT</h1>
            <input class="m3r1" id="3.1.1" type="number" value="" readonly/>
            <input class="m3r1" id="3.1.2" type="number" value="" readonly/>
            <input class="m3r1" id="3.1.3" type="number" value="" readonly/>
            <input class="m3r2" id="3.2.1" type="number" value="" readonly/>
            <input class="m3r2" id="3.2.2" type="number" value="" readonly/>
            <input class="m3r2" id="3.2.3" type="number" value="" readonly/>
            <input class="m3r3" id="3.3.1" type="number" value="" readonly/>
            <input class="m3r3" id="3.3.2" type="number" value="" readonly/>
            <input class="m3r3" id="3.3.3" type="number" value="" readonly/>
        </div>
    </div>
<script>
var matrix1 = [[],[],[]]
var matrix2 = [[],[],[]]
var matrix3 = [[],[],[]]
function getmatrix(matrixnumber) { // This function 
    matrixtemp = [[],[],[]]
    var temp
        for (let j = 1; j < 4; j++) {
            var temp1 = []
            for (let k = 1; k < 4; k++) {
                temp = document.getElementById(""+matrixnumber+"."+j+"."+k+"").value
                temp1.push(temp)
            }
            matrixtemp[j-1]=temp1
        }
    return matrixtemp
}
function operations(operation) {
    var alert = false
    for (let i = 1; i < 3; i++) {
        for (let j = 1; j < 4; j++) {
            for (let k = 1; k < 4; k++) {
                if (isNaN(parseFloat(document.getElementById(""+i+"."+j+"."+k+"").value))) {
                    window.alert("Please Enter a Number for Every Space")
                    alert = true
                }
            }
        }
    }
    if (!alert) {
        if (operation == "add") {
            addmatrix()
        }
        else if (operation == "subtract") {
            subtractmatrix()
        }
        else if (operation == "multiply") {
            multiplymatrix()
        }
    }
}
function addmatrix() {
    var m1 = getmatrix(1)
    var m2 = getmatrix(2)
    var temp
    for (let i = 1; i < 4; i++) {
        for (let j = 1; j < 4; j++) {
            document.getElementById("3."+i+"."+j+"").value = parseFloat(m1[i-1][j-1]) + parseFloat(m2[i-1][j-1])
        }
    }
}
function subtractmatrix() {
    var m1 = getmatrix(1)
    var m2 = getmatrix(2)
    var temp
    for (let i = 1; i < 4; i++) {
        for (let j = 1; j < 4; j++) {
            document.getElementById("3."+i+"."+j+"").value = parseFloat(m1[i-1][j-1]) - parseFloat(m2[i-1][j-1])
        }
    }
}
function multiplymatrix() {
    var m1 = getmatrix(1)
    var m2 = getmatrix(2)
    for (let a = 0; a < 3; a++) {
        for (let b = 0; b < 3; b++) {
            document.getElementById("3."+(a+1)+"."+(b+1)+"").value = parseFloat(m1[a][0]) * parseFloat(m2[0][b]) + parseFloat(m1[a][1]) * parseFloat(m2[1][b]) + parseFloat(m1[a][2]) * parseFloat(m2[2][b])
        }
    }
}
function reset() {
    for (let i = 1; i < 4; i++) {
        for (let j = 1; j < 4; j++) {
            document.getElementById("1."+i+"."+j+"").value = 0
            document.getElementById("2."+i+"."+j+"").value = 0
            document.getElementById("3."+i+"."+j+"").value = ""
        }
    }
}
</script>
</body>
</html>