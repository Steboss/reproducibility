#APR 2016 Stefano Bosisio
#Script to collect gradient from reference simulations
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
plt.rcParams['figure.figsize']=(12.0,10.0)
from  numpy import *
import sys,os


def plot_grad(forward,name_for,backward,name_back):

    lambda_val = forward[:,0]
    grad_for = forward[:,1]
    grad_for_err = forward[:,2]

    grad_back = []
    grad_back_err = []
    for i in range(len(backward)-1,-1,-1):
        grad_back.append(-1*backward[:,1][i])
        grad_back_err.append(backward[:,2][i])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    forw = ax.errorbar(lambda_val, grad_for, yerr=grad_for_err, marker = 'o',label=name_for,color='blue')
    backw =ax.errorbar(1-lambda_val, grad_back, yerr=grad_back_err,marker='o',label=name_back,color='green')
    ax.set_ylabel("$\partial$G/$\partial\lambda$",fontsize=25)
    ax.set_xlabel(r'$\lambda$',fontsize=25)
    plt.legend(loc='best',fontsize=25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(True)



    for i,j in zip(lambda_val,grad_for):
        ax.annotate("%.2f"%j,xy=(i,j-2),fontsize=12,color='blue')#,stretch='ultra-condensed',rotation=0)
    for i,j in zip(lambda_val,grad_back):
        ax.annotate("%.2f"%j,xy=(i,j+2),fontsize=12,color='green')#,stretch='condensed',rotation=0)

    return fig


#plot of different masses allbonds gradients
dm_mf_abv = loadtxt("different_masses/all_bonds/2MF/vacuum/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_mf_abf = loadtxt("different_masses/all_bonds/2MF/free/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_met_abv = loadtxt("different_masses/all_bonds/methane/vacuum/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_met_abf = loadtxt("different_masses/all_bonds/methane/free/gradient_profile.dat",usecols=[0,1,2],skiprows=1)

dm_mf_nov = loadtxt("different_masses/no_constr/2MF/vacuum/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_mf_nof = loadtxt("different_masses/no_constr/2MF/vacuum/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_met_nov = loadtxt("different_masses/no_constr/methane/vacuum/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_met_nof = loadtxt("different_masses/no_constr/methane/free/gradient_profile.dat",usecols=[0,1,2],skiprows=1)

#plot of same masses all bonds and no
sm_mf_abv = loadtxt("same_masses/all_bonds/2MF/vacuum/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_mf_abf = loadtxt("same_masses/all_bonds/2MF/free/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_met_abv = loadtxt("same_masses/all_bonds/methane/vacuum/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_met_abf = loadtxt("same_masses/all_bonds/methane/free/gradient_profile.dat",usecols=[0,1,2],skiprows=1)

sm_mf_nov = loadtxt("same_masses/no_constr/2MF/vacuum/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_mf_nof = loadtxt("same_masses/no_constr/2MF/free/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_met_nov = loadtxt("same_masses/no_constr/methane/vacuum/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_met_nof = loadtxt("same_masses/no_constr/methane/free/gradient_profile.dat",usecols=[0,1,2],skiprows=1)


if not os.path.exists("output_results"):
    os.makedirs("output_results")

fig = plot_grad(dm_mf_abv,"2-methylfuran",dm_met_abv,"methane")
with PdfPages('output_results/diff_mass_vac_allbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(dm_mf_abf,"2-methylfuran",dm_met_abf,"methane")
with PdfPages('output_results/diff_mass_wat_allbonds.pdf') as pdf:
    pdf.savefig(fig)

fig=plot_grad(dm_mf_nov,"2-methylfuran",dm_met_nov,"methane")
with PdfPages('output_results/diff_mass_vac_noconstr.pdf') as pdf:
    pdf.savefig(fig)

fig=plot_grad(dm_mf_nof,"2-methylfuran",dm_met_nof,"methane")
with PdfPages('output_results/diff_mass_wat_noconstr.pdf') as pdf:
    pdf.savefig(fig)

fig=plot_grad(sm_mf_abv,"2-methylfuran",sm_met_abv,"methane")
with PdfPages('output_results/same_mass_vac_allbonds.pdf') as pdf:
    pdf.savefig(fig)

fig=plot_grad(sm_mf_abf,"2-methylfuran",sm_met_abf,"methane")
with PdfPages('output_results/same_mass_wat_allbonds.pdf') as pdf:
    pdf.savefig(fig)

fig=plot_grad(sm_mf_nov,"2-methylfuran",sm_met_nov,"methane")
with PdfPages('output_results/same_mass_vac_noconstr.pdf') as pdf:
    pdf.savefig(fig)

fig=plot_grad(sm_mf_nof,"2-methylfuran",sm_met_nof,"methane")
with PdfPages('output_results/same_mass_free_noconstr.pdf') as pdf:
    pdf.savefig(fig)




#then don'twforget we have AVERAGE.dat file to analyse!:


#2methylfurane different masses all bonds
mf_dm_ab = loadtxt("different_masses/all_bonds/2MF/AVERAGE.dat",usecols=[0])
#2methylfurane different masses noconst:
mf_dm_no = loadtxt("different_masses/no_constr/2MF/AVERAGE.dat",usecols=[0])
#2methylfurane same masses all bonds:
mf_sm_ab = loadtxt("same_masses/all_bonds/2MF/AVERAGE.dat",usecols=[0])
#2methylfurane same masses noconst:
mf_sm_no = loadtxt("same_masses/no_constr/2MF/AVERAGE.dat",usecols=[0])

#methane different masses all bonds:
met_dm_ab = loadtxt("different_masses/all_bonds/methane/AVERAGE.dat", usecols=[0])
#methane different masses noconst:
met_dm_no = loadtxt("different_masses/no_constr/methane/AVERAGE.dat", usecols=[0])
#methane same masses all bonds:
met_sm_ab = loadtxt("same_masses/all_bonds/methane/AVERAGE.dat",usecols=[0])
#methane same masses noconst:
met_sm_no = loadtxt("same_masses/no_constr/methane/AVERAGE.dat", usecols=[0])


output = open("output_results/VALUES.dat","w")

output.write("DIFFERENT MASSES ALL BONDS:\n")
output.write("2MF:      %.3f    \n"%(mf_dm_ab))
output.write("MET:      %.3f    \n"%(met_dm_ab))

output.write("DIFFERENT MASSES NO CONSTR:\n")
output.write("2MF:      %.3f    \n"%(mf_dm_no))
output.write("MET:      %.3f    \n"%(met_dm_no))

output.write("SAME MASSES ALL BONDS:\n")
output.write("2MF:      %.3f    \n"%(mf_sm_ab))
output.write("MET:      %.3f    \n"%(met_sm_ab))

output.write("SAME MASSES NO CONSTR:\n")
output.write("2MF:      %.3f    \n"%(mf_sm_no))
output.write("MET:      %.3f    \n"%(met_sm_no))
