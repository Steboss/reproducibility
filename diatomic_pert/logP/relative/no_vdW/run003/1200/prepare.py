#SEPT 2016 Stefano Bosisio
#Script to copy file form inputfiles folder to target vacuum/cyclo/water
#Usage: python prepare.py
import os,sys


cyclo_path  = "inputfiles/cyclo/"
water_path  = "inputfiles/water/"
vacuum_path = "inputfiles/vacuum/"

#ALL BODNS PATH
cyclo_ab_input = "cyclo/allbonds/input/"
cyclo_ab_output = "cyclo/allbonds/output/"

water_ab_input = "water/allbonds/input/"
water_ab_output = "water/allbonds/output/"

vacuum_ab_input = "vacuum/allbonds/input/"
vacuum_ab_output = "vacuum/allbonds/output/"

#NONE PATH
cyclo_no_input = "cyclo/none/input/"
cyclo_no_output = "cyclo/none/output/"

water_no_input = "water/none/input/"
water_no_output = "water/none/output/"

vacuum_no_input = "vacuum/none/input/"
vacuum_no_output = "vacuum/none/output/"

#####

elems =["SYSTEM.top","SYSTEM.crd","MORPH.pert"]


print("copying topologies and coordiantes...")
for el in elems:

    what = "cp %s/%s  %s/." %(cyclo_path,el,cyclo_ab_input)
    os.system(what)
    what = "cp %s/%s %s/."  %(water_path,el,water_ab_input)
    os.system(what)
    what = "cp %s/%s %s/." %(vacuum_path,el,vacuum_ab_input)
    os.system(what)
    what = "cp %s/%s  %s/." %(cyclo_path,el,cyclo_no_input)
    os.system(what)
    what = "cp %s/%s %s/."  %(water_path,el,water_no_input)
    os.system(what)
    what = "cp %s/%s %s/." %(vacuum_path,el,vacuum_no_input)
    os.system(what)

print("copying sim.cfg..")
#now copy the sim in ab and none
os.system("cp %s/sim.cfg.allbonds  %s/sim.cfg" %(cyclo_path,cyclo_ab_input))
os.system("cp %s/sim.cfg.allbonds  %s/sim.cfg" %(water_path,water_ab_input))
os.system("cp %s/sim.cfg.allbonds  %s/sim.cfg" %(vacuum_path,vacuum_ab_input))

os.system("cp %s/sim.cfg.none  %s/sim.cfg" %(cyclo_path,cyclo_no_input))
os.system("cp %s/sim.cfg.none  %s/sim.cfg" %(water_path,water_no_input))
os.system("cp %s/sim.cfg.none  %s/sim.cfg" %(vacuum_path,vacuum_no_input))
###############
#now copy the running files
print("copying running files...")
os.system("cp inputfiles/protocol/vacuum.sh   %s/." %vacuum_ab_output)
os.system("cp inputfiles/protocol/water.sh   %s/." %water_ab_output)
os.system("cp inputfiles/protocol/cyclo.sh   %s/." %cyclo_ab_output)

os.system("cp inputfiles/protocol/vacuum.sh   %s/." %vacuum_no_output)
os.system("cp inputfiles/protocol/water.sh   %s/." %water_no_output)
os.system("cp inputfiles/protocol/cyclo.sh   %s/." %cyclo_no_output)

print("Here we are :D")
