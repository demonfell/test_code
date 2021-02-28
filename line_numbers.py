#!/usr/bin/env python3
import sys
from os import path

file_to_modify = sys.argv[1] 

try: 
    fin = open(file_to_modify, 'r')
    file_data = fin.readlines()
    fin.close()

except FileNotFoundError:
        print('File must exist')
        sys.exit(1)
except:
    print('File must be readable.')

replacement_data = []
try:
    for i in range(0,len(file_data)):
        replacement_data.append("{} {}".format(i+1, file_data[i]))  
except NameError:
        print("Data could not be read!")
try:
    with open(file_to_modify,'w') as fout:
        for x in replacement_data:
            fout.write(x)
except:
    print("File must be writable.")
