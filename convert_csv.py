# convert_csv.py
# by James Pemantell
# _Illustrated Guide to Python_ Chapter 19, exercise 2
# convert a csv with name, address, and age to a list of dictionaries

from collections import defaultdict

with open('/Users/james/temp.csv', 'r') as fin:
    heading = list(fin.readline().rstrip('\n').split(','))
    big_list = fin.readlines()

address_list = []

for line in big_list:
    member = tuple(line.split(','))
    dynamic_dict = defaultdict(list)
    for heading_name in heading:
        dynamic_dict[heading_name]
    dynamic_dict['name'].append(member[0]) 
    dynamic_dict['address'].append(member[1])
    dynamic_dict['age'].append(int((member[2].strip('\n'))))  
    address_list.append(dynamic_dict)
    dynamic_dict = {} 

print(address_list)