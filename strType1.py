
"""
a str is "sequence":
    len(), for, in, not in, [], [:], [::], +, *, ...
"""
# Creation

text="First 'abc' example"
print(text)

text='First "abc" example'
print(text)

text="First \
'abc' \
example"

print(text)

text="""First 

example"""
print(text)

text='''First 
another
line
example'''
print(text)

nb=str(3.45)
print(nb, type(nb))
