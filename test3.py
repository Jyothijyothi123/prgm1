import pandas as pd
df=pd.read_csv('data.csv')
dup=df.duplicated().sum()
print("number of duplicated rows:",dup)
print("number of rows in dataframe :",df.shape)
df_new=df
df_new=df_new.drop_duplicates()
dup1=df_new.duplicated().sum()
print("number of Duplicated rows after deleting the values:",dup1)
print("number of rows in dataframe:",df_new.shape)
