#APR 2015 Stefano Bosisio
#Script to extract DG values from analysis_gro once everything has been done
#Output:AVERAGE.dat:  DG +-/ err
sys.path.append('/home/steboss/.local/lib/python2.7/site-packages/numpy-1.12.0.dev0+1b6831b-py2.7-linux-x86_64.egg')
from numpy import * 



mbar = open("freenrg-MBAR.dat", "r")
reader = mbar.readlines()
mbar_result = float(reader[len(reader)-4].split()[7])
mbar_err = float(reader[len(reader)-4].split()[10])

output_mbar = open("AVERAGE_MBAR.dat","w")
output_mbar.write("DG =   %.3f	+/- %.3f kcal/mol" % (mbar_result,mbar_err))
