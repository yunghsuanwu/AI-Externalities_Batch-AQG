import pandas as pd

df1 = pd.read_csv('tasks.csv')
df2 = pd.read_csv('batch-tasks-03Feb.csv')
df3 = pd.read_csv('batch-tasks-04Feb.csv')
df4 = pd.read_csv('batch-tasks-05Feb.csv')

df_concat = pd.concat([df1, df2, df3, df4])
df_concat.to_csv('batch-tasks-06Feb.csv', index=False)