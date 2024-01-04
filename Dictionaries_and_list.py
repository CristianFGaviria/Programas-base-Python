person = {
    'name': 'Cristian',
    'lastName': 'Gaviria',
    'age': 29,
    'twitter': '@notengo'
}
person["name"] = "Cristian"
del person["age"]
my_list = list(person)
my_list2 = list(person.values())
print(my_list)
print(my_list2)