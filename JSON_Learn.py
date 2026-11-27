import json

# GUARDAR A UN JSON
numeros = [1,2,3,4,5]
with open("lista.json", "w") as f: # la "w" es para indicar write mode
    json.dump(numeros, f)

# CARGAR DESDE UN JSON
with open("lista.json") as f: # la "r" es para indicar read mode. es el modo por defecto asi que la omito
    print(json.load(f))
