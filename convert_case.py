def convert_case(my_string, separator):
    my_string_list = []
    if (separator != '_') and (separator != '-'):
        print("Only - and _ are valid separators.")
    else:
        for char in my_string:
            # Do not append separator to the first list element
            if char.isupper() and char == my_string[0]:
                my_string_list.append(char.swapcase())
            elif char.isupper() and char != my_string[0]:
                my_string_list.append(separator+char.swapcase())
            elif char.islower():
                my_string_list.append(char)
    return "".join(my_string_list)      

my_string = 'JamieTestVariable'
convert_case(my_string,'_')