#little script for  volume and density calculation for a given trajectory, topology and coord
#python density_calculator.py  trajectory  topology coordinates

import argparse,sys,os,numpy,math
import mdtraj as md
from parmed.amber import *
import matplotlib.pyplot as plt




trajectory = sys.argv[1]
topology = sys.argv[2]
coordinates = sys.argv[3]

timestep = 2 #fs
N_a = 6.02214*10**23 #Avogadros number

traj = md.load(trajectory, top=topology)
base = AmberParm(topology, coordinates)

##calculation of masses###
mass = 0 
for atom in base.atoms:
    mass = mass + atom.mass

##calcualtion of density###
##according to amber formula    Masses/(6.022*10**23*Vol)  with Masses = Total mass of the system, 6.022*10**23 particles/mol Avogadros number, Vol is in nm**3 
##volume is converted into cm**3 by  10**-21

actual_density = []
volume = []

for lengths in traj.unitcell_lengths:
    vol = lengths.prod()*10**-21  #conversion to cm**3
    density = mass/(N_a*vol)
    actual_density.append(density)
    volume.append(vol*10**21) #appending volume in nm**3

#####average density, plot of density along time of simulation, average volume and plot volume ####


avg_density = numpy.mean(actual_density)
print("Average density %f  g/cc" % avg_density)
avg_volume = numpy.mean(volume)
print("Average box size %f nm^3" % avg_volume)



time_axis_ns = numpy.linspace(0,len(traj), len(traj)) #conversion to ns (or is it better to ps?)

density_file = open("density.dat","w")
for i in range(0,len(time_axis_ns)):
    density_file.write("%.3f        %.3f\n" %(time_axis_ns[i],actual_density[i]))


plt.plot(time_axis_ns, actual_density, "o--", label="density")

plt.xlabel("Time (ps)",fontsize= 18)
plt.ylabel("Density (g/cm$\^3$)",fontsize= 18)
plt.legend(loc="best")
plt.savefig("density.png")

plt.clf()

