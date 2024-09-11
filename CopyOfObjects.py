# Part 1: the assigment operator
    
data=[5,6,7]

bis=data

print(bis, id(bis))
bis.append(67)
print(bis)
print(data, id(data))

del bis
print(data)

# Part 2: the copy() method
data=[5,6,7]

bis=data.copy() # <=> bis=data[:]

print(bis, id(bis))
bis.append(67)
print(bis)
print(data, id(data))

del bis
print(data)

# Part 3: the copy module
    
data=[5,6,7]

import copy
bis=copy.copy(data) 

print(bis, id(bis))
bis.append(67)
print(bis)
print(data, id(data))

del bis
print(data)
