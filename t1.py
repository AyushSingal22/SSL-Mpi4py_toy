#!/usr/bin/env python3
from mpi4py import MPI

import time
import csv
from datetime import datetime
def get_time():
    dt_obj = datetime.now()
    print('current datetime :',dt_obj)


if __name__=="__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        get_time()

        data =0
        file_obj = open("data/Values_CDM2.csv")
        reader = csv.DictReader(file_obj)
        tf1 = open("Out/o1.txt" , "w")
        for x in reader:
            data+=1
            tf1.write(str(x))
        req = comm.irecv(source=1, tag=11)
        data += req.wait()
        req = comm.irecv(source=2, tag=12)
        data += req.wait()
        req = comm.irecv(source=3, tag=13)
        data += req.wait()
        print(data)

        get_time()
        
    elif rank == 1:
        data = 0
        tf1 = open("Out/o0.txt" , "w")
        file_obj = open("data/Values_CDM2.csv")
        reader = csv.DictReader(file_obj)
        for x in reader:
            data+=1
            tf1.write(str(x))
        req = comm.isend(data, dest=0, tag=11)
        req.wait()
    elif rank == 2:
        data = 0
        file_obj = open("data/Values_ESPT.csv")
        tf1 = open("Out/o2.txt" , "w")
        reader = csv.DictReader(file_obj)
        for x in reader:
            data+=1
            tf1.write(str(x))
        req = comm.isend(data, dest=0, tag=12)
        req.wait()
    elif rank == 3:
        data = 0
        file_obj = open("data/Values_ESPT2.csv")
        tf1 = open("Out/o3.txt" , "w")
        reader = csv.DictReader(file_obj)
        for x in reader:
            data+=1
            tf1.write(str(x))
        req = comm.isend(data, dest=0, tag=13)
        req.wait()

        


    


    




