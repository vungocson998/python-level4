# String is immutable in python
# Slicing
# Formating
# Trinple quotes
# Find and replace pattern
# Split
# Upper and lower
# Using dir and help function
# Some functions build-in string obj
# Advanced: pattern processing


myString1 = "Hello, world"

print(len(myString1))
print(myString1[7::])

myString2 = "1234"
print(myString2[::-1])
print(myString2*4)
print(myString2 + "5678")
#Type error: print(myString2 + 5678)

# String is immutable in python
myString3 = "Ted"
# So we can change directly character in-placed
# myString3[0] = 'C' #Error
# But we can do this instead
myString3 = 'C' + myString3[1::]
print(myString3)

# Find pattern
print(myString1.find("world"))

# Replace patter
print(myString1.replace("world", "my world"))

# Split
myString4 = "aaa,bb,cccc,dddd"
print(myString4.split(',')) # list type

# Upper and lower case
print(myString4.upper())
print(myString4.lower())

# isalpha() isdigit()
print("abcad".isalpha())
print("123".isdigit())

# remove white space on the right site
print("adasdad\n\n\n\n")
print("ahasdha\n\n\n\n".rstrip())
print("Test")

# formating
print("Number: {0}, Name: {1}, age: {2}".format(1, "Ted", 20))

# getting help: 
# dir function return all the attributes of object
# help function
print(dir("string"))
#help("string".encode)

# print charactor ASCII code
print(ord('A'))

# use triple quotes to print multiline string
print("""Hello,
My name is TED,
and i am coding python""")

# Advanced: pattern matching
import re
match1 = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
print(match1.groups())