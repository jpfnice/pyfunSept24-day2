

phone={"Julia":56789, "Marc":56554, "Martin":78776, "Dave":87766}

print(len(phone))
print(phone)

print(phone["Marc"])
print(phone.get("Marc"))

for k in phone:
    print(k)

for v in phone.values():
    print(v)

for pair in phone.items():
    print(pair)

for k,v in phone.items():
    print(k,v)
    
phone["Maria"]=98887 # A new pair is added
print(len(phone))
print(phone)

phone["Marc"]=98767 # To update Marc's phone number

if "Martin" in phone:
    print(phone["Martin"])
    
#print(phone["Martini"])

del phone["Marc"] # <=> phone.pop("Marc)
print(phone)

