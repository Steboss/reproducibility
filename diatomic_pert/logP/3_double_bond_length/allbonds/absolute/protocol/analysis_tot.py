#JULY 2016 Stefano Bosisio
#Script to create lambda.dat files for analysis_gro Script +  plot gradients
#Future: extrapolate part of the script ot have gradients plot only
#Usage: python analysis_tot.py

import math
import sys,os,shutil
sys.path.append('/home/steboss/.local/lib/python2.7/site-packages/numpy-1.12.0.dev0+1b6831b-py2.7-linux-x86_64.egg')
from numpy import * 



#print("!!!WARNING: at the moment the gradietns values are multiply by 0.593 kcal/mol!!!")
dcdfolders = []
dcdpath = os.getcwd()

print("Looking for simfile.dat files")
for root, dirs, files in os.walk(dcdpath):
    if "lambda" in root:
        for name in files:
            if "simfile.dat" in name:
                path = root + "/" + name

                dcdfolders.append(path)

dcdfolders.sort()
print("Found in these folders simfile.dat\n")
print(dcdfolders)

#print("Finding path to analysis_gro folder:\n")
#path_gro = os.getcwd() + "/analysis_gro"

#if not os.path.exists(path_gro):#
#    os.makedirs(path_gro)#creation of analysis_gro folder wher eall the lambda will be moved to
#print(path_gro)

numb_files = len(dcdfolders)


###########Initialitation of list for plotting gradients#######################
avg_grad_value = []
std_err_value = []
bigga = open("gradient_profile.dat","w")
bigga.write("Lam\t\tGrad(kcal/mol)\t\tStdErr(kcal/mol)\n")
#############################################################################
#print("Now cycling throuh the simfile.dat files")
for numb in range(0, numb_files):
    val = (dcdfolders[numb])
    if val.index("lambda"):
        l = val.index("lambda")
        val_split = val[l:].split("/")   #that's necessary cause it's reading the folder name, split it and gives the lambda value
        index = val_split[0].index("-")
        lambda_val = val_split[0][(index+1):]
        #output_name = "lambda-"+str(lambda_val) +".dat" #output file nmae  is e.g. lambda-0.00
        #output_file = open(output_name,"w")
    else:
        print("Be careful, are you sure lambdas folders are here?")


    input_lambda = open(dcdfolders[numb],"r")
    read_file = input_lambda.readlines()
    index_start = read_file.index('#   [step]      [potential kcal/mol]       [gradient kcal/mol]      [forward Metropolis]     [backward Metropolis]                   [u_kl]\n') +1
    values_data = read_file[index_start:]  #copy all the values of the simfile
    time_grad = loadtxt(values_data,usecols=[0,2]) # use the columns 0(time) and 2 (gradients)
    #output_file.write("# lambba_val.val %s\n" % str(lambda_val))
    #output_file.write("#time (ps)      gradients (kcal/mol*lam)\n")
    #elements_data = len(time_grad)
    #for x in range(0,elements_data-1):
    #    output_file.write("%.3f            %.10f\n" %(time_grad[:,0][x]*2,time_grad[:,1][x]))  #multiplication by 2 cause we have 2ps

    #current_file = os.getcwd() + "/" + str(output_name)
    #dest_file = path_gro + "/" + str(output_name)
    #print(current_file)
    #print(dest_file)
    #os.rename(current_file,dest_file)


    mean_value = mean(time_grad[:,1])
    std_value  = std(time_grad[:,1])
    std_err    = std_value/math.sqrt(len(time_grad[:,1]))

    #avg_grad_value.append(mean_value)
    #std_err_value.append(std_err)  uncomment and add the lotting part if you want the png files
    print("Writing grad_profile.dat for lambda %s" % lambda_val)
    bigga.write("%s\t\t%.4f\t\t%.4f\n" %(lambda_val, mean_value,std_err))
