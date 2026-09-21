
import csv
from operator import index


APP = "Instagram"

past7days = []


# list = [chr(i+ ord('a')) for i in range(26)]

# v = list[0:len(list)-1:2]
# u = list[1:len(list)-1:2]
with open("digital_behaviour.csv","r",newline="",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for val in reader:
        past7days.append(int(val["Instagram_Minutes"]))

past7days = past7days[len(past7days)-7:len(past7days)]
sum1  = (sum(past7days))

avg = (sum1/len(past7days))
max = ((max(past7days)))
min = min(past7days)
u = ([(past7days[i]) for i in range(len(past7days)) if past7days[i]>avg])


print(past7days);
print(f"The app name : {APP} , total minutes : {sum1},avg mins : {avg},max_mins day : {past7days.index(max)} , min_mins day : {past7days.index(min)} , days with mins above avg : {u}")




