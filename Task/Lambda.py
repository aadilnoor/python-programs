a = lambda a : print("My name is",a)
a("Aadil")


# Using lambda function to check even or odd number

# Get input from the user
numbers = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input into a list of integers
numbers = [int(num) for num in numbers]

# Check if each number is even or odd using lambda function
results = list(map(lambda num: "even" if num % 2 == 0 else "odd", numbers))

# Print the results
for num, result in zip(numbers, results):
    print("Number {} is {}".format(num, result))