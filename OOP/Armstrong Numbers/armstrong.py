"Hi. My name is Pranav Ramakrishnan. This is my submission for Assignment 1 regarding calculating Armstrong Numbers."


def get_input():
    user_input = input("Enter an integer from 10 through 100,000,000: ")
    while user_input.isnumeric() is False or int(user_input) < 10 or int(user_input) > 100000000:
        user_input = input("Please only enter an integer between 10 and 100,000,000! Try again: ")

    return int(user_input)


def calculate_armstrong(num):
    print("The Armstrong Numbers between 10 and", num, "are:\n")
    count = 0
    for val in range(10, num + 1):
        current_number = val
        n = len(str(val))
        digit_sum = 0
        while current_number > 0:
            digit = current_number % 10
            current_number = current_number // 10
            digit_sum = digit_sum + digit ** n
        if digit_sum == val:
            count = count + 1
            print(val)
    print("\nThe total number of Armstrong Numbers is", count)


max_num = get_input()
calculate_armstrong(max_num)
