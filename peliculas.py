import statistics as stats

def listar_titulo_anyo_duracion(doc):
	for i in doc:
   		print("Titulo:",i["title"],"// Año:",i["year"],"// Duración:",i["duration"])

def mostrar_peliculas_num_actores(doc):
	for i in doc:
		print("Titulo:",i["title"],"// Nº de actores/actrices:",len(i["actors"]))

def sinopsis_dos_palabras_dadas(doc,primera_palabra,segunda_palabra):
	lista_peliculas = []
	for i in doc:
		sinopsis = i["storyline"]
		if sinopsis.count(primera_palabra) > 0 and sinopsis.count(segunda_palabra) > 0:
			lista_peliculas.append(i["title"])
	return lista_peliculas

def mostrar_peliculas_actor_dado(doc,actor):
	lista_peliculas = []
	for i in doc:
		for nombre_actor in i["actors"]:
			if nombre_actor == actor:
				lista_peliculas.append(i["title"])
	return lista_peliculas

def mostrar_titulo_url_poster(doc,fecha_1,fecha_2):
	lista_1 = []
	lista_2 = []
	lista_ratings = []
	lista_peliculas = []
	lista_url = []
	media_peliculas = {}
	for i in doc:
		if fecha_1 <= i["releaseDate"] and fecha_2 >= i["releaseDate"]:
			lista_ratings.append(sum(i["ratings"]) / len(i["ratings"]))
			if sum(i["ratings"]) / len(i["ratings"]) == max(lista_ratings):
				lista_peliculas.append(i["title"])
				lista_url.append(i["posterurl"])
	media_peliculas = [lista_peliculas[:3],lista_url[:3]]
	lista_1.append(media_peliculas[0])
	lista_2.append(media_peliculas[1])
	return zip(lista_1,lista_2)

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

	if opcion=="2":
		print(mostrar_peliculas_num_actores(doc))

	if opcion=="3":
		primera_palabra = input("Dime una palabra: ")
		segunda_palabra = input("Dime otra palabra: ")
		for pelicula in sinopsis_dos_palabras_dadas(doc,primera_palabra,segunda_palabra):
			print("Título:",pelicula)

	if opcion=="4":
		actor = input("Dime el nombre de un actor: ")
		for pelicula in mostrar_peliculas_actor_dado(doc,actor):
			print("Título:",pelicula)

	if opcion=="5":
		fecha_1 = input("Dime una fecha: ")
		fecha_2 = input("Dime otra fecha: ")
		for pelicula,url in mostrar_titulo_url_poster(doc,fecha_1,fecha_2):
			print("Títulos:",pelicula,"URLs:",url)

	if opcion =="0":
		break