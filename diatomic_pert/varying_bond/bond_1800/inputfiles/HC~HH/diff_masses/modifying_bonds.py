#USage: python modifiying.py   vacuum.parm7 vacuum.rst7  1.500 _ligands/solvated.parm7 _ligands/solvated.rst7
from parmed.amber import * 
import sys,os

base = AmberParm(sys.argv[1],sys.argv[2])
req=float(sys.argv[3])
base.residues[0].atoms[0].bonds[0].type.req = req

base.remake_parm()

base.write_parm("new.parm7")
base.write_rst7("new.rst7")

os.system("rm vacuum.parm7")
os.system("mv new.parm7 vacuum.parm7")
os.system("rm vacuum.rst7")
os.system("mv new.rst7 vacuum.rst7")

morph = open("MORPH.pert","r").readlines()
outputmorph = open("MORPH_new","w")

for f in morph:
    if "initial_equil" in f:
        outputmorph.write("                initial_equil %.3f\n" %(req))
    else:
        outputmorph.write(f)

os.system("rm MORPH.pert")
os.system("mv MORPH_new MORPH.pert")


#now water part
base =AmberParm(sys.argv[4],sys.argv[5])
base.residues[0].atoms[0].bonds[0].type.req = req

base.remake_parm()
base.write_parm("_ligands/new.parm7")
base.write_rst7("_ligands/new.rst7")

os.system("rm _ligands/solvated.parm7")
os.system("rm _ligands/solvated.rst7")
os.system("mv _ligands/new.parm7 _ligands/solvated.parm7")
os.system("mv _ligands/new.rst7  _ligands/solvated.rst7")


#now modifying the opposite morph:

back_morph = open("../../HH~HC/diff_masses/MORPH.pert","r").readlines()
tmp_morph = open("../../HH~HC/diff_masses/new_morph","w")

for f in back_morph:
    if "final_equil" in f:
        tmp_morph.write("                final_equil   %.3f\n" %(req))
    else:
        tmp_morph.write(f)


os.system("rm ../../HH~HC/diff_masses/MORPH.pert")
os.system("mv ../../HH~HC/diff_masses/new_morph ../../HH~HC/diff_masses/MORPH.pert")
