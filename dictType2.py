

phone={"Julia":[56789], "Marc":[56554, 78777], "Martin":[], "Dave":[87766]}

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
    
phone["Maria"]=[98887] # A new pair is added
print(len(phone))
print(phone)

phone["Marc"].append("65555") # To update Marc's phone number
print(phone)
if "Martin" in phone:
    print(phone["Martin"])
    
#print(phone["Martini"])

del phone["Marc"] # <=> phone.pop("Marc)
print(phone)

