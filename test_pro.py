from Analytic import *
from main import Habit


class Test_counter:
    def setup_method(self):
        # set up a database file for testing
        self.db = get_db("test.db")

    def test_add_habit(self):
        # add habit into the database
        add_habit(self.db, "run", "running", "daily")
        add_habit(self.db, "swim", "swimming", "weekly")
        add_habit(self.db, "dance", "dancing", "daily")
        add_habit(self.db, "walk", "daily walk", "daily")
        add_habit(self.db, "type", "weekly typing practice", "weekly")

    def test_create(self):
        # create a new habit
        habit = Habit(self.db, "code", "coding", "weekly")
        # save the habit
        habit.save_habit(self.db)
        # verify the habit
        assert verification(self.db, "code")

    def test_complete_habit(self):
        # complete habit
        habit1 = Habit(self.db, "dance", "dancing", "daily")
        habit1.complete_habit(self.db)
        # verify the streak
        assert get_streak(self.db, "dance") == 1
        habit = Habit(self.db, "code", "coding", "weekly")
        habit.complete_habit(self.db)
        assert get_streak(self.db, "code") == 1

    def test_remove_habit(self):
        # test remove option
        remove_habit(self.db, "code")
        assert verification(self.db, "code") is None
        remove_habit(self.db, "run")
        assert verification(self.db, "run") is None

    def test_check_habit(self):
        # test check-off option
        check_habit(self.db, "type", "2022-10-27 15:15:23")
        check_habit(self.db, "type", "2022-10-28 15:13:43")
        # verify the database is not empty
        assert last_checked(self.db, "type") is not None

    def test_update_habit(self):
        update_habit(self.db, "type", 13)
        assert get_streak(self.db, "type") == 13
        update_habit(self.db, "swim", 4)
        assert get_streak(self.db, "swim") == 4

    def test_longest_streak(self):
        # set the value of current streak to 8
        update_habit(self.db, "type", 8)
        update_count(self.db, "type", 8)
        # check the current streak
        assert get_streak(self.db, "type") == 8
        assert get_longest_streak(self.db, "type") == 8
        # change the value of current streak to 5
        update_habit(self.db, "type", 5)
        assert get_streak(self.db, "type") == 5
        # check longest streak is 8 days
        assert get_longest_streak(self.db, "type") == 8
        # check functionality with 0
        assert get_longest_streak(self.db, "swim") is None

    def test_show_habits(self):
        # test all habits
        habits = show_habits(self.db)
        assert show_habits(self.db) is not None

    def test_habit_with_period(self):
        # test habit with different period
        period = get_period(self.db, "walk")
        period2 = get_period(self.db, "type")
        assert period == "daily"
        assert period2 == "weekly"

    def test_show_all_logs(self):
        # test habit logs
        verification(self.db, "type")
        show_all_logs(self.db, "swim")
        assert show_all_logs(self.db, "type") is None

    def test_last_checked(self):
        # test last entry
        verification(self.db, "swim")
        last_checked(self.db, "swim")
        assert last_checked(self.db, "swim") is not None

    def test_analyse(self):
        # test longest for all habit
        streak = get_streak(self.db, "swim")
        longest_of_all(self.db)
        assert streak == 4
        # longest of all is 10 (habit talk)
        assert longest_of_all(self.db) == 10


def teardown_method(self):
    import os
    pass
