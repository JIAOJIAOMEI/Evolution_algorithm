# Name: Mei Jiaojiao
# Specilization: Artificial Intelligence
# Time and date: 7/25/22 14:42

import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

np.set_printoptions(threshold=sys.maxsize)

pd.options.display.max_columns = None
# pd.options.display.max_rows = None

df_com = pd.read_csv(
    "/Users/meijiaojiao/Desktop/New Evolution/combinations_result.csv",
    header=0)
df_com = pd.DataFrame(data=df_com.values,
                      columns=df_com.columns,
                      index=[i for i in range(1, len(df_com)+1, 1)])

print(df_com)
Baldwin = pd.read_csv(
    "/Users/meijiaojiao/Desktop/New Evolution/Baldwin_table_long.csv",
    index_col=[0, 1],
    header=0,
    sep=","
)
Baldwin.columns = [i for i in range(1, len(df_com)+1, 1)]

Baldwin = Baldwin.stack()
Baldwin = Baldwin.rename_axis(index=["Function", "Times", "Combinations"])
Baldwin = Baldwin.reset_index(level=[0, 2], name="Fitness")
Baldwin = Baldwin.reset_index(drop=False)
Baldwin["Mode"] = "Baldwin"


Lamarck = pd.read_csv(
    "/Users/meijiaojiao/Desktop/New Evolution/Lamarck_table_long.csv",
    index_col=[0, 1],
    header=0,
    sep=","
    )

Lamarck.columns = [i for i in range(1, len(df_com)+1, 1)]
Lamarck = Lamarck.stack()
Lamarck = Lamarck.rename_axis(index=["Function", "Times", "Combinations"])
Lamarck = Lamarck.reset_index(level=[0, 2], name="Fitness")
Lamarck = Lamarck.reset_index(drop=False)
Lamarck["Mode"] = "Lamarck"

df = pd.concat([Lamarck, Baldwin], axis=0)
df = pd.DataFrame(data=df.values,
                  columns=df.columns,
                  index=[i for i in range(1, len(df) + 1, 1)])
df[['iterations', 'mutation_rate', 'local_search', 'num_individuals',
    'm_range', 'range_mutation', 'crossover_probability']] = pd.DataFrame(
    [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]], index=df.index)

for i in range(0, len(df_com), 1):
    print(i)
    df.loc[df['Combinations'] == i + 1, 'iterations'] = df_com.iloc[i, 0]
    df.loc[df['Combinations'] == i + 1, 'mutation_rate'] = df_com.iloc[i, 1]
    df.loc[df['Combinations'] == i + 1, 'local_search'] = df_com.iloc[i, 2]
    df.loc[df['Combinations'] == i + 1, 'num_individuals'] = df_com.iloc[i, 3]
    df.loc[df['Combinations'] == i + 1, 'm_range'] = df_com.iloc[i, 4]
    df.loc[df['Combinations'] == i + 1, 'range_mutation'] = df_com.iloc[i, 5]
    df.loc[df['Combinations'] == i + 1, 'crossover_probability'] = df_com.iloc[i, 6]

df["Fitness"] = df["Fitness"].astype("float64")

print(df)

df.to_csv("./plot_df.csv",
          header=True,
          index=True)


