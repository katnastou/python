list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(0,len(list1))}

"""
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
dict(zip(list1,list2))  
"""

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {person[i][0]:person[i][1] for i in range(0,len(person))}

#answer = {thing[0]: thing[1] for thing in person}
#answer = {k:v for k,v in person}
#answer = dict(person)