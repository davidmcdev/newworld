from pathlib import Path

import duckdb
import pandas as pd

DATA_DIR = Path('data/processed')
PARQUET_DIR = DATA_DIR / 'parquet'
PARQUET_DIR.mkdir(exist_ok=True)

csv_path = DATA_DIR / 'hunts.csv'
parquet_path = PARQUET_DIR / 'hunts.parquet'

tabla = pd.read_csv(csv_path)

assert 'prey_type' in tabla.columns, 'Al archivo le falta la columna prey_type'
assert tabla[['prey_type']].notna().all().all(), 'Algunas columnas de prey_type están vacías'

tabla.to_parquet(parquet_path, engine='pyarrow', index=False)
print('  CSV:', csv_path.stat().st_size, 'bytes')
print('  Parquet:', parquet_path.stat().st_size, 'bytes')

conexion = duckdb.connect()

hunt_query = '''
    SELECT 
        prey_type as presa,
        COUNT(*) as hunt_count,
    FROM read_parquet('data/processed/parquet/hunts.parquet')
    GROUP BY prey_type
    ORDER by hunt_count DESC
'''

hunt_summary = conexion.execute(hunt_query).fetch_df()
print(hunt_summary)


hunt_summary.to_csv(
    'reports/hunts_by_prey_sql.csv',
    index=False
)

conexion.close()