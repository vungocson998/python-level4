# In python, we dont need to care about large number
# In C, this operation might be overflow
#print(2**1000000, "\n")
#print(len(str(2**1000000))) # Number of digits on result

# Import math module

import math

print(math.pi)
print(math.sqrt(81))

# Import random module

import random
i = 0
for i in range(0,3):
    print(random.random())
    i = i + 1

i = 0
for i in range(0,3):
    print(random.choices([1,2,3]))
    i = i + 1

