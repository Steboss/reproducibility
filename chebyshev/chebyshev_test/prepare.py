#!/usr/bin/python
import os,sys,shutil
#
# Prepare input files for a somd simulation using:
#python prepare  pert_folder
#preparation of: different

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
print ("For this test remember to modify masses in same_masses folders!")
print ("Actually it seems FESetup is mapping with different masses!")
basedir = os.getcwd()


folders = ["diff_masses/all_bonds","diff_masses/h_bonds",\
            "same_masses/all_bonds","same_masses/h_bonds"]

scheme = ["no_simm","simm","equi"]

#if os.path.exists("diff_masses/"):
#    sys.exit("Error folders exist already!")

for fold in folders:
    for sch in scheme:
        os.makedirs("%s/%s/%s/free/input" % (fold,pert,sch))
        os.makedirs("%s/%s/%s/free/output" % (fold,pert,sch))
        os.makedirs("%s/%s/%s/vacuum/input" % (fold,pert,sch))
        os.makedirs("%s/%s/%s/vacuum/output" % (fold,pert,sch))

#diff_masses/all_bonds/transforamtion/no_simm

cmds = []
for fold in folders:
    for sch in scheme:

        cmds.append("cp -r %s/vacuum.parm7 %s/%s/%s/vacuum/input/SYSTEM.top" % (inputfolder,fold,pert,sch))
        cmds.append("cp -r %s/vacuum.pdb %s/%s/%s/vacuum/input/SYSTEM.pdb" % (inputfolder,fold,pert,sch))
        cmds.append("cp -r %s/vacuum.rst7 %s/%s/%s/vacuum/input/SYSTEM.crd"% (inputfolder,fold,pert,sch))
        cmds.append("cp -r %s/MORPH.pert %s/%s/%s/vacuum/input/" % (inputfolder,fold,pert,sch))

        cmds.append("cp -r %s/protocol/analysis_gro %s/%s/%s/vacuum/output/." % (basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/analysis_alchemical.py %s/%s/%s/vacuum/output/." % (basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/extract_results.py %s/%s/%s/vacuum/output/."% (basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/grad_profile.py %s/%s/%s/vacuum/output/."% (basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/vacuum_analysis.sh %s/%s/%s/vacuum/output/." % (basedir,fold,pert,sch))

for cmd in cmds:
    os.system(cmd)

cmds = []
cmds =["cp -r %s/protocol/sim-vac_allbonds_nosim.cfg diff_masses/all_bonds/%s/no_simm/vacuum/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-vac_allbonds_nosim.cfg same_masses/all_bonds/%s/no_simm/vacuum/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-vac_allbonds_simm.cfg diff_masses/all_bonds/%s/simm/vacuum/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-vac_allbonds_simm.cfg same_masses/all_bonds/%s/simm/vacuum/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-vac_allbonds.cfg diff_masses/all_bonds/%s/equi/vacuum/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-vac_allbonds.cfg same_masses/all_bonds/%s/equi/vacuum/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-vac_hbonds_nosim.cfg diff_masses/h_bonds/%s/no_simm/vacuum/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-vac_hbonds_nosim.cfg same_masses/h_bonds/%s/no_simm/vacuum/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-vac_hbonds_simm.cfg diff_masses/h_bonds/%s/simm/vacuum/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-vac_hbonds_simm.cfg same_masses/h_bonds/%s/simm/vacuum/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-vac_hbonds.cfg diff_masses/h_bonds/%s/equi/vacuum/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-vac_hbonds.cfg same_masses/h_bonds/%s/equi/vacuum/input/sim.cfg" % (basedir,pert),

      "cp -r %s/protocol/vacuum_no.sh diff_masses/all_bonds/%s/no_simm/vacuum/vacuum.sh" % (basedir,pert),
      "cp -r %s/protocol/vacuum_no.sh diff_masses/h_bonds/%s/no_simm/vacuum/vacuum.sh" % (basedir,pert),

      "cp -r %s/protocol/vacuum_simm.sh diff_masses/all_bonds/%s/simm/vacuum/vacuum.sh" % (basedir,pert),
      "cp -r %s/protocol/vacuum_simm.sh diff_masses/h_bonds/%s/simm/vacuum/vacuum.sh" % (basedir,pert),

      "cp -r %s/protocol/vacuum_no.sh same_masses/all_bonds/%s/no_simm/vacuum/vacuum.sh" % (basedir,pert),
      "cp -r %s/protocol/vacuum_no.sh same_masses/h_bonds/%s/no_simm/vacuum/vacuum.sh" % (basedir,pert),

      "cp -r %s/protocol/vacuum_simm.sh same_masses/all_bonds/%s/simm/vacuum/vacuum.sh" % (basedir,pert),
      "cp -r %s/protocol/vacuum_simm.sh same_masses/h_bonds/%s/simm/vacuum/vacuum.sh" % (basedir,pert),

      "cp -r %s/protocol/vacuum.sh diff_masses/all_bonds/%s/equi/vacuum/vacuum.sh" % (basedir,pert),
      "cp -r %s/protocol/vacuum.sh diff_masses/h_bonds/%s/equi/vacuum/vacuum.sh" % (basedir,pert),
      "cp -r %s/protocol/vacuum.sh same_masses/all_bonds/%s/equi/vacuum/vacuum.sh" % (basedir,pert),
      "cp -r %s/protocol/vacuum.sh same_masses/h_bonds/%s/equi/vacuum/vacuum.sh" % (basedir,pert),
        ]
for cmd in cmds:
    os.system(cmd)

cmds = []
for fold in folders:
    for sch in scheme:

        cmds.append("cp -r %s/_ligands/solvated.parm7 %s/%s/%s/free/input/SYSTEM.top" % (inputfolder,fold,pert,sch))
        cmds.append("cp -r %s/_ligands/solvated.pdb %s/%s/%s/free/input/SYSTEM.pdb" % (inputfolder,fold,pert,sch))
        cmds.append("cp -r %s/_ligands/solvated.rst7 %s/%s/%s/free/input/SYSTEM.crd"% (inputfolder,fold,pert,sch))
        cmds.append("cp -r %s/MORPH.pert %s/%s/%s/free/input/" % (inputfolder,fold,pert,sch))

        cmds.append("cp -r %s/protocol/analysis_gro %s/%s/%s/free/output/." % (basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/analysis_alchemical.py %s/%s/%s/free/output/." % (basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/extract_results.py %s/%s/%s/free/output/."% (basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/grad_profile.py %s/%s/%s/free/output/."% (basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/water_analysis.sh %s/%s/%s/free/output/." % (basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/coulcor.sh %s/%s/%s/free/." %(basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/FUNC_* %s/%s/%s/free/output/." %(basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/ljcor.sh %s/%s/%s/free/." %(basedir,fold,pert,sch))
        cmds.append("cp -r %s/protocol/parse* %s/%s/%s/free/output/." %(basedir,fold,pert,sch))

for cmd in cmds:
    os.system(cmd)

cmds = []
cmds =["cp -r %s/protocol/sim-free_allbonds_nosim.cfg diff_masses/all_bonds/%s/no_simm/free/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-free_allbonds_nosim.cfg same_masses/all_bonds/%s/no_simm/free/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-free_allbonds_simm.cfg diff_masses/all_bonds/%s/simm/free/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-free_allbonds_simm.cfg same_masses/all_bonds/%s/simm/free/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-free_allbonds.cfg diff_masses/all_bonds/%s/equi/free/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-free_allbonds.cfg same_masses/all_bonds/%s/equi/free/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-free_hbonds_nosim.cfg diff_masses/h_bonds/%s/no_simm/free/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-free_hbonds_nosim.cfg same_masses/h_bonds/%s/no_simm/free/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-free_hbonds_simm.cfg diff_masses/h_bonds/%s/simm/free/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-free_hbonds_simm.cfg same_masses/h_bonds/%s/simm/free/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-free_hbonds.cfg diff_masses/h_bonds/%s/equi/free/input/sim.cfg" % (basedir,pert),
      "cp -r %s/protocol/sim-free_hbonds.cfg same_masses/h_bonds/%s/equi/free/input/sim.cfg" % (basedir,pert),

      "cp -r %s/protocol/water_no.sh diff_masses/all_bonds/%s/no_simm/free/water.sh" % (basedir,pert),
      "cp -r %s/protocol/water_no.sh diff_masses/h_bonds/%s/no_simm/free/water.sh" % (basedir,pert),

      "cp -r %s/protocol/water_simm.sh diff_masses/all_bonds/%s/simm/free/water.sh" % (basedir,pert),
      "cp -r %s/protocol/water_simm.sh diff_masses/h_bonds/%s/simm/free/water.sh" % (basedir,pert),

      "cp -r %s/protocol/water_no.sh same_masses/all_bonds/%s/no_simm/free/water.sh" % (basedir,pert),
      "cp -r %s/protocol/water_no.sh same_masses/h_bonds/%s/no_simm/free/water.sh" % (basedir,pert),

      "cp -r %s/protocol/water_simm.sh same_masses/all_bonds/%s/simm/free/water.sh" % (basedir,pert),
      "cp -r %s/protocol/water_simm.sh same_masses/h_bonds/%s/simm/free/water.sh" % (basedir,pert),

      "cp -r %s/protocol/water.sh diff_masses/all_bonds/%s/equi/free/water.sh" % (basedir,pert),
      "cp -r %s/protocol/water.sh diff_masses/h_bonds/%s/equi/free/water.sh" % (basedir,pert),
      "cp -r %s/protocol/water.sh same_masses/all_bonds/%s/equi/free/water.sh" % (basedir,pert),
      "cp -r %s/protocol/water.sh same_masses/h_bonds/%s/equi/free/water.sh" % (basedir,pert)]

for cmd in cmds:
    os.system(cmd)


print("Enjoy submitting simulations :)")
