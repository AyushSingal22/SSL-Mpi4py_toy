#!/usr/bin/python
from re import X
import threading
import csv
from datetime import datetime
def get_time():
    dt_obj = datetime.now()
    print('current datetime :',dt_obj)
x=0
def inc():
    global x
    x+=1

def help(path , out):
    reader= csv.DictReader(open(path))
    # cleprint(path)
    for row in reader:
        inc()
        out.write(str(row))
   

 
 
if __name__ =="__main__":
    get_time()
    outfiles = [open("Out/o0.txt" , "w") , open("Out/o1.txt" , "w") , open("Out/o2.txt" , "w") ,open("Out/o3.txt" , "w")]
    filenames = ["data/Values_CDM.csv" , "data/Values_CDM2.csv" , "data/Values_ESPT.csv" , "data/Values_ESPT2.csv"]

    t0 = threading.Thread(target=help, args=(filenames[0],outfiles[0] ,))
    t1 = threading.Thread(target=help, args=(filenames[1],outfiles[1] ,))
    t2 = threading.Thread(target=help, args=(filenames[2],outfiles[2]) ,)
    t3 = threading.Thread(target=help, args=(filenames[3],outfiles[3] ,))
 
    t0.start()
    t1.start()
    t2.start()
    t3.start()
    
    t0.join()
    t1.join()
    t2.join()
    t3.join()
 
    # both threads completely executed
    print(x)
    get_time()