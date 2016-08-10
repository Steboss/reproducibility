#July 2016 Stefano Bosisio
#Collect results from simulation of absolute free energy calcualtion for HH HC case only
# Output:  output_results/run00X/VALUES.dat
# In values.dat results are vided into categories
#Usage: python  analysis.py  run001
#run001 is: run001/diff_masses/all_bonds/HC/free/vanish   (same_masses, h_bonds, HH )
from numpy import *
import os,sys
import matplotlib.pyplot as plt
import seaborn as sbn
sbn.set_style("whitegrid")

def extractVanish(energy):
    #The final state is in the vacuum phase
    #So we need to take out the solute from the water:  vacuum - water
    seeker = open(energy,"r")
    reader_energy = seeker.readlines()
    result = -1*float(reader_energy[len(reader_energy)-1].split()[2])
    error = float(reader_energy[len(reader_energy)-1].split()[4])

    return result, error

def addResults( results ):
    DG = 0.0
    err = 0.0

    for result in results:
        #print result
        DG += result[0]
        err += pow(result[1],2)
    err = sqrt(err)
    return [DG, err]

def subResultsTwo( results ):
    DG = 0.0
    err = 0.0

    DG = results[0][0]-results[1][0]
    err += pow(results[0][1],2)
    err += pow(results[1][1],2)
    err = sqrt(err)
    return [DG, err]


def plot_grad_two(forward,name_for,backward,name_back):
    #Function to plot forward and backward directions
    color = sbn.color_palette()

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

    fig = plt.figure(figsize(5,5))
    ax = fig.add_subplot(111)
    forw = ax.errorbar(lambda_val, grad_for, yerr=grad_for_err, marker = 'o',label=name_for,color='blue')
    backw =ax.errorbar(lambda_back, grad_back, yerr=grad_back_err,marker='o',label=name_back,color='green')
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

    return fig

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

################
###MAIN SCRIPT##
################


if not os.path.exists("output_results/"):
    os.makedirs("output_results/")


directory = sys.argv[1]

print("Creation of output folder output_results/%s" % directory)

if not os.path.exists("output_results/%s" % directory):
    os.makedirs("output_results/%s"  % directory)


dict = {}

vanish_dirs = []
for root, dirs, files in os.walk(directory):
    #gromacs result: AVERAGE_gro.dat
    if "free" in dirs:
        vanish_path = root+ "/free/vanish/output"
        vanish_dirs.append(vanish_path)
    else:
        continue

print("looking for vanish directory in free folders...")
for dirs in vanish_dirs:

    masses = dirs.split("/")[1]
    bonds  = dirs.split("/")[2]
    mol    = dirs.split("/")[3]
    path_gro = dirs + "/AVERAGE_gro.dat"
    path_mbar = dirs + "/AVERAGE_MBAR.dat"
    path_grad = dirs + "/gradient_profile.dat"

    if os.path.exists(path_gro):
        name = mol +"_" + masses + "_" + bonds + "_" + "GRO"
        dict[name] = extractVanish(path_gro)
    if os.path.exists(path_mbar):
        name = mol +"_" + masses + "_" + bonds + "_" + "MBAR"
        dict[name] = extractVanish(path_mbar)
    if os.path.exists(path_grad):
        name = ("output_results/%s/" % directory) + mol +"_" + masses + "_" + bonds + ".pdf"
        plot_grad_single(path_grad,name,mol,masses,bonds)



print("Writing output in output_results/")
print(dict)

output_folder = "output_results/%s/VALUES.dat" % directory
output = open(output_folder,"w")

output.write("Different masses all bonds:\n")

output.write("%s   Gro:  %.3f    %.3f\n" % ("HH", dict["HH_diff_masses_all_bonds_GRO"][0], dict["HH_diff_masses_all_bonds_GRO"][1]))
output.write("%s   Gro:  %.3f    %.3f\n" % ("HC", dict["HC_diff_masses_all_bonds_GRO"][0], dict["HC_diff_masses_all_bonds_GRO"][1]))

output.write("%s   Mbar: %.3f    %.3f\n" % ("HH", dict["HH_diff_masses_all_bonds_MBAR"][0], dict["HH_diff_masses_all_bonds_MBAR"][1]))
output.write("%s   Mbar: %.3f    %.3f\n" % ("HC", dict["HC_diff_masses_all_bonds_MBAR"][0], dict["HC_diff_masses_all_bonds_MBAR"][1]))

output.write("Different masses h bonds:\n")

output.write("%s   Gro:  %.3f    %.3f\n" % ("HH", dict["HH_diff_masses_h_bonds_GRO"][0], dict["HH_diff_masses_h_bonds_GRO"][1]))
output.write("%s   Gro:  %.3f    %.3f\n" % ("HC", dict["HC_diff_masses_h_bonds_GRO"][0], dict["HC_diff_masses_h_bonds_GRO"][1]))

output.write("%s   Mbar: %.3f    %.3f\n" % ("HH", dict["HH_diff_masses_h_bonds_MBAR"][0], dict["HH_diff_masses_h_bonds_MBAR"][1]))
output.write("%s   Mbar: %.3f    %.3f\n" % ("HC", dict["HC_diff_masses_h_bonds_MBAR"][0], dict["HC_diff_masses_h_bonds_MBAR"][1]))

output.write("Same masses all bonds:\n")

output.write("%s   Gro:  %.3f    %.3f\n" % ("HH", dict["HH_same_masses_all_bonds_GRO"][0], dict["HH_same_masses_all_bonds_GRO"][1]))
output.write("%s   Gro:  %.3f    %.3f\n" % ("HC", dict["HC_same_masses_all_bonds_GRO"][0], dict["HC_same_masses_all_bonds_GRO"][1]))

output.write("%s   Mbar: %.3f    %.3f\n" % ("HH", dict["HH_same_masses_all_bonds_MBAR"][0], dict["HH_same_masses_all_bonds_MBAR"][1]))
output.write("%s   Mbar: %.3f    %.3f\n" % ("HC", dict["HC_same_masses_all_bonds_MBAR"][0], dict["HC_same_masses_all_bonds_MBAR"][1]))

output.write("Same masses h bonds:\n")

output.write("%s   Gro:  %.3f    %.3f\n" % ("HH", dict["HH_same_masses_h_bonds_GRO"][0], dict["HH_same_masses_h_bonds_GRO"][1]))
output.write("%s   Gro:  %.3f    %.3f\n" % ("HC", dict["HC_same_masses_h_bonds_GRO"][0], dict["HC_same_masses_h_bonds_GRO"][1]))

output.write("%s   Mbar: %.3f    %.3f\n" % ("HH", dict["HH_same_masses_h_bonds_MBAR"][0], dict["HH_same_masses_h_bonds_MBAR"][1]))
output.write("%s   Mbar: %.3f    %.3f\n" % ("HC", dict["HC_same_masses_h_bonds_MBAR"][0], dict["HC_same_masses_h_bonds_MBAR"][1]))
