#SEPT 2016 Stefano Bosisio
#Script to automatically create the template/folder for reprodubicility project batch 3
#
#The output structure will be:
#                                   -->discharge/water.sh, FUNC.py, coulcor.sh, ljcor.sh
#                           free    -->input/SYSTEM.top, SYSTEM.crd, MORPH.pert.discharge, MORPH.pert.vanish, sim.cfg
#                         /         -->vanish/same as discharge
#                moleculeA
#                /        \         --> discharge
#        absolute          vacuum   --> input
#       /                           --> vanish
#run00X
#       \
#        relative    free  --> input
#               \   /      --> output
#               A~B
#                   \
#                   vacuum --> input
#                          --> output
#Usage python create_world  inputfiles/methane~ethane

import os,sys




def absolute_create(inputpath,run_folder):
#Now let's start with the absolute folder
#If the folder starts with "methane" we continue, otherwise we create the absolute stuff
#Sanity check on the name: if it ends with "/" we gonna remove it
    if inputpath[-1]=="/":
        inputpath = inputpath[:len(inputpath)-1]    #lets copy inputpath without the final /
#    else:
#        continue

    pert_name = inputpath.split("/")[-1]  #take the name of the perturbation e.g. methane~ethane

    if pert_name.split("~")[0] =="methane":
        return
    else:
        #the absolute is for the first molecule in the pert
        pert_folder = pert_name.split("~")[0]
        print("Let's create %s/absolute/%s" %(run_fold,pert_folder))
        os.mkdir("%s/absolute/%s" %(run_fold,pert_folder))  #let's create run001/absolute/ethane
        fullpath = "%s/absolute/%s" % (run_folder,pert_folder)


#Create the folder stucture

    folders_todo = ["%s/free" % fullpath, "%s/free/input" %fullpath,\
     "%s/free/discharge" %fullpath, "%s/free/vanish" %fullpath, "%s/vacuum" %fullpath,\
     "%s/vacuum/input" %fullpath, "%s/vacuum/vanish" %fullpath, "%s/vacuum/discharge" %fullpath ]

    for fold in folders_todo:
        print("Creation of folder %s" %fold)
        os.mkdir(fold)

#Now we have to copy everything  (protocol/absolute/)
#VACUUM:
    print("Copying files for vacuum")
    cmds = ["cp %s/vacuum.parm7  %s/vacuum/input/SYSTEM.top" % (inputpath,fullpath), \
            "cp %s/vacuum.rst7   %s/vacuum/input/SYSTEM.crd" % (inputpath,fullpath),\
            "cp %s/MORPH.pert.discharge %s/vacuum/input/."   % (inputpath,fullpath),\
            "cp %s/MORPH.pert.vanish    %s/vacuum/input/."   % (inputpath,fullpath),\
            "cp protocol/absolute/sim.cfg.vacuum %s/vacuum/input/sim.cfg" % (fullpath),\
            "cp protocol/absolute/vacuum.discharge.sh  %s/vacuum/discharge/vacuum.sh" %(fullpath),\
            "cp protocol/absolute/vacuum.vanish.sh     %s/vacuum/vanish/vacuum.sh" %(fullpath)]

    for cmd in cmds:
        os.system(cmd)

#WATER
    print("Copying files for water")
    cmds = ["cp %s/solvated/solvated.parm7  %s/free/input/SYSTEM.top" % (inputpath,fullpath), \
            "cp %s/solvated/solvated.rst7   %s/free/input/SYSTEM.crd" % (inputpath,fullpath),\
            "cp %s/MORPH.pert.discharge %s/free/input/."   % (inputpath,fullpath),\
            "cp %s/MORPH.pert.vanish    %s/free/input/."   % (inputpath,fullpath),\
            "cp protocol/absolute/sim.cfg.water %s/free/input/sim.cfg" % (fullpath),\
            "cp protocol/absolute/water.discharge.sh  %s/free/discharge/water.sh" %(fullpath),\
            "cp protocol/absolute/water.vanish.sh     %s/free/vanish/water.sh" %(fullpath),\
            "cp protocol/absolute/coulcor.sh  %s/free/discharge/." %(fullpath),\
            "cp protocol/absolute/FUNC.py     %s/free/discharge/." %(fullpath),\
            "cp protocol/absolute/ljcor.sh    %s/free/vanish/." %(fullpath)]

    for cmd in cmds:
        os.system(cmd)


def relative_create(inputpath,run_folder):
#Now let's start with the absolute folder
#If the folder starts with "methane" we continue, otherwise we create the absolute stuff
#Sanity check on the name: if it ends with "/" we gonna remove it
    if inputpath[-1]=="/":
        inputpath = inputpath[:len(inputpath)-1]    #lets copy inputpath without the final /
#    else:
#        continue

    pert_name = inputpath.split("/")[-1]  #take the name of the perturbation e.g. methane~ethane

    pert_folder = pert_name #e.g. methane~ethane
    print("Let's create %s/relative/%s" %(run_fold,pert_folder))
    os.mkdir("%s/relative/%s" %(run_fold,pert_folder))  #let's create run001/absolute/ethane
    fullpath = "%s/relative/%s" % (run_folder,pert_folder)

#Create the folder stucture

    folders_todo = ["%s/free" % fullpath, "%s/free/input" %fullpath,\
     "%s/free/output" %fullpath, "%s/vacuum/" %fullpath, "%s/vacuum/input" %fullpath,\
     "%s/vacuum/output" %fullpath]

    for fold in folders_todo:
        print("Creation of folder %s" %fold)
        os.mkdir(fold)

#Now we have to copy everything  (protocol/absolute/)
#VACUUM:
#coulcor.sh  FUNC.py  ljcor.sh

    print("Copying files for vacuum")
    cmds = ["cp %s/vacuum.parm7  %s/vacuum/input/SYSTEM.top" % (inputpath,fullpath), \
            "cp %s/vacuum.rst7   %s/vacuum/input/SYSTEM.crd" % (inputpath,fullpath),\
            "cp %s/MORPH.onestep.pert %s/vacuum/input/MORPH.pert"   % (inputpath,fullpath),\
            "cp protocol/relative/sim.cfg.vacuum %s/vacuum/input/sim.cfg" % (fullpath),\
            "cp protocol/relative/vacuum.sh  %s/vacuum/output/." %(fullpath)]

    for cmd in cmds:
        os.system(cmd)

#WATER
    print("Copying files for water")
    cmds = ["cp %s/solvated/solvated.parm7  %s/free/input/SYSTEM.top" % (inputpath,fullpath), \
            "cp %s/solvated/solvated.rst7   %s/free/input/SYSTEM.crd" % (inputpath,fullpath),\
            "cp %s/MORPH.onestep.pert %s/free/input/MORPH.pert"   % (inputpath,fullpath),\
            "cp protocol/relative/sim.cfg.water %s/free/input/sim.cfg" % (fullpath),\
            "cp protocol/relative/water.sh  %s/free/output/." %(fullpath),\
            "cp protocol/relative/coulcor.sh  %s/free/output/." %(fullpath),\
            "cp protocol/relative/FUNC_0.py     %s/free/output/." %(fullpath),\
            "cp protocol/relative/FUNC_1.py     %s/free/output/." %(fullpath),\
            "cp protocol/relative/ljcor.sh    %s/free/output/." %(fullpath)]

    for cmd in cmds:
        os.system(cmd)



#############
#MAIN SCRIPT#
#############

#We give the inputpath with the folder where  MORPH, top & Co are stored

inputpath = sys.argv[1]  #e.g. inputfiles/methane~ethane/
run_fold = sys.argv[2]   #e.g. create all the morph here. So we give run001
#run001 will be:  run001/absolute run001/relative

#Sanity check on the run_numb:  (not necessary this time)
#if os.path.exists(run_fold):
#    print("Run folder %s already exists!" % run_fold)
#    sys.exit()
#else:
#    print("Run folder %s will be create" % run_fold)

whoisit = inputpath.split("/")[-1]
print("Creation of absolute for %s" %whoisit)

absolute_create(inputpath,run_fold)

print("Creation of relative for %s" %whoisit)
relative_create(inputpath,run_fold)

print("Now everyting is ready.Lets submit via an automatic bash :D")
