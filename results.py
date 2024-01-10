import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

import matplotlib.pyplot as plt

df = pd.read_csv('test_results_izasc.csv', names=['id', 'target', 'prediction'])

targets = df['target']

predictions = df['prediction']

print(f"R^2: {r2_score(targets, predictions)}; MSE: {mean_squared_error(targets, predictions)}; MAE: {mean_absolute_error(targets, predictions)}")

plt.figure()
plt.scatter(targets, predictions)
plt.xlabel('True values')
plt.ylabel('Predicted values')
plt.savefig('results_izasc.png')
