#!/usr/bin/env python3
from mpi4py import MPI
import time
from datetime import datetime

 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def get_time():
    dt_obj = datetime.now()
    print('current datetime :',dt_obj)

print(rank)
# if rank == 0:
#     print("here at  0")
#     get_time()
    
# if rank == 1:
#     print("here at  1")
#     get_time()
# if rank == 2:
#     print("here at  2")
#     get_time()

# if rank == 3:
#     print("here at  3")
#     get_time()

    




