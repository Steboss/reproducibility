#APR 2015 Stefano Bosisio
#Collect results from simulation folder:
# ethane~methane  fesetup_input  isobutane~propane  neopentane~isobutane  prepare.py  propane~ethane
#-AVERAGE DG_wat: AVERAGE.dat: DG +/- err
#-AVERAGE DG_vac: AVERAGE.dat  DG +/- err
#-DG_LJCOR      : freenrg-LJCOR.dat : DG +/- err
#-DG_FUNC       : freenrg-COULCOR.dat: DG +/- err
from numpy import *
from math import *
import os,sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
plt.rcParams['figure.figsize']=(12.0,10.0)
#Scheme: collect all the free energies
#Calcualte the rel.hyd.f.e. as:
#DG_wat - DG_vac  + (DG_func_1 - DG_func_0) + LJCOR
#DG_Func_1 -DG_func0 = DGFUNC

def relativehydration(water,vacuum,func,lj):
    #DG_vac/wat extract : [2] [4] average.dat
    #DG_FUNC : [2] [4]  freenrg-COULCOR.dat
    #LJCOR   : [2] [4]  freenrg-LJCOR.dat
    water.seek(0)
    vacuum.seek(0)
    func.seek(0)
    lj.seek(0)
    reader_wat  = water.readlines()
    reader_vac  = vacuum.readlines()
    reader_func = func.readlines()
    reader_lj   = lj.readlines()

    wat = float(reader_wat[len(reader_wat)-1].split()[2])
    #print(wat)
    err_wat = float(reader_wat[len(reader_wat)-1].split()[4])
#    print(wat)
    vac = float(reader_vac[len(reader_vac)-1].split()[2])
    #print(vac)
    err_vac = float(reader_vac[len(reader_vac)-1].split()[4])
#    print(vac)
    #print(reader_func[len(reader_func)-1].split())
    #print(reader_func[len(reader_func)-1].split()[2])
    func = float(reader_func[len(reader_func)-1].split()[2])
    #print(func)
    err_func = float(reader_func[len(reader_func)-1].split()[4])
    #print(err_func)
    ljcor = float(reader_lj[len(reader_lj)-1].split()[2])
    err_ljcor = float(reader_lj[len(reader_lj)-1].split()[4])

    DGhyd = wat - vac + func + ljcor
    errhyd = math.sqrt(err_wat**2 + err_vac**2 + err_func**2 + err_ljcor**2)
    return DGhyd,errhyd

def plot_grad(forward,name_for):

    lambda_val = forward[:,0]
    grad_for = forward[:,1]
    grad_for_err = forward[:,2]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    forw = ax.errorbar(lambda_val, grad_for, yerr=grad_for_err, marker = 'o',label=name_for,color='blue')
    ax.set_ylabel("$\partial$G/$\partial\lambda$",fontsize=25)
    ax.set_xlabel(r'$\lambda$',fontsize=25)
    plt.legend(loc='best',fontsize=25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.grid(True)

    return fig
###MAIN
# ethane~methane  fesetup_input  isobutane~propane  neopentane~isobutane  prepare.py  propane~ethane
#different masses all bonds 2methylfuran: water, vacuum, func1-0, LJCOR
etmet_grovac = open("ethane~methane/run001/vacuum/output/AVERAGE_gro.dat","r")
etmet_TIvac = open("ethane~methane/run001/vacuum/output/AVERAGE_TI.dat","r")
etmet_MBARvac = open("ethane~methane/run001/vacuum/output/AVERAGE_MBAR.dat","r")

etmet_growat = open("ethane~methane/run001/free/output/AVERAGE_gro.dat","r")
etmet_TIwat = open("ethane~methane/run001/free/output/AVERAGE_TI.dat","r")
etmet_MBARwat = open("ethane~methane/run001/free/output/AVERAGE_MBAR.dat","r")

etmet_func = open("ethane~methane/run001/free/output/freenrg-COULCOR.dat","r")
etmet_LJ = open("ethane~methane/run001/free/output/freenrg-LJCOR.dat","r")

##isobutane propane
isopro_grovac = open("isobutane~propane/run001/vacuum/output/AVERAGE_gro.dat","r")
isopro_TIvac = open("isobutane~propane/run001/vacuum/output/AVERAGE_TI.dat","r")
isopro_MBARvac = open("isobutane~propane/run001/vacuum/output/AVERAGE_MBAR.dat","r")

isopro_growat = open("isobutane~propane/run001/free/output/AVERAGE_gro.dat","r")
isopro_TIwat = open("isobutane~propane/run001/free/output/AVERAGE_TI.dat","r")
isopro_MBARwat = open("isobutane~propane/run001/free/output/AVERAGE_MBAR.dat","r")

isopro_func = open("isobutane~propane/run001/free/output/freenrg-COULCOR.dat","r")
isopro_LJ = open("isobutane~propane/run001/free/output/freenrg-LJCOR.dat","r")

##Neopentane isobutane
neoiso_grovac = open("neopentane~isobutane/run001/vacuum/output/AVERAGE_gro.dat","r")
neoiso_TIvac = open("neopentane~isobutane/run001/vacuum/output/AVERAGE_TI.dat","r")
neoiso_MBARvac = open("neopentane~isobutane/run001/vacuum/output/AVERAGE_MBAR.dat","r")

neoiso_growat = open("neopentane~isobutane/run001/free/output/AVERAGE_gro.dat","r")
neoiso_TIwat = open("neopentane~isobutane/run001/free/output/AVERAGE_TI.dat","r")
neoiso_MBARwat = open("neopentane~isobutane/run001/free/output/AVERAGE_MBAR.dat","r")

neoiso_func = open("neopentane~isobutane/run001/free/output/freenrg-COULCOR.dat","r")
neoiso_LJ = open("neopentane~isobutane/run001/free/output/freenrg-LJCOR.dat","r")

#propane ethane
proeth_grovac = open("propane~ethane/run001/vacuum/output/AVERAGE_gro.dat","r")
proeth_TIvac = open("propane~ethane/run001/vacuum/output/AVERAGE_TI.dat","r")
proeth_MBARvac = open("propane~ethane/run001/vacuum/output/AVERAGE_MBAR.dat","r")

proeth_growat = open("propane~ethane/run001/free/output/AVERAGE_gro.dat","r")
proeth_TIwat = open("propane~ethane/run001/free/output/AVERAGE_TI.dat","r")
proeth_MBARwat = open("propane~ethane/run001/free/output/AVERAGE_MBAR.dat","r")

proeth_func = open("propane~ethane/run001/free/output/freenrg-COULCOR.dat","r")
proeth_LJ = open("propane~ethane/run001/free/output/freenrg-LJCOR.dat","r")


# ethane~methane  fesetup_input  isobutane~propane  neopentane~isobutane  prepare.py  propane~ethane
etmet_gro,etmet_gro_err = relativehydration(etmet_growat,etmet_grovac,etmet_func,etmet_LJ)
etmet_TI,etmet_TI_err = relativehydration(etmet_TIwat,etmet_TIvac,etmet_func,etmet_LJ)
etmet_MB,etmet_MB_err = relativehydration(etmet_MBARwat,etmet_MBARvac,etmet_func,etmet_LJ)

isopro_gro,isopro_gro_err =relativehydration(isopro_growat,isopro_grovac,isopro_func,isopro_LJ)
isopro_TI,isopro_TI_err =relativehydration(isopro_TIwat,isopro_TIvac,isopro_func,isopro_LJ)
isopro_MB,isopro_MB_err =relativehydration(isopro_MBARwat,isopro_MBARvac,isopro_func,isopro_LJ)

neoiso_gro,neoiso_gro_err = relativehydration(neoiso_growat,neoiso_grovac,neoiso_func,neoiso_LJ)
neoiso_TI,neoiso_TI_err = relativehydration(neoiso_TIwat,neoiso_TIvac,neoiso_func,neoiso_LJ)
neoiso_MB,neoiso_MB_err = relativehydration(neoiso_MBARwat,neoiso_MBARvac,neoiso_func,neoiso_LJ)

proeth_gro,proeth_gro_err = relativehydration(proeth_growat,proeth_grovac,proeth_func,proeth_LJ)
proeth_TI,proeth_TI_err = relativehydration(proeth_TIwat,proeth_TIvac,proeth_func,proeth_LJ)
proeth_MB,proeth_MB_err = relativehydration(proeth_MBARwat,proeth_MBARvac,proeth_func,proeth_LJ)

#save everything in output_results:
if not os.path.exists("output_results"):
    os.makedirs("output_results")

# ethane~methane  fesetup_input  isobutane~propane  neopentane~isobutane  prepare.py  propane~ethane

hyd_output = open("output_results/VALUES.dat","w")

hyd_output.write("Neopentane~isobutane\n")
hyd_output.write("Spline:    %8.5f +/- %8.5f\n" %(neoiso_gro,neoiso_gro_err))
hyd_output.write("TIregr:    %8.5f +/- %8.5f\n" %(neoiso_TI,neoiso_TI_err))
hyd_output.write("MBAR  :    %8.5f +/- %8.5f\n" %(neoiso_MB,neoiso_MB_err))
hyd_output.write("Isobutane~propane\n")
hyd_output.write("Spline:    %8.5f +/- %8.5f\n" %(isopro_gro,isopro_gro_err))
hyd_output.write("TIregr:    %8.5f +/- %8.5f\n" %(isopro_TI,isopro_TI_err))
hyd_output.write("MBAR  :    %8.5f +/- %8.5f\n" %(isopro_MB,isopro_MB_err))
hyd_output.write("Propane~ethane\n")
hyd_output.write("Spline:    %8.5f +/- %8.5f\n" %(proeth_gro,proeth_gro_err))
hyd_output.write("TIregr:    %8.5f +/- %8.5f\n" %(proeth_TI,proeth_TI_err))
hyd_output.write("MBAR  :    %8.5f +/- %8.5f\n" %(proeth_MB,proeth_MB_err))
hyd_output.write("Ethane~methane\n")
hyd_output.write("Spline:    %8.5f +/- %8.5f\n" %(etmet_gro,etmet_gro_err))
hyd_output.write("TIregr:    %8.5f +/- %8.5f\n" %(etmet_TI,etmet_TI_err))
hyd_output.write("MBAR  :    %8.5f +/- %8.5f\n" %(etmet_MB,etmet_MB_err))

neomet_gro = neoiso_gro + isopro_gro + proeth_gro - etmet_gro
neomet_gro_err = sqrt(neoiso_gro_err**2 + isopro_gro_err**2 + proeth_gro_err**2 + etmet_gro_err**2)

neomet_TI = neoiso_TI + isopro_TI + proeth_TI - etmet_TI
neomet_TI_err = sqrt(neoiso_TI_err**2 + isopro_TI_err**2 + proeth_TI_err**2 + etmet_TI_err**2)

neomet_MB = neoiso_MB + isopro_MB + proeth_MB - etmet_MB
neomet_MB_err  = sqrt(neoiso_MB_err**2 + isopro_MB_err**2 + proeth_MB_err**2 + etmet_MB_err**2)


hyd_output.write("Neopentane~methane\n")
hyd_output.write("Spline:    %8.5f +/- %8.5f\n"% (neomet_gro,neomet_gro_err))
hyd_output.write("TIregr:    %8.5f +/- %8.5f\n"% (neomet_TI,neomet_TI_err))
hyd_output.write("MBAR  :    %8.5f +/- %8.5f\n"% (neomet_MB,neomet_MB_err))

#Create gradient profiles and save them to output_results
etmet_vac = loadtxt("ethane~methane/run001/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
etmet_wat = loadtxt("ethane~methane/run001/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
##isobutane propane
isopro_vac = loadtxt("isobutane~propane/run001/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
isopro_wat = loadtxt("isobutane~propane/run001/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
##Neopentane isobutane
neoiso_vac = loadtxt("neopentane~isobutane/run001/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
neoiso_wat = loadtxt("neopentane~isobutane/run001/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#propane ethane
proeth_vac = loadtxt("propane~ethane/run001/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
proeth_wat = loadtxt("propane~ethane/run001/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)


fig = plot_grad(etmet_vac,"ethane~methane")
if not os.path.exists("output_results/ethane~methane"):
    os.makedirs("output_results/ethane~methane")
with PdfPages('output_results/ethane~methane/ethane_methane_vac.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(etmet_wat,"ethane~methane")
with PdfPages('output_results/ethane~methane/ethane_methane_wat.pdf') as pdf:
    pdf.savefig(fig)

if not os.path.exists("output_results/isobutane~propane"):
    os.makedirs("output_results/isobutane~propane")
fig = plot_grad(isopro_vac,"isobutane~propane")
with PdfPages('output_results/isobutane~propane/isob_prop_vac.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(isopro_wat,"isobutane~propane")
with PdfPages('output_results/isobutane~propane/isob_prop_wat.pdf') as pdf:
    pdf.savefig(fig)

if not os.path.exists("output_results/neopentane~isobutane"):
    os.makedirs("output_results/neopentane~isobutane")
fig = plot_grad(neoiso_vac,"neopentane~isobutane")
with PdfPages('output_results/neopentane~isobutane/neop_isob_vac.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(neoiso_wat,"neopentane~isobutane")
with PdfPages('output_results/neopentane~isobutane/neop_isob_wat.pdf') as pdf:
    pdf.savefig(fig)

if not os.path.exists("output_results/propane~ethane"):
    os.makedirs("output_results/propane~ethane")
fig = plot_grad(proeth_vac,"propane~ethane")
with PdfPages('output_results/propane~ethane/prop_eth_vac.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(proeth_wat,"propane~ethane")
with PdfPages('output_results/propane~ethane/prop_eth_wat.pdf') as pdf:
    pdf.savefig(fig)
