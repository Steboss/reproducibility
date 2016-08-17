#!/usr/bin/python
import os,sys,shutil,re
#
# Prepare input files for a somd simulation using:
#python prepare  pert_folder
#preparation of: different

try:
    pertHC = sys.argv[1]  #perturbation folder e.g. HC/diff_masses
    pertHH = sys.argv[2]  #perturbation folder e.g. HH/diff_masses
except IndexError:
    print "Usage is script setupfolder"
    sys.exit(-1)

#Sanity check on the presence of a final "/"
splitter_testHC = pertHC.split("/")
splitter_testHH = pertHH.split("/")

if splitter_testHC[len(splitter_testHC)-1]=="" :
    pertHC = pertHC[:len(pertHC)-1]
if splitter_testHH[len(splitter_testHH)-1]=="" :
    pertHH = pertHH[:len(pertHH)-1]


absolute_path = os.getcwd()
total_HC = absolute_path + "/" + pertHC
total_HH = absolute_path + "/" + pertHH
HC = total_HC.split("/")[-1]
HH = total_HH.split("/")[-1]

#print(HC,HH)
print("Setting up %s and %s ..." % (HC,HH))
basedir = os.getcwd()

#Run number detection
dir = os.listdir(basedir)
index = 1
for f in dir:
    #print f
    if f.find("run0") > -1:
        #print f
        index += 1
runfolder = "run%003d" % index
print("Creation of folder %s" %(runfolder))
cmd = "mkdir %s" % runfolder
os.system(cmd)

HC_vanish_input = "%s/diff_masses/all_bonds/%s/free/vanish/input" %(runfolder,HC)
HC_vanish_output = "%s/diff_masses/all_bonds/%s/free/vanish/output" %(runfolder,HC)

HH_vanish_input = "%s/diff_masses/all_bonds/%s/free/vanish/input" %(runfolder,HH)
HH_vanish_output = "%s/diff_masses/all_bonds/%s/free/vanish/output" %(runfolder,HH)

os.makedirs("%s" % (HC_vanish_input))
os.makedirs("%s" % (HC_vanish_output))
os.makedirs("%s" % (HH_vanish_input))
os.makedirs("%s" % (HH_vanish_output))

cmds = []


#free
cmds.append("cp -r %s/_ligands/solvated.parm7 %s/SYSTEM.top" % (total_HC,HC_vanish_input))
cmds.append("cp -r %s/_ligands/md00004.rst7  %s/SYSTEM.crd"% (total_HC,HC_vanish_input))
cmds.append("cp -r %s/MORPH.pert.vanish %s/MORPH.pert" % (total_HC,HC_vanish_input))
#free protocol
cmds.append("cp -r %s/protocol/sim-free.cfg %s/sim.cfg" % (basedir,HC_vanish_input))
cmds.append("cp -r %s/protocol/analysis_tot.py %s/." % (basedir,HC_vanish_output))
cmds.append("cp -r %s/protocol/mbar.sh %s/." % (basedir,HC_vanish_output))
cmds.append("cp -r %s/protocol/water.sh %s/." % (basedir,HC_vanish_output))
cmds.append("cp -r %s/protocol/extract_results.py %s/." % (basedir,HC_vanish_output))

for cmd in cmds:
    os.system(cmd)


cmds = []


#free
cmds.append("cp -r %s/_ligands/solvated.parm7 %s/SYSTEM.top" % (total_HH,HH_vanish_input))
cmds.append("cp -r %s/_ligands/md00004.rst7  %s/SYSTEM.crd"% (total_HH,HH_vanish_input))
cmds.append("cp -r %s/MORPH.pert.vanish %s/MORPH.pert" % (total_HH,HH_vanish_input))
#free protocol
cmds.append("cp -r %s/protocol/sim-free.cfg %s/sim.cfg" % (basedir,HH_vanish_input))
cmds.append("cp -r %s/protocol/analysis_tot.py %s/." % (basedir,HH_vanish_output))
cmds.append("cp -r %s/protocol/mbar.sh %s/." % (basedir,HH_vanish_output))
cmds.append("cp -r %s/protocol/water.sh %s/." % (basedir,HH_vanish_output))
cmds.append("cp -r %s/protocol/extract_results.py %s/." % (basedir,HH_vanish_output))

for cmd in cmds:
    os.system(cmd)

print("Enjoy submitting simulations :)")   
