print("Programa para calcular el presupuesto de 3 meses del año")

enero = int(input("Ingresa tu presupuesto del primer mes: "))
febrero = int(input("Ingresa tu presupuesto del segundo mes: "))
marzo = int(input("Ingresa tu presupuesto de del tercer mes: "))

presupuesto = enero + febrero + marzo
text = f"Su presupuesto es de = {presupuesto}"
print (text)

promedio = int(input("Ingrese la cantidad de meses en que se va a gastar el presupuesto: "))
presupuesto_final = presupuesto / promedio
print(f"Su presupuesto mensual final es de = {presupuesto_final}")

