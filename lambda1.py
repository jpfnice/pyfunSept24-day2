data=[5,6,-2,4,10,-2,7,-23]

newlist=[]
for e in data:
    newlist.append(e**2)
print(newlist)

newlist=[e**2 for e in data] # a "list comprehension"
print(newlist)

# def f1(a):
#     return a**2

newlist=list(map(lambda a: a**2, data))
print(newlist)

text="12,34,56,67,78,78"
result=text.split(",")
result=list(map(int, result))
print(result)

data=[5,6,-2,4,10,-2,7,-23,77]

# def f2(a):
#     return a > 0

result=list(filter(lambda a: a>0, data))
print(result)

# def even(a):
#     return a % 2==0

result=list(filter(lambda a: a%2==0, data))
print(result)