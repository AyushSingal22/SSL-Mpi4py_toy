
import csv
from datetime import datetime
def get_time():
    dt_obj = datetime.now()
    print('current datetime :',dt_obj)

get_time()
data=0
filenames = ["data/Values_CDM.csv" , "data/Values_CDM2.csv" , "data/Values_ESPT.csv" , "data/Values_ESPT2.csv"]
reader = [csv.DictReader(open(filenames[0])) , csv.DictReader(open(filenames[1])), csv.DictReader(open(filenames[2])) , csv.DictReader(open(filenames[3]))]
outfiles = [open("Out/o0.txt" , "w") , open("Out/o1.txt" , "w") , open("Out/o2.txt" , "w") ,open("Out/o3.txt" , "w")]
for row in reader[0] : 
    data+=1
    outfiles[0].write(str(row))
for row in reader[1] :
    data+=1
 
    outfiles[1].write(str(row))

for row in reader[2] : 
    data+=1

    outfiles[2].write(str(row))

for row in reader[3] : 
    data+=1

    outfiles[3].write(str(row))

print(data)
get_time()