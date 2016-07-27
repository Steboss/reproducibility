#APR 2015 Stefano Bosisio
#Script to extract DG values from analysis_gro once everything has been done
#Output:AVERAGE.dat:  DG +-/ err
from numpy import *

gromacs=open("analysis_gro/results.txt","r")
reader = gromacs.readlines()
len_read = len(reader) - 1

DG = float(reader[len_read].split()[1])
err = float(reader[len_read].split()[3])



output_mean = open("AVERAGE_gro.dat","w")

output_mean.write("DG =   %.3f	+/- %.3f kcal/mol" % (DG,err))


TI=open("freenrg-TI.dat","r")
reader = TI.readlines()

counter = 0 
for f in reader:
    splitter=f.split()
    if "TI" in splitter:
        if counter==2:
            DG=float(f.split()[3])*0.593
            err=float(f.split()[5])*0.593
        else:
            counter+=1


output_mean = open("AVERAGE_TI.dat","w")

output_mean.write("DG =   %.3f	+/- %.3f kcal/mol" % (DG,err))
