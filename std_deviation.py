import csv
import math

with open("data.csv",newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean
squrad=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squrad.append(a)
sum=0
for i in squrad:
    sum=sum+1
result=sum/(len(data)-1)
std_deviation= math.sqrt(result)
print(std_deviation)