# Create a file name data.txt and write "Hello, world!"
# Understand w, r, a, rb, w+, r+, a+

# w mode
f = open("data.txt", 'w')
f.writelines("Hello, world!\n")
f.close()

# a mode
f = open("data.txt", 'a')
f.writelines("Hello, world!\n")
f.close()

# r mode
f = open("data.txt", "r")
data = f.read()
f.close()
#print(data)

#rb mode
f = open("data.txt", "rb")
bin_data = f.read()
f.close()
#print(bin_data)

#w+ mode
f = open("data.txt", "w+") #Truncate
f.write("New line.")
new_data = f.read() #Can not read any things
print(new_data)
f.close()

#r+ mode
f = open("data.txt", "r+")
f.write("New line 2.")
new_data = f.read() #Can not read any things
print(new_data)
f.close()

#a+ mode
f = open("data.txt", "a+")
f.write("New line 3.")
new_data = f.read() #Can not read any things
print(new_data)
f.close()