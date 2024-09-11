
def fct1(a=1, b=1):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        temp=a*b
        return temp
    else:
        print("Wrong arguments types !")
        return None


nb=12
result=fct1(nb, 56)
print(result)
result=fct1(nb)
print(result)
result=fct1()
print(result)