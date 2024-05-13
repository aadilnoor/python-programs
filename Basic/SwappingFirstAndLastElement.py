

from doctest import OutputChecker


mylist = [12, 35, 9, 56, 24]
mylist[0], mylist[-1] = mylist[-1], mylist[0]
print("Swapping List :", mylist)

# Output [24,35,9,56,12]