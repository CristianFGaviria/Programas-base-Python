numbers = (1,2,3,4,5,6)
strings = ("Cristian", "Geraldine", "Sol")
print (strings)
print(type(strings))
print("0 =>" , strings[0])
print("-1 =>" , strings[-1])



my_list = list(strings)
print (my_list)
print(type(my_list))

my_list.append("Blanca")
my_list.append("Fernando")
print (my_list)

my_tuple = tuple(my_list)
print (my_tuple)