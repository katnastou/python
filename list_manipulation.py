'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list_in, com, loc, value=None):
    if com=="remove" and loc=="end" :
        last_val = list_in.pop()
        return last_val
        #remove last element pop
    elif com=="remove" and loc=="beginning" :
        first_val = list_in.pop(0)
        return first_val
        #remove first element shift
    elif com=="add" and loc=="beginning":
        list_in.insert(0,value)
        return list_in
        #add value to start unshift
    elif com=="add" and loc=="end":
        list_in.append(value)
        return list_in
        #add value to end push

list_manipulation([1,2,3], "remove", "end")