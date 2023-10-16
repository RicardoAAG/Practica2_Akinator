import sys
import json

def cargar_base_de_datos(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def take_chance(respuesta, propiedad):
    if respuesta == "s":
        res = True
    else:
        res = False
    
    to_remove = []
    for p in personajes["personajes"]:
        if p["propiedades"][propiedad] != res:
            to_remove.append(p)
    
    for p in to_remove:
        personajes["personajes"].remove(p)

    if len(personajes["personajes"]) == 1:
        print("\nTu personaje es " + personajes["personajes"][0]["nombre"])
        sys.exit()

preguntas: dict = cargar_base_de_datos('akinator_preguntas.json')
personajes: dict = cargar_base_de_datos('akinator_base_de_datos.json')

num_preguntas = len(preguntas["preguntas"])

print("Adivinador de personajes de Pokemones")
for i in range(0, num_preguntas):
    pregunta = preguntas["preguntas"][i]
    propiedad_buscar = pregunta["propiedad"]
    respuesta = input(f"{pregunta['pregunta']} (s/n): ")
    take_chance(respuesta, propiedad_buscar)

nueva_respuesta: str = input("No se ha encontrado un personaje que coincida con las respuestas proporcionadas. En quien estabas pensando?.")          
