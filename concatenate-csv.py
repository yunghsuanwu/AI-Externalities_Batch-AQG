import pandas as pd

df1 = pd.read_csv('tasks.csv')
df2 = pd.read_csv('batch-tasks-06Feb-rerun.csv')
df3 = pd.read_csv('batch-tasks-06Feb.csv')


df_concat = pd.concat([df1, df2, df3])
df_concat.to_csv('daily-task-expansion-10Feb.csv', index=False)