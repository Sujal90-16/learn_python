# Dictionaries
dic = {
    "Sujal": "Human Being",
    "Spoon": "Object"
}
print(dic["Sujal"])

dicc = {
    321:"Shubham",
    230:"Sahil",
    454:"Rahul",
    675:"Yash"
}
print(dicc[321])

info = {"name":"Aryan", "age":19,"eligible":True}
print(info)
print(info.get("name2"))
print(info.get("eligible"))
print(info["name"])

# print(info["name2"])

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key ,value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
