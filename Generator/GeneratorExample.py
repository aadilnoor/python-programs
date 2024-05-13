def number():
    num = 1
    while num <= 100:
        yield num
        num += 1
        
for number in number():
    print(number)
