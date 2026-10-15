from pathlib import Path

import pandas as pd

DATA_DIR = Path('data/processed')
REPORTS_DIR = Path('reports')
REPORTS_DIR.mkdir(exist_ok=True)

hunts = pd.read_csv(DATA_DIR / 'hunts.csv')
resources = pd.read_csv(DATA_DIR / 'resources.csv')

if hunts.empty:
    total_cacerias = 0
    print('No hay cacerías completadas registradas')
else:
    total_cacerias = len(hunts)
    recuento_por_prey_type = hunts['prey_type'].sort_values(ascending=False).value_counts()
    porcentaje_tipo_presa = (hunts['prey_type'].value_counts(normalize=True) * 100).round(1)
    recuento_por_simulation_day = hunts['simulation_day'].value_counts().sort_index()

print('Total de cacerías:', total_cacerias)
if not hunts.empty:
    print('Recuento por prey type de mayor a menor frecuencia:', recuento_por_prey_type)
    print('Porcentaje por cada tipo de presa:', porcentaje_tipo_presa)
    print('Recuento por cada simulation day:', recuento_por_simulation_day)

comidas = resources[resources['resource_type'] == 'food']
if comidas.empty:
    print('No hay eventos de comida')
    incrementos = 0
    decrementos = 0
    balance_neto = 0
    print('Incrementos:', incrementos)
    print('Decrementos:', decrementos)
else:
    incrementos = comidas[comidas['amount_delta'] > 0]
    decrementos = (comidas[comidas['amount_delta'] < 0]).copy()
    decrementos['amount_delta'] = decrementos['amount_delta'].abs()
    balance_neto = comidas['amount_delta'].sum()
    print('Incrementos:', incrementos.groupby('resource_type')['amount_delta'].sum())
    print('Decrementos:', decrementos.groupby('resource_type')['amount_delta'].sum())
print('Balance neto:', balance_neto)

assert recuento_por_prey_type.sum() == total_cacerias, 'La suma de los recuentos por presa no coincide con el total de cacerías'

total_incrementos = incrementos['amount_delta'].sum()
total_decrementos = decrementos['amount_delta'].sum()
assert(total_incrementos - total_decrementos), 'Los incrementos menos las reducciones no coinciden con el balance de comida'

resumen_final = pd.DataFrame([
    {'metric': 'hunt_events', 'value': len(hunts)},
    {'metric': 'food_change_events', 'value': len(comidas)},
    {'metric': 'food_gains', 'values': incrementos.groupby('resource_type')['amount_delta'].sum()},
    {'metric': 'food_reductions', 'values': decrementos.value_counts().sum()},
    {'metric': 'food_net_change', 'value': balance_neto}
])

resumen_final.to_csv(REPORTS_DIR / 'hunting_summary.csv', index=False)