---
toc: true
comments: false
layout: post
title: Simple Calculator 
description: This is a simple calculator in HTML
type: hacks
courses: {"compsci": {week: 1} }
---


<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Simple Calculator</title>
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        margin: 0;
        padding: 0;
    }
    .calculator {
        width: 300px;
        margin: 50px auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    input[type="text"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
    }
    button {
        width: 50px;
        height: 50px;
        font-size: 18px;
        margin: 5px;
    }
</style>
</head>
<body>
    <div class="calculator">
        <input type="text" id="result" readonly>
        <br>
        <button onclick="appendValue('1')">1</button>
        <button onclick="appendValue('2')">2</button>
        <button onclick="appendValue('3')">3</button>
        <button onclick="appendValue('+')">+</button>
        <br>
        <button onclick="appendValue('4')">4</button>
        <button onclick="appendValue('5')">5</button>
        <button onclick="appendValue('6')">6</button>
        <button onclick="appendValue('-')">-</button>
        <br>
        <button onclick="appendValue('7')">7</button>
        <button onclick="appendValue('8')">8</button>
        <button onclick="appendValue('9')">9</button>
        <button onclick="appendValue('*')">*</button>
        <br>
        <button onclick="appendValue('0')">0</button>
        <button onclick="clearResult()">C</button>
        <button onclick="calculate()">=</button>
        <button onclick="appendValue('/')">/</button>
    </div>

    <script>
        function appendValue(value) {
            document.getElementById('result').value += value;
        }

        function clearResult() {
            document.getElementById('result').value = '';
        }

        function calculate() {
            const resultField = document.getElementById('result');
            const expression = resultField.value;
            try {
                resultField.value = eval(expression);
            } catch (error) {
                resultField.value = 'Error';
            }
        }
    </script>
</body>
</html>