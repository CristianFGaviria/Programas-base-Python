# CRUD crear, leer actualizar o eliminar

numbers = [1,2,3,4,5]
print(numbers[1])
numbers[-1] = 10
print (numbers)

numbers.append(700)
print (numbers)

numbers.insert(0, "hola")
print (numbers)

numbers.insert(3, "change")
print(numbers)

task = ["todo 1" , "todo 2", "todo 3"]
new_list = numbers + task
print(new_list)

index = new_list.index("todo 2")
new_list[index] = "todo changed"
print (new_list)

new_list.remove("todo 1")
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1,4,6,5,3]
numbers_a.sort()
print (numbers)

strings = ["re" , "ab", "ed"]
strings.sort()
print (strings)
