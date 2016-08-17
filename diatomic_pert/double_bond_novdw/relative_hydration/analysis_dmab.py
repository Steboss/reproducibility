#JULY 2016 Stefano Bosisio
#Collect results from simulation folder:
#-AVERAGE DG_wat: AVERAGE.dat: DG +/- err
#-AVERAGE DG_vac: AVERAGE.dat  DG +/- err
#python  analysis.py runX
import math
import os,sys
from numpy import *
import matplotlib.pyplot as plt
import seaborn as sbn
sbn.set_style("whitegrid")
 

def extractEnergy(energy):

    seeker = open(energy,"r")
    reader_energy = seeker.readlines()
    result = float(reader_energy[len(reader_energy)-1].split()[2])
    error = float(reader_energy[len(reader_energy)-1].split()[4])

    return result, error


def plot_grad_two(grad_forw,name_for,grad_backw,name_back,saving):
    #Function to plot forward and backward directions
    color = sbn.color_palette()

    forward = loadtxt(grad_forw,usecols=[0,1,2],skiprows=1)
    backward = loadtxt(grad_backw,usecols=[0,1,2],skiprows=1)

    lambda_val = forward[:,0]
    grad_for = forward[:,1]
    grad_for_err = forward[:,2]

    grad_back = []
    grad_back_err = []
    lambda_back = []
    for i in range(len(backward)-1,-1,-1):
        grad_back.append(-1*backward[:,1][i])
        grad_back_err.append(backward[:,2][i])
        lambda_back.append(1-backward[:,0][i])

    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    forw = ax.errorbar(lambda_val, grad_for, yerr=grad_for_err, marker = 'o',label=name_for,color=color[0])
    backw =ax.errorbar(lambda_back, grad_back, yerr=grad_back_err,marker='o',label=name_back,color=color[1])
    ax.set_ylabel("$\partial$G/$\partial\lambda$",fontsize=20)
    ax.set_xlabel(r'$\lambda$',fontsize=20)
    plt.legend(loc='best',fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.tight_layout()
    plt.grid(True)

    for i,j in zip(lambda_val,grad_for):
        ax.annotate("%.2f"%j,xy=(i,j-2),fontsize=12,color='blue')#,stretch='ultra-condensed',rotation=0)
    for i,j in zip(lambda_val,grad_back):
        ax.annotate("%.2f"%j,xy=(i,j+2),fontsize=12,color='green')#,stretch='condensed',rotation=0)

    plt.savefig(saving)

def plot_grad_single(inputfile,name,mol,masses,bonds):
    #To plot a single pgradient profile
    #inputfile: gradient_profile.dat
    #name : output_results/run001/HH_same_masses.....pdf
    color = sbn.color_palette()

    reader = loadtxt(inputfile,usecols=[0,1,2],skiprows=1)
    lambda_val = reader[:,0]
    grad_val   = reader[:,1]
    grad_err   = reader[:,2]

    label= mol + "_"  + masses + "_" + bonds

    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111)
    ax.errorbar(lambda_val,grad_val,yerr=grad_err,marker='o',color=color[0],label=label)
    ax.set_ylabel("$\partial$G/$\partial\lambda$",fontsize=20)
    ax.set_xlabel(r'$\lambda$',fontsize=20)
    plt.legend(loc='best',fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(name)


#################
###MAIN SCRIPT###
#################

if not os.path.exists("output_results/"):
    os.makedirs("output_results/")


directory = sys.argv[1]

if not os.path.exists("output_results/%s" % directory):
    os.makedirs("output_results/%s"  % directory)

if not os.path.exists("output_results/%s/diff_masses" % directory):
    os.makedirs("output_results/%s/diff_masses"  % directory)

if not os.path.exists("output_results/%s/diff_masses/all_bonds" % directory):
    os.makedirs("output_results/%s/diff_masses/all_bonds"  % directory)


dict = {}
dict["diff_masses_mbar_allbonds"] = {}


print("Let me detect the gradients and plot them too")

#######Let's do it manually!
print("Calculating different masses all bonds terms")
#Different Masses 1) Save the gradients 2) save the values
#Free
diff_mass_allb = "%s/diff_masses/all_bonds" % directory
forward_grad_wat = "%s/HC~HH/free/output/gradient_profile.dat" % diff_mass_allb
name_forward_wat = "HC~HH"
back_grad_wat    = "%s/HH~HC/free/output/gradient_profile.dat"  % diff_mass_allb
name_back_wat    = "HH~HC"
wheretosave = ("output_results/%s" % directory)  + "/diff_masses/all_bonds/free.pdf"
plot_grad_two(forward_grad_wat,name_forward_wat,back_grad_wat,name_back_wat,wheretosave)
#Vacuum
forward_grad_vac =  "%s/HC~HH/vacuum/output/gradient_profile.dat"  % diff_mass_allb
name_forward_vac = "HC~HH"
back_grad_vac    ="%s/HH~HC/vacuum/output/gradient_profile.dat"  % diff_mass_allb
name_bac_vac     = "HH~HC"
wheretosave = ("output_results/%s" % directory)  + "/diff_masses/all_bonds/vac.pdf"
plot_grad_two(forward_grad_vac,name_forward_vac,back_grad_vac,name_bac_vac,wheretosave)
path = "%s/HC~HH/free/output/AVERAGE_MBAR.dat" % diff_mass_allb
name = "HC~HH_free"
dict["diff_masses_mbar_allbonds"][name] = extractEnergy(path)

#Free energy values vacuum
path = "%s/HC~HH/vacuum/output/AVERAGE_MBAR.dat"% diff_mass_allb
name = "HC~HH_vacuum"
dict["diff_masses_mbar_allbonds"][name] = extractEnergy(path)


#Free energy values free
path = "%s/HH~HC/free/output/AVERAGE_MBAR.dat" % diff_mass_allb
name = "HH~HC_free"
dict["diff_masses_mbar_allbonds"][name] = extractEnergy(path)
#Free energy values vacuum
path = "%s/HH~HC/vacuum/output/AVERAGE_MBAR.dat"% diff_mass_allb
name = "HH~HC_vacuum"
dict["diff_masses_mbar_allbonds"][name] = extractEnergy(path)

#MBAR
dict["diff_masses_mbar_allbonds"]["DG_mbar_HC~HH"]= dict["diff_masses_mbar_allbonds"]["HC~HH_free"][0]  - dict["diff_masses_mbar_allbonds"]["HC~HH_vacuum"][0]
dict["diff_masses_mbar_allbonds"]["DG_mbarerr_HC~HH"]=math.sqrt(dict["diff_masses_mbar_allbonds"]["HC~HH_free"][1]**2  + dict["diff_masses_mbar_allbonds"]["HC~HH_vacuum"][1]**2)

dict["diff_masses_mbar_allbonds"]["DG_mbar_HH~HC"]= dict["diff_masses_mbar_allbonds"]["HH~HC_free"][0]  - dict["diff_masses_mbar_allbonds"]["HH~HC_vacuum"][0]
dict["diff_masses_mbar_allbonds"]["DG_mbarerr_HH~HC"]=math.sqrt(dict["diff_masses_mbar_allbonds"]["HH~HC_free"][1]**2  + dict["diff_masses_mbar_allbonds"]["HH~HC_vacuum"][1]**2)
################################################################################################################################################

print("Writing output in output_results/%s" % directory)


output_name = "output_results/%s/VALUES.dat" % directory
hyd_output =  open(output_name,"w")



output_folder = "output_results/%s/VALUES.dat" % directory
output = open(output_folder,"w")

output.write("Different masses all bonds:\n")
output.write("%s   MBAR:  %.3f    %.3f\n\n" % ("HH~HC", dict["diff_masses_mbar_allbonds"]["DG_mbar_HH~HC"], dict["diff_masses_mbar_allbonds"]["DG_mbarerr_HH~HC"]))
output.write("%s   MBAR:  %.3f    %.3f\n\n" % ("HH~HC", dict["diff_masses_mbar_allbonds"]["DG_mbar_HC~HH"], dict["diff_masses_mbar_allbonds"]["DG_mbarerr_HC~HH"]))
