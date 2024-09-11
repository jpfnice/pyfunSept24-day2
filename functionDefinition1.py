
def fct1(a, b):
    temp=a*b  # temp is a "local" variable
    return temp


nb=10 # is a "global" variable
result=fct1(nb, 56) # positional arguments
print(result)

result=fct1("ab", 4)
print(result)
    
# result=fct1("ab", "de") # Exception !!
# print(result)

# #print(nb, nb**2, sep="-")

result=fct1(a="ab", b=4) # named arguments
print(result)

result=fct1("ab", b=4)
print(result)