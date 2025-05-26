#### Design Document


## Overview

Study Buddy is an education website that was designed to make studing more fun and engaging. I was able to do this this through a series of game modes-- Test, Match and Sprint. Each of these game modes give a unique learning experience and allow users to test what they know in a laid-back and fun way. The application allows for users to reinforce their learning in a stress-free way, the method of learning that has been shown to display the most benefits.

One thing to note about this code is that there was an extensive search that was used in finding the particular bootstrap code to obtain the clean and sleak asthetic that I wanted to achieve and achieve an overall UI that I was happy to showcase. Another key feature to note is that there was minimal CSS that was used in this project and this was done on purpose. Though tedious, there was much less debugging involved with regards to the style choices, with bugs being nonexistent as a result.

Under the hood Studdy Buddy is powered by Flask, sqlite is used to design and retireve data from these databasses to provide a clean and smooth gaming experience for the user. Both the test and match games draw from their own distinct databases. The test game draws from questions.db while the match game draws from the topics.db. Sprint does not rely on a database and instead creates new data when necessary for a more memory-efficient game mode. Extensive debugging and iteration were involved in ensuring that both the backend logic and frontend responsiveness worked well together- as to extend beyond functionality.

## Features

# Test Function:

The test function is one of the key minigames that StuddyBuddy uses to keep games interesting. The game is made so that a question is outputted with three different answers below it. The user is then meant to click on the correct answer. If the correct answer is chosen then

What does it do:

When you run the test function it takes in prewritten data in the questions.db database. It then processes that data using the packages such as flask and json to output these pieces of information onto the user interface.

Inputs: The key pieces of data that the test game takes in are below

- Questions from questions.db
- Answers from questions.db
- Weather or not an answer is true or false
    --> Information that is held within questions.db
- More pieces of information about the database to make user access easier

Outputs:

- A result to show weather a question is correct or incorrect
- An addition to the overall point system within the flask code to keep track of user

Significance and Use:

This function is one of the key games that StuddyBuddy uses to keep users intersted in their studying and overall learning. This section in particular involved an extensive amount of debugging.

# Match Function

What does it do:

Match is a different method of studying that is meant to test users ability to find the relationship, between a given topic/question and multiple different words that are given.

Instead of using the questions database, a seperate database is used to contain the different questions. This is so that the questions for each game are contain their own essence of questions. With there being more direct questions in test, and less direct questions in match.

Inputs: The key pieces of data that the match game takes in are below

- Topics from topics.db
- Choices from topics.db
- Weather the choice is a distractor or a correct answer
    --> Retrieved from topics.db as well.

Outputs:

-Topics are outputted onto the website and replace the question.
-Choices are outputted as draggable options
-Text is outputted to showcase weather the correct answer was chosen or not.

Significance and Use:

One major pivot with the match game is that I had decided to use a mixture of javascript and flask for the drag and drop. While with test, it was majority flask that was used to give the website functionality, in match there was javscript use to make the website not only easier to deal with as javascript proved itself to be much simpler, but also make the website much better in style.

Moreover, in match there are distractor and non-distractor assignments that are given to each of the choices, giving the match game its own sort of flare.

# Sprint Function
The Sprint function is meant to put the users arithmetic skills to the test. Users are tasked to solve the math problems as fast as they possibly can to rack up points. The Sprint Funtion randomly generates two numbers and the operation that must be down between them

Inputs:
- User Input
    --> Holds the supposed product of the operation

Output:
-The arithmetic operation that must be completed
-Weather or not the User Input was Correct

Significance and Use:

The Sprint game uses a particular function to randomly generate new functions. It generates one initially to get the game started and generates new operations when need be.



