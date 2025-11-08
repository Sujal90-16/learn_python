# Good Morning sir
import time

hour = int(time.strftime('%H'))
print("Current Hour:", hour)

if hour >= 0 and hour < 12:
    print("Good morning sir!!")
elif hour >= 12 and hour < 16:
    print("Good afternoon sir!!!")
elif hour >= 16 and hour < 20:
    print("Good evening sir!!!")
else:
    print("Good night sir!!!")
