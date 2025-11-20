# Operations in Tuples
countries = ("spain","italy","india","england","germany")
temp =list(countries)
temp.append("russia")     #add item
temp.pop(4)               #remove item
temp[2]="finland"         #change item
countries=tuple(temp)
print(countries)

country1 = ("pakistan","bangladesh","afganisthan","srilanka")
country2 = ("india","vietnam","china")
SEA = country1 + country2
print(SEA)

tuple1 = (1,2,3,2,1,4,5,6,4,7,3,8,5,4,9,4,6,3,4)
res = tuple1.count(4)
rest = tuple1.index(3,10)
print("count of 4 in tuple1 is :",res)
print("index of 3 in tuple1 is :",rest)
