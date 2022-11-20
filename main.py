from database import *
from datetime import *


class Habit:
    def __init__(self, db, name: str, task_specification: str, period):
        """This creates new habit.The name and period should be defined

        Args:
            name: Name of the habit.
            task_specification: Description for the habit.
            period: A time-period for your habit (eg. daily or weekly)
        """
        self.db = db
        self.name = name
        self.task_specification = task_specification
        self.period = period
        self.streak = 0
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.name}:{self.task_specification}:{self.period}"

    def increase(self):
        """Increase the streak by 1"""
        self.streak = get_streak(self.db, self.name)
        self.streak += 1

    def reset(self):
        """Reset the streak to one"""
        self.streak = 1

    def save_habit(self, db):
        """create new habit in the database otherwise update the habit if already in db"""
        add_habit(self.db, self.name, self.task_specification, self.period)

    def delete_habit(self, db):
        """removes the user habit from the database"""
        name = verification(self.db, self.name)
        if name:
            remove_habit(self.db, self.name)
            self.name = None
            self.task_specification = None
            self.period = None
            self.streak = 0
        else:
            print("Enter a valid habit name")

    def add_event(self, db):
        """increase the counter by 1"""
        self.increase()
        check_habit(self.db, self.name)
        update_habit(self.db, self.name, self.streak)
        self.longest(self.db)

    def decrement_event(self, db):
        """reset counter to 1 if streak breaks"""
        self.streak = 1
        check_habit(self.db, self.name)
        update_habit(self.db, self.name, self.streak)
        self.longest(self.db)

    def daily_habit(self, db):
        """complete daily habit than add into database"""
        today = date.today()
        format = "%Y-%m-%d %H:%M:%S"
        last = last_checked(self.db, self.name)
        last1 = [i[0] for i in last]
        ls = last1[-1]
        if len(ls) < 0:
            self.add_event(self)
        else:
            last_check = datetime.strptime(ls, format).date()
            if today - last_check < timedelta(days=1):
                print("Habit Already Checked Come Again Tomorrow")
            elif today - last_check < timedelta(days=2):
                self.add_event(self)
            else:
                self.decrement_event(db)

    def weekly_habit(self, db):
        """complete weekly habit and add into database"""
        today = date.today()
        format = "%Y-%m-%d %H:%M:%S"
        last = last_checked(self.db, self.name)
        last1 = [i[0] for i in last]
        if len(last1) < 0:
            self.add_event(self)
        else:
            ls = last1[-1]
            last_check = datetime.strptime(ls, format).date()
            if today - last_check < timedelta(days=7):
                print("Habit Already Checked Come Again Next Week")
            elif today - last_check < timedelta(days=8):
                self.add_event(self)
            else:
                self.decrement_event(db)

    def complete_habit(self, db):
        """completes the habit in the database"""
        name = verification(self.db, self.name)
        if name:
            streak = get_streak(self.db, self.name)
            period = get_period(self.db, self.name)
            per = period
            if per == 'daily':
                if streak == 0:
                    self.add_event(self)
                else:
                    self.daily_habit(db)
            else:
                if streak == 0:
                    self.add_event(self)
                else:
                    self.weekly_habit(db)
        else:
            print("Enter a valid habit name")

    def longest(self, db):
        """ Calculate longest_streak using the current streak value"""
        streak = get_streak(self.db, self.name)
        count = get_streak_from_count(self.db, self.name)
        if streak >= count:
            self.streak = get_streak(self.db, self.name)
            update_count(self.db, self.name, self.streak)

