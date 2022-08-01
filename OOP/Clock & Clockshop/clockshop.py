from clock import Clock


class ClockShop:

    def __init__(self):
        self.__list_of_clocks = []

    def fill_clock_shop(self, list_of_times):
        for string in list_of_times:
            clock_list = string.split(':')
            hour = int(clock_list[0])
            minute = int(clock_list[1])
            second = int(clock_list[2])
            clock_object = Clock()
            clock_object.set_hour(hour)
            clock_object.set_minute(minute)
            clock_object.set_second(second)
            self.__list_of_clocks.append(clock_object)

    def sort_clocks(self):
        """
        Credit to Darence Thong
        """
        self.__list_of_clocks = self.merge_sort(self.__list_of_clocks)

    def merge_sort(self, __list_of_clocks):
        """
        Credit to Darence Thong
        """
        if len(__list_of_clocks) > 1:
            split = len(__list_of_clocks) // 2
            left = __list_of_clocks[:split]
            right = __list_of_clocks[split:]
            left = self.merge_sort(left)
            right = self.merge_sort(right)
            output = []
            left_index = 0
            right_index = 0
            inst_c = 0
            while left_index < len(left) and right_index < len(right):
                inst_c += 1
                if left[left_index] < right[right_index]:
                    output.append(left[left_index])
                    left_index += 1
                else:
                    output.append(right[right_index])
                    right_index += 1
            while left_index < len(left):
                output.append((left[left_index]))
                left_index += 1
            while right_index < len(right):
                output.append(right[right_index])
                right_index += 1
            return output
        return __list_of_clocks

    def find_clock(self, a_clock):
        for i, clock in enumerate(self.__list_of_clocks):
            if clock == a_clock:
                return i
        else:
            return -1

    def __str__(self):
        string_list = ''
        for obj in self.__list_of_clocks:
            string_list += str(obj) + '\n'
        return string_list

    def get_clock(self, index):
        if index < 0:
            raise ValueError('Cannot enter negative index')
        elif index > len(self.__list_of_clocks) - 1:
            raise ValueError('ClockShop is empty, no clocks')
        else:
            for i, clock in enumerate(self.__list_of_clocks):
                if i == index:
                    return clock

    def set_clock(self, a_clock, index):
        if len(self.__list_of_clocks) == 0:
            raise ValueError('No clocks to set value')
        elif index < 0 or index > len(self.__list_of_clocks):
            raise ValueError('You cannot enter negative value or it is beyond range for index')
        self.__list_of_clocks[index] = a_clock
