#JULY 2016 Stefano Bosisio
#Test onSire gradients vs OpenMM gradient
import sys,os
from numpy import *
import matplotlib.pyplot as plt
import seaborn as sbn
sbn.set_style("whitegrid")



def plot_grad_two(openmm,sire,sireAB,lambdalist,saving):
    #Function to plot forward and backward directions
    color = sbn.color_palette()

    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    oplist = []
    operr = []
    sirelist = []
    sireerr = []
    sireABlist = []
    sireABerr = []
    for  lam in lambdalist:
        oplist.append(openmm[lam][0])
        sirelist.append(sire[lam][0])
        sireABlist.append(sireAB[lam][0])

        operr.append(openmm[lam][1])
        sireerr.append(sire[lam][1])
        sireABerr.append(sireAB[lam][1])

    #print(oplist)
    #print(sirelist)
    #print(sireABlist)

    #print(operr)
    #print(sireerr)
    #print(sireABerr)

    ax.errorbar(lambdalist,oplist,marker="o",label="OpenMM",color=color[0],yerr=operr)
    ax.errorbar(lambdalist,sirelist,marker="o",label="Sire",color=color[1],yerr=sireerr)
    ax.errorbar(lambdalist,sireABlist,marker="o",label="Sire-AB",color=color[2],yerr=sireABerr)

    ax.set_ylabel("$\partial$G/$\partial\lambda$",fontsize=20)
    ax.set_xlabel(r'$\lambda$',fontsize=20)
    plt.legend(loc='best',fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.tight_layout()
    plt.grid(True)
    #ax.set_ylim(-0.001,0.001)
    #for i,j in zip(lam,openmm[lam]):
    #    ax.annotate("%.2f"%j,xy=(i,j-2),fontsize=12,color=color[0])#,stretch='ultra-condensed',rotation=0)
    #for i,j in zip(lam,sire[lam]):
    #    ax.annotate("%.2f"%j,xy=(i,j+2),fontsize=12,color=color[1])#,stretch='condensed',rotation=0)

    plt.savefig(saving)




input_folder = sys.argv[1]  #run001/diff_mass/all_bonds/HC~HH/free/output

#I am going to take the simfile.dat file and gradient_cum.dat
#from simfile let's compute the average gradietn and std err
#from gradient_cum.dat take the 2nd column last value

dcdfolders = []
gradientcum = []
print("Let's find the simfile.dat and gradient.cum files")
for root, dirs, files in os.walk(input_folder):
    if "lambda" in root:
        for name in files:
            if "simfile.dat" in name:
                path = root + "/" + name

                dcdfolders.append(path)
            if "gradient_stat.dat" in name:
                path = root + "/" + name
                gradientcum.append(path)

print("Found:")
print(dcdfolders)
print(gradientcum)

dict_openmm = {}
numb_files = len(dcdfolders)
lambda_list = []
for numb in range(0, numb_files):
    val = (dcdfolders[numb])
    if val.index("lambda"):
        l = val.index("lambda")
        val_split = val[l:].split("/")   #that's necessary cause it's reading the folder name, split it and gives the lambda value
        index = val_split[0].index("-")
        lambda_val = val_split[0][(index+1):]
        dict_openmm[lambda_val] = {}
        lambda_list.append(lambda_val)
    else:
        print("Be careful, are you sure lambdas folders are here?")


    input_lambda = open(dcdfolders[numb],"r")
    read_file = input_lambda.readlines()
    index_start = read_file.index('#   [step]      [potential kcal/mol]       [gradient kcal/mol]      [forward Metropolis]     [backward Metropolis]                   [u_kl]\n') +1
    values_data = read_file[index_start:]  #copy all the values of the simfile
    time_grad = loadtxt(values_data,usecols=[0,2]) # use the columns 0(time) and 2 (gradients)

    elements_data = len(time_grad)
    #print(time_grad[:,1])
    time_grad[:,1]= time_grad[:,1]    #*0.593   #let's take out the reduce units
    #print(time_grad[:,1])
    mean_value = mean(time_grad[:,1])
    std_value  = std(time_grad[:,1])
    std_err    = std_value/math.sqrt(len(time_grad[:,1]))
    dict_openmm[lambda_val] = (mean_value,std_err)

dict_sire = {}
dict_sireAB = {}
numb_files = len(gradientcum)

for numb in range(0, numb_files):
    val = (gradientcum[numb])
    if val.index("lambda"):
        l = val.index("lambda")
        val_split = val[l:].split("/")   #that's necessary cause it's reading the folder name, split it and gives the lambda value
        index = val_split[0].index("-")
        lambda_val = val_split[0][(index+1):]
        dict_sire[lambda_val] = {}
    else:
        print("Be careful, are you sure lambdas folders are here?")

    grad_corr = loadtxt(gradientcum[numb],usecols=[1,2],skiprows=2)  #allbonds correction
    grad_AB = loadtxt(gradientcum[numb],usecols=[3,4],skiprows=2)    #take out allb corr

    dict_sire[lambda_val] = (grad_corr[-1][1],grad_corr[-1][1])

    dict_sireAB[lambda_val] = (grad_AB[-1][0],grad_AB[-1][1])

print(dict_sire)
print(dict_sireAB)
lambda_list.sort()

outputfile = ("%s/sire_openmm.dat" % input_folder)
output = open(outputfile,"w")
output.write("Lambda,GradSire,GradSireAB,GradOpenMM\n")  #GradSireAB : no allbonds correction
for lam in lambda_list :
    print("Processing lambda %s" %lam)
    output.write("%s,%s,%s,%s\n" % (lam,dict_sire[lam],dict_sireAB[lam],dict_openmm[lam]))


saving = "%s/sire_openmm.pdf" % input_folder
plot_grad_two(dict_openmm,dict_sire,dict_sireAB,lambda_list,saving)
