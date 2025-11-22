# Dictionaries methods
info = {"name":"Aryan", "age":19,"eligible":True}
print(info)
info.update({"age":23})
info.update({"DOB":2003})
print(info)
emp1 = {122 : 34, 234 : 45, 677 : 87, 786 : 90, 453 : 74, 546 : 74}
emp2 = {132 : 24, 354 : 42, 574: 47, 865 : 66}
emp1.update(emp2)
print(emp1)

emp1.clear()
print(emp1)

empt ={}
print(empt)

emp1.pop(122)
print(emp1)

emp1.popitem()
print(emp1) 

del emp1[122]
print(emp1)
