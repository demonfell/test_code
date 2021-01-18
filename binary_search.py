animal_list = ['anteater',
 'antelope',
 'bird',
 'cat',
 'deer',
 'monkey',
 'penguin',
 'snake',
 'turtle',
 'walrus',
 'zebra']

def list_bisect(search_term, list_name):
    mid = int(len(list_name)/2)+1
    end = len(list_name)
    if list_name[mid][0] <= search_term[0]:
        for i in range(0,mid):
            if search_term == list_name[i]:
                return i
    elif list_name[mid][0] >= search_term[0]:
        for i in range(mid,end):
            if search_term == list_name[i]:
                return i
    else: 
        return -1

list_bisect('monkey', animal_list)

            
