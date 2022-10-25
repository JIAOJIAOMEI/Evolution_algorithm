# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 10/25/22 18:25

import numpy as np
import pandas as pd
import functions_parameter
import matplotlib.pyplot as plt


genotype_range_list =[]

for i in range(1,24,1):
    func, num_genes, genotype_range = functions_parameter.choose_func(i)
    genotype_range_list.append(genotype_range)

ratio_list=[]

for i in genotype_range_list:
    low_bound, high_bound = i
    print(low_bound,high_bound)
    k = np.round(2/(high_bound-low_bound),4)
    ratio_list.append(k)
print(ratio_list)

df1 = pd.read_csv("./SSGA_percent_f1_f23_1000000_50d-10.csv",header=0,index_col=[0])
df2 = pd.read_csv("./SSGA_percent_f1_f23_1000000_50d-11.csv",header=0,index_col=[0])
df3 = pd.read_csv("./SSGA_percent_f1_f23_1000000_50d-12.csv",header=0,index_col=[0])
# print(df1)
df = pd.concat([df1,df2,df3],axis=1)
df.columns = ["col"+str(i) for i in range(1,61,1)]
df = df.applymap(lambda x:x if not '%' in str(x) else x.replace('%',''))
df = df.applymap(lambda x: int(x)/100)
print(df)

dist_cols = 1
dist_rows = 60
plt.figure(figsize=(22 * dist_cols,3.5 * dist_rows))
for i in range(1,60,1):
    plt.subplot(dist_rows, dist_cols, i)
    x = ["F"+str(i+1)+"_"+str(ratio_list[i]) for i in range(23)]
    print(x)
    y1 = df["col"+str(i)].tolist()
    plt.scatter(x,y1)
    plt.xlabel("2/(upper-lower)")
    plt.ylabel("percentage value")
plt.savefig("./SSGA_N_old20.pdf", dpi=1000)
plt.show()