---
toc: false
comments: false
layout: default
title: Binary Blackjack
description: This is a blackjack game where all values are in binary
type: hacks
courses: { compsci: {week: 13} }
---

<html lang="en">
<head>
    <!-- Meta tags for character set and viewport -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Title of the webpage -->
    <title>Binary Blackjack</title>
    <!-- Styles for the webpage -->
    <style>
        body {
            width: 100%;
            height: 100%;
            margin: 0em 0%;
            background-color: #8ec1da;
            background-image: url("https://static.vecteezy.com/system/resources/previews/016/124/733/non_2x/poker-and-casino-playing-card-black-background-vector.jpg");
            background-position: center bottom;
        }
        .title {
            position: fixed;
            top: 10%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 80px;
            font-family: Verdana, sans-serif;
        }
        .playercardsbox, .dealercardsbox, .playerscorebox, .dealerscorebox {
            position: fixed;
            top: 72%;
            transform: translate(-50%, -50%);
            background-color: rgba(128, 128, 128, 0.5);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            font-size: 30px;
            font-family: Verdana, sans-serif;
            overflow-y: auto; /*Enable vertical scroll if needed */
        }
        .playercardsbox, .playerscorebox {
            left: 30%;
            max-height: 100%; /* Allow it to grow to the full height of the viewport*/
        }
        .dealercardsbox, .dealerscorebox {
            left: 70%;
            max-height: 100%;
        }
        .playerscorebox, .dealerscorebox {
            position: fixed;
            top: 78%;
            transform: translate(-50%, -50%);
            background-color: rgba(128, 128, 128, 0.5);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            font-size: 30px;
            font-family: Verdana, sans-serif;
        }
        .result {
            position: fixed;
            top: 37%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 150px;
            font-family: Verdana, sans-serif;
            color: red;
            display: none;
        }
        .hitbutton, .standbutton, .resetbutton {
            position: fixed;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: rgba(38, 152, 255, 0.5);
            border: none;
            width: 10%;
            height: 10%;
            border-radius: 10px;
            font-size: 30px;
            font-family: Verdana, sans-serif;
        }
        .hitbutton:hover, .standbutton:hover, .resetbutton:hover {
            background-color: rgba(38, 152, 255, 0.3) !important;
        }
        .standbutton {
            top: 72%
        }
        .hitbutton {
            top: 60%
        }
        .resetbutton {
            top: 84%;
            display: block
        }
    </style>
</head>

<body>
<div>
    <!-- Title of the game -->
    <h1 class="title">Binary Blackjack</h1>
</div>
<div class="playercardsbox" id="playercardsbox">
    <!-- Player's card box with placeholder text -->
    <p><strong>Player Cards:</strong></p>
</div>
<div class="dealercardsbox" id="dealercardsbox">
    <!-- Dealer's card box with placeholder text -->
    <p><strong>Dealer Cards:</strong></p>
</div>
<!--
<div class="playerscorebox" id="playerscorebox">
    <p><strong>Player Score:</strong><br><span id="playerscore"></span></p>
</div>
<div class="dealerscorebox" id="dealerscorebox">
    <p><strong>Dealer Score:</strong><br><span id="dealerscore"></span></p>
</div>
-->
<div class="result" id="result">Bust!</div>
<div>
    <!-- Buttons for player actions -->
    <button class="hitbutton" onclick="getplayercard()">Hit</button>
    <button class="standbutton" onclick="stand()">Stand</button>
    <button class="resetbutton" onclick="resetGame()">Reset</button>
</div>

<script>
    // Game variables
    var cardcounter = 52;
    var playercardcounter = 0;
    var dealercardcounter = 0;
    var playerBusted = false;

    // Function to generate a deck of cards
    function generatecards() {
        var numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"];
        var suits = ["♠︎", "♥︎", "♦︎", "♣︎"];
        var cards = [];
        for (let i = 0; i < numbers.length; i++) {
            for (let j = 0; j < suits.length; j++) {
                cards.push(numbers[i] + suits[j]);
            }
        }
        return cards;
    }

    // Initialize the deck
    var deck = generatecards();

    // Function to deal initial cards to the player
    function playercards() {
        // Generate random indices for two cards
        var num1 = Math.floor(Math.random()*52);
        var num2 = Math.floor(Math.random()*51);
        // Convert cards to binary and remove them from the deck
        var card1 = cardtobinary(deck[num1]);
        deck.splice(num1, 1);
        cardcounter -= 1;
        var card2 = cardtobinary(deck[num2]);
        deck.splice(num2, 1);
        cardcounter -= 1;
        // Display player's cards and calculate the score
        var card1Element = document.getElementById("playercardsbox");
        card1Element.innerHTML += card1 + "<br>";
        card1Element.innerHTML += card2 + "<br>";
        playercardcounter = 2;
        calculatePlayerScore();
    }

    // Function to deal initial cards to the dealer
    function dealercards() {
        // Generate random indices for two cards
        var num1 = Math.floor(Math.random()*50);
        var num2 = Math.floor(Math.random()*49);
        // Convert cards to binary and remove them from the deck
        var dealercard1 = cardtobinary(deck[num1]);
        deck.splice(num1, 1);
        cardcounter -= 1;
        var dealercard2 = cardtobinary(deck[num2]);
        deck.splice(num2, 1);
        cardcounter -= 1;
        // Display dealer's cards and calculate the score
        var dealercard1Element = document.getElementById("dealercardsbox");
        dealercard1Element.innerHTML += dealercard1 + "<br>";
        dealercard1Element.innerHTML += dealercard2 + "<br>";
        dealercardcounter = 2;
        calculateDealerScore();
    }

    // Function to calculate the player's score
    function calculatePlayerScore() {
        // Get player's cards from the HTML content
        var playerCards = document.getElementById("playercardsbox").textContent;
        // Extract card values from the text content
        var cardValues = playerCards.match(/\d+|A|J|Q|K/g);
        var sum = 0;

        if (cardValues) {
            // Calculate the sum of card values
            for (var i = 0; i < cardValues.length; i++) {
                var value = 0;
                // Assign values to cards (considering Ace as 11)
                if (cardValues[i] === "A") {
                    value = 11;
                } else if (["J", "Q", "K"].includes(cardValues[i])) {
                    value = 10;
                } else {
                    value = parseInt(cardValues[i]);
                }
                sum += todecimal(value);
            }
        }
        // Adjust for Ace if needed
        for (var i = 0; i < cardValues.length; i++) {
            if (cardValues[i] === "A" && sum > 21) {
                sum -= 10;
            }
        }
        // Return the calculated score
        return sum;
    }

    // Function to calculate the dealer's score
    function calculateDealerScore() {
        // Get dealer's cards from the HTML content
        var dealerCards = document.getElementById("dealercardsbox").textContent;
        // Extract card values from the text content
        var cardValues = dealerCards.match(/\d+|A|J|Q|K/g);
        var sum = 0;

        if (cardValues) {
            // Calculate the sum of card values
            for (var i = 0; i < cardValues.length; i++) {
                var value = 0;
                // Assign values to cards (considering Ace as 11)
                if (cardValues[i] === "A") {
                    value = 11;
                } else if (["J", "Q", "K", "10"].includes(cardValues[i])) {
                    value = 10;
                } else {
                    value = parseInt(cardValues[i]);
                }
                sum += todecimal(value);
            }
        }
        // Adjust for Ace if needed
        for (var i = 0; i < cardValues.length; i++) {
            if (cardValues[i] === "A" && sum > 21) {
                sum -= 10;
            }
        }
        // Return the calculated score
        return sum;
    }

    // Function to draw a card for the player
    function getplayercard() {
        // Check if the player is not busted
        if (!playerBusted) {
            // Generate a random card index
            var tempnum = Math.floor(Math.random() * cardcounter);
            var temp = deck[tempnum];
            // Convert the card to binary and update the deck
            var card = cardtobinary(temp);
            deck.splice(tempnum, 1);
            cardcounter -= 1;
            // Display the drawn card
            var cardElement = document.getElementById("playercardsbox");
            cardElement.innerHTML += card + "<br>";
            playercardcounter += 1;
            // Calculate the player's score and handle bust
            var playerScore = calculatePlayerScore();
            if (playerScore > 21) {
                handlePlayerBust();
            }
        }
    }

    // Function to handle the player bust
    function handlePlayerBust() {
        playerBusted = true;
        document.getElementById("result").innerText = "Bust!";
        document.getElementById("result").style.display = "block";
    }

    // Function to handle player's stand action
    function stand() {
        // Check if the player is not busted
        if (!playerBusted) {
            // Check if the dealer has a higher score and compare scores
            if (calculateDealerScore() > calculatePlayerScore()) {
                compareScores();
            }
            // Draw cards for the dealer until reaching a score of 17 or higher
            while (calculateDealerScore() < 17) {
                getdealercard();
            }
        }
        // Compare scores after the dealer's final draw
        compareScores();
    }

    // Function to draw a card for the dealer
    function getdealercard() {
        // Generate a random card index
        var tempnum = Math.floor(Math.random() * cardcounter);
        var card = cardtobinary(deck[tempnum]);
        // Remove the drawn card from the deck
        deck.splice(tempnum, 1);
        cardcounter -= 1;
        // Display the drawn card for the dealer
        var cardElement = document.getElementById("dealercardsbox");
        cardElement.innerHTML += card + "<br>";
        // Calculate the dealer's score
        calculateDealerScore();
    }

    // Function to compare the final scores and determine the winner
    function compareScores() {
        var playerScore = calculatePlayerScore();
        var dealerScore = calculateDealerScore();
        // Check for bust, win, tie, or loss
        if (playerScore > 21) {
            handlePlayerBust();
        } else if (dealerScore > 21 || playerScore > dealerScore) {
            document.getElementById("result").innerText = "You Win!";
            document.getElementById("result").style.display = "block";
        } else if (playerScore === dealerScore) {
            document.getElementById("result").innerText = "It's a Tie!";
            document.getElementById("result").style.display = "block";
        } else {
            document.getElementById("result").innerText = "You Lose!";
            document.getElementById("result").style.display = "block";
        }
    }

    // Function to reset the game
    function resetGame() {
        // Reset game variables and display
        cardcounter = 52;
        playercardcounter = 0;
        dealercardcounter = 0;
        document.getElementById("playercardsbox").innerHTML = "<p><strong>Player Cards:</strong></p>";
        document.getElementById("dealercardsbox").innerHTML = "<p><strong>Dealer Cards:</strong></p>";
        //document.getElementById("playerscore").innerText = "";
        //document.getElementById("dealerscore").innerText = "";
        document.getElementById("result").style.display = "none";
        playerBusted = false;
        // Regenerate the deck and deal initial cards
        deck = generatecards();
        playercards();
        dealercards();
    }
    function cardtobinary(decimalnum) {
        // Extract the card value and suit from the input
        var value = decimalnum;

        // Check if the card is an Ace ('A') or a face card (['J', 'Q', 'K', '10'])
        if (decimalnum[0] === "A") {
            value = 11;
        } else if (["J", "Q", "K", "10"].includes(decimalnum[0])) {
            value = 10;
        }
        // Determine the suit of the card
        if (decimalnum[1] == 0) {
            var suit = decimalnum[2];
        } else {
            var suit = decimalnum[1];
        }
        // Convert the card value to a decimal number
        var decimalNumber = parseInt(value);
        var decimaltemp = parseInt(value);
        // Convert the decimal number to binary using bitwise operations
        var binaryResult = "";
        while (decimalNumber > 0) {
            var remainder = decimalNumber % 2;
            binaryResult = remainder + binaryResult;
            decimalNumber = Math.floor(decimalNumber / 2);
        }
        // Handle special case when the card value is 0
        if (decimaltemp == 0) {
            binaryResult = "0";
        }
        // Ensure the binary representation is 5 digits long and append the suit
        var output = String(binaryResult) + suit;
        while (output.length != 5) {
            output = "0" + output;
        }
        return output;
    }

    function tobinary(decimalnum) {
        // Convert decimal to binary using bitwise operations
        var decimalNumber = parseInt(decimalnum);
        var decimaltemp = parseInt(decimalnum);
        var binaryResult = "";
        while (decimalNumber > 0) {
            var remainder = decimalNumber % 2;
            binaryResult = remainder + binaryResult;
            decimalNumber = Math.floor(decimalNumber / 2);
        }
        // Handle special case when the decimal number is 0
        if (decimaltemp == 0) {
            binaryResult = "0";
        }
        return binaryResult;
    }

    function cardtodecimal(binarynum) {
        // Implement this function if needed
    }

    function todecimal(binarynum) {
        // Convert binary to decimal using the parseInt function
        var decimalResult = parseInt(binarynum, 2);
        return decimalResult;
    }

// Function calls to initialize the game
playercards();
dealercards();
calculatePlayerScore();
calculateDealerScore();
