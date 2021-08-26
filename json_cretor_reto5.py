import json

lista_articulos=[
{
	"Codigo":10,
	"Nom_articulo":"jabon",
	"Valor":2500,
	"Cantidad":6,
	"Subtotal":0.0,
	"Descuento":0.0
},
{
	"Codigo":20,
	"Nom_articulo":"crema",
	"Valor":9800,
	"Cantidad":4,
	"Subtotal":0.0,
	"Descuento":0.0
},
{
	"Codigo":30,
	"Nom_articulo":"cepillo",
	"Valor":6000,
	"Cantidad":7,
	"Subtotal":0.0,
	"Descuento":0.0
},
{
	"Codigo":40,
	"Nom_articulo":"servilletas",
	"Valor":3000,
	"Cantidad":2,
	"Subtotal":0.0,
	"Descuento":0.0
},
{
	"Codigo":50,
	"Nom_articulo":"desodorante",
	"Valor":5000,
	"Cantidad":6,
	"Subtotal":0.0,
	"Descuento":0.0
}
]

print(lista_articulos)

with open("cliente_merquefacil.json","w") as archivo:
	json.dump(lista_articulos,archivo)
	print("Archivo Exportado Exitosamente")
