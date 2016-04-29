#!/usr/bin/python
import os,sys,shutil
#
# Prepare input files for a somd simulation using:
# all _perturbations folders in the input folder
# the protocol in sim.cfg
# the lambdas schedule in lambdas.schedule
# the submission syntax script sub-somd.sh
# ./populate.py ../01-setup sim.cfg lambdas.schedule

try:
    inputfolder = sys.argv[1]  #perturbation folder
except IndexError:
    print "Usage is script setupfolder"
    sys.exit(-1)

absolute_path = os.getcwd()
total_path = absolute_path + "/" + inputfolder
inputfolder = total_path
elems = inputfolder.split("/")

pert = elems[-1]
print ("Setting up %s ... " % pert)
print ("Remember not to give the final / to the pert folder")
basedir = os.getcwd()
if not os.path.exists(pert):
    cmd = "mkdir %s" % pert
    os.system(cmd)

os.chdir(pert)
files = os.listdir(os.getcwd())
index = 1
for f in files:
    #print f
    if f.find("run") > -1:
        index += 1
runfolder = "run%003d" % index
cmd = "mkdir %s" % runfolder
os.system(cmd)

if index > 1:
    print ("Previous run folders exist, files set up in %s " % runfolder)

os.chdir(runfolder)
# For each calculation we need
# SYSTEM.pdb SYSTEM.top SYSTEM.crd
# MORPH.pert MORPH.flex
# sim.cfg
# somd-freenrg.sh (that one makes subfolders according to lamba values)
# Inside runfolder, create a subfolder vacuum
#analysis_alchemical.py  coulcor.sh          FUNC_0.py  grad_profile.py  mbar.sh       parselj.py         sim-free.cfg    vacuum.sh
#analysis_gro            extract_results.py  FUNC_1.py  ljcor.sh         parsecoul.py  plot_gradients.py  sim-vacuum.cfg  water.sh

cmd = "mkdir vacuum"
os.system(cmd)
cmd = "mkdir vacuum/input"  #"mkdir -p vacuum/{input,output}" doesn't work
os.system(cmd)
cmd = "mkdir vacuum/output"
os.system(cmd)
cmds = ["cp %s/vacuum.parm7 vacuum/input/SYSTEM.top" % inputfolder,
        "cp %s/vacuum.pdb vacuum/input/SYSTEM.pdb" % inputfolder,
        "cp %s/vacuum.rst7 vacuum/input/SYSTEM.crd" % inputfolder,
        "cp %s/MORPH.pert vacuum/input/" % inputfolder,
        "cp %s/protocol/sim-vacuum.cfg vacuum/input/sim.cfg" % basedir,
        "cp %s/protocol/vacuum.sh vacuum/." % basedir,
        "cp -r %s/protocol/analysis_gro vacuum/output/." % basedir,
        "cp %s/protocol/analysis_alchemical.py vacuum/output/." % basedir,
        "cp %s/protocol/extract_results.py vacuum/output/." % basedir,
        "cp %s/protocol/grad_profile.py vacuum/output/." % basedir,
        "cp %s/protocol/run.sh  ." % basedir,
        "cp %s/protocol/mbar.sh vacuum/." % basedir,
        "cp %s/protocol/vacuum_analysis.sh vacuum/output/." % basedir
        ]
for cmd in cmds:
    os.system(cmd)
# Also create a folder free if inputfolder contains _ligands
#analysis_alchemical.py  coulcor.sh          FUNC_0.py  grad_profile.py  mbar.sh       parselj.py         sim-free.cfg    vacuum.sh
#analysis_gro            extract_results.py  FUNC_1.py  ljcor.sh         parsecoul.py  plot_gradients.py  sim-vacuum.cfg  water.sh
files = os.listdir(inputfolder)
match = False
for f in files:
    if f.find("_ligands") > -1:
        match = True
        break
if match:
    cmd = "mkdir free"
    os.system(cmd)
    cmd = "mkdir free/input"
    os.system(cmd)
    cmd = "mkdir free/output"
    os.system(cmd)
    cmds = ["cp %s/_ligands/solvated.parm7 free/input/SYSTEM.top" % inputfolder,
            "cp %s/_ligands/solvated.pdb free/input/SYSTEM.pdb" % inputfolder,
            "cp %s/_ligands/solvated.rst7 free/input/SYSTEM.crd" % inputfolder,
            "cp %s/MORPH.pert free/input/" % inputfolder,
            "cp %s/protocol/sim-free.cfg free/input/sim.cfg" % basedir,
            "cp %s/protocol/water.sh free/." % basedir,
            "cp -r %s/protocol/analysis_gro vacuum/output/." % basedir,
            "cp %s/protocol/analysis_alchemical.py free/output/." % basedir,
            "cp %s/protocol/extract_results.py free/output/." % basedir,
            "cp %s/protocol/grad_profile.py free/output/." % basedir,
            "cp %s/protocol/coulcor.sh free/." % basedir,
            "cp %s/protocol/FUNC_* free/output/." % basedir,
            "cp %s/protocol/ljcor.sh free/." % basedir,
            "cp %s/protocol/parse* free/output/." % basedir,
            "cp %s/protocol/mbar.sh free/." % basedir,
            "cp %s/protocol/water_analysis.sh free/output/." % basedir
            ]
    for cmd in cmds:
        os.system(cmd)

# Also create a folder bound if inputfolder contains _complexes
match = False
for f in files:
    if f.find("_complexes") > -1:
        match = True
        break
if match:
    cmd = "mkdir bound"
    os.system(cmd)
    cmds = ["cp %s/_complexes/solvated.parm7 bound/SYSTEM.top" % inputfolder,
            "cp %s/_complexes/solvated.pdb bound/SYSTEM.pdb" % inputfolder,
            "cp %s/_complexes/solvated.rst7 bound/SYSTEM.crd" % inputfolder,
            "cp %s/MORPH.pert bound/" % inputfolder,
            "cp %s/ligand.flex bound/MORPH.flex" % inputfolder,
            "cp %s/protocol/sim-bound.cfg bound/sim.cfg" % basedir,
            "cp %s/protocol/somd-freenrg.sh bound/" % basedir,
            "cp %s/protocol/test-somd-freenrg.sh bound/" % basedir
            ]
    for cmd in cmds:
        os.system(cmd)
