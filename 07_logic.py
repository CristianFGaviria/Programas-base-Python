# and
print ("AND")
print ("true AND true =>", True and True)
print ("true AND false =>", True and False)
print ("false AND true =>", False and True)
print ("false AND false =>", False and False)

#age = int(input("Ingresa tu edad: "))
#print(age > 17 and age >= 18)

# OR
print ("OR")
print ("true AND true =>", True or True)
print ("true AND false =>", True or False)
print ("false AND true =>", False or True)
print ("false AND false =>", False or False)

#role = input("Digita el Rol => ")
#print(role == "Admin" or role == "Seller" )

# NOT
print(not True)
print(not False)
print ("true AND true =>", not (True and True))
print ("true AND false =>", not (True and False))
print ("false AND true =>", not (False and True))
print ("false AND false =>", not (False and False))

age = int(input("Ingresa tu edad: "))
print(not (age > 17 and age >= 18))