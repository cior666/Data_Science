import pandas as pd
df = pd.read_csv(r"C:\Users\silvi\OneDrive\Escritorio\Carrera Data Science\Datasets\athlete_events.csv\athlete_events.csv")
df_recortado = df.head(3000)
df_recortado.to_csv(r"C:\Users\silvi\OneDrive\Escritorio\Carrera Data Science\Datasets\athlete_events.csv\athlete_events_recortado.csv", index=False)