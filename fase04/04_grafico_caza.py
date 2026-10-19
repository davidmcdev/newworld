from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_DIR = Path('data/processed')
CHARTS_DIR = Path('reports/charts')
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

hunts = pd.read_csv(DATA_DIR / 'hunts.csv')

tipos_de_presa = hunts['prey_type'].value_counts()

assert not tipos_de_presa.empty, 'La tabla está vacía por lo que no se puede generar el gráfico'

plt.figure(figsize=(8, 4))
tipos_de_presa.plot.bar(color='steelblue')
plt.title('Recuento por cada tipo de presa')
plt.xlabel('Tipo de presa')
plt.ylabel('Cantidad de presas cazadas')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig(CHARTS_DIR / '05_hunts_by_prey.png')
plt.close()