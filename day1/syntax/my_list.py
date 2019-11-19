# Ordered colections and no-fixed size
# Not immutable --> can change value of elements
# Slicing
# Contatenation
# append(), pop(), sort(), reverse()

# Bound checking: although list has no fixed-size 
# but python does not allow us to reference items that are not present

# Nesting: we offen use numpy instead

# Advanced: Comprehensions

# append(), pop(), sort(), reverse()
list1 = [1,2,5,123,5123,5,1,123,5]
print(type(list1))

list1.append(1000000)
list1.sort()
print(list1)
print(list1.pop(len(list1)-1))

list1.reverse()
print(list1)

list2 = ["A", "b", "a"]
list2.sort()
print(list2)

# Advanced: Comprehensions
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

col2 = [row[1]for row in M]
print(col2)

col2_plus_1 = [row[1] + 1 for row in M]
print(col2_plus_1)

col2_even_elements = [row[1] for row in M if row[1]%2 == 0]
print(col2_even_elements)

#diagonal matrix: ma tran duong cheo
diagonal = [M[i][i] for i in [0, 1, 2]]
print(diagonal)