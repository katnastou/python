answer1 = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

list1 =list(range(1,101))
answer =  [x for x in list1 if x%12==0]

str1 = "amazing"
answer3 = [x for x in str1 if x not in "aeiou"]

#nested list comprehension

board = [[num for num in range(1,4)] for val in range(1,4)]

print(board)

tic = [["X" if num%2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
empty = [["*" for i in range(1,4)] for x in range(1,4)]