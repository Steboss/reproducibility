from parmed.amber import * 
import os,sys

base = AmberParm(sys.argv[1],sys.argv[2])

res = base.residues[0]

base.LJ_depth[0] = base.LJ_depth[1]
base.LJ_radius[0] = base.LJ_radius[1]

base.recalculate_LJ()

base.write_parm("test.parm7")
base.write_rst7("test.rst7")

