from database import *
import time_machine


class Test_set_up:
    # make a connection with database file
    db = sqlite3.connect("test.db")

    """Down below is 4 weeks of pre-defined data. I entered the data in two different ways for daily habit data entered
       manually and for weekly habits using time-machine.
       The reason for using different methods is that I want to know the pro's and con's of both the methods."""
    def test_data(self):
        # four weeks of pre-defined data
        db = sqlite3.connect("test.db")
        cur = db.cursor()
        # habit talk has the most success
        test_data = [("talk", "2022-10-25 00:00:00", 10),
                     ("talk", "2022-10-24 00:00:00", 9),
                     ("talk", "2022-10-23 00:00:00", 8),
                     ("talk", "2022-10-22 00:00:00", 7),
                     ("talk", "2022-10-19 00:00:00", 7),
                     ("talk", "2022-10-18 00:00:00", 6),
                     ("talk", "2022-10-17 00:00:00", 5),
                     ("talk", "2022-10-15 00:00:00", 5),
                     ("talk", "2022-10-14 00:00:00", 4),
                     ("talk", "2022-10-13 00:00:00", 3),
                     ("talk", "2022-10-12 00:00:00", 2),
                     ("talk", "2022-10-10 00:00:00", 2),
                     ("talk", "2022-10-09 00:00:00", 1),
                     ("talk", "2022-10-06 00:00:00", 1),
                     ("talk", "2022-10-04 00:00:00", 1),
                     # Habit sun has most troubles on the way
                     ("sun", "2022-10-25 00:00:00", 2),
                     ("sun", "2022-10-24 00:00:00", 2),
                     ("sun", "2022-10-22 00:00:00", 2),
                     ("sun", "2022-10-20 00:00:00", 2),
                     ("sun", "2022-10-19 00:00:00", 1),
                     ("sun", "2022-10-17 00:00:00", 1),
                     ("sun", "2022-10-13 00:00:00", 1),
                     ("sun", "2022-10-05 00:00:00", 1),
                     # Habit meditation
                     ("meditation", "2022-10-26 00:00:00", 3),
                     ("meditation", "2022-10-25 00:00:00", 2),
                     ("meditation", "2022-10-24 00:00:00", 2),
                     ("meditation", "2022-10-22 00:00:00", 2),
                     ("meditation", "2022-10-20 00:00:00", 2),
                     ("meditation", "2022-10-19 00:00:00", 1),
                     ("meditation", "2022-10-17 00:00:00", 1),
                     ("meditation", "2022-10-13 00:00:00", 1),
                     ("meditation", "2022-10-05 00:00:00", 1),
                     ]

        cur.executemany("INSERT INTO count VALUES(?,?,?)", test_data)
        db.commit()

    @time_machine.travel("2022-01-01 00:00:00 +0000")
    def test_date2(self):
        # this function is for testing purpose only
        assert date.today().isoformat() == "2022-01-01"

    @time_machine.travel("2022-10-01 00:00:00 +0000")
    def test_on_01(self):
        # test on 1-10-2022
        self.db = sqlite3.connect("test.db")
        last_checked(self.db, "meditation")
        assert last_checked(self.db, "meditation") is not None
        assert get_streak_from_count(self.db, "meditation") == 3

    @time_machine.travel("2022-10-08 00:00:00 +0000")
    def test_on_08(self):
        check_habit(self.db, "reading")
        check_habit(self.db, "stretch")

    @time_machine.travel("2022-10-15 00:00:00 +0000")
    def test_on_15(self):
        # check habit on 15-10-2022
        check_habit(self.db, "reading")
        assert last_checked(self.db, "reading") is not None
        assert get_streak_from_count(self.db, "reading") == 1

    @time_machine.travel("2022-10-22 00:00:00 +0000")
    def test_on_22(self):
        # check reading and stretch on 22-10-2022
        check_habit(self.db, "reading")
        check_habit(self.db, "stretch")
        assert date.today().isoformat() == "2022-10-22"
        assert get_streak_from_count(self.db, "meditation") == 3

    @time_machine.travel("2022-10-29 00:00:00 +0000")
    def test_on_29(self):
        # testing on 29
        check_habit(self.db, "reading")
        check_habit(self.db, "stretch")
        assert get_streak_from_count(self.db, "stretch") == 4


def teardown_method(self):
    import os
    pass
