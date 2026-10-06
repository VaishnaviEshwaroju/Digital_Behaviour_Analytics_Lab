import pandas as pd
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

df = pd.read_csv("digital_behaviour.csv")

plt.figure(figsize=(50,25))
df["Total_Screen_time"] = df["Instagram_Minutes"] + df["WhatsApp_Minutes"] + df["YouTube_Minutes"]
plt.bar(df["Date"],df["Total_Screen_time"],color="green")
plt.title("Total_Screen_time on each day")
plt.xlabel("Date")
plt.ylabel("Total_Screen_time")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("c1.png")
plt.close()

app_totals = {}
app_totals["Total_Instagram_Minutes"] = int(df["Instagram_Minutes"].sum())
app_totals["Total_YouTube_Minutes"] = int(df["YouTube_Minutes"].sum())
app_totals["Total_WhatsApp_Minutes"] = int(df["WhatsApp_Minutes"].sum())
app_totals["Total_LinkedIn_Minutes"] = int(df["LinkedIn_Minutes"].sum())

total = app_totals["Total_Instagram_Minutes"] + app_totals["Total_YouTube_Minutes"] + app_totals["Total_WhatsApp_Minutes"] + app_totals["Total_LinkedIn_Minutes"]

# print(app_totals)
plt.figure(figsize=(15,15),dpi=100)
plt.bar(app_totals.keys(),app_totals.values(),color="green")
plt.title("Bar Graph for app totals")
plt.xlabel("App_name")
plt.ylabel("Minutes")
plt.xticks(rotation=90)
plt.savefig("pc.png")
plt.close()

plt.figure(figsize=(15,10))
plt.plot(df["Date"],df["Study_Minutes"],marker="s",label="study_minutes",color="green")
plt.plot(df["Date"],df["Instagram_Minutes"],marker="o",label="Instagram_minutes",color="black")
plt.legend()
plt.title("Scatter plot for studyminutes on each day")
plt.xlabel("Date")
plt.ylabel("Study_Minutes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plot.png")
plt.close()

plt.figure(figsize=(15,15),dpi=500)
s = pd.Series(app_totals)
s = s/total
plt.pie(s,labels=app_totals.keys(),autopct="%1.1f%%",startangle=90)
plt.title("Piechart for app totals")
plt.savefig("pco.png")
plt.close()


