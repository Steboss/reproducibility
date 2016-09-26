#SEPT 2016 Stefano Bosisio
#Script to change the bond length for CH to HH simulations
#Usage : python change_bonds   req(float)
from parmed.amber import *
import sys

base = AmberParm("SYSTEM.top","SYSTEM.crd")
req = float(sys.argv[1])

base.residues[0].atoms[0].bonds[0].type.req = req

base.remake_parm()

base.write_parm("SYSTEM.top")
base.write_rst7("SYSTEM.crd")
