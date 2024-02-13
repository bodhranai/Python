import csv
from itertools import groupby

csv_file_path = 'data.csv'
csv_file_out_path1 = 'report1.csv'
csv_file_out_path2 = 'report2.csv'
recordList=[]
sumOfQuant=[]
data1Output=[] # average order amount
data2Output=[] # most popular ordered item

with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        recordList.append((row['Id'],row['Brand'],row['Quantity'],row['Customer']))

sorted_List=sorted(recordList,key=lambda x:x[1])
grouped_list=groupby(sorted_List,key=lambda x:x[1])


class CSVWriter:
    def write(self, fileName, data):
       with open(fileName, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for row in data:
            csv_writer.writerow(row)
    def pop(self,list):
        for item in list:
            if item[1] < list[0][1]:
                item.pop()
        return list

writer=CSVWriter()

for key,group in grouped_list:
    for item in group:
        sumOfQuant.append(int(item[2]))
        
    average = int(sum(sumOfQuant) / int(len(sumOfQuant)))
    data1Output.append([key,average])
    writer.write(csv_file_out_path1,data1Output)
    
    data2Output.append([key,int(len(sumOfQuant))])
    data2Sorted = sorted(data2Output,key=lambda x:x[1],reverse=True)
    topN = max(data2Sorted)[1]
    topN_filtered = list(filter(lambda x: x[1] > topN, data2Sorted))

    writer.write(csv_file_out_path2,topN_filtered)
  
    sumOfQuant =[]
    print()

      

