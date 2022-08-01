from datetime import datetime


class Clock:

    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def hour(self):
        return self.__hour

    def minute(self):
        return self.__minute

    def second(self):
        return self.__second

    def set_hour(self, new_hour):
        if isinstance(new_hour, int):
            self.__hour = new_hour
            while int(new_hour) < 0 or int(new_hour) > 23:
                raise ValueError("new_hour was not an number between 0 and 23")
        else:
            raise ValueError("new_hour passed to set_hour was not an integer")

    def set_minute(self, new_minute):
        if isinstance(new_minute, int):
            self.__minute = new_minute
            while int(new_minute) < 0 or int(new_minute) > 59:
                raise ValueError("new_minute was not an number between 0 and 59")
        else:
            raise ValueError("new_minute passed to set_minute was not an integer")

    def set_second(self, new_second):
        if isinstance(new_second, int):
            self.__second = new_second
            while int(new_second) < 0 or int(new_second) > 59:
                raise ValueError("new_second was not an number between 0 and 59")
        else:
            raise ValueError("new_second passed to set_second was not an integer")

    def advance_hour(self, amount_to_advance):
        if isinstance(amount_to_advance, int):
            self.__hour = amount_to_advance
            while int(amount_to_advance) < 0 or int(amount_to_advance) > 23:
                raise ValueError("amount_to_advance was not an number between 0 and 23")
        else:
            raise ValueError("amount_to_advance passed to advance_hour was not an integer")

    def advance_minute(self, amount_to_advance):
        if isinstance(amount_to_advance, int):
            self.__minute = amount_to_advance
            if self.__minute > 59:
                self.__minute = 60 - amount_to_advance
                self.__hour = self.__hour + 1
                if self.__hour > 23:
                    self.__hour = 0
            while int(amount_to_advance) < 0 or int(amount_to_advance) > 59:
                raise ValueError("amount_to_advance was not an number between 0 and 59")
        else:
            raise ValueError("amount_to_advance passed to advance_minute was not an integer")

    def set_to_current_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    def __str__(self):
        return "%s:%s:%s" % (self.__hour, self.__minute, self.__second)

    def __repr__(self):
        return "%s:%s:%s" % (self.__hour, self.__minute, self.__second)

    def __eq__(self, other):
        if isinstance(other, Clock):
            return self.__hour == other.hour() and self.__minute == other.minute() and self.__second == other.second()
        return False

    def __lt__(self, other):
        if isinstance(other, Clock):
            if self.__hour < other.__hour:
                return True
            elif self.__hour == other.__hour and self.__minute < other.__minute:
                return True
            elif self.__hour == other.__hour and self.__minute == other.__minute and self.__second < other.__second:
                return True
            else:
                return False

        raise Exception("other argument to less than was not a Clock: " % other)

    def __gt__(self, other):
        if isinstance(other, Clock):
            if isinstance(other, Clock):
                if self.__hour > other.__hour:
                    return True
                elif self.__hour == other.__hour and self.__minute > other.__minute:
                    return True
                elif self.__hour == other.__hour and self.__minute == other.__minute and self.__second > other.__second:
                    return True
                else:
                    return False

            raise Exception("other argument to greater than was not a Clock: " % other)
