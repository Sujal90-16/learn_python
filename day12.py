# String Methods
# strings are immutable
a = "!!!!Sujal!! !!Sujal!! "
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Sujal","rohan"))
print(a.split(" "))

blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

strr = "Welcome to the console !!!!!"
print(strr.center(60))
print(len(strr.center(60)))
print(len(strr))
print(a.count("Sujal"))

ster = "Welcome to the console !!"
print(ster.endswith("!!")) 
print(a.endswith("!!"))
print(ster.endswith("to",4,10))

sta = "He's name is Don. He is an honest man"
print(sta.find("is"))
print(sta.find("ishh"))
print(sta.index("is"))
# print(sta.index("ishh"))
print(sta.isalnum())
print(sta.islower())
print(sta.isupper())
print(sta.isalpha())
print(sta.isprintable())
print(sta.isspace())
print(sta.istitle())
print(sta.startswith("He's"))
print(sta.swapcase())
print(sta.title())

stt = "WelcomeToTheConsole"
print(stt.isalnum())
print(stt.isalpha())
print(stt.islower())
print(stt.isprintable())
print(stt.isspace())
print(stt.istitle())
print(stt.isupper())
print(stt.startswith("He's"))
print(stt.swapcase())
print(stt.title())