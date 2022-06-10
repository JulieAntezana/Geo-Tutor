# Geo-Tutor

Repository for a Geometry Tutor Web App using Python and the Django framework.

# Overview

I am a software engineer who wants to create a geometry tutorial website for middle school students.

How to start a test server on your computer: Click on the link for more information:

https://code.visualstudio.com/docs/python/tutorial-django

Open the math app folder in vs code
Open terminal
python manage.py migrate
python manage.py runserver

To see the first page of the app hold down the control button and click on the link or type in the browser: http://127.0.0.1:8000/.

My purpose for writing this software is to help middle school and high school students improve their geometry skills.

Link to YouTube demonstration, 4-5 minutes of the software running (starting the server and navigating through the web pages) and a walkthrough of the code:

https://youtu.be/eEPV2l_zm5A

# Web Pages

The web app has tutorial lessons about geometry topics. Each lesson has a quiz to help the student practice what they have learned and measure their success. Students can earn points and rewards as they progress through the lessons. There is a student registration form which is connected to a database and displays the data on the "Student Directory" page. I have included a "Contact Us" form that connects with the database that displays the data on a "Message Log" page. Most pages can be accessed by clicking on the navigation bar at the top of the page.

Description of what is dynamically created on each page: Each page has a header, navigation bar and footer which is dynamically created from a template. The quizzes will be dynamically created in the future. The student directory and the message log are dynamically created from the "students" database and the "contacts" database. The data is collected via a "Registration" form and a "Contact Us" form. In the future, I plan to create a scoring system that will award points at the end of each lesson.

# Development Environment

The tools used to develop the software are Visual Studio Code, Django framework and GitHub.

The programming language used was Python. The libraries used were from python, django, and sqlite3.

# Useful Websites

Websites that I found to be helpful in this project: (to be added at a later date)

- [Django docs](https://docs.djangoproject.com/en/3.0/contents/) Tutorial
- [Visual Studio Code Django Tutorial](https://code.visualstudio.com/docs/python/tutorial-django) Tutorial
- [w3schools Django Tutorial](https://www.w3schools.com/django/index.php) Tutorial
- [IXL Learning Website ](https://www.ixl.com/math/lessons/types-of-angles) Geometry content
- [Sololearn](https://www.sololearn.com/learning/1059) Model as an example
- [Unsplash](https://unsplash.com/) Free photos
- [Vecteezy](https://www.vecteezy.com/) Free logo

# Future Work

Things that I need to fix, improve, and add in the future: (to be determined at a later date)

- Create an administrator login and make the Student Directory and Message Log accessible only to administrators.
- Create an input form to create quizzes in the administrator login.
- Implement the ability to score the quizzes and award points when the lesson is complete.
