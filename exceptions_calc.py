import re

def check_numbers_input(my_nums):
    my_numbers = []
    for num_test in my_nums:
        # check for floating point number
        if type(num_test) == str:
            if re.search(r"\.", num_test):
                try: 
                    my_numbers.append(float(num_test))    
                except ValueError as e:
                    print("Value must be integer or floating point.")
                    print(e)
            else:
                try: 
                   my_numbers.append(int(num_test)) 
                except ValueError as e:
                    print("Value must be integer or floating point.")
                    print(e)
        elif (type(num_test) == int) or (type(num_test) == float):
                my_numbers.append(num_test)
    return tuple(my_numbers)

def perform_calc(user_nums,user_operator):
    if user_operator == '+':
        return user_nums[0] + user_nums[1]
    elif user_operator == '-':
        return user_nums[0] - user_nums[1]
    elif user_operator == '*':
        return user_nums[0] * user_nums[1]
    elif user_operator == '/':
        try:
            return user_nums[0] / user_nums[1]
        except ZeroDivisionError:
            print("Division by Zero is not permitted.")

def request_operator():
    accepted_operators = ('+','-','/','*')
    global user_input_operator
    while not user_input_numbers in accepted_operators:
        user_input_operator = input("""Enter a mathematical operator:
            +    addition
            -    subtraction
            /    division
            *    multiplication
            """)
        if user_input_operator in accepted_operators:
            return user_input_operator
        else: 
            print("You must choose an accepted operator from the list.")

user_input_numbers = tuple(input("Enter 2 numbers in the format X,Y: ").split(','))
checked_nums = check_numbers_input(user_input_numbers)
request_operator()
perform_calc(checked_nums, user_input_operator)
