import pandas as pd
import numpy as np
#dataframes - excel sheet (table)
#series - collections of rows
#index - the position of row

df = pd.read_csv("digital_behaviour.csv")

#print first 5 rows
print(df.head())

#print laast 5 rows
print(df.tail())

#no. of rows and cols in df
print(df.shape)

#name of cols
li = df.columns
print(list(df.columns))

#describe every column
print(df[li].describe())

#instagram column total
print(df["Instagram_Minutes"].sum())

#avg study time
print(df["Study_Minutes"].mean())

#max in youtube minutes
print(df["YouTube_Minutes"].max())

# show days where st > 100
p = df[df["Instagram_Minutes"]>100]
print(p)

#show days where st>180
print(df[df["Study_Minutes"]>180])

#show me days where insta was high and study was lower
print(df[df["Study_Minutes"]<(df["Instagram_Minutes"])])

print(df[((df["Instagram_Minutes"]>100) & (df["Study_Minutes"]<100))])

#sort first 5 values of insta_mins in desc

list1 = (df["Instagram_Minutes"])
list1 = list1.sort_values(ascending=False)
print(list1.head())

l2 = df["Study_Minutes"].sort_values(ascending=False)
print(l2.head())

#adding new column
df["Total_Screen_time"] = df["Instagram_Minutes"] + df["YouTube_Minutes"] + df["WhatsApp_Minutes"] + df["LinkedIn_Minutes"]

print(df.head())

#adding new col

df["Screen_Hours"] = (df["Total_Screen_time"]/60).round(2)
print(df.head())

#adding new col

df["Digital_Balance"] = (df["Study_Minutes"]/(df["Total_Screen_time"])).round(2)

#new col using numpy
# df["Day_Type"] = np.where(df["Total_Screen_time"]>300,("Heavy"),("Normal"))

# print(df.head())

#similar to above one but using pandas

df["Day_Type"] = "normal"

df.loc[df["Total_Screen_time"]>300,"Day_Type"] = "heavy"

li = df[df["Day_Type"]=="heavy"]
print(df["Day_Type"].value_counts())


l = ["YouTube_Minutes","Instagram_Minutes","WhatsApp_Minutes","LinkedIn_Minutes"]
df["max"] = df[l].max(axis=1)

print(df.head())





