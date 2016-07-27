#APR 2015 Stefano Bosisio
#Collect results from simulation folder:
#-AVERAGE DG_wat: AVERAGE.dat: DG +/- err
#-AVERAGE DG_vac: AVERAGE.dat  DG +/- err
#-DG_LJCOR      : freenrg-LJCOR.dat : DG +/- err
#-DG_FUNC       : freenrg-COULCOR.dat: DG +/- err
from numpy import *
import os,sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
plt.rcParams['figure.figsize']=(12.0,10.0)


def relativehydration(water,vacuum,func,lj):
    #DG_vac/wat extract : [2] [4] average.dat
    #DG_FUNC : [2] [4]  freenrg-COULCOR.dat
    #LJCOR   : [2] [4]  freenrg-LJCOR.dat

    name  = water.split("/")[2]
    constraint = water.split("/")[1]
    spacing = water.split("/")[3]
    integration = water.split("/")[6].split("_")[1].split(".")[0]

    reader_wat  = open(water,"r").readlines()
    reader_vac  = open(vacuum,"r").readlines()
    reader_func = open(func,"r").readlines()
    reader_lj   =  open(lj,"r").readlines()
    wat = float(reader_wat[len(reader_wat)-1].split()[2])
    err_wat = float(reader_wat[len(reader_wat)-1].split()[4])

    vac = float(reader_vac[len(reader_vac)-1].split()[2])
    err_vac = float(reader_vac[len(reader_vac)-1].split()[4])

    funct = float(reader_func[len(reader_func)-1].split()[2])
    err_func = float(reader_func[len(reader_func)-1].split()[4])

    ljcor = float(reader_lj[len(reader_lj)-1].split()[2])
    err_ljcor = float(reader_lj[len(reader_lj)-1].split()[4])

    DGhyd = wat - vac + funct + ljcor
    errhyd = math.sqrt(err_wat**2 + err_vac**2 + err_func**2 + err_ljcor**2)

    name_csv = "output_results/"+name+"_"+constraint+"_"+spacing+"_"+integration+".csv"
    csv_file =  open(name_csv,"w")
    csv_file.write("%s with %s constraints and %s spacing with %s integration" %(name,constraint,spacing,integration))
    csv_file.write("DG_vac,err,DG_wat,err,FUNC,LJCOR,DDG_HYD,err")
    csv_file.write("%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f" %(vac,err_vac,wat,err_wat,funct,ljcor,DGhyd,errhyd))


    return DGhyd,errhyd

def plot_grad(forward,name_for,backward,name_back):

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

    fig = plt.figure()
    ax = fig.add_subplot(111)
    forw = ax.errorbar(lambda_val, grad_for, yerr=grad_for_err, marker = 'o',label=name_for,color='blue')
    backw =ax.errorbar(lambda_back, grad_back, yerr=grad_back_err,marker='o',label=name_back,color='green')
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

 #if not os.path.exists(path):
        #return [999.0, 999.0], [999.0, 999.0], [999.0, 999.0]



#save everything in output_results:
if not os.path.exists("output_results/"):
    os.makedirs("output_results/")

###MAIN
#different masses all bonds 2MF EQUI
dm_2mf_abv_equi =  "diff_masses/all_bonds/2methylfurane~methane/equi/vacuum/output/AVERAGE_gro.dat"
dm_2mf_abTIv_equi  =  "diff_masses/all_bonds/2methylfurane~methane/equi/vacuum/output/AVERAGE_TI.dat"
dm_2mf_abw_equi  =  "diff_masses/all_bonds/2methylfurane~methane/equi/free/output/AVERAGE_gro.dat"
dm_2mf_abTIw_equi = "diff_masses/all_bonds/2methylfurane~methane/equi/free/output/AVERAGE_TI.dat"
dm_2mf_abF_equi  =  "diff_masses/all_bonds/2methylfurane~methane/equi/free/output/freenrg-COULCOR.dat"
dm_2mf_abLJ_equi  =  "diff_masses/all_bonds/2methylfurane~methane/equi/free/output/freenrg-LJCOR.dat"
#different masses all bonds 2MF NO_SIMM
dm_2mf_abv_no =  "diff_masses/all_bonds/2methylfurane~methane/no_simm/vacuum/output/AVERAGE_gro.dat"
dm_2mf_abTIv_no =  "diff_masses/all_bonds/2methylfurane~methane/no_simm/vacuum/output/AVERAGE_TI.dat"
dm_2mf_abw_no =  "diff_masses/all_bonds/2methylfurane~methane/no_simm/free/output/AVERAGE_gro.dat"
dm_2mf_abTIw_no= "diff_masses/all_bonds/2methylfurane~methane/no_simm/free/output/AVERAGE_TI.dat"
dm_2mf_abF_no =  "diff_masses/all_bonds/2methylfurane~methane/no_simm/free/output/freenrg-COULCOR.dat"
dm_2mf_abLJ_no =  "diff_masses/all_bonds/2methylfurane~methane/no_simm/free/output/freenrg-LJCOR.dat"
#different masses all bonsd 2MF  SIMM
dm_2mf_abv =  "diff_masses/all_bonds/2methylfurane~methane/simm/vacuum/output/AVERAGE_gro.dat"
dm_2mf_abTIv =  "diff_masses/all_bonds/2methylfurane~methane/simm/vacuum/output/AVERAGE_TI.dat"
dm_2mf_abw =  "diff_masses/all_bonds/2methylfurane~methane/simm/free/output/AVERAGE_gro.dat"
dm_2mf_abTIw= "diff_masses/all_bonds/2methylfurane~methane/simm/free/output/AVERAGE_TI.dat"
dm_2mf_abF =  "diff_masses/all_bonds/2methylfurane~methane/simm/free/output/freenrg-COULCOR.dat"
dm_2mf_abLJ =  "diff_masses/all_bonds/2methylfurane~methane/simm/free/output/freenrg-LJCOR.dat"

#different masses h  bonds 2MF EQUI
dm_2mf_hbv_equi =  "diff_masses/h_bonds/2methylfurane~methane/equi/vacuum/output/AVERAGE_gro.dat"
dm_2mf_hbTIv_equi  =  "diff_masses/h_bonds/2methylfurane~methane/equi/vacuum/output/AVERAGE_TI.dat"
dm_2mf_hbw_equi  =  "diff_masses/h_bonds/2methylfurane~methane/equi/free/output/AVERAGE_gro.dat"
dm_2mf_hbTIw_equi = "diff_masses/h_bonds/2methylfurane~methane/equi/free/output/AVERAGE_TI.dat"
dm_2mf_hbF_equi  =  "diff_masses/h_bonds/2methylfurane~methane/equi/free/output/freenrg-COULCOR.dat"
dm_2mf_hbLJ_equi  =  "diff_masses/h_bonds/2methylfurane~methane/equi/free/output/freenrg-LJCOR.dat"
#different masses h bonds 2MF NO_SIMM
dm_2mf_hbv_no =  "diff_masses/h_bonds/2methylfurane~methane/no_simm/vacuum/output/AVERAGE_gro.dat"
dm_2mf_hbTIv_no =  "diff_masses/h_bonds/2methylfurane~methane/no_simm/vacuum/output/AVERAGE_TI.dat"
dm_2mf_hbw_no =  "diff_masses/h_bonds/2methylfurane~methane/no_simm/free/output/AVERAGE_gro.dat"
dm_2mf_hbTIw_no= "diff_masses/h_bonds/2methylfurane~methane/no_simm/free/output/AVERAGE_TI.dat"
dm_2mf_hbF_no =  "diff_masses/h_bonds/2methylfurane~methane/no_simm/free/output/freenrg-COULCOR.dat"
dm_2mf_hbLJ_no =  "diff_masses/h_bonds/2methylfurane~methane/no_simm/free/output/freenrg-LJCOR.dat"
#different masses h bonsd 2MF  SIMM
dm_2mf_hbv =  "diff_masses/h_bonds/2methylfurane~methane/simm/vacuum/output/AVERAGE_gro.dat"
dm_2mf_hbTIv =  "diff_masses/h_bonds/2methylfurane~methane/simm/vacuum/output/AVERAGE_TI.dat"
dm_2mf_hbw =  "diff_masses/h_bonds/2methylfurane~methane/simm/free/output/AVERAGE_gro.dat"
dm_2mf_hbTIw= "diff_masses/h_bonds/2methylfurane~methane/simm/free/output/AVERAGE_TI.dat"
dm_2mf_hbF =  "diff_masses/h_bonds/2methylfurane~methane/simm/free/output/freenrg-COULCOR.dat"
dm_2mf_hbLJ =  "diff_masses/h_bonds/2methylfurane~methane/simm/free/output/freenrg-LJCOR.dat"


#same masses all bonds 2MF EQUI
sm_2mf_abv_equi =  "same_masses/all_bonds/2methylfurane~methane/equi/vacuum/output/AVERAGE_gro.dat"
sm_2mf_abTIv_equi  =  "same_masses/all_bonds/2methylfurane~methane/equi/vacuum/output/AVERAGE_TI.dat"
sm_2mf_abw_equi  =  "same_masses/all_bonds/2methylfurane~methane/equi/free/output/AVERAGE_gro.dat"
sm_2mf_abTIw_equi = "same_masses/all_bonds/2methylfurane~methane/equi/free/output/AVERAGE_TI.dat"
sm_2mf_abF_equi  =  "same_masses/all_bonds/2methylfurane~methane/equi/free/output/freenrg-COULCOR.dat"
sm_2mf_abLJ_equi  =  "same_masses/all_bonds/2methylfurane~methane/equi/free/output/freenrg-LJCOR.dat"
#same masses all bonds 2MF NO_SIMM
sm_2mf_abv_no =  "same_masses/all_bonds/2methylfurane~methane/no_simm/vacuum/output/AVERAGE_gro.dat"
sm_2mf_abTIv_no =  "same_masses/all_bonds/2methylfurane~methane/no_simm/vacuum/output/AVERAGE_TI.dat"
sm_2mf_abw_no =  "same_masses/all_bonds/2methylfurane~methane/no_simm/free/output/AVERAGE_gro.dat"
sm_2mf_abTIw_no= "same_masses/all_bonds/2methylfurane~methane/no_simm/free/output/AVERAGE_TI.dat"
sm_2mf_abF_no =  "same_masses/all_bonds/2methylfurane~methane/no_simm/free/output/freenrg-COULCOR.dat"
sm_2mf_abLJ_no =  "same_masses/all_bonds/2methylfurane~methane/no_simm/free/output/freenrg-LJCOR.dat"
#same masses all bonsd 2MF  SIMM
sm_2mf_abv =  "same_masses/all_bonds/2methylfurane~methane/simm/vacuum/output/AVERAGE_gro.dat"
sm_2mf_abTIv =  "same_masses/all_bonds/2methylfurane~methane/simm/vacuum/output/AVERAGE_TI.dat"
sm_2mf_abw =  "same_masses/all_bonds/2methylfurane~methane/simm/free/output/AVERAGE_gro.dat"
sm_2mf_abTIw= "same_masses/all_bonds/2methylfurane~methane/simm/free/output/AVERAGE_TI.dat"
sm_2mf_abF =  "same_masses/all_bonds/2methylfurane~methane/simm/free/output/freenrg-COULCOR.dat"
sm_2mf_abLJ =  "same_masses/all_bonds/2methylfurane~methane/simm/free/output/freenrg-LJCOR.dat"

#same masses h  bonds 2MF EQUI
sm_2mf_hbv_equi =  "same_masses/h_bonds/2methylfurane~methane/equi/vacuum/output/AVERAGE_gro.dat"
sm_2mf_hbTIv_equi  =  "same_masses/h_bonds/2methylfurane~methane/equi/vacuum/output/AVERAGE_TI.dat"
sm_2mf_hbw_equi  =  "same_masses/h_bonds/2methylfurane~methane/equi/free/output/AVERAGE_gro.dat"
sm_2mf_hbTIw_equi = "same_masses/h_bonds/2methylfurane~methane/equi/free/output/AVERAGE_TI.dat"
sm_2mf_hbF_equi  =  "same_masses/h_bonds/2methylfurane~methane/equi/free/output/freenrg-COULCOR.dat"
sm_2mf_hbLJ_equi  =  "same_masses/h_bonds/2methylfurane~methane/equi/free/output/freenrg-LJCOR.dat"
#same masses h bonds 2MF NO_SIMM
sm_2mf_hbv_no =  "same_masses/h_bonds/2methylfurane~methane/no_simm/vacuum/output/AVERAGE_gro.dat"
sm_2mf_hbTIv_no =  "same_masses/h_bonds/2methylfurane~methane/no_simm/vacuum/output/AVERAGE_TI.dat"
sm_2mf_hbw_no =  "same_masses/h_bonds/2methylfurane~methane/no_simm/free/output/AVERAGE_gro.dat"
sm_2mf_hbTIw_no= "same_masses/h_bonds/2methylfurane~methane/no_simm/free/output/AVERAGE_TI.dat"
sm_2mf_hbF_no =  "same_masses/h_bonds/2methylfurane~methane/no_simm/free/output/freenrg-COULCOR.dat"
sm_2mf_hbLJ_no =  "same_masses/h_bonds/2methylfurane~methane/no_simm/free/output/freenrg-LJCOR.dat"
#same masses h bonds 2MF NO_SIMM
sm_2mf_hbv =  "same_masses/h_bonds/2methylfurane~methane/simm/vacuum/output/AVERAGE_gro.dat"
sm_2mf_hbTIv =  "same_masses/h_bonds/2methylfurane~methane/simm/vacuum/output/AVERAGE_TI.dat"
sm_2mf_hbw =  "same_masses/h_bonds/2methylfurane~methane/simm/free/output/AVERAGE_gro.dat"
sm_2mf_hbTIw= "same_masses/h_bonds/2methylfurane~methane/simm/free/output/AVERAGE_TI.dat"
sm_2mf_hbF =  "same_masses/h_bonds/2methylfurane~methane/simm/free/output/freenrg-COULCOR.dat"
sm_2mf_hbLJ =  "same_masses/h_bonds/2methylfurane~methane/simm/free/output/freenrg-LJCOR.dat"
################################################################################################################################

#different masses all bonds met EQUI
dm_met_abv_equi =  "diff_masses/all_bonds/methane~2methylfurane/equi/vacuum/output/AVERAGE_gro.dat"
dm_met_abTIv_equi  =  "diff_masses/all_bonds/methane~2methylfurane/equi/vacuum/output/AVERAGE_TI.dat"
dm_met_abw_equi  =  "diff_masses/all_bonds/methane~2methylfurane/equi/free/output/AVERAGE_gro.dat"
dm_met_abTIw_equi = "diff_masses/all_bonds/methane~2methylfurane/equi/free/output/AVERAGE_TI.dat"
dm_met_abF_equi  =  "diff_masses/all_bonds/methane~2methylfurane/equi/free/output/freenrg-COULCOR.dat"
dm_met_abLJ_equi  =  "diff_masses/all_bonds/methane~2methylfurane/equi/free/output/freenrg-LJCOR.dat"
#different masses all bonds met NO_SIMM
dm_met_abv_no =  "diff_masses/all_bonds/methane~2methylfurane/no_simm/vacuum/output/AVERAGE_gro.dat"
dm_met_abTIv_no =  "diff_masses/all_bonds/methane~2methylfurane/no_simm/vacuum/output/AVERAGE_TI.dat"
dm_met_abw_no =  "diff_masses/all_bonds/methane~2methylfurane/no_simm/free/output/AVERAGE_gro.dat"
dm_met_abTIw_no= "diff_masses/all_bonds/methane~2methylfurane/no_simm/free/output/AVERAGE_TI.dat"
dm_met_abF_no =  "diff_masses/all_bonds/methane~2methylfurane/no_simm/free/output/freenrg-COULCOR.dat"
dm_met_abLJ_no =  "diff_masses/all_bonds/methane~2methylfurane/no_simm/free/output/freenrg-LJCOR.dat"
#different masses all bonsd met  SIMM
dm_met_abv =  "diff_masses/all_bonds/methane~2methylfurane/simm/vacuum/output/AVERAGE_gro.dat"
dm_met_abTIv =  "diff_masses/all_bonds/methane~2methylfurane/simm/vacuum/output/AVERAGE_TI.dat"
dm_met_abw =  "diff_masses/all_bonds/methane~2methylfurane/simm/free/output/AVERAGE_gro.dat"
dm_met_abTIw= "diff_masses/all_bonds/methane~2methylfurane/simm/free/output/AVERAGE_TI.dat"
dm_met_abF =  "diff_masses/all_bonds/methane~2methylfurane/simm/free/output/freenrg-COULCOR.dat"
dm_met_abLJ =  "diff_masses/all_bonds/methane~2methylfurane/simm/free/output/freenrg-LJCOR.dat"

#different masses h  bonds met EQUI
dm_met_hbv_equi =  "diff_masses/h_bonds/methane~2methylfurane/equi/vacuum/output/AVERAGE_gro.dat"
dm_met_hbTIv_equi  =  "diff_masses/h_bonds/methane~2methylfurane/equi/vacuum/output/AVERAGE_TI.dat"
dm_met_hbw_equi  =  "diff_masses/h_bonds/methane~2methylfurane/equi/free/output/AVERAGE_gro.dat"
dm_met_hbTIw_equi = "diff_masses/h_bonds/methane~2methylfurane/equi/free/output/AVERAGE_TI.dat"
dm_met_hbF_equi  =  "diff_masses/h_bonds/methane~2methylfurane/equi/free/output/freenrg-COULCOR.dat"
dm_met_hbLJ_equi  =  "diff_masses/h_bonds/methane~2methylfurane/equi/free/output/freenrg-LJCOR.dat"
#different masses h bonds met NO_SIMM
dm_met_hbv_no =  "diff_masses/h_bonds/methane~2methylfurane/no_simm/vacuum/output/AVERAGE_gro.dat"
dm_met_hbTIv_no =  "diff_masses/h_bonds/methane~2methylfurane/no_simm/vacuum/output/AVERAGE_TI.dat"
dm_met_hbw_no =  "diff_masses/h_bonds/methane~2methylfurane/no_simm/free/output/AVERAGE_gro.dat"
dm_met_hbTIw_no= "diff_masses/h_bonds/methane~2methylfurane/no_simm/free/output/AVERAGE_TI.dat"
dm_met_hbF_no =  "diff_masses/h_bonds/methane~2methylfurane/no_simm/free/output/freenrg-COULCOR.dat"
dm_met_hbLJ_no =  "diff_masses/h_bonds/methane~2methylfurane/no_simm/free/output/freenrg-LJCOR.dat"
#different masses h bonsd met  SIMM
dm_met_hbv =  "diff_masses/h_bonds/methane~2methylfurane/simm/vacuum/output/AVERAGE_gro.dat"
dm_met_hbTIv =  "diff_masses/h_bonds/methane~2methylfurane/simm/vacuum/output/AVERAGE_TI.dat"
dm_met_hbw =  "diff_masses/h_bonds/methane~2methylfurane/simm/free/output/AVERAGE_gro.dat"
dm_met_hbTIw= "diff_masses/h_bonds/methane~2methylfurane/simm/free/output/AVERAGE_TI.dat"
dm_met_hbF =  "diff_masses/h_bonds/methane~2methylfurane/simm/free/output/freenrg-COULCOR.dat"
dm_met_hbLJ =  "diff_masses/h_bonds/methane~2methylfurane/simm/free/output/freenrg-LJCOR.dat"


#same masses all bonds met EQUI
sm_met_abv_equi =  "same_masses/all_bonds/methane~2methylfurane/equi/vacuum/output/AVERAGE_gro.dat"
sm_met_abTIv_equi  =  "same_masses/all_bonds/methane~2methylfurane/equi/vacuum/output/AVERAGE_TI.dat"
sm_met_abw_equi  =  "same_masses/all_bonds/methane~2methylfurane/equi/free/output/AVERAGE_gro.dat"
sm_met_abTIw_equi = "same_masses/all_bonds/methane~2methylfurane/equi/free/output/AVERAGE_TI.dat"
sm_met_abF_equi  =  "same_masses/all_bonds/methane~2methylfurane/equi/free/output/freenrg-COULCOR.dat"
sm_met_abLJ_equi  =  "same_masses/all_bonds/methane~2methylfurane/equi/free/output/freenrg-LJCOR.dat"
#same masses all bonds met NO_SIMM
sm_met_abv_no =  "same_masses/all_bonds/methane~2methylfurane/no_simm/vacuum/output/AVERAGE_gro.dat"
sm_met_abTIv_no =  "same_masses/all_bonds/methane~2methylfurane/no_simm/vacuum/output/AVERAGE_TI.dat"
sm_met_abw_no =  "same_masses/all_bonds/methane~2methylfurane/no_simm/free/output/AVERAGE_gro.dat"
sm_met_abTIw_no= "same_masses/all_bonds/methane~2methylfurane/no_simm/free/output/AVERAGE_TI.dat"
sm_met_abF_no =  "same_masses/all_bonds/methane~2methylfurane/no_simm/free/output/freenrg-COULCOR.dat"
sm_met_abLJ_no =  "same_masses/all_bonds/methane~2methylfurane/no_simm/free/output/freenrg-LJCOR.dat"
#samasses all bonsd met  SIMM
sm_met_abv =  "same_masses/all_bonds/methane~2methylfurane/simm/vacuum/output/AVERAGE_gro.dat"
sm_met_abTIv =  "same_masses/all_bonds/methane~2methylfurane/simm/vacuum/output/AVERAGE_TI.dat"
sm_met_abw =  "same_masses/all_bonds/methane~2methylfurane/simm/free/output/AVERAGE_gro.dat"
sm_met_abTIw= "same_masses/all_bonds/methane~2methylfurane/simm/free/output/AVERAGE_TI.dat"
sm_met_abF =  "same_masses/all_bonds/methane~2methylfurane/simm/free/output/freenrg-COULCOR.dat"
sm_met_abLJ =  "same_masses/all_bonds/methane~2methylfurane/simm/free/output/freenrg-LJCOR.dat"

#same masses h  bonds met EQUI
sm_met_hbv_equi =  "same_masses/h_bonds/methane~2methylfurane/equi/vacuum/output/AVERAGE_gro.dat"
sm_met_hbTIv_equi  =  "same_masses/h_bonds/methane~2methylfurane/equi/vacuum/output/AVERAGE_TI.dat"
sm_met_hbw_equi  =  "same_masses/h_bonds/methane~2methylfurane/equi/free/output/AVERAGE_gro.dat"
sm_met_hbTIw_equi = "same_masses/h_bonds/methane~2methylfurane/equi/free/output/AVERAGE_TI.dat"
sm_met_hbF_equi  =  "same_masses/h_bonds/methane~2methylfurane/equi/free/output/freenrg-COULCOR.dat"
sm_met_hbLJ_equi =  "same_masses/h_bonds/methane~2methylfurane/equi/free/output/freenrg-LJCOR.dat"
#same masses h bonsd met   NOSIMM
sm_met_hbv_no =  "same_masses/h_bonds/methane~2methylfurane/no_simm/vacuum/output/AVERAGE_gro.dat"
sm_met_hbTIv_no =  "same_masses/h_bonds/methane~2methylfurane/no_simm/vacuum/output/AVERAGE_TI.dat"
sm_met_hbw_no =  "same_masses/h_bonds/methane~2methylfurane/no_simm/free/output/AVERAGE_gro.dat"
sm_met_hbTIw_no= "same_masses/h_bonds/methane~2methylfurane/no_simm/free/output/AVERAGE_TI.dat"
sm_met_hbF_no =  "same_masses/h_bonds/methane~2methylfurane/no_simm/free/output/freenrg-COULCOR.dat"
sm_met_hbLJ_no =  "same_masses/h_bonds/methane~2methylfurane/no_simm/free/output/freenrg-LJCOR.dat"
#same masses h bonsd met  SIMM
sm_met_hbv =  "same_masses/h_bonds/methane~2methylfurane/simm/vacuum/output/AVERAGE_gro.dat"
sm_met_hbTIv =  "same_masses/h_bonds/methane~2methylfurane/simm/vacuum/output/AVERAGE_TI.dat"
sm_met_hbw =  "same_masses/h_bonds/methane~2methylfurane/simm/free/output/AVERAGE_gro.dat"
sm_met_hbTIw= "same_masses/h_bonds/methane~2methylfurane/simm/free/output/AVERAGE_TI.dat"
sm_met_hbF =  "same_masses/h_bonds/methane~2methylfurane/simm/free/output/freenrg-COULCOR.dat"
sm_met_hbLJ =  "same_masses/h_bonds/methane~2methylfurane/simm/free/output/freenrg-LJCOR.dat"

print("Calculating relative free energies of hydration...")
############################################################################################################################
#2MF GROMACS:
DM_2MF_ABEQ,DM_2MF_ABEQerr = relativehydration(dm_2mf_abw_equi,dm_2mf_abv_equi,dm_2mf_abF_equi,dm_2mf_abLJ_equi)  #diff mass, all bonds, equi
DM_2MF_HBEQ,DM_2MF_HBEQerr = relativehydration(dm_2mf_hbw_equi,dm_2mf_hbv_equi,dm_2mf_hbF_equi,dm_2mf_hbLJ_equi)
DM_2MF_ABNO,DM_2MF_ABNOerr = relativehydration(dm_2mf_abw_no,dm_2mf_abv_no,dm_2mf_abF_no,dm_2mf_abLJ_no)
DM_2MF_HBNO,DM_2MF_HBNOerr = relativehydration(dm_2mf_hbw_no,dm_2mf_hbv_no,dm_2mf_hbF_no,dm_2mf_hbLJ_no)
DM_2MF_AB,DM_2MF_ABerr = relativehydration(dm_2mf_abw,dm_2mf_abv,dm_2mf_abF,dm_2mf_abLJ)
DM_2MF_HB,DM_2MF_NOerr = relativehydration(dm_2mf_hbw,dm_2mf_hbv,dm_2mf_hbF,dm_2mf_hbLJ)

SM_2MF_ABEQ,SM_2MF_ABEQerr = relativehydration(sm_2mf_abw_equi,sm_2mf_abv_equi,sm_2mf_abF_equi,sm_2mf_abLJ_equi)  #same mass, all bonds, equi
SM_2MF_HBEQ,SM_2MF_HBEQerr = relativehydration(sm_2mf_hbw_equi,sm_2mf_hbv_equi,sm_2mf_hbF_equi,sm_2mf_hbLJ_equi)
SM_2MF_ABNO,SM_2MF_ABNOerr = relativehydration(sm_2mf_abw_no,sm_2mf_abv_no,sm_2mf_abF_no,sm_2mf_abLJ_no)
SM_2MF_HBNO,SM_2MF_HBNOerr = relativehydration(sm_2mf_hbw_no,sm_2mf_hbv_no,sm_2mf_hbF_no,sm_2mf_hbLJ_no)
SM_2MF_AB,SM_2MF_ABerr = relativehydration(sm_2mf_abw,sm_2mf_abv,sm_2mf_abF,sm_2mf_abLJ)
SM_2MF_HB,SM_2MF_NOerr = relativehydration(sm_2mf_hbw,sm_2mf_hbv,sm_2mf_hbF,sm_2mf_hbLJ)
#2MF TI:
DM_2MF_ABTIEQ,DM_2MF_ABTIEQerr = relativehydration(dm_2mf_abTIw_equi,dm_2mf_abTIv_equi,dm_2mf_abF_equi,dm_2mf_abLJ_equi)  #diff mass, all bonds, equi
DM_2MF_HBTIEQ,DM_2MF_HBTIEQerr = relativehydration(dm_2mf_hbTIw_equi,dm_2mf_hbTIv_equi,dm_2mf_hbF_equi,dm_2mf_hbLJ_equi)
DM_2MF_ABTINO,DM_2MF_ABTINOerr = relativehydration(dm_2mf_abTIw_no,dm_2mf_abTIv_no,dm_2mf_abF_no,dm_2mf_abLJ_no)
DM_2MF_HBTINO,DM_2MF_HBTINOerr = relativehydration(dm_2mf_hbTIw_no,dm_2mf_hbTIv_no,dm_2mf_hbF_no,dm_2mf_hbLJ_no)
DM_2MF_ABTI,DM_2MF_ABTIerr = relativehydration(dm_2mf_abTIw,dm_2mf_abTIv,dm_2mf_abF,dm_2mf_abLJ)
DM_2MF_HBTI,DM_2MF_NOTIerr = relativehydration(dm_2mf_hbTIw,dm_2mf_hbTIv,dm_2mf_hbF,dm_2mf_hbLJ)

SM_2MF_ABTIEQ,SM_2MF_ABTIEQerr = relativehydration(sm_2mf_abTIw_equi,sm_2mf_abTIv_equi,sm_2mf_abF_equi,sm_2mf_abLJ_equi)  #same mass, all bonds, equi
SM_2MF_HBTIEQ,SM_2MF_HBTIEQerr = relativehydration(sm_2mf_hbTIw_equi,sm_2mf_hbTIv_equi,sm_2mf_hbF_equi,sm_2mf_hbLJ_equi)
SM_2MF_ABTINO,SM_2MF_ABTINOerr = relativehydration(sm_2mf_abTIw_no,sm_2mf_abTIv_no,sm_2mf_abF_no,sm_2mf_abLJ_no)
SM_2MF_HBTINO,SM_2MF_HBTINOerr = relativehydration(sm_2mf_hbTIw_no,sm_2mf_hbTIv_no,sm_2mf_hbF_no,sm_2mf_hbLJ_no)
SM_2MF_ABTI,SM_2MF_ABTIerr = relativehydration(sm_2mf_abTIw,sm_2mf_abTIv,sm_2mf_abF,sm_2mf_abLJ)
SM_2MF_HBTI,SM_2MF_NOTIerr = relativehydration(sm_2mf_hbTIw,sm_2mf_hbTIv,sm_2mf_hbF,sm_2mf_hbLJ)
#######################################################################################################################



#######################################################################################################################
#MET GROMACS:
#met GROMACS:
DM_MET_ABEQ,DM_MET_ABEQerr = relativehydration(dm_met_abw_equi,dm_met_abv_equi,dm_met_abF_equi,dm_met_abLJ_equi)  #diff mass, all bonds, equi
DM_MET_HBEQ,DM_MET_HBEQerr = relativehydration(dm_met_hbw_equi,dm_met_hbv_equi,dm_met_hbF_equi,dm_met_hbLJ_equi)
DM_MET_ABNO,DM_MET_ABNOerr = relativehydration(dm_met_abw_no,dm_met_abv_no,dm_met_abF_no,dm_met_abLJ_no)
DM_MET_HBNO,DM_MET_HBNOerr = relativehydration(dm_met_hbw_no,dm_met_hbv_no,dm_met_hbF_no,dm_met_hbLJ_no)
DM_MET_AB,DM_MET_ABerr = relativehydration(dm_met_abw,dm_met_abv,dm_met_abF,dm_met_abLJ)
DM_MET_HB,DM_MET_NOerr = relativehydration(dm_met_hbw,dm_met_hbv,dm_met_hbF,dm_met_hbLJ)

SM_MET_ABEQ,SM_MET_ABEQerr = relativehydration(sm_met_abw_equi,sm_met_abv_equi,sm_met_abF_equi,sm_met_abLJ_equi)  #same mass, all bonds, equi
SM_MET_HBEQ,SM_MET_HBEQerr = relativehydration(sm_met_hbw_equi,sm_met_hbv_equi,sm_met_hbF_equi,sm_met_hbLJ_equi)
SM_MET_ABNO,SM_MET_ABNOerr = relativehydration(sm_met_abw_no,sm_met_abv_no,sm_met_abF_no,sm_met_abLJ_no)
SM_MET_HBNO,SM_MET_HBNOerr = relativehydration(sm_met_hbw_no,sm_met_hbv_no,sm_met_hbF_no,sm_met_hbLJ_no)
SM_MET_AB,SM_MET_ABerr = relativehydration(sm_met_abw,sm_met_abv,sm_met_abF,sm_met_abLJ)
SM_MET_HB,SM_MET_NOerr = relativehydration(sm_met_hbw,sm_met_hbv,sm_met_hbF,sm_met_hbLJ)
#met TI:
DM_MET_ABTIEQ,DM_MET_ABTIEQerr = relativehydration(dm_met_abTIw_equi,dm_met_abTIv_equi,dm_met_abF_equi,dm_met_abLJ_equi)  #diff mass, all bonds, equi
DM_MET_HBTIEQ,DM_MET_HBTIEQerr = relativehydration(dm_met_hbTIw_equi,dm_met_hbTIv_equi,dm_met_hbF_equi,dm_met_hbLJ_equi)
DM_MET_ABTINO,DM_MET_ABTINOerr = relativehydration(dm_met_abTIw_no,dm_met_abTIv_no,dm_met_abF_no,dm_met_abLJ_no)
DM_MET_HBTINO,DM_MET_HBTINOerr = relativehydration(dm_met_hbTIw_no,dm_met_hbTIv_no,dm_met_hbF_no,dm_met_hbLJ_no)
DM_MET_ABTI,DM_MET_ABTIerr = relativehydration(dm_met_abTIw,dm_met_abTIv,dm_met_abF,dm_met_abLJ)
DM_MET_HBTI,DM_MET_NOTIerr = relativehydration(dm_met_hbTIw,dm_met_hbTIv,dm_met_hbF,dm_met_hbLJ)

SM_MET_ABTIEQ,SM_MET_ABTIEQerr = relativehydration(sm_met_abTIw_equi,sm_met_abTIv_equi,sm_met_abF_equi,sm_met_abLJ_equi)  #same mass, all bonds, equi
SM_MET_HBTIEQ,SM_MET_HBTIEQerr = relativehydration(sm_met_hbTIw_equi,sm_met_hbTIv_equi,sm_met_hbF_equi,sm_met_hbLJ_equi)
SM_MET_ABTINO,SM_MET_ABTINOerr = relativehydration(sm_met_abTIw_no,sm_met_abTIv_no,sm_met_abF_no,sm_met_abLJ_no)
SM_MET_HBTINO,SM_MET_HBTINOerr = relativehydration(sm_met_hbTIw_no,sm_met_hbTIv_no,sm_met_hbF_no,sm_met_hbLJ_no)
SM_MET_ABTI,SM_MET_ABTIerr = relativehydration(sm_met_abTIw,sm_met_abTIv,sm_met_abF,sm_met_abLJ)
SM_MET_HBTI,SM_MET_NOTIerr = relativehydration(sm_met_hbTIw,sm_met_hbTIv,sm_met_hbF,sm_met_hbLJ)
#######################################################################################################################


print("Writing output in output_results/")

hyd_output =  open("output_results/VALUES.dat","w")

hyd_output.write("Different masses All Bonds Equidistant Windows\n")
hyd_output.write("2MF Spline:    %8.5f +/- %8.5f\n" %(DM_2MF_ABEQ,DM_2MF_ABEQerr))
hyd_output.write("2MF TI:    %8.5f +/- %8.5f\n" %(DM_2MF_ABTIEQ,DM_2MF_ABTIEQerr))

hyd_output.write("MET Spline:    %8.5f +/- %8.5f\n" %(DM_MET_ABEQ,DM_MET_ABEQerr))
hyd_output.write("MET TI:    %8.5f +/- %8.5f\n" %(DM_MET_ABTIEQ,DM_MET_ABTIEQerr))

hyd_output.write("Different masses All Bonds Chebyshev equidistant Phi\n")
hyd_output.write("2MF Spline:    %8.5f +/- %8.5f\n" %(DM_2MF_AB,DM_2MF_ABerr))
hyd_output.write("2MF TI:    %8.5f +/- %8.5f\n" %(DM_2MF_ABTI,DM_2MF_ABTIerr))

hyd_output.write("MET Spline:    %8.5f +/- %8.5f\n" %(DM_MET_AB,DM_MET_ABerr))
hyd_output.write("MET TI:    %8.5f +/- %8.5f\n" %(DM_MET_ABTI,DM_MET_ABTIerr))

hyd_output.write("Different masses All Bonds Chebyshev not-equidistant Phi\n")
hyd_output.write("2MF Spline:    %8.5f +/- %8.5f\n" %(DM_2MF_ABNO,DM_2MF_ABNOerr))
hyd_output.write("2MF TI:    %8.5f +/- %8.5f\n" %(DM_2MF_ABTINO,DM_2MF_ABTINOerr))

hyd_output.write("MET Spline:    %8.5f +/- %8.5f\n" %(DM_MET_ABNO,DM_MET_ABNOerr))
hyd_output.write("MET TI:    %8.5f +/- %8.5f\n" %(DM_MET_ABTINO,DM_MET_ABTINOerr))
hyd_output.write("\n")

hyd_output.write("Same masses All Bonds Equidistant Windows\n")
hyd_output.write("2MF Spline:    %8.5f +/- %8.5f\n" %(SM_2MF_ABEQ,SM_2MF_ABEQerr))
hyd_output.write("2MF TI:    %8.5f +/- %8.5f\n" %(SM_2MF_ABTIEQ,SM_2MF_ABTIEQerr))

hyd_output.write("MET Spline:    %8.5f +/- %8.5f\n" %(SM_MET_ABEQ,SM_MET_ABEQerr))
hyd_output.write("MET TI:    %8.5f +/- %8.5f\n" %(SM_MET_ABTIEQ,SM_MET_ABTIEQerr))

hyd_output.write("Same masses All Bonds Chebyshev equidistant Phi\n")
hyd_output.write("2MF Spline:    %8.5f +/- %8.5f\n" %(SM_2MF_AB,SM_2MF_ABerr))
hyd_output.write("2MF TI:    %8.5f +/- %8.5f\n" %(SM_2MF_ABTI,SM_2MF_ABTIerr))

hyd_output.write("MET Spline:    %8.5f +/- %8.5f\n" %(SM_MET_AB,SM_MET_ABerr))
hyd_output.write("MET TI:    %8.5f +/- %8.5f\n" %(SM_MET_ABTI,SM_MET_ABTIerr))

hyd_output.write("Same masses All Bonds Chebyshev not-equidistant Phi\n")
hyd_output.write("2MF Spline:    %8.5f +/- %8.5f\n" %(SM_2MF_ABNO,SM_2MF_ABNOerr))
hyd_output.write("2MF TI:    %8.5f +/- %8.5f\n" %(SM_2MF_ABTINO,SM_2MF_ABTINOerr))

hyd_output.write("MET Spline:    %8.5f +/- %8.5f\n" %(SM_MET_ABNO,SM_MET_ABNOerr))
hyd_output.write("MET TI:    %8.5f +/- %8.5f\n" %(SM_MET_ABTINO,SM_MET_ABTINOerr))

################################################################################################################################
print("loading gradient profiles files...")
#############################################################################################################
#DIFFERENT MASSES 2METYILFURAN
#different masses all bonds met EQUI
dm_mf_abv_equi =  loadtxt("diff_masses/all_bonds/2methylfurane~methane/equi/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)#
dm_mf_abw_equi  =  loadtxt("diff_masses/all_bonds/2methylfurane~methane/equi/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)#
#different masses all bonds met NO_SIMM
dm_mf_abv_no =  loadtxt("diff_masses/all_bonds/2methylfurane~methane/no_simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_mf_abw_no =  loadtxt("diff_masses/all_bonds/2methylfurane~methane/no_simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#different masses all bonsd met  SIMM
dm_mf_abv =  loadtxt("diff_masses/all_bonds/2methylfurane~methane/simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_mf_abw =  loadtxt("diff_masses/all_bonds/2methylfurane~methane/simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)

#different masses h  bonds met EQUI,usecols=[0,1,2],skiprows=1)
dm_mf_hbv_equi =  loadtxt("diff_masses/h_bonds/2methylfurane~methane/equi/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_mf_hbw_equi  =  loadtxt("diff_masses/h_bonds/2methylfurane~methane/equi/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#different masses h bonds met NO_SIMM
dm_mf_hbv_no =  loadtxt("diff_masses/h_bonds/2methylfurane~methane/no_simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_mf_hbw_no =  loadtxt("diff_masses/h_bonds/2methylfurane~methane/no_simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#different masses h bonsd met  SIMM
dm_mf_hbv =  loadtxt("diff_masses/h_bonds/2methylfurane~methane/simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_mf_hbw =  loadtxt("diff_masses/h_bonds/2methylfurane~methane/simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#############################################################################################################
#DIFFERENT MASSES METHANE
#different masses all bonds met EQUI
dm_met_abv_equi =  loadtxt("diff_masses/all_bonds/methane~2methylfurane/equi/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)#
dm_met_abw_equi  =  loadtxt("diff_masses/all_bonds/methane~2methylfurane/equi/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)#
#different masses all bonds met NO_SIMM
dm_met_abv_no =  loadtxt("diff_masses/all_bonds/methane~2methylfurane/no_simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_met_abw_no =  loadtxt("diff_masses/all_bonds/methane~2methylfurane/no_simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#different masses all bonsd met  SIMM
dm_met_abv =  loadtxt("diff_masses/all_bonds/methane~2methylfurane/simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_met_abw =  loadtxt("diff_masses/all_bonds/methane~2methylfurane/simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)

#different masses h  bonds met EQUI,usecols=[0,1,2],skiprows=1)
dm_met_hbv_equi =  loadtxt("diff_masses/h_bonds/methane~2methylfurane/equi/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_met_hbw_equi  =  loadtxt("diff_masses/h_bonds/methane~2methylfurane/equi/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#different masses h bonds met NO_SIMM
dm_met_hbv_no =  loadtxt("diff_masses/h_bonds/methane~2methylfurane/no_simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_met_hbw_no =  loadtxt("diff_masses/h_bonds/methane~2methylfurane/no_simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#different masses h bonsd met  SIMM
dm_met_hbv =  loadtxt("diff_masses/h_bonds/methane~2methylfurane/simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
dm_met_hbw =  loadtxt("diff_masses/h_bonds/methane~2methylfurane/simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#############################################################################################################

#############################################################################################################
#SAME MASSES 2METHYLFURANE
#same masses all bonds met EQUI
sm_mf_abv_equi =  loadtxt("same_masses/all_bonds/2methylfurane~methane/equi/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)#
sm_mf_abw_equi  =  loadtxt("same_masses/all_bonds/2methylfurane~methane/equi/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)#
#same masses all bonds met NO_SIMM
sm_mf_abv_no =  loadtxt("same_masses/all_bonds/2methylfurane~methane/no_simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_mf_abw_no =  loadtxt("same_masses/all_bonds/2methylfurane~methane/no_simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#samasses all bonsd met  SIMM,usecols=[0,1,2],skiprows=1)
sm_mf_abv =  loadtxt("same_masses/all_bonds/2methylfurane~methane/simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_mf_abw =  loadtxt("same_masses/all_bonds/2methylfurane~methane/simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)

#same masses h  bonds met EQUI
sm_mf_hbv_equi =  loadtxt("same_masses/h_bonds/2methylfurane~methane/equi/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_mf_hbw_equi  =  loadtxt("same_masses/h_bonds/2methylfurane~methane/equi/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#same masses h bonsd met   NOSIMM
sm_mf_hbv_no =  loadtxt("same_masses/h_bonds/2methylfurane~methane/no_simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_mf_hbw_no =  loadtxt("same_masses/h_bonds/2methylfurane~methane/no_simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#same masses h bonsd met  SIMM
sm_mf_hbv =  loadtxt("same_masses/h_bonds/2methylfurane~methane/simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_mf_hbw =  loadtxt("same_masses/h_bonds/2methylfurane~methane/simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#############################################################################################################
#SAME MASSES METHANE
#same masses all bonds met EQUI
sm_met_abv_equi =  loadtxt("same_masses/all_bonds/methane~2methylfurane/equi/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)#
sm_met_abw_equi  =  loadtxt("same_masses/all_bonds/methane~2methylfurane/equi/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)#
#same masses all bonds met NO_SIMM
sm_met_abv_no =  loadtxt("same_masses/all_bonds/methane~2methylfurane/no_simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_met_abw_no =  loadtxt("same_masses/all_bonds/methane~2methylfurane/no_simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#samasses all bonsd met  SIMM,usecols=[0,1,2],skiprows=1)
sm_met_abv =  loadtxt("same_masses/all_bonds/methane~2methylfurane/simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_met_abw =  loadtxt("same_masses/all_bonds/methane~2methylfurane/simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)

#same masses h  bonds met EQUI
sm_met_hbv_equi =  loadtxt("same_masses/h_bonds/methane~2methylfurane/equi/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_met_hbw_equi  =  loadtxt("same_masses/h_bonds/methane~2methylfurane/equi/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#same masses h bonsd met   NOSIMM
sm_met_hbv_no =  loadtxt("same_masses/h_bonds/methane~2methylfurane/no_simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_met_hbw_no =  loadtxt("same_masses/h_bonds/methane~2methylfurane/no_simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
#same masses h bonsd met  SIMM
sm_met_hbv =  loadtxt("same_masses/h_bonds/methane~2methylfurane/simm/vacuum/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)
sm_met_hbw =  loadtxt("same_masses/h_bonds/methane~2methylfurane/simm/free/output/gradient_profile.dat",usecols=[0,1,2],skiprows=1)


if not os.path.exists("output_results/equi"):
    os.makedirs("output_results/equi")
if not os.path.exists("output_results/no_simm"):
    os.makedirs("output_results/no_simm")
if not os.path.exists("output_results/simm"):
    os.makedirs("output_results/simm")
#################################################################################
#diffmass all bonds equi:
print("gradient profiles plot making...")
fig = plot_grad(dm_mf_abv_equi,"2-methylfuran",dm_met_abv_equi,"methane")
with PdfPages('output_results/equi/diff_mass_vac_allbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(dm_mf_abw_equi,"2-methylfuran",dm_met_abw_equi,"methane")
with PdfPages('output_results/equi/diff_mass_wat_allbonds.pdf') as pdf:
    pdf.savefig(fig)

#diffmass all bonds nosim
fig = plot_grad(dm_mf_abv_no,"2-methylfuran",dm_met_abv_no,"methane")
with PdfPages('output_results/no_simm/diff_mass_vac_allbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(dm_mf_abw_no,"2-methylfuran",dm_met_abw_no,"methane")
with PdfPages('output_results/no_simm/diff_mass_wat_allbonds.pdf') as pdf:
    pdf.savefig(fig)

#diffmass all bonds simm
fig = plot_grad(dm_mf_abv,"2-methylfuran",dm_met_abv,"methane")
with PdfPages('output_results/simm/diff_mass_vac_allbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(dm_mf_abw,"2-methylfuran",dm_met_abw,"methane")
with PdfPages('output_results/simm/diff_mass_wat_allbonds.pdf') as pdf:
    pdf.savefig(fig)
############################################################################################
#diffmass all hb equi:
fig = plot_grad(dm_mf_hbv_equi,"2-methylfuran",dm_met_hbv_equi,"methane")
with PdfPages('output_results/equi/diff_mass_vac_hbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(dm_mf_hbw_equi,"2-methylfuran",dm_met_hbw_equi,"methane")
with PdfPages('output_results/equi/diff_mass_wat_hbonds.pdf') as pdf:
    pdf.savefig(fig)

#diffmass all hb nosimm:
fig = plot_grad(dm_mf_hbv_no,"2-methylfuran",dm_met_hbv_no,"methane")
with PdfPages('output_results/no_simm/diff_mass_vac_hbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(dm_mf_hbw_no,"2-methylfuran",dm_met_hbw_no,"methane")
with PdfPages('output_results/no_simm/diff_mass_wat_hbonds.pdf') as pdf:
    pdf.savefig(fig)

#diffmass all hb simm:
fig = plot_grad(dm_mf_hbv,"2-methylfuran",dm_met_hbv,"methane")
with PdfPages('output_results/simm/diff_mass_vac_hbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(dm_mf_hbw,"2-methylfuran",dm_met_hbw,"methane")
with PdfPages('output_results/simm/diff_mass_wat_hbonds.pdf') as pdf:
    pdf.savefig(fig)
###########################################################################################


#################################################################################
#samemass all bonds equi:
fig = plot_grad(sm_mf_abv_equi,"2-methylfuran",sm_met_abv_equi,"methane")
with PdfPages('output_results/equi/same_mass_vac_allbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(sm_mf_abw_equi,"2-methylfuran",sm_met_abw_equi,"methane")
with PdfPages('output_results/equi/same_mass_wat_allbonds.pdf') as pdf:
    pdf.savefig(fig)

#diffmass all bonds nosim
fig = plot_grad(sm_mf_abv_no,"2-methylfuran",sm_met_abv_no,"methane")
with PdfPages('output_results/no_simm/same_mass_vac_allbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(sm_mf_abw_no,"2-methylfuran",sm_met_abw_no,"methane")
with PdfPages('output_results/no_simm/same_mass_wat_allbonds.pdf') as pdf:
    pdf.savefig(fig)

#diffmass all bonds simm
fig = plot_grad(sm_mf_abv,"2-methylfuran",sm_met_abv,"methane")
with PdfPages('output_results/simm/same_mass_vac_allbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(sm_mf_abw,"2-methylfuran",sm_met_abw,"methane")
with PdfPages('output_results/simm/same_mass_wat_allbonds.pdf') as pdf:
    pdf.savefig(fig)
############################################################################################
#diffmass all hb equi:
fig = plot_grad(sm_mf_hbv_equi,"2-methylfuran",sm_met_hbv_equi,"methane")
with PdfPages('output_results/equi/same_mass_vac_hbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(sm_mf_hbw_equi,"2-methylfuran",sm_met_hbw_equi,"methane")
with PdfPages('output_results/equi/same_mass_wat_hbonds.pdf') as pdf:
    pdf.savefig(fig)

#diffmass all hb nosimm:
fig = plot_grad(sm_mf_hbv_no,"2-methylfuran",sm_met_hbv_no,"methane")
with PdfPages('output_results/no_simm/same_mass_vac_hbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(sm_mf_hbw_no,"2-methylfuran",sm_met_hbw_no,"methane")
with PdfPages('output_results/no_simm/same_mass_wat_hbonds.pdf') as pdf:
    pdf.savefig(fig)

#diffmass all hb simm:
fig = plot_grad(sm_mf_hbv,"2-methylfuran",sm_met_hbv,"methane")
with PdfPages('output_results/simm/same_mass_vac_hbonds.pdf') as pdf:
    pdf.savefig(fig)

fig = plot_grad(sm_mf_hbw,"2-methylfuran",sm_met_hbw,"methane")
with PdfPages('output_results/simm/same_mass_wat_hbonds.pdf') as pdf:
    pdf.savefig(fig)
###########################################################################################
print("Reordering everything before the boss is coming...")
cmd = "mv output_results/*equi*.csv output_results/equi/."
os.system(cmd)
cmd = "mv output_results/*no_simm*.csv output_results/no_simm/."
os.system(cmd)
cmd = "mv output_results/*simm*.csv output_results/simm/."
os.system(cmd)
print("All done, all is fine! :D Enjoy")
