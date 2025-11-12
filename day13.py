#  If-else conditional Statements
# # conditionals operators
# # <,>,<=,>=,==,!=
# print(age<18)
# print(age<=18)
# print(age>=18)
# print(age==18)
# print(age!=18)

# if-else
age = int(input("Enter your age: "))
print("Your age is: ",age)
if(age >= 18):
    print("Eligible to Drive")
else:
    print("You are not eligible to Drive")
print("Hello")


# elif
num = int(input("Enter the value of num: "))
print("Your num is: ",num)
if(num < 0):
    print("Number is negative")
elif(num == 0):
    print("Number is zero")
elif(num == 999):
    print("Number is special")
else:
    print("Number is positive")
print("I am happy now")

# nested if-else
n = int(input("Enter the number: "))
print("Your number is: ",n)
if(n < 0):
    print("Number is negative")
elif(n > 0):
    if(n <= 10):
        print("Number is between 1-10")
    elif(n >10 and n<=20):
        print("Number is between 11-20")
    else:
        print("Number is geater than 20")
else:
    print("Number is zero")
print("I am satisfied with the output")