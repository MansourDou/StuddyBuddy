## Studdy Buddy


# Introduction

Studdy Buddy is an educational web application that brings studying to a more fun, interactive, and low-key level. The website consists of three distinct game modes—Test, Match, and Sprint—each with a unique method of learning. This guide is intended to walk you through exactly how to install, use, and run Studdy Buddy as well as describe what each game does in the background. By the conclusion of this Studdy Buddy User manual, you should be prepared to test or use the project independently without additional assistance.


# Getting Started
To run Studdy Buddy, you will require the latest version of Python, Flask, and SQLite3 on your system. Flask, similar to python can be installed through the command prompt if necessary. After getting your environment set up, you can download the project, make sure that this includes all of the databases. These databases are essential in powering the Test and Match game modes, and each has a specific schema. The questions.db database would have a table called questions with columns for the question itself, three answer choices, and flags indicating which answer is correct. The topics.db database would have topic and choice data suitable for the drag-and-drop feature of the Match game.

Each of these games have their own rules and this tutorial will teach you how to play them!

# Different Game Modes
The Test mode of the game displays the user a question along with three available answers. Once the user selects an answer, the application checks whether it's correct using pre-established flags within questions.db. The application provides instant feedback and adds to the user's score, which is tracked using Flask's session. To play the game simply select the correct answer and receive the feedback from the website.

With the match game, users are asked to match a question or topic with a number of potential answer choices by dragging and dropping them into place. The Match mode utilizes the topics.db database, which contains correct answers as well as distractors. The game uses both Flask and JavaScript together to enable a more interactive feel, and was designed to be more open-ended and more theoretically challenging than the Test game. JavaScript came particularly in handy to manage the drag-and-drop elements and allow more responsiveness on the interface. With this game you simply match the word with the topic. Through the JavaScript that was used with this game, it is possible to simply drag and drop the word into the hole, making the game more fun as a whole...  No pun intended.

Sprint is the fastest-paced of the three games and is intended to improve users' mental math skills. Sprint does not use a database. Sprint instead dynamically creates two numbers and a mathematical operation. It then asks the user to calculate it as quickly as possible. After the user types an answer, the program immediately reacts and generates a new question. This approach keeps memory usage low and gameplay quick. To win this game simply do the mental math and type up the result of the operation and try to get as many as possible correct.

# Stylistic Choices
Studdy Buddy was written with minimal custom CSS to keep bugs at a minimum and development easy. Most styling is achieved by using Bootstrap components in a wise manner such that a clean and responsive user interface is achieved. The aim was to create something that's visually bleeding edge but easy to maintain and debug.

If something seems to be broken or is unclear despite this documentation, please don't hesitate to contact me for assistance. You can reach me via email at mansourdoumbia@college.harvard.edu. Thanks for giving Studdy Buddy a try—I hope you find it helpful and fun to use!

# Contact

Any questions can be directed towards myself at any time.
Email: mansourdoumbia@college.harvard.edu



