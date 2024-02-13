import csv
from itertools import groupby
from itertools import accumulate
from itertools import count

csv_file_path = 'data.csv'
recordList=[]
sumOfQuant=[]
countofItems=[]

with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        recordList.append((row['Id'],row['Brand'],row['Quantity'],row['Customer']))

sorted_List=sorted(recordList,key=lambda x:x[1])
grouped_list=groupby(sorted_List,key=lambda x:x[1])

for key,group in grouped_list:
    
    print(key)
    for item in group:
        print(item)
        sumOfQuant.append(int(item[2]))
        
    average = int(sum(sumOfQuant) / int(len(sumOfQuant)))
    countofItems=(key,int(len(sumOfQuant)))
    
    print("Average:", average)
    sumOfQuant =[]
    print()

