def listar_titulo_anyo_duracion(doc):
	for i in doc:
   		print("Titulo:",i["title"],"// Año:",i["year"],"// Duración:",i["duration"])


import json

import codecs

doc = json.load(codecs.open('movies.json', 'r', 'utf-8-sig'))

while True:
	print('''1.- Listar el título, año y duración de todas las películas.
2.- Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una.
3.- Mostrar las películas que contengan en la sinopsis dos palabras dadas.
4.- Mostrar las películas en las que ha trabajado un actor dado.
5.- Mostrar el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas.
0.- Salir''')

	opcion = input("Opción: ")

	if opcion=="1":
		print(listar_titulo_anyo_duracion(doc))

	if opcion =="0":
		break