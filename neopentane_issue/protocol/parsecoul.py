#!/usr/bin/python
#APR 2015 Stefano Bosisio - Julien Michel
#Script to collect lj correction and coulomb correction (FUNC only)
import os,sys,math

#FUNC 
stream0 = open(sys.argv[1],"r") #func at lambda 0 
buffer = stream0.readlines()
length0 = len(buffer) - 1
DG_func_0 = float(buffer[length0].split()[2])
err_0 = float(buffer[length0].split()[4])

stream1 = open(sys.argv[2],"r") #func at lambda 1
buffer = stream1.readlines()
length1 = len(buffer) - 1
DG_func_1 = float(buffer[length1].split()[2])
err_1 = float(buffer[length1].split()[4])

DG_func = DG_func_1 - DG_func_0
err = math.sqrt(err_0**2 + err_1**2)
print("DG_func_corr = %8.5f +/- %8.5f kcal/mol " %(DG_func,err))
