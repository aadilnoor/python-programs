def generator():
        
        n=1
        while n<=10:
             agr=n*n
             yield agr
             n=n+1
o=generator()
print(next(o))
print(next(o))
for j in o :
    print(j)
    