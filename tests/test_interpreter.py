import datetime
import pytest
from classes.Interpreter import Interpreter


class TestInterpreter:
    test_hours = 13
    test_minutes = 21

    def get_interpreter(self):
        string = str(self.test_hours) + ':' + str(self.test_minutes)
        date = datetime.datetime.strptime(string, "%H:%M")
        return Interpreter(date)


    # test that given a datetime object, the constructor
    # correctly extracts the hours and stores as integer
    def test_constructor_assigns_hours(self):
        i = self.get_interpreter()
        assert i.hours == 1

    # test that given a datetime object, the constructor
    # correctly extracts the hours and stores as integer
    def test_constructor_assigns_minutes(self):
        i = self.get_interpreter()
        assert i.minutes == 21

    # test that hours are translated correctly
    def test_hours_translation(self):
        i = self.get_interpreter()
        assert i.translate_hours() == 'one'

    # test that standard minutes (i.e. 21) return translated correctly
    def test_standard_minute_translation(self):
        i = self.get_interpreter()
        assert i.translate_minutes() == 'twenty one minutes'

    # test that 30 minute values are translated to 'half'
    def test_thirty_minute_translation(self):
        i = Interpreter(datetime.datetime.strptime("13:30", "%H:%M"))
        assert i.translate_minutes() == 'half'

    # test that single minute values aren't added to a ten factor
    def test_single_minute_translation(self):
        i = Interpreter(datetime.datetime.strptime("13:04", "%H:%M"))
        assert i.translate_minutes() == 'four minutes'

    # test that response when on the hour returns an o'clock value
    def test_response_oclock(self):
        i = Interpreter(datetime.datetime.strptime("11:00", "%H:%M"))
        i.run()

        assert i.build_response() == "eleven o'clock"

    # test that response when mins<30 contains 'past'
    def test_response_minutes_past(self):
        i = Interpreter(datetime.datetime.strptime("11:30", "%H:%M"))
        i.run()

        assert ' past ' in i.build_response()

    # test that response when mins<30 contains 'to'
    def test_response_minutes_to(self):
        i = Interpreter(datetime.datetime.strptime("11:43", "%H:%M"))
        i.run()

        assert ' to ' in i.build_response()

    # test that Interpreter throws an error if input value becomes a string
    def test_exception_on_input_string(self):
        i = Interpreter(datetime.datetime.strptime("11:43", "%H:%M"))
        i.hours = '11'

        with pytest.raises(TypeError) as error:
            i.run()

    # test that hours are incremented in response for minutes>30
    def test_hours_incremented_for_minutes_over_30(self):
        i = Interpreter(datetime.datetime.strptime("11:43", "%H:%M"))
        returnval = i.run()

        assert returnval == 'Seventeen minutes to twelve'

    # test that 15mins past returns 'quarter'
    def test_15_mins_past_returns_quarter(self):
        i = Interpreter(datetime.datetime.strptime("11:15", "%H:%M"))
        returnval = i.run()

        assert returnval == 'Quarter past eleven'

    # test that 45mins past returns 'quarter' to next hour
    def test_45_mins_past_returns_quarter(self):
        i = Interpreter(datetime.datetime.strptime("11:45", "%H:%M"))
        returnval = i.run()

        assert returnval == 'Quarter to twelve'


