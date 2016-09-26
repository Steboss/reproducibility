import os,sys


files = os.listdir(os.getcwd())
files.sort()
#print(files)

cyclo_allbonds = "/cyclo/allbonds/output/analysis_gro/results.txt"
cyclo_none     = "/cyclo/none/output/analysis_gro/results.txt"

water_allbonds = "/water/allbonds/output/analysis_gro/results.txt"
water_none     = "/water/none/output/analysis_gro/results.txt"

vacuum_allbonds= "/vacuum/allbonds/output/analysis_gro/results.txt"
vacuum_none    = "/vacuum/none/output/analysis_gro/results.txt"

cyclo = []
water = []
vacuum = []


print("Collecting paths...")
for f in files:
    if f =="extract_results.py" or f=="cyclo_results.csv" or f=="water_results.csv"  or\
       f=="vacuum_results.csv"  or f=="README" or f=="analyze_script.sh" or f=="move_alc.py":
        continue
    else:

        allbonds = f + cyclo_allbonds
        none     = f + cyclo_none
        cyclo.append(allbonds)
        cyclo.append(none)

        allbonds = f + water_allbonds
        none     = f + water_none
        water.append(allbonds)
        water.append(none)

        allbonds = f + vacuum_allbonds
        none     = f + vacuum_none
        vacuum.append(allbonds)
        vacuum.append(none)

#print(complete_files)

output_cyclo = open("cyclo_results.csv","w")
output_cyclo.write("Bond Lengths, DDG\n")

output_water= open("water_results.csv","w")
output_water.write("Bond Lengths, DDG\n")

output_vacuum = open("vacuum_results.csv","w")
output_vacuum.write("Bond Lengths, DDG\n")


print("Writing cyclohexane csv...")
for c in cyclo:
    inputf = open(c,"r")
    readerf = inputf.readlines()
    result_line = readerf[len(readerf)-1]
    ddg = result_line.split()[1]

    bond = c.split("/")[0]
    constraint = c.split("/")[2]
    run = bond + "_" + constraint
    print(ddg)
    output_cyclo.write("%s,%s\n" %(run,ddg))

print("Writing water csv...")
for c in water:
    inputf = open(c,"r")
    readerf = inputf.readlines()
    result_line = readerf[len(readerf)-1]
    ddg = result_line.split()[1]

    bond = c.split("/")[0]
    constraint = c.split("/")[2]
    run = bond + "_" + constraint

    output_water.write("%s,%s\n" %(run,ddg))

print("Writing vacuum csv...")
for c in vacuum:
    inputf = open(c,"r")
    readerf = inputf.readlines()
    result_line = readerf[len(readerf)-1]
    ddg = result_line.split()[1]

    bond = c.split("/")[0]
    constraint = c.split("/")[2]
    run = bond + "_" + constraint

    output_vacuum.write("%s,%s\n" %(run,ddg))
print("FINISH :D")
'''

files = os.listdir( os.getcwd() )

files.sort()

for f in files:
    if f.endswith(".mol2"):
        name, ftype = f.split(".mol2")
        cmd = "babel -imol2 %s.mol2 -ocdxml %s.cdxml" %(name, name)
        os.system(cmd)
        print cmd
'''
