import pandas as pd

df = pd.read_csv('each-zeolite-info.csv', dtype=str, low_memory=False)

df = df[['zeolite', 'kH_C18']]

zeolite_names = ['LTA-0', 'LTA-1', 'LTA-2']

df = df[df['zeolite'].isin(zeolite_names)]

df.rename(columns = {'zeolite': 'id', 'kH_C18': 'adsorption'}, inplace=True)

df['adsorption'] = df['adsorption'].astype(float)

df['id'] = df['id'].astype(str)

df.to_csv('~/cgcnn/example_dir/id_prop.csv', index=False, header=False)