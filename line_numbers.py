import sys
from os import path

file_to_modify = sys.argv[1]

# currently, the script will operate on a file that does not exist
# and produce an empty file. I'd like to wok around that. Looking at 
# solution from https://docs.python.org/3/tutorial/errors.html
# try: 
#    path.isfile(file_to_modify)
# except: 
#    raise Exception 
#    print("File must exist.")
    
try: 
    with open(file_to_modify, 'r') as fin:
        file_data = fin.readlines()
except:
    print("File must be readable.") 

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