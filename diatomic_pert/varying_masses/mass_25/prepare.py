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
HC = total_HC.split("/")[-2]
HH = total_HH.split("/")[-2]
#print(HC,HH)
print("Setting up %s and %s ..." % (HC,HH))
basedir = os.getcwd()

#Run number detection
dir = os.listdir(basedir)
index = 1
for f in dir:
    #print f
    if f.find("run0") > -1:
        print f
        index += 1
runfolder = "run%003d" % index
print("Creation of folder %s" %(runfolder))
cmd = "mkdir %s" % runfolder
os.system(cmd)

HC_vacuum_input = "%s/diff_masses/all_bonds/%s/vacuum/input" %(runfolder,HC)
HC_vacuum_output = "%s/diff_masses/all_bonds/%s/vacuum/output" %(runfolder,HC)
HC_free_input = "%s/diff_masses/all_bonds/%s/free/input" %(runfolder,HC)
HC_free_output = "%s/diff_masses/all_bonds/%s/free/output" %(runfolder,HC)

HH_vacuum_input = "%s/diff_masses/all_bonds/%s/vacuum/input" %(runfolder,HH)
HH_vacuum_output = "%s/diff_masses/all_bonds/%s/vacuum/output"%(runfolder,HH)
HH_free_input = "%s/diff_masses/all_bonds/%s/free/input"%(runfolder,HH)
HH_free_output = "%s/diff_masses/all_bonds/%s/free/output"%(runfolder,HH)

os.makedirs("%s" % (HC_vacuum_input))
os.makedirs("%s" % (HC_vacuum_output))
os.makedirs("%s" % (HC_free_input))
os.makedirs("%s" % (HC_free_output))

os.makedirs("%s" % (HH_vacuum_input))
os.makedirs("%s" % (HH_vacuum_output))
os.makedirs("%s" % (HH_free_input))
os.makedirs("%s" % (HH_free_output))

#NOw copying everyting
cmds = []

#vacuum
cmds.append("cp -r %s/vacuum.parm7 %s/SYSTEM.top" % (total_HC,HC_vacuum_input))
cmds.append("cp -r %s/vacuum.rst7 %s/SYSTEM.crd"% (total_HC,HC_vacuum_input))
cmds.append("cp -r %s/MORPH.pert %s/." % (total_HC,HC_vacuum_input))
#vacuum protocol
cmds.append("cp -r %s/protocol/sim-vacuum.cfg %s/sim.cfg" % (basedir,HC_vacuum_input))
cmds.append("cp -r %s/protocol/analysis_tot.py %s/." % (basedir,HC_vacuum_output))
cmds.append("cp -r %s/protocol/mbar.sh %s/." % (basedir,HC_vacuum_output))
cmds.append("cp -r %s/protocol/vacuum.sh %s/." % (basedir,HC_vacuum_output))
cmds.append("cp -r %s/protocol/extract_results.py %s/." % (basedir,HC_vacuum_output))
#free
cmds.append("cp -r %s/_ligands/solvated.parm7 %s/SYSTEM.top" % (total_HC,HC_free_input))
cmds.append("cp -r %s/_ligands/solvated.rst7  %s/SYSTEM.crd"% (total_HC,HC_free_input))
cmds.append("cp -r %s/MORPH.pert %s/." % (total_HC,HC_free_input))
#free protocol
cmds.append("cp -r %s/protocol/sim-free.cfg %s/sim.cfg" % (basedir,HC_free_input))
cmds.append("cp -r %s/protocol/analysis_tot.py %s/." % (basedir,HC_free_output))
cmds.append("cp -r %s/protocol/mbar.sh %s/." % (basedir,HC_free_output))
cmds.append("cp -r %s/protocol/water.sh %s/." % (basedir,HC_free_output))
cmds.append("cp -r %s/protocol/extract_results.py %s/." % (basedir,HC_free_output))

for cmd in cmds:
    os.system(cmd)

#NOw copying everyting
cmds = []

#vacuum
cmds.append("cp -r %s/vacuum.parm7 %s/SYSTEM.top" % (total_HH,HH_vacuum_input))
cmds.append("cp -r %s/vacuum.rst7 %s/SYSTEM.crd"% (total_HH,HH_vacuum_input))
cmds.append("cp -r %s/MORPH.pert %s/." % (total_HH,HH_vacuum_input))
#vacuum protocol
cmds.append("cp -r %s/protocol/sim-vacuum.cfg %s/sim.cfg" % (basedir,HH_vacuum_input))
cmds.append("cp -r %s/protocol/analysis_tot.py %s/." % (basedir,HH_vacuum_output))
cmds.append("cp -r %s/protocol/mbar.sh %s/." % (basedir,HH_vacuum_output))
cmds.append("cp -r %s/protocol/vacuum.sh %s/." % (basedir,HH_vacuum_output))
cmds.append("cp -r %s/protocol/extract_results.py %s/." % (basedir,HH_vacuum_output))
#free
cmds.append("cp -r %s/_ligands/solvated.parm7 %s/SYSTEM.top" % (total_HH,HH_free_input))
cmds.append("cp -r %s/_ligands/solvated.rst7  %s/SYSTEM.crd"% (total_HH,HH_free_input))
cmds.append("cp -r %s/MORPH.pert %s/." % (total_HH,HH_free_input))
#free protocol
cmds.append("cp -r %s/protocol/sim-free.cfg %s/sim.cfg" % (basedir,HH_free_input))
cmds.append("cp -r %s/protocol/analysis_tot.py %s/." % (basedir,HH_free_output))
cmds.append("cp -r %s/protocol/mbar.sh %s/." % (basedir,HH_free_output))
cmds.append("cp -r %s/protocol/water.sh %s/." % (basedir,HH_free_output))
cmds.append("cp -r %s/protocol/extract_results.py %s/." % (basedir,HH_free_output))

for cmd in cmds:
    os.system(cmd)

print("Enjoy submitting simulations :)")
