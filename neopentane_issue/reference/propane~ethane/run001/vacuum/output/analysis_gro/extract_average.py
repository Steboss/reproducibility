#to be imported in analysis_gro folder!
import os


inputfiles = open("results.txt","r")
reader = inputfiles.readlines()

average = float(reader[len(reader)-1].split()[1])

outputfile = open("../AVERAGE.dat","w")
outputfile.write("%.3f" % average)


