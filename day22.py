# List Methods 
l = [7,3,9,1,2,8,6,4,5]
print(l)
l.append(10)
print(l)
l.sort()
print(l) 
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l.count(1))
m = l.copy()
m[0] = 0
print(m) 
print(l.insert(1, 345))

n = [900,1200,1500]
l.extend(n)
print(l)

k = l + n
print(k)
