from parmed.amber import * 
import os,sys


base = AmberParm(sys.argv[1],sys.argv[2])
mass = float(sys.argv[3])
atomC = base.residues[0].atoms[0]
atomC.mass = mass
base.remake_parm()
base.write_parm("test.parm7")

os.system("rm vacuum.parm7")
os.system("mv test.parm7 vacuum.parm7")
#Now water
base = AmberParm(sys.argv[4],sys.argv[5])
atomC = base.residues[0].atoms[0]
atomC.mass = mass
base.remake_parm()
base.write_parm("_ligands/test.parm7")
os.system("rm _ligands/solvated.parm7")
os.system("mv _ligands/test.parm7 _ligands/solvated.parm7")
