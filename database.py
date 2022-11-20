import datetime
import sqlite3
from datetime import *


def get_db(name="habit.db"):
    """ Function to create and maintain connection with the database"""
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    """Function that creates tables into the database"""
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Habit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    task_specification TEXT,
    period TEXT,
    created_at INTEGER,
    streak INTEGER ) """)

    cur.execute("""CREATE TABLE IF NOT EXISTS count (
    name TEXT,
    Checked_at INTEGER,
    streak INTEGER,
    FOREIGN KEY (name) REFERENCES Habit(name))""")

    db.commit()


def add_habit(db, name, task_specification, period, streak=0):
    """ add a new habit into the database """
    cur = db.cursor()
    cur.execute("SELECT name FROM Habit WHERE name=?", (name,))
    result = cur.fetchone()
    if result:
        print("Habit already exists")
    else:
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO Habit VALUES (NULL,?,?,?,?,?)",
                    (name, task_specification, period, created_at, streak))
        db.commit()
        print("Habit created successfully")
        print("Thanks for the info.\nNow...")


def check_habit(db, name, checked_at=None, streak=0):
    """ check a specific habit """
    cur = db.cursor()
    if checked_at is None:
        checked_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO count VALUES(?,?,?)", (name, checked_at, streak))
    print("Habit check off successfully")
    print("Name :-", name)
    print("checked_at :-", checked_at)
    db.commit()


def update_habit(db, name, streak):
    """updates the value of streak in the habit table"""
    cur = db.cursor()
    cur.execute("UPDATE Habit SET streak=? WHERE name=?", (streak, name))
    db.commit()


def verification(db, name):
    """ verify habit from the database """
    cur = db.cursor()
    cur.execute("SELECT name FROM Habit WHERE name=?", (name,))
    return cur.fetchone()


def last_checked(db, name):
    """ return the last of last check off """
    cur = db.cursor()
    cur.execute("SELECT checked_at FROM count WHERE name=?", (name,))
    return cur.fetchall()


def get_streak(db, name):
    """ return the current streak from the database """
    cur = db.cursor()
    cur.execute("SELECT streak FROM Habit WHERE name=?", (name,))
    streak_count = cur.fetchall()
    return streak_count[0][0]


def get_streak_from_count(db, name):
    """ return the longest streak from table count """
    cur = db.cursor()
    cur.execute("SELECT streak FROM count WHERE name=?", (name,))
    str_count = cur.fetchall()
    return str_count[0][0]


def update_count(db, name, streak):
    """updates the value of streak in count table"""
    cur = db.cursor()
    cur.execute("UPDATE count SET streak=? WHERE name=?", (streak, name))
    db.commit()


def get_period(db, name):
    """ select periodicity of a specified habit """
    cur = db.cursor()
    cur.execute("SELECT period FROM Habit WHERE name=?", (name,))
    return cur.fetchall()[0][0]


def show_habits(db):
    """ return a habit with all information """
    cur = db.cursor()
    cur.execute("SELECT * FROM Habit ")
    return cur.fetchall()


def habit_with_period(db, period):
    """ return a list of habit according to their period """
    if period == "daily":
        cur = db.cursor()
        cur.execute("SELECT * FROM Habit WHERE period=?", (period,))
        return cur.fetchall()
    else:
        cur = db.cursor()
        cur.execute("SELECT * FROM Habit WHERE period=?", (period,))
        return cur.fetchall()


def longest_of_all(db):
    """select the max streak from all defined habit """
    cur = db.cursor()
    cur.execute("SELECT MAX(streak) FROM count")
    return cur.fetchall()[0][0]


def show_all_logs(db, name):
    """ return a list of all habit checked_at dates """
    result = verification(db, name)
    if result:
        cur = db.cursor()
        cur.execute('SELECT checked_at FROM count WHERE name=?', (name,))
        long = cur.fetchone()
        if long:
            cur.execute("SELECT checked_at FROM count WHERE name=?", (name,))
            log = cur.fetchall()
            print(f"Your logs for {name}")
            print(f"checked at \n {log}")
        else:
            print("No Logs For This Habit Yet")
    else:
        print("No logs for this habit exists in our database")


def remove_habit(db, name):
    """ delete the specified habit from the database """
    cur = db.cursor()
    cur.execute("DELETE FROM Habit WHERE name=?", (name,))
    cur.execute("DELETE FROM count WHERE name=?", (name,))
    db.commit()
    print("Habit removed successfully")
