---
toc: false
comments: false
layout: post
title: Data Structure Writeup
permalink: datastruct/
---
## Blog Python Model code and SQLite Database

### Show your unique collection/table in database, display rows and columns in the table of the SQLite database from VSCode using SQLite3 Editor

This right here is a picture of my database for my login system. Each row is an individual user, and the columns are for the properties: name, uid, password, date of birth, and pronouns.
![Image](https://github.com/nighthawkcoders/teacher_portfolio/assets/142526022/0b8b6755-80ca-41de-88c0-ce3d7eae2d99)

### Show your unique code that was created to initialize table and create test data from VSCode model

These next two images are the code for initializing the table.
This first image is defining the User class, and the different variables associated with each user. Each line defines a new parameter of the user and has properties like if the value can be null or has to be unique.

![Image](https://github.com/nighthawkcoders/teacher_portfolio/assets/142526022/b22cd717-dc44-4e35-8379-030b41eb26d7)

This next image is a function which defines the values that appear in the table. It uses the User class to define each user, along with the parameters for each user.

![Image](https://github.com/nighthawkcoders/teacher_portfolio/assets/142526022/45e84e52-f5fc-4548-b66e-e9650fbba78b)

## Blog Python API code and use of List and Dictionaries

### Show a list as extracted from database as Python objects in VSCode using Debugger

This image shows a list extracted from the database as a Python object. This screenshot is taken in debugger after running the search function. We see multiple Design objects which have been freshly loaded from our database.

![Image](https://github.com/nighthawkcoders/teacher_portfolio/assets/142526022/0cc70d38-14b2-46fe-8210-cda81b075f28)

## Blog Python API code and use of Postman to request and respond with JSON

### Show Python API code definition for request and response using GET, POST, UPDATE methods in VSCode. Discuss algorithmic condition used to direct request to appropriate Python method based on request method

This image here shows the python code for the UserAPI class, defining the post and get methods. For the post method, the class first uses the request.get_json() line to get read the data, then checks to see if the data is valid. Then, it sets up the user using the User class, defining the name and uid parameters. Finally, the post method adds the user to the database. For the get method, the class extracts all users from the database, then prepares all the data for output in json. Finally, the get method returns the data.

Show algorithmic conditions used to validate data on a POST condition in VSCode.
This algorithm also has code to validate data, as while checking to see if the data is valid, if the name, uid, or date of birth is not properly formatted, the program will raise an error.

![Image](https://github.com/nighthawkcoders/teacher_portfolio/assets/142526022/fcf66b78-2a2c-49eb-9016-463d2b2a1a1d)

### Show URL request and Body requirements for GET, POST, and UPDATE methods in Postman

These next three images show the URL request and Body requirements for Get, Post, and Update. The Get method requires no body to work, while the Post and Update methods require a specific user's information.

![image](https://github.com/AustinZhang1/student/assets/142526022/0b67cd78-d5ce-4dc7-a3e3-af0020b303d3)
![image](https://github.com/AustinZhang1/student/assets/142526022/c3da648d-0152-4c45-aba2-33aa7827f5e4)
![image](https://github.com/AustinZhang1/student/assets/142526022/e342a69f-580b-43b3-aaea-321c0fa23c22)

### Show the JSON response data for 200 success conditions on GET, POST, and UPDATE methods in Postman

Here I show the GET, POST, and UPDATE methods with 200 success messages.

![Image](https://github.com/nighthawkcoders/teacher_portfolio/assets/142526022/b859a066-c944-46d0-ada4-a89564635f62)
![Image](https://github.com/nighthawkcoders/teacher_portfolio/assets/142526022/10873aa1-db95-4045-aa87-5c316017cb97)
![image](https://github.com/AustinZhang1/student/assets/142526022/ce24b0d6-1b45-4cf9-a766-aea6846312cc)

### Show the JSON response for error for 400 when missing body on a POST request in Postman

When the post request is missing a body inside the curly braces, it will return a 400 bad request error.

![image](https://github.com/AustinZhang1/student/assets/142526022/699f2e5f-bf1e-4c27-a956-8dec3ca3d9d5)

### Show the JSON response for error for 404 when providing an unknown user ID to a UPDATE request in Postman

In postman, when the user id is unknown, the UPDATE request will not work and will return a 404 error.

![image](https://github.com/AustinZhang1/student/assets/142526022/43f99f10-c23e-4042-ad7d-299497eb8630)

## Blog JavaScript API fetch code and formatting code to display JSON

### Show response of JSON objects from fetch of GET, POST, and UPDATE methods in Chrome inspect

![image](https://github.com/AustinZhang1/student/assets/142526022/f07df2a4-1b29-4f67-9a39-47a7b666cc00)

### Show a demo (GET) of obtaining an Array of JSON objects that are formatted into the browsers screen in the Chrome browser

![image](https://github.com/AustinZhang1/student/assets/142526022/c4e5d45b-5e9f-423d-bc5a-5b99e41ae4b9)

### Describe fetch and method that obtained the Array of JSON objects in JavaScript code

This screenshot demonstrates the fetch method in my frontend Javascript code. It uses the fetch method to send a POST request to get the backend data. Then, it checks if the authentication of the data is correct, and correctly logs in users that are authorized.

![image](https://github.com/AustinZhang1/student/assets/142526022/f2f3e859-f75d-429a-82d0-5dc07006c400)

### Show code that performs iteration and formatting of data into HTML in JavaScript code

This code properly formats the data into Javascript code so that it is usable.

![image](https://github.com/AustinZhang1/student/assets/142526022/8d290949-501d-43b5-b6d6-a103be9c4474)

### Show and describe code that handles success. Describe how code shows success to the user in the Chrome Browser screen in JavaScript code

This code handles successes when trying to authenticate the user.

![image](https://github.com/AustinZhang1/student/assets/142526022/4602e873-7fe6-4b87-8214-27c62f47b4f9)

### Show and describe code that handles failure. Describe how the code shows failure to the user in the Chrome Browser screen in JavaScript code

This code handles failures when trying to authenticate the user.s

![image](https://github.com/AustinZhang1/student/assets/142526022/0d20763c-eb39-4c16-837b-e102b8c2d73b)