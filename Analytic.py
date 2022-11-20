from database import *


def show_all_habit(db):
    """
    Gets information about all habits
    :param db:create connection with database
    :return:a list of all habit with their all information
    """
    list = show_habits(db)
    for row in list:
        print("Habit Name: ", row[1])
        print("Specification: ", row[2])
        print("Period: ", row[3])
        print("Creation: ", row[4])
        print("Current streak:", row[5])
        print("\n")


def show_logs(db, name):
    """
     Returns a list of dates
    :param db:To maintain a connection with the database
    :param name:Name of the specified habit
    :return:a list of all check-off dates
    """
    result = show_all_logs(db, name)


def get_habit_with_period(db, period):
    """
    Gets information from database and return to the user
    :param db:Create a connection with the database
    :param period:timespan of a habit (eg:- daily or weekly)
    :return:a list of habits with specified period
    """
    list = habit_with_period(db, period)
    for row in list:
        print(f"Name: {row[1]}")
        print(f"created_at: {row[4]}")
        print(f"Current streak: {row[5]}")
        print("\n")


def get_longest_streak(db, name):
    """
    Select current streak and from that return the longest run
    :param db:maintain a connection to database
    :param name:name of the specified habit
    :return:longest streak
    """
    verify = verification(db, name)
    if verify:
        cur = db.cursor()
        cur.execute("SELECT name FROM count where name=?", (name,))
        result = cur.fetchone()
        if result:
            longest = get_streak_from_count(db, name)
            print(f"Longest streak for habit '{name}' is \n {longest} days ")
            return longest
        else:
            print(f"Longest streak for habit '{name}' is \n {0} days")
    else:
        print("Enter A Valid Habit Name")


def get_longest_of_all(db):
    """
     from database return the longest run streak of all habit
    :param db:Maintain connection with database
    :return:longest run from all defined habit
    """
    long = longest_of_all(db)
    print(f"Longest streak for all defined habits is \n {long} days ")
