string = raw_input()
l=list(string)
a,b,c,d,e=False,False,False,False,False
for i in l:
    if i.isalnum():
        a=True
    if i.isalpha():
        b=True
    if i.isdigit():
        c=True
    if i.islower():
        d=True
    if i.isupper():
        e=True
print a
print b
print c
print d
print e
