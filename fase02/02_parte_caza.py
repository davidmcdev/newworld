from pathlib import Path

import pandas as pd

DATASET = Path (
    'data/raw/nevworld_6540446722987033903_20261005_182722.jsonl'
)

OUTPUT_DIR = Path('data/processed')

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_json(DATASET, lines=True)

def event_table(event_type, columns):
    selected = ['run_id', 'event_index', 'tick', *columns]

    available = [
        column for column in selected
        if column in df.columns
    ]

    table = df.loc[
            df['type'] == event_type,
            available,
        ].copy()

    table = table.reindex(columns=['run_id', 'event_index', 'tick', 'villager_id', 'prey_type', 'simulation_day'])

    assert table[selected].notna().all().all(), 'Faltan campos obligatorios'

    if not table.empty:
        table['simulation_day'] = table['tick'] // 12000

    return table

tabla = event_table('hunt_completed', ['villager_id', 'prey_type'])

output = OUTPUT_DIR / f'hunts.csv'

tabla.to_csv(output, index=False)

print(output, '->', len(tabla), 'filas')