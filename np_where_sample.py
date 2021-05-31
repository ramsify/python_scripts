import pandas as pd
import numpy as np

d1 = {'Group': ['A', 'A', 'B', 'C'],
      'Prd': ['HSMP', 'HSMP', 'PMP', 'HSMP'],
      'Size': [5.0, 8.0, 25.0, 6.0],
      'SYard': ['Bhopal', 'Ahmedabad', 'Kanpur', 'Mumbai'],
      'Plant': ['BSL', 'BSL', 'RSP', 'BSL']}
d2 = {'SYard': ['Mumbai', 'Bhopal', 'Ahmedabad', 'Kanpur'],
      'BSL': [2950.0, 3300.0, 1750.0, 3150.0],
      'RSP': [1700.0, 2600.0, 3000.0, 2550.0]}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
print("\n DataFrame_1 \n =========== \n", df1)
print("\n DataFrame_2 \n =========== \n", df2)
df1.set_index(['SYard'], inplace=True)
df2.set_index(['SYard'], inplace=True)
df3 = pd.concat([df1, df2], axis=1)
print(
    "\n DataFrame (df1 & df2 combined) before applying 'np.where'\n =========================================================== \n",
    df3)
df4 = df3
df4['PPM'] = np.where((df4.Plant == 'BSL'), df4.BSL, df4.RSP)
df4.reset_index(inplace=True)
df4.rename(columns={'index': 'SYard'}, inplace=True)
df4.set_index(['SYard', 'Plant'], inplace=True)
print("\n DataFrame after applying 'np.where'\n =================================== \n", df4)
df5 = df4[['Group', 'Prd', 'Size', 'PPM']]
print("\n", df5)
df5.to_csv('P.csv')
print("Output file has been generated successfully")
