#!/usr/bin/env python3

def return_age(value):
    next_age = (int(value) + 1)
    return next_age

value = input("How old are you? ")
next_age = return_age(value)

print("You will be {} years old next year.".format(next_age))
