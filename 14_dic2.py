person = {
  "name" : "Cristian",
  "las_name": "Gaviria",
  "langs": ["python", "golang"],
  "age": 28
}
print(person)
person["name"] = "Geraldine"
person["age"] -= 6
person["langs"].append("Enfermeria")


del person["las_name"]
#person.pop("age")
print(person)

print("items")
print(person.items())

print("keys")
print(person.keys())

print("values")
print(person.values())
