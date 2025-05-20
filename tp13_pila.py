
class Traje:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado


    def __str__(self):
        return f"{self.modelo} - {self.pelicula} - {self.estado}"

pila_trajes = [
    Traje("Mark III", "Iron Man", "Dañado"),
    Traje("Mark XLIV", "Avengers: Age of Ultron", "Dañado"),
    Traje("Mark XLVI", "Capitan America: Civil War", "Impecable"),
    Traje("Mark XLVII", "Spider-Man: Homecoming", "Dañado"),
    Traje("Mark L", "Avengers: Infinity War", "Destruido"),
    Traje("Mark LXXXV", "Avengers: Endgame", "Destruido"),
    Traje("Mark XLVII", "Spider-Man: Homecoming", "Dañado"),
]

# a
print("a) Verificar uso del modelo Mark XLIV (Hulkbuster):")
peliculas_hulkbuster = [traje.pelicula for traje in pila_trajes if traje.modelo == "Mark XLIV"]
if peliculas_hulkbuster:
    print("Mark XLIV fue utilizado en:")
    for p in peliculas_hulkbuster:
        print("-", p)
else:
    print("Mark XLIV no fue utilizado en ninguna película.")

#  b
print("\nb) Modelos que quedaron dañados (sin perder info de la pila):")
for traje in pila_trajes:
    if traje.estado == "Dañado":
        print("-", traje)

#  c
print("\nc) Eliminando modelos destruidos:")
pila_aux = []
while pila_trajes:
    traje = pila_trajes.pop()
    if traje.estado == "Destruido":
        print("-", traje.modelo)
    else:
        pila_aux.append(traje)

while pila_aux:
    pila_trajes.append(pila_aux.pop())


# e
print("\ne) Agregar modelo Mark LXXXV si no está repetido en la misma película:")
nuevo_traje = Traje("Mark LXXXV", "Avengers: Endgame", "Impecable")
existe = any(t.modelo == nuevo_traje.modelo and t.pelicula == nuevo_traje.pelicula for t in pila_trajes)
if not existe:
    pila_trajes.append(nuevo_traje)
    print("Modelo agregado correctamente.")
else:
    print("No se agregó porque ya existe ese modelo en esa película.")

#  f
print("\nf) Trajes utilizados en 'Spider-Man: Homecoming' y 'Capitan America: Civil War':")
for traje in pila_trajes:
    if traje.pelicula in ["Spider-Man: Homecoming", "Capitan America: Civil War"]:
        print("-", traje.modelo, "en", traje.pelicula)