dict = {"Vasya": 1975, "Egor":1999, "Masha":2002}
print(dict)
print(dict["Egor"])
print(dict.get("Max"))
dict.update({"Sasha":2001})
print(dict)
a = dict.pop("Vasya")
print(dict)
print(a)