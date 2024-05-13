# Using slicing:

string = "Hello"
reversed_string = string[::-1]
print(reversed_string)

# With the reversed() function and join():

string = "Hello"
reversed_string = ''.join(reversed(string))
print(reversed_string)


# By creating a loop:

string = "Hello"
reversed_string = ''
for char in string:
    reversed_string = char + reversed_string
print(reversed_string)

# Using recursion:

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

string = "Hello"
reversed_string = reverse_string(string)
print(reversed_string)

