# hashlib viene con Python: sha256 calcula la huella del archivo.
from hashlib import sha256
# Path permite trabajar con rutas de archivos y carpetas.
from pathlib import Path
# Importamos de time un contador para medir duraciones en segundos.
from time import perf_counter

import pandas as pd

# Esta ruta se interpreta desde la raíz de bigdata-game.
path = Path('data/intercambio/envio/partida_A.jsonl')
path2 = Path('data/intercambio/envio/partida_B.jsonl')
# La huella representa los bytes del archivo que acabamos de leer.
huella = sha256(path.read_bytes()).hexdigest()
huella2 = sha256(path2.read_bytes()).hexdigest()
print(path.name, path.stat().st_size, huella)
print(path2.name, path.stat().st_size, huella2)

ruta_adrian = Path('data/intercambio/recibido/adrian')
ruta_juane = Path('data/intercambio/recibido/juane')

ficheros_adrian = {'partida_A.jsonl' : '5fc57004976080f1e2cea279d8a4bf16dd0e1841ca1f5840c43367f58980701c', 
            'partida_B.jsonl' : '5fc57004976080f1e2cea279d8a4bf16dd0e1841ca1f5840c43367f58980701c'}

ficheros_juane = {'partida_A.jsonl' : '8cd131e17e00e69d0ed8a06af1d08664594c5c8ee0eeeb4e8d69482bd86896d7', 
            'partida_B.jsonl' : '8cd131e17e00e69d0ed8a06af1d08664594c5c8ee0eeeb4e8d69482bd86896d7'}

print('Comprobacion ficheros Adrián: ')
for fichero, huella in ficheros_adrian.items():
    ruta = ruta_adrian / fichero
    if ruta.is_file():
        huella_fichero = sha256(ruta.read_bytes()).hexdigest()
        print('----------------------------------------')
        print(f'Fichero: {fichero}')
        print(f'Tamaño del fichero: {path.stat().st_size}')
        print(f'Huella esperada: {huella}')
        print(f'Huella recibida: {huella_fichero}')
        print(f'{'Coincide' if huella == huella_fichero else 'NO coincide'}')
        print(fichero)
        print(huella)
    else:
        print('Fichero no recibido')

print('Comprobacion ficheros Juane: ')
for fichero, huella in ficheros_juane.items():
    ruta = ruta_juane / fichero
    if ruta.is_file():
        huella_fichero = sha256(ruta.read_bytes()).hexdigest()
        print('----------------------------------------')
        print(f'Fichero: {fichero}')
        print(f'Tamaño del fichero: {path.stat().st_size}')
        print(f'Huella esperada: {huella}')
        print(f'Huella recibida: {huella_fichero}')
        print(f'{'Coincide' if huella == huella_fichero else 'NO coincide'}')
        print(fichero)
        print(huella)
    else:
        print('Fichero no recibido')
