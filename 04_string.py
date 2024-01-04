name = "Cristian"
print("name")
last_name = "Gaviria Leon"
print(last_name)

age = 28

full_name = name + " " +last_name
print(full_name)

quote = "I'm Cristian"
print(quote)

quote2 = 'She said "Hello" '
print(quote2)

# primera forma de dar format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template)

#segunda forma de dar format
template2 = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template2)

#tercera forma de dar format y mejor
template3 = f"Hola, mi nombre es {name} mi apellido es {last_name} y mi edad es {age} años"
print(template3)