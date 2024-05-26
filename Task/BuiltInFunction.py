def show(num):
    
    if num%2==0:
        return "even"
    else:
        return "odd"
    
lst = [1,2,3,4,5,6]
m = map(show,lst)
print(list(m))

# Using lamda expression
m1 = map(lambda num : "even" if num%2==0 else "odd", lst)
print(list(m1))

# reduce function
from functools import reduce
lst2 = [14,32,31,34]
print(reduce(lambda x,y : x+y , lst2))

# zip function
# its return list of tuple
x = [1,2,3]
y = [4,5,6]
print(list(zip(x,y)))

# zip 
d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}
print(list(zip(d1,d2)))

# unzip
a = list(zip(d1,d2))
b,c = zip(*a)
print(b)
print(c)

# enumerate
lst3 = ['a','b','c']
for number ,item in enumerate(lst3, start=1):
    print(number,item)
    
month = ['january','Febuary','March' ]
print(list(enumerate(month,start=1)))