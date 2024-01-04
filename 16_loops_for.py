'''
for element in range(1, 21):
  print (element)
'''
my_list = [23, 24, 85, 50, 43]
for element in my_list:
  print (element)

my_tuple = ("Geras" , "Blanca", "Fercho")
for element in my_tuple:
   print (element)

product ={
  "name": "Camisa",
  "price": 100,
  "Stock": 89
}

for key in product:
  print (key, "=>" , product[key])

for key, value in product.items():
  print(key,"=>", value)