# Lists
marks = [3,7,4,"Sujal",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[-3])

if 7 in marks:
    print("Yes")
else:
    print("No")

# same thing applies for string as well
if "uja" in "Sujal":
    print("Yes")
else:
    print("No")

print(marks)
print(marks[:])
print(marks[1:-1])
print(marks[1:4:2]) #JumpIndex

#  list comprehension
lst = [i for i in range(4)]
print(lst)
lst = [i*i for i in range(7) if i%2==0 ]
print(lst)
