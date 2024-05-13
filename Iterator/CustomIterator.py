class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            result = self.start
            self.start += 1
            return result

my_range = MyRange(1,5)

for number in my_range:
    print(number)

