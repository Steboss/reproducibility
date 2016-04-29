#2015 Nov
# Script for having gradient profile, updated ( for the new Sire)
# It will look for gradients.dat file, then we average it and plot the gradient

import argparse
import sys
import os
import numpy
import math
import datetime
import matplotlib.pyplot as plt
from matplotlib import rcParams
from numpy import loadtxt


dcdpath = os.getcwd()
 

   
dcdfolders = []
print("Looking for gradients.dat files")

for root, dirs, files in os.walk(dcdpath):
    if "lambda" in root:
        for name in files:
            if "gradients.dat" in name:
                path = root + "/" + name
                
                dcdfolders.append(path)

dcdfolders.sort()
print("Found in these folders gradients dat\n")
print(dcdfolders)



lambdalist= []   #for storing lambda values to final plot 
avg_grad_value = [] #to store gradients average values for plot
errorvalue = [] #to store error of gradients for plot
std_value = []  # deviation standard of the gradients for final dat file

outputfile="gradient_profile.dat"  #final dat file with  average gradients, standard dev and error
bigga = open(outputfile, 'w') 
bigga.write("Lambda   \t\t    Avg_Grad\t\t     Std.Dev.\t\t     Error\t\t \n")

numb_files = len(dcdfolders)
for numb in range(0, numb_files):
    val = (dcdfolders[numb])
    if val.index("lambda"):
        l = val.index("lambda")
        val_split = val[l:].split("/")   #that's necessary cause it's reading the folder name, split it and gives the lambda value
            
    else:
        print("Be careful, are you sure lambdas folders are here?")

        
    index = val_split[0].index("-")
        
    lambda_val = val_split[0][index+1:]
    lambdalist.append(lambda_val)   #appending to la
 
    print("Processing lambda_val	%s" %lambda_val)

    mean_grad = loadtxt(dcdfolders[numb],usecols=[1]) # column  mean_grad[:,1] gives gradients, here we can print simply mean_grad as it is
    

    mean = numpy.mean(mean_grad)
    devstd = numpy.std(mean_grad)
    
    avg_grad_value.append(numpy.mean(mean_grad))
    std_value.append(numpy.std(mean_grad))
    error = numpy.std(mean_grad)/math.sqrt(len(mean_grad))
    errorvalue.append(error)
         
    
    
    bigga.write("%s    \t\t    %.4f\t\t     %.4f\t\t     %.4f\t\t \n" %(lambda_val, mean, devstd, error))





plt.errorbar(lambdalist, avg_grad_value, yerr=std_value, marker = 'o')
ylab=plt.ylabel(r'$\frac{\partial G}{\partial \lambda} (kcal/mol)$',fontsize=20)   

xlab = plt.xlabel(r'$\lambda$', fontsize=20)
xlab.set_position((0.5, 0.5)) 

plt.savefig('gradient.png')

plt.clf()

