# f-strings
letter = "Hey my name is {} and i am from {}"
country = "India"
name = "Sujal"
print(letter.format(name , country))
print(letter.format(country , name))
print(f"Hey my name is {name} and i am from {country}")
print(f"we use f-string like this:- Hey my name is {{name}} and i am from {{country}}")
print(f"we use f-string like this:- Hey my name is {{name}} and i am from {country}")

price = 103.8756
txt = f"for only {price:.2f} dollars!"
# print(txt.format(price=103.8756)) 
print(txt)
print(f"{2* 60}")
print(type(f"{2* 60}"))