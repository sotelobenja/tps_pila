class Personaje:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas

    def __str__(self):
        return f"{self.nombre} - {self.peliculas} películas"

pila_personajes = [
    Personaje("Iron Man", 10),
    Personaje("Thor", 8),
    Personaje("Hulk", 7),
    Personaje("Groot", 4),
    Personaje("Rocket Raccoon", 5),
    Personaje("Black Widow", 9),
    Personaje("Doctor Strange", 3),
    Personaje("Captain America", 9),
    Personaje("Gamora", 6),
    Personaje("Drax", 4),
]

#  a
print("a) Posiciones de Rocket Raccoon y Groot (posición 1 es la cima):")
pos_rocket = pos_groot = None
for i, personaje in enumerate(reversed(pila_personajes), 1):  # posición 1 en la cima
    if personaje.nombre == "Rocket Raccoon":
        pos_rocket = i
    if personaje.nombre == "Groot":
        pos_groot = i

print(f"- Rocket Raccoon está en la posición: {pos_rocket if pos_rocket else 'No encontrado'}")
print(f"- Groot está en la posición: {pos_groot if pos_groot else 'No encontrado'}")

#  b
print("\nb) Personajes con más de 5 películas:")
for personaje in pila_personajes:
    if personaje.peliculas > 5:
        print(f"- {personaje.nombre}: {personaje.peliculas} películas")

#  c
print("\nc) Cantidad de películas en las que participó Black Widow:")
pelis_bw = next((p.peliculas for p in pila_personajes if p.nombre == "Black Widow"), 0)
print(f"- Black Widow participó en {pelis_bw} películas")

#  d
print("\nd) Personajes cuyos nombres empiezan con C, D o G:")
for personaje in pila_personajes:
    if personaje.nombre.startswith(("C", "D", "G")):
        print(f"- {personaje.nombre}")