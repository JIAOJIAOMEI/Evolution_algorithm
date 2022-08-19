# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 8/1/22 13:11

import pandas as pd

df_com = pd.read_csv(
    "/Users/meijiaojiao/Desktop/New Evolution/combinations_result.csv",
    header=0)
print(df_com)
print("\n")
Lamarck = pd.read_csv(
    "/Users/meijiaojiao/Desktop/New Evolution/Lamarck_table_long.csv",
    index_col=[0, 1],
    header=0,
    sep=","
)

print("This is the result for Badlwin(F1)")
print(Lamarck)
pd.options.display.max_rows = None

Lamarck.loc["Max"] = Lamarck.max()
Lamarck.loc["Min"] = Lamarck.min()
Lamarck.loc["Std"] = Lamarck.std()
Lamarck.loc["Mean"] = Lamarck.mean()

df = pd.DataFrame(data=Lamarck.loc[["Max","Min","Std","Mean"]].values,
                  index=["Max","Min","Std","Mean"])
print("\n")
print("This is the result:max_min_std_mean for Badlwin(F1)")
print(df)
print("\n")
print("This is min index for the four rows")
print(df.idxmin(1))
print("\n")
print("This is min value for the four rows")
print(df.min(1))
print("\n")
print("This is min combiantion for the four rows")
print(df_com.columns.values.tolist())
for i in df.idxmin(1):
    print(df_com.iloc[i].values.tolist())


print("\n")
print("This is max index for the four rows")
print(df.idxmax(1))
print("\n")
print("This is max value for the four rows")
print(df.max(1))
print("\n")
print("This is max combiantion for the four rows")
for i in df.idxmax(1):
    print(df_com.iloc[i].values.tolist())