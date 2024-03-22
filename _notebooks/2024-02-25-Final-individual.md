---
toc: False
comments: True
layout: post
title: Individual Final CPT 
description: CSP Tri 2 Final 
courses: { compsci: {week: 18} }
type: tangibles
---

# Project Overview: 
## ByteJam: Austin, Saaras, Eric, Sri, Cayden 

Game website with multiple games of different genres. 

## My Feature: 

The Casino. A series of games that is an online 'casino' with fake money. The user can pick between blackjack, baccarat, slot machine, or poker to play, and can bet their virtual money on the outcome of the game. In all the games, the player plays against a virtual banker, or another player in poker, and all of the logic is cleverly coded in javascript. This game connects with the global leaderboard through betting systems and randomized cards/spins.

math question gets displayed each round. The User answers the math question by submitting the answer in the answer box. If the user answers the question correctly, two dice are rolled, and the user moves forward on a board based on that roll. The board has different boxes/steps with different values set to each box. The user plays against the AI, who always rolls after the users turn. Each step/box the user lands on gives or takes differing set amounts of money. The player who gets to 500$ first wins. 

[Collegeboard Requirements](https://apcentral.collegeboard.org/media/pdf/ap-csp-student-task-directions.pdf)

## Component A: Program Code 

| Requirements | Completed | 
| --------------- | -----------------| 
| Instructions for input from the user (including user actions that trigger events) | Allow input from user through an input box  ![CodePic](https://media.discordapp.net/attachments/974516458300256316/1211222389736738876/input.png?ex=65ed69c1&is=65daf4c1&hm=26e1794eeb3ccd6a145879212014f5550f4096d2b4954cf0ba8730fd0554c128&=&format=webp&quality=lossless&width=2700&height=156) ---------------- ![CodePic](https://media.discordapp.net/attachments/974516458300256316/1211222389463973948/inputinstructions.png?ex=65ed69c1&is=65daf4c1&hm=a55a51fab4574540f4c855649afe34d13a964ea7539146dab9aa1dd662b83e8f&=&format=webp&quality=lossless&width=798&height=1306)  |
| Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the program’s purpose | This code assigns a specific price value to each position on the game board. For instance, the second item in the list (1:100) corresponds to the second box on the visual board, which is valued at 100. These values align with the visual representation of the board but are primarily used for calculations and algorithms rather than visual display purposes.  ![CodePic](https://media.discordapp.net/attachments/974516458300256316/1211222387861758002/list.png?ex=65ed69c0&is=65daf4c0&hm=eb9299bdf9bc6a28ebce7d5b0fe0091944633dabaff0ba6488ff250021b8f494&=&format=webp&quality=lossless&width=872&height=1306) | 
| One procedure that contributes to the program’s intended purpose, where you have defined: the procedure’s name, the return type (if necessary), one or more parameters | This code takes the parameters: Token, Steps in order to update player/ai position and total money. If the token is the player, then the steps given will update the playerposition, vice versa. It will also update and display the total amount of money the player/AI has. It also handles winning and losing. When playermoney/aimoney reaches 500, a notification will appear with either You win or You lose, and reset the game after. The submitanswer function mentioned above calls this procedure.  ![CodePic](https://media.discordapp.net/attachments/974516458300256316/1211222388184973342/procedure.png?ex=65ed69c0&is=65daf4c0&hm=0a40071a28e12eae8483c4ddd97e80f6c8913b835752ff2f0427894085ddcb49&=&format=webp&quality=lossless&width=1664&height=1306) |
| An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure | Selection: If/Else Statements, since the code is choosing to either move player and ai if the player answered correctly, or just move the ai if the player did not answer correctly. Iteration: SetTimeout Function, since it allows the program to repeat by moving the ai, and changing the displayed question while updating the display of who's turn it is after a delay. ![CodePic](https://media.discordapp.net/attachments/974516458300256316/1211222388474122350/calls.png?ex=65ed69c0&is=65daf4c0&hm=3f8dc064b318d2781ef69b730d51472ea75cb02080bb33863a898d5fecd0feaa&=&format=webp&quality=lossless&width=1916&height=1306) |
| Calls to your student-developed procedure | Calling move function. ![CodePic](https://media.discordapp.net/attachments/974516458300256316/1211222388474122350/calls.png?ex=65ed69c0&is=65daf4c0&hm=3f8dc064b318d2781ef69b730d51472ea75cb02080bb33863a898d5fecd0feaa&=&format=webp&quality=lossless&width=1916&height=1306) |
| Instructions for textual output based on input and program functionality | Textually inform user if they won/lost. ![CodePic](https://media.discordapp.net/attachments/974516458300256316/1211222388763791390/textual_output.png?ex=65ed69c0&is=65daf4c0&hm=82237624f81da02eae42c929bbbc16bad1849b7760d02e06fe660726fafac354&=&format=webp&quality=lossless&width=1544&height=752) |
| Instructions for visual output based on input and program functionality | Update position of player/ai on visual board. ![CodePic](https://media.discordapp.net/attachments/974516458300256316/1211222389082423356/visual_output.png?ex=65ed69c0&is=65daf4c0&hm=f5af7a71f35a1a1effcdf78d02d0edb4c31e0d0809a01170d19299f6ddaf7a57&=&format=webp&quality=lossless&width=2392&height=1306) |

## Component B: Video 

[Video Link](https://drive.google.com/file/d/15C9iKChv8fbQRyN_Z1NLMsFOUbKZYY-s/view?usp=sharing)

| Requirements | Completed | 
| --------------- | -----------------| 
| Input to your program | Y - Show Submit Answer into Answer Box |
| At least one aspect of the functionality of your program | Y - Show that Game Functions as Expected W/O Bugs |
| Output produced by your program | Y - Show Visual Movement, Display Steps Moved, Money Gained, Show Victory/Loss Notification |
| Your video may NOT contain: Any distinguishing information about yourself, Voice narration (though text captions are encouraged) | Y |
| Your video must be: Either .webm, .mp4, .wmv, .avi, or .mov format | Y - .mp4 File |
| No more than 1 minute in length | Y - 1 Minute Long |
| No more than 30MB in file size | Y - 28 MB|