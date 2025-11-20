# Tuples
tup = (1,4,7,"Sujal", True)
tu = (1)
print(type(tu))
tu = (1,)
print(type(tu)) 
print(tup)
print(tup[0])
print(tup[-1])
print(type(tup))

if 4 in tup:
    print("4 is presnt in tuple")
else:
    print("4 is not present in the tuple")

tup2 = tup[1:4]
print(tup2)
