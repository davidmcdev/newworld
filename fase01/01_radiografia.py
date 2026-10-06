from pathlib import Path

import pandas as pd

DATASET = Path (
    'data/raw/nevworld_6540446722987033903_20261005_182722.jsonl'
)

if not DATASET.exists():
    raise FileNotFoundError(
        f'No se encuentra el archivo {DATASET.resolve()}'
    )

df = pd.read_json(DATASET, lines=True)

required = [
     'run_id', 'event_index', 'tick', 'type'
]

assert not df.empty, 'El dataset está vacío'
assert all(column in df.columns for column in required), 'Faltan columnas principales'
assert not df.duplicated(['run_id', 'event_index']).any(), 'Hay eventos duplicados'

ordered = df.sort_values('event_index')
assert ordered['tick'].is_monotonic_increasing, 'Los ticks retroceden'

print('\nPrimeras filas: ')
print(df.head())

print(f'\nNombre del archivo: {DATASET.name}')

filas, columnas = df.shape
print(f'Número total de evento: {filas}')
print(f'Número de columnas: {columnas}')
print(f'Nombres de las columnas: {df.columns.to_list()}')
print(f'Tipo del primer evento registrado: {df['type'].iloc[0]}')

recuento_eventos = df['type'].value_counts()
evento_mas_frecuente = recuento_eventos.idxmax()
evento_mayor_cantidad = recuento_eventos.max()

print(f'\nTipo de evento más frecuente y cantidad: {evento_mas_frecuente} - {evento_mayor_cantidad}')
print(f'\nRecuento de todos los tipos de eventos registrados: {df['type'].value_counts()}')
print(f'\nrun_id: {df['run_id'].iloc[0]}')
print(f'\nSemilla: {df['seed'].iloc[0]}')
print(f'\nVersión del esquema de la primera fila: {df['schema_version'].iloc[0]}')
print(f'\nTick mínimo: {df['tick'].min()}')
print(f'\nTick máximo: {df['tick'].max()}')
print(f'\nResultado validaciones: Todas las validaciones son correctas')