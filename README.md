
# The Habit tracker
***
Helps you track your habits anytime anywhere.

## Table of content 
- [what is a habit tracker](#what-is-a-habit-tracker)
- [why you need this](#why-you-need-this)
- [Getting started](#getting-started)
- [Installation](#installation)
- [How do we run the program](#how-do-we-rum-the-program)
- [Usage](#usage)
- *[Create](#create)
- *[Check-off](#check-off)
- *[Analyse](#analyse)
- +[All tracked habits](#all-habits)
- +[Habits with same period](#habit-with-same-period)
- +[Longest streak](#longest-streak)
- +[Habit logs](#habit-logs)
- *[Remove](#remove)
- *[Exit](#exit)
- [Predefined habit](#predefined-habit)
- [Contact](#contact)

## What is a habit tracker
***
Habit trackers help you to monitor your progress on the positive habits you want to form. They encourage you to keep going and provide clear insight into how well you’re really doing.
## Why you need this 
***
If you want to stick with a habit for good, one simple and effective thing you can do is keep a habit tracker. Elite performers will often measure, quantify, and track their progress in various ways. Each little measurement provides feedback. It offers a signal of whether they are making progress or need to change course.

## Getting started
***
Firstly you have to download the python 3.10+ version on your operating system. You can download this from python [official website](https://www.python.org/downloads/).

# Installation
***
After installing python you can install Questionary using commandline.

``````commandline
pip install questionary
``````
Next thing you need is to install pytest. Which we use to test our project
````commandline
pip install -u pytest
````
We also used a library called [time-machine](https://pypi.org/project/time-machine/) in testing for mocking the time
````commandline
pip install time-machine
````
or 
````commandline
python -m pip install time-machine
````
## How do we rum the program
***
After installing the necessary dependencies.Open you command or terminal window and use cd (to change directories) to select your habit track folder and then type

````commandline
python CLI.PY
````

# Usage
***
Here you can select an option of your choice using the arrow key.
## Create
***
After selecting the create option you can create any habit simply by putting name, task specification/ description and timespan (eg:- daily or weekly) 
## Check off
***
This option will help you to complete your desired tasks
## Analyse
***
This functionality will help you to analyse your habits 
#### All habits
it will return your all currently tracked habits with name, specification, their creation and current streak.

#### Habit with same period
Here you can easily check your progress for different time period. There are two option "daily" or "weekly". You can select any of your choice.
#### Longest streak 
This option will give you the opportunity to analyse your longest streak for a specific habit. You have to enter the name of the habit that you want to analyse.
#### Longest of All
Helps you find your longest streak of all defined habits.
#### Habit logs
This button will help you to analyse at which habit you struggle the most.
It shows the all checked_at dates of specified habit. 

## Remove 
***
Removes the entered habit from the database.

## Exit
***
Close the program

# Predefined habit
***
 There are 5 predefined habits:-
1. (talk, talk with a positive person, daily habit) 
2. (sun, get some sunlight , daily habit)
3. (meditation, daily 10m meditation, daily habit)
4. (stretch, stretch all body parts, weekly habit)
5. (reading, read a book every week, weekly habit)

To see all predefined habit go to analyse > analyse all tracked habits

# Functionality
The program returns current streak and longest streak both for all habits. There are different options for both functionality.
One can check daily habit once in a day. For weekly habits check-off once in week on same day of last checkoff.

# Contact
If you want to collaborate or have a suggestion than create a pull request. 
or you can mail me at  john.9pssr@aleeas.com

if you find any error or face problem in running the application. 
message on session id:-
05e1491bbc7f952b73f07f643fdb8a22f416a493ad29931e51f167671bd0da4f3d
