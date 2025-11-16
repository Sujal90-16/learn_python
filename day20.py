# function arguements
# default arguements
def average(a = 5, b = 9):
    print("The average is", (a+b)/2)
average()

# keyword arguements
def average(a, b ):
    print("The average is", (a+b)/2)
average(a = 12, b = 10)

# required arguements
def average(a, b, c=3):
    print("The average is", (a+b+c)/2)
average(12,5)

# variable length arguement
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + 1
    print("the average is", sum/len(numbers))
average(4,6,9,3,5,7,2)