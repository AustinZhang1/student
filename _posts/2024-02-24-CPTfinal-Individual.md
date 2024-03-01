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

The Casino. A series of four games: Baccarat, Blackjack, Poker, and a Slot Machine. Apart from Poker, which I am still working on, Baccarat, Blackjack, and the Slot machine all follow standard casino rules which I found online and implemented logic for in Javascript. The Games are also to be connected to the leaderboard for the final product to turn into Collegeboard.

[Collegeboard Requirements](https://apcentral.collegeboard.org/media/pdf/ap-csp-student-task-directions.pdf)

## Component A: Program Code 

| Requirements | Completed | 
| --------------- | -----------------| 
| Instructions for input from the user (including user actions that trigger events) | One example of this is in the Baccarat game, players are prompted with a box to input the amount of "money" they would like to bet on this round, and that data is then read and stored when the round begins.  |
| Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the program’s purpose | This code utilizes a list to create and keep track of a standard deck of cards. At the beginning of the game, the standard deck of 52 cards is generated, then any subsequent usage of cards will utilize this deck and draw from it, removing the cards after drawing. The list makes it quick and easy to maintain and keep the logic for drawing cards and displaying them much easier. ![CodePic](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEXa9eePds%2BzC%2FeZ67uPuZ3esFfDt50sG3SN4a7ZrI5wICNRriXXqBP8Hk%2BPv2eH%2F%2BT2LPwDixDIEBbhMgd1ytdb1Y%2BO8peKYEKfmV8ooknTgGUxh6M3ouZ5JypUb9soBSNwUBiJZYPwyMhNzUNdVOmLU7xtwBF7howEj4lHGnIQNlEmW1vR6t9HwvlBrVSlA7UXrqKioRYJKaZFG6eCVj5n8fpX%2FDNJQlRYs3AaIPezijR3jmDuztNyW96KkLXgTTs6U54opqfTE0fxQ9welsmXMmU%2FtLAJTBrx%2BerXvon7oh%2Bc8klVkr2MjcXxePznm49j5q8xbgRB1j3IXNF7DY0kLXvhvHE2FS8cQXxF%2B9oTpVah7%2BD%2BUuWOnR6VO2%2Fnc%2FzgQ2OGtnxmu28YvIOUZPFlOJbNV40wlWmgkORgKKo0x3Fp7qB%2F3nlL1EFGTmycL5qVW3rNf0nRZsZLyvwQyYCmVw5fikeuzV1pqQMFyMvaAvoDNO2LDBsiy%2BNsqvEkGIV5P9RSxBfFL9%2BhBnWDm1SF21mK7v%2FSDZvHvGgK%2B5%2FAQ3%2FTz%2Bx4R5kgt1BgoZwpLvM%3D&sz=w1920-h919) | 
| One procedure that contributes to the program’s intended purpose, where you have defined: the procedure’s name, the return type (if necessary), one or more parameters | Procedure Name (defaultcheck) (This function is to check who won in the baccarat game, player or banker), parameters: player (score of player) and banker (score of banker).  ![CodePic](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEUGf9lgNsZ849mqs2ty2Ywm4gLJS9ss8ovcxk7b9BRAHsR9tlX%2FAsnan9k6FratkWntq91HN7R86RXodNIX%2FhdidDjkS31HGqnL5SadaWjb%2FkQ5D9uFprJoaDgbI94Ydr07gRnv7dVFqNJUk0zjLi1wCsw29OHKPb9CY9Ptbm8QrCAL%2FDeiJ%2Fk1VMffE3o9IBeoIEwp3rO7LAbqo1uJrNeJ5NjsABiT%2Bd9skb1Qx13GkjadWwZe%2FOMaG1xKtlDP%2FcwvY4JCCeZUKDbEHCTj4JCgOUKgWOFJMigWKHVcXbaP8xeg0NS8m8Jx%2BjjfmdQE15DfR0Ds8g5JvVWs4X3%2B71EM9xBu8Z0R0Pj5Z3dzOnqA6tFf%2FBKCdZ6hZDvZBu%2FegzP%2BLsdN%2FyFtDiV5T9nGbwIztFQgUTFqqOOqQBc71aWiQzZ0gRRjWyQg%2F0pGYNdN%2B1FejHUJxIm6APM5EynoRvpxV8v9ykwIZJI5DfVDlFUDVxJ0Uw9oBXFKc3JOrMeIZWaFImMsivSBiGW8Z97pSHNcytSvgg4%2BI2m793X84gP6bFIwYslpUhiObQ3rxaw4&sz=w1920-h919) |
| An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure | Selection: If/Else Statements in a for loop. This introduces sequencing and selection to the code as it runs through the sequence checking the values of cards and assigns the correct value to the card, which is added to the total sum. ![CodePic](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEUe98gbA4uCbWJmDnLTKB2x1q1hBwqepYy94b4cR6GE9Pb1miTr4jC%2Bk8IY7EvW%2FedVCNCV9VSBRybS89QzQ9jdXfh%2BJ07U%2FadMwH11no5uyMd%2B1Cvw1BkUI6Ng5K2oKzMhEatl45%2Fvfzq3kH4D3xQYEXAIQE%2FtMJIFenzs9QXdg%2BXtAJ5oacZGvFImYcpN2Gxj3OTtzq745zhpvfJjuINgPcErRxhxLUJyVlAv6PLmJvlzQ31J9nJXQFEULzjXCdeYOlzcOh9wUGk4B2qJtci7s930rBAqOvsCERPKFmoEhqzElgkYHCgXPejU22deSueS5xaGJ7S%2Fp4cNvuuHsGAHes5vqRM5G%2FbebRsKZlH2NOCopXt49B%2BULytV%2FTkkmPnm9KGB9v5AoW6DGR2eYEFw380ihAizsD0V1lshxzfRmLVrOGO%2BMKkFygzrKAxCMLi1V4VWCx%2FQov7%2FOSHfCGpBJF4coT1DAAF%2FEZ1Ksk6T2cMHBJ67Fm35hRTpGM%2F%2FTSFwaBxXuR6sG3YC8kkUQcErunjrDkeoIdF4efHNrvpRVoX%2BDWn5hsbPfdQE0YLH&sz=w1920-h919) |
| Calls to your student-developed procedure | Calling move function: defaultcheck() ![CodePic](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEWZXmARmlTdT81bBliexN%2FeQhMPu1Sfqd1NsqWPUF9m6YJ1HMCSoyQ5HPB5kjZggMMNinbqnt5h1AHSNnwgBrkO3TI2sfLmHyVRaKit1Don9i6M5TJ3pdnJs%2BoQ%2Fw9GUdSt7KH25tf5Gu8Br4EOCoTGss6TBPpdTkwlMrtRZRaamwjXsLqoZgODe%2BLXr6J040llHWOBvAU1DzqU5jC8JYN4LHRA0Gax5mCQiGI10i8%2FvBCGpDXACq0dSMf5MCN7Q6s2WsBViOB7VOcBEBRVDKunPkgxbeZH%2F5hkhOVADLL%2F%2FdEwH1SpBNCHvjGNEOuy726qhqWY8ydb5rPpFVDI%2FiCZsFz4jUdXMcT%2FyOUUsx2HMLJUs4H2yLI3Wf3iaIt5XJr1NV2Mzs9ofagfWFXxphfMOWWctPtr73NtMEEV7Ma5qXS%2FRiSKBtgvC%2BQDaNAUbkXwuHUad%2BXwNYnT7H6ZWHlPm4DmW5urbcn7gxEqObvoQ%2BKCworTjVDfdlJblD9tR1kTi0e1%2BL2yb94hntCbnx4jzDOdoDaAXGxbqqWTVJRZgASbivzq3WZbqD4OVLp9DGH5XH4%3D&sz=w1920-h919) |
| Instructions for output (tactile, audible, visual, or ) based on input and program functionality | Textually inform user if they won/lost. Makes large, red text appear saying You Win or You Lose. ![CodePic](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEUnUNxpLNMILLcVRbyt53615YD2Lj3UVxMjRVLlCiF8dm6kq%2FiR5PVc3AUgEG1S2D11jiIdydUxXa%2B7zBX3%2Bv0Zt1hf9ZGinggoYSzB2s%2FtyN1kWF7r9BDOJoUKfKkjYAIWgFf19IZDioEJiD5kEp8TVYsDfSae8b%2Bh%2FBDY%2Bb3IvIgs3jwAclsGvmDr4KRJpWDdc2iXomn1sisDxeEGNYF3fLriBuLaQ3GljUU3LIBw3Axg5taxS%2FkKeLqrOkLcUGBwTJHRxR3U%2B6KufTv%2FONJPekkcKLhA3POhYEnkJEic4ygrLxgj3PjEP6hMU8GmrGt87jcU65bTPFYBfba3D6D2lyKwfHA1qsOTsoAaLKSuayoFXGjo5sQflglWpT9K6nO%2FWNfdl3%2BVlZfbzH7bX3pv7KgqFkQo1z3vUAlmgd68X2h71lrwmqzToPH1NchxuFkaugrdA8tpNBwCiI%2Bhw7kM5S1%2BSQsPdoo%2BozghmG566z2na78%2FpLLK7w7Cw%2Bjq22baBPpPhsWlf1LZHpH83u6P5WG5pxaPY5ygzo4L%2F%2B1VS3CNqrmE0IYftdNx7hhGQA%3D%3D&sz=w1920-h919) |

## Component B: Video 

[Video Link](https://drive.google.com/file/d/1aOWz_UwLGDch4MraemMwkJNCxebUoQEi/view?usp=drive_link)

| Requirements | Completed | 
| --------------- | -----------------| 
| Input to your program | Y - Show submitting the bet amount in baccarat |
| At least one aspect of the functionality of your program | Y - Show that Games Function as Expected W/O Bugs |
| Output produced by your program | Y - Changes money accordingly, Show Victory/Loss Notification |
| Your video may NOT contain: Any distinguishing information about yourself, Voice narration (though text captions are encouraged) | Y |
| Your video must be: Either .webm, .mp4, .wmv, .avi, or .mov format | Y - .mp4 File |
| No more than 1 minute in length | Y - 1 Minute Long |
| No more than 30MB in file size | Y - 16.3 MB|