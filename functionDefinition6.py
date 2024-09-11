
fct1(2,3)

# variable number of arguments:
def fct1(a, *args):
    print(args)


nb=12
result=fct1(nb, 56)
print(result)
result=fct1(2,3,4,True,"abc")
print(result)
result=fct1()
print(result)


def mysum(*numbers):
    total=0
    for e in numbers:
        total += e
    return total

print(mysum(5,6,7,10,20))
print(mysum())
print(mysum(100,200))


somme=mysum # somme is now an alias of mysum

print(somme(6,7,8))
print(mysum(6,7,8))




