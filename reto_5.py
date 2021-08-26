import json

with open("cliente_merquefacil.json","r") as archivo:
	cliente_mercado=json.load(archivo)
	print("Archivo Importado Exitosamente")

def menu():
	opcion=input("\n****Menu opciones****\n (1)Calculo de subtotales.\n (2)Calculo de descuentos.\n (3)Imprimir factura\n (4)Salir del sistema\n Digita la Opcion: ")
	return opcion
	

def subtotales():
	print("**********SUBTOTALES**********")
	print("\n")
	print("|{:<8}|{:<15}|{:<10}|".format("CODIGO","ARTICULO","SUBTOTAL"))
	for i in range(len(cliente_mercado)):
		cliente_mercado[i]["Subtotal"]=cliente_mercado[i]["Valor"]*cliente_mercado[i]["Cantidad"]
		print("|{:<8}|{:<15}|{:<10}|".format(cliente_mercado[i]["Codigo"],cliente_mercado[i]["Nom_articulo"],cliente_mercado[i]["Subtotal"]))

def descuento():
	print("**********DESCUENTO**********")
	print("\n")
	print("|{:<8}|{:<15}|{:<10}|{:<10}|".format("CODIGO","ARTICULO","CANTIDAD","DESCUENTO"))
	porcen=0.5
	for i in range(len(cliente_mercado)):
		if cliente_mercado[i]["Cantidad"]>5:
			cliente_mercado[i]["Subtotal"]=cliente_mercado[i]["Valor"]*cliente_mercado[i]["Cantidad"]
			cliente_mercado[i]["Descuento"]=cliente_mercado[i]["Subtotal"]*porcen
			print("|{:<8}|{:<15}|{:<10}|{:<10}|".format(cliente_mercado[i]["Codigo"],cliente_mercado[i]["Nom_articulo"],cliente_mercado[i]["Cantidad"],cliente_mercado[i]["Descuento"]))

def factura():
	print("**********FACTURA**********")
	print("\n")
	print("|{:<8}|{:<15}|{:<10}|{:<10}|{:<10}|{:<10}|".format("CODIGO","ARTICULO","VALOR","CANTIDAD","SUBTOTAL","DESCUENTO"))
	for i in range(len(cliente_mercado)):
		print("|{:<8}|{:<15}|{:<10}|{:<10}|{:<10}|{:<10}|".format(cliente_mercado[i]["Codigo"],cliente_mercado[i]["Nom_articulo"],cliente_mercado[i]["Valor"],cliente_mercado[i]["Cantidad"],cliente_mercado[i]["Subtotal"],cliente_mercado[i]["Descuento"]))#formato para que todo este en columnas.
	cont=0
	conte=0	
	for x in range(len(cliente_mercado)):
		sub=cliente_mercado[x]["Subtotal"]
		des=cliente_mercado[x]["Descuento"]
		cont+=sub
		conte+=des
	print("\nTOTAL A PAGAR: ",cont-conte)



opcion=" "
while opcion!="4":
	opcion=menu()
	
	if opcion=="1":
		subtotales()

	if opcion=="2":
		descuento()

	if opcion=="3":
		factura()

	if opcion=="4":
		print("\nTermino el programa")