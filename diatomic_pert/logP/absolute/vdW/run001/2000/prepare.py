#SEPT 2016 Stefano Bosisio
#Script to copy file form inputfiles folder to target vacuum/cyclo/water
#Usage: python prepare.py
import os,sys


cyclo_path  = "inputfiles/cyclo/"
water_path  = "inputfiles/water/"
vacuum_path = "inputfiles/vacuum/"

#ALL BODNS PATH
cyclo_ab_input = "cyclo/allbonds/input/"

water_ab_input = "water/allbonds/input/"

vacuum_ab_input = "vacuum/allbonds/input/"

#NONE PATH
cyclo_no_input = "cyclo/none/input/"

water_no_input = "water/none/input/"

vacuum_no_input = "vacuum/none/input/"

#FOLDER TO BE CREATED
cyclo_ab_discharge = "cyclo/allbonds/discharge"
cyclo_ab_vanish  = "cyclo/allbonds/vanish"

water_ab_discharge = "water/allbonds/discharge"
water_ab_vanish   = "water/allbonds/vanish"

vacuum_ab_discharge = "vacuum/allbonds/discharge"
vacuum_ab_vanish = "vacuum/allbonds/vanish"

cyclo_no_discharge = "cyclo/none/discharge"
cyclo_no_vanish  = "cyclo/none/vanish"

water_no_discharge = "water/none/discharge"
water_no_vanish   = "water/none/vanish"

vacuum_no_discharge = "vacuum/none/discharge"
vacuum_no_vanish = "vacuum/none/vanish"
##Create the directories:
print("Creating discarging and vanishing directories..")
os.makedirs(cyclo_ab_discharge)
os.makedirs(cyclo_ab_vanish)
os.makedirs(cyclo_no_discharge)
os.makedirs(cyclo_no_vanish)
os.makedirs(water_ab_discharge)
os.makedirs(water_no_discharge)
os.makedirs(water_ab_vanish)
os.makedirs(water_no_vanish)
os.makedirs(vacuum_ab_discharge)
os.makedirs(vacuum_no_discharge)
os.makedirs(vacuum_ab_vanish)
os.makedirs(vacuum_no_vanish)





elems =["SYSTEM.top","SYSTEM.crd","MORPH.pert.discharge","MORPH.pert.vanish"]


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
os.system("cp inputfiles/protocol/vacuum.discharge.sh   %s/." %vacuum_ab_discharge)
os.system("cp inputfiles/protocol/vacuum.vanish.sh   %s/." %vacuum_ab_vanish )

os.system("cp inputfiles/protocol/vacuum.discharge.sh   %s/." %vacuum_no_discharge)
os.system("cp inputfiles/protocol/vacuum.vanish.sh   %s/." %vacuum_no_vanish )

os.system("cp inputfiles/protocol/water.discharge.sh   %s/." %water_ab_discharge)
os.system("cp inputfiles/protocol/water.vanish.sh   %s/." %water_ab_vanish )

os.system("cp inputfiles/protocol/water.discharge.sh   %s/." %water_no_discharge)
os.system("cp inputfiles/protocol/water.vanish.sh   %s/." %water_no_vanish )

os.system("cp inputfiles/protocol/cyclo.discharge.sh   %s/." %cyclo_ab_discharge)
os.system("cp inputfiles/protocol/cyclo.vanish.sh   %s/." %cyclo_ab_vanish )

os.system("cp inputfiles/protocol/cyclo.discharge.sh   %s/." %cyclo_no_discharge)
os.system("cp inputfiles/protocol/cyclo.vanish.sh   %s/." %cyclo_no_vanish )

print("Here we are :D")
