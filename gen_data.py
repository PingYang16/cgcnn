import pandas as pd

df = pd.read_csv('each-zeolite-info.csv', dtype=str, low_memory=False)

df = df[['zeolite','set','kH_C18']]

df = df[df['set'] == 'IZA']

df['kH_C18'] = pd.to_numeric(df['kH_C18'], errors='coerce')  # Convert 'kH_C18' column to numeric

df = df[df['kH_C18'] != 0]  # Filter rows where 'kH_C18' is not zero

df = df[['zeolite', 'kH_C18']]

df.rename(columns = {'zeolite': 'id', 'kH_C18': 'adsorption'}, inplace=True)

df['adsorption'] = df['adsorption'].astype(float)

df['id'] = df['id'].astype(str)

df.to_csv('~/cgcnn/IZASC_re/id_prop.csv', index=False, header=False)