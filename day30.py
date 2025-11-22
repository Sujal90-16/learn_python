# String Methods
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
print(s1.union(s2))
print(s1, s2)
s1.update(s2)
print(s1, s2)

print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1, s2)

print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1, s2)

print(s1.difference(s2))
s1.difference_update(s2)
print(s1, s2)

print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))

s1.add(17)
print(s1)
s1.remove(2)
print(s1)
s1.discard(17)
print(s1)

s1.pop()
print(s1)

del s1
print(s1)

s1.clear()
print(s1)

info = {"kapil",2,5,True,4.5,7.8}
if "kapil" in info:
    print("Kapil is present")
else:
    print("Kapil is not present")
