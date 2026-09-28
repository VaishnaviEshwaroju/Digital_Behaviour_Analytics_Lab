import numpy as np
import csv

insta_times = []
study_times = []
with open("digital_behaviour.csv","r",newline="",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        insta_times.append(int(row["Instagram_Minutes"]))
        study_times.append(int(row["Study_Minutes"]))

insta_times = insta_times[0:7]
study_times = study_times[0:7]

arr1 = np.array(insta_times)
arr2 = np.array(study_times)

t1 = arr1.sum()
t2 = arr2.sum()

avgi = arr1.mean()
avgs = arr2.mean()

maxi = arr1.max()
maxs = arr2.max()

mini = arr1.min()
mins = arr2.min()

ci = 0
for val in arr1:
    if(val > avgi):
        ci += 1

cs = 0
for val in arr2:
    if val> avgs:
        cs += 1

print("For insta_time")
print(arr1,t1,avgi,maxi,mini,ci)
print(arr1[:3],arr1[0::2])
print("For study_time")
print(arr2,t2,avgs,maxs,mins,cs)
print(arr2[:3],arr2[0::2])

hoursi = arr1/60
hourss = arr2/60
diff = arr1 - arr2
k = np.round(hoursi,2)
hoursi = hoursi.round(2)
hourss = hourss.round(2)

print(arr1[arr1>avgi])
print(arr2[arr2>avgs])

print((arr2>100).sum())
#another of filtering
greater = filter(lambda bool_ : bool_,arr1>100)
print(diff)

    

  
