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

Baldwin = pd.read_csv(
    "/Users/meijiaojiao/Desktop/Evolution_Baldwin_vs_Lamarck/Data/Long_format_table/Baldwin_table_long_1_3072.csv",
    index_col=[0, 1],
    header=0,
    sep=","
    )
Baldwin.columns = [i for i in range(1, 3073, 1)]

Baldwin = Baldwin.stack()
Baldwin = Baldwin.rename_axis(index=["Function", "Times", "Combinations"])
Baldwin = Baldwin.reset_index(level=[0, 2], name="Fitness")
Baldwin = Baldwin.reset_index(drop=False)
Baldwin["Mode"] = "Baldwin"
df_com = pd.read_csv(
    "/Users/meijiaojiao/Desktop/Evolution_Baldwin_vs_Lamarck/Data/parameter_combinations/combinations_result.csv",
    header=0)
df_com = pd.DataFrame(data=df_com.values,
                      columns=df_com.columns,
                      index=[i for i in range(1, 3073, 1)])

Lamarck = pd.read_csv(
    "/Users/meijiaojiao/Desktop/Evolution_Baldwin_vs_Lamarck/Data/Long_format_table/Lamarck_table_long_1_3072.csv",
    index_col=[0, 1],
    header=0,
    sep=","
    )
Lamarck.columns = [i for i in range(1, 3073, 1)]
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
    'm_range', 'range_mutation']] = pd.DataFrame([[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]], index=df.index)

for i in range(0, 3072, 1):
    print(i)
    df.loc[df['Combinations'] == i + 1, 'iterations'] = df_com.iloc[i, 0]
    df.loc[df['Combinations'] == i + 1, 'mutation_rate'] = df_com.iloc[i, 1]
    df.loc[df['Combinations'] == i + 1, 'local_search'] = df_com.iloc[i, 2]
    df.loc[df['Combinations'] == i + 1, 'num_individuals'] = df_com.iloc[i, 3]
    df.loc[df['Combinations'] == i + 1, 'm_range'] = df_com.iloc[i, 4]
    df.loc[df['Combinations'] == i + 1, 'range_mutation'] = df_com.iloc[i, 5]

df["Fitness"] = df["Fitness"].astype("float64")


def show_graph(df, lst):
    sns.set()
    fig = plt.figure(figsize=(18, 12))
    for i in range(len(lst)):
        ax = fig.add_subplot(2, 3, i + 1)
        sns.violinplot(x=lst[i], y="Fitness", hue='Mode', data=df, ax=ax, margin_titles=True, palette="Set2",
                       legend=True, dodge=True, inner="quartile", split=True)
        ax.set_title(lst[i])
        plt.subplots_adjust(wspace=0.3, hspace=0.3)


cols = ['iterations', 'mutation_rate', 'local_search',
        'num_individuals', 'm_range', 'range_mutation']

for i in range(1, 24, 1):
    cond = df["Function"] == "F" + str(i)
    show_graph(df=df[cond], lst=cols)
    plt.savefig('/Users/meijiaojiao/Desktop/Evolution_Baldwin_vs_Lamarck/Plots/Violin_F{0}.png'.format(i), dpi=1000)
