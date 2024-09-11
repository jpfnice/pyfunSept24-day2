
"""
a str is "sequence":
    len(), for, in, not in, [], [:], [::], +, *, ...
"""
# Creation of a string with a "formatted" string

nb=3
text=f"nb is {nb} nb ** 2 is {nb**2}" 
print(text)

nb=99
text=f"nb is {nb} nb/3 is {10/3}" 
print(text)

nb=99
text=f"nb is {nb:>10} nb/3 is {10/3:.2f}" 
print(text)

