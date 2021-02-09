import math
import datetime


class Interpreter:
    # constructor
    def __init__(self, input_value: datetime.datetime):
        self.hours = int(input_value.strftime("%I"))
        self.minutes = int(input_value.strftime("%M"))
        self.operator = None
        self.translated_hours = None
        self.translated_minutes = None


    # Kick off the interpreting
    def run(self) -> str:
        # quick sanity check
        if isinstance(self.hours, int) is False or isinstance(self.minutes, int) is False:
            raise TypeError("Input data must be an integer value")

        '''
        first let's work out whether the minutes are zero, greater than 30 or less than 30
        this will give us our operator (to/past)
        '''
        if self.minutes == 0:
            # minutes are zero - it's on the hour so we don't need an operator
            self.operator = False

        elif self.minutes > 30:
            # minutes are greater than 30 - we should use 'to' (20 to 4)
            self.operator = 'to'

            # also, if the operator is 'to', we need to subtract the minutes from the hour
            self.minutes = 60 - self.minutes

            # we also need to increment the hour by one if the operator is static
            self.hours += 1

            # cast back to hours so that we still get '1' and not '13' if previous number was 12
            updated_hours = datetime.datetime.strptime(str(self.hours), "%H").strftime("%I")
            self.hours = int(updated_hours)

        else:
            # minutes are 30 or under - we should use past (20 past 4)
            self.operator = 'past'

        # now we know our operator, we can send off the minutes for interpretation
        if self.minutes > 0:
            self.translated_minutes = self.translate_minutes()

        # translate the hours
        self.translated_hours = self.translate_hours()

        # put it all together
        translated_string = self.build_response()

        # return the result
        return translated_string.capitalize()


    # parse the hours into a human readable format
    def translate_hours(self) -> str:
        # map 12 hour to array key and return
        hour_map = ['twelve', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                    'twelve']

        return hour_map[self.hours]


    # parse the minutes into a human readable format
    def translate_minutes(self) -> str:
        # init return val list
        return_val = []

        # firstly, let's take care of the easy one
        if self.minutes == 30:
            return 'half'
        else:
            # cast our tens and singles so that we can map values to indices
            tens = ["", "", "twenty", "thirty", "forty", "fifty"]
            singles = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                       "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen",
                       "twenty"]

            # get the number of tens in minutes by dividing the minutes by 10 and flooring it
            m_tens = math.floor(self.minutes / 10)

            # if the minute value when divided by 10 and floored is zero or one (i.e. it's 19 or under)
            if m_tens <= 1:
                # we only need to return a single number rather that a combination of tens and singles.
                return_val.append(singles[self.minutes])
            else:
                # otherwise, used the floored value to fetch the 10's multiple
                mins_list = [tens[int(m_tens)], singles[(self.minutes % 10)]]

                '''
                mins_list will have an empty item if time is a factor of 10
                so let's filter the list to remove them
                '''
                filtered_list = filter(lambda x: x != '', mins_list)

                # convert to a ' ' separated string and append to the return list
                return_val.append(' '.join(filtered_list))

            '''
            finally, if the resulting number is not divisible by 5, add 'minutes'
            just because "eight minutes to four" is more semantic than "eight to four"
            but "ten to four" is more semantic than "ten minutes to four"
            '''
            if self.minutes % 5:
                return_val.append("minutes" if self.minutes > 1 else "minute")

            # list to string
            return ' '.join(return_val)


    # Build the response to return to the view
    def build_response(self) -> str:
        # hours only - no minutes
        if self.operator is False:
            return self.translated_hours + " o'clock"
        else:
            # minutes + {past|to} + hour
            return self.translated_minutes + " " + self.operator + " " + self.translated_hours
