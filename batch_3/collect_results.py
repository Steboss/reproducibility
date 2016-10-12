#FEB 2016 Stefano Bosisio
#Script to analyze in one shot all the reproducibility project molecules
#Usage: python  collect_results  run001/relative  run001.csv    to save the file
#Output:  csv file with: molecules--free(TI,FUNC_0,FUNC_1,LRC)--vacuum(TI)--



import sys,os

#####
def readTI(path):

    results = open(path,"r")
    reader = results.readlines()
    try:
        DG_TI = reader[len(reader)-1].split()[1]
        DG_TI_err = reader[len(reader)-1].split()[2]
    except:
        DG_TI = 999.0
        DG_TI_err = 999.0

    return float(DG_TI)


def readCOULCOR(path):

    coulcor = open(path,"r")
    reader = coulcor.readlines()
    try:
        FUNC = reader[len(reader)-1].split()[2]
    except:
        FUNC = 999.0

    return float(FUNC)

def readLJCOR(path):

    ljcor = open(path,"r")
    reader = ljcor.readlines()
    #print(reader[len(reader)-2])
    try:
        LJCOR = reader[len(reader)-2].split()[2]
    except:
        LJCOR = 999.0

    return float(LJCOR)

#####


inputfolder = sys.argv[1]
#path = os.getcwd()
#let's go with relative path
dirs = [d for d in os.listdir(inputfolder) if os.path.isdir(os.path.join(inputfolder,d))]
excluded = ["analyze_script.sh"]

results = {}

print("Extracting results")

for mol in dirs:
    if mol in excluded:
        continue
    else:
        #print(mol)

        results[mol] = {}
        #ethane~methanol/free/output/analysis_gro/results.txt
        try:
            results[mol]['DG_TI_free'] = readTI("%s/%s/free/output/analysis_gro/results.txt" % (inputfolder,mol))

        except:
            results[mol]['DG_TI_free'] = float(999.0)

        try:
            results[mol]['DG_TI_vac'] = readTI("%s/%s/vacuum/output/analysis_gro/results.txt" % (inputfolder,mol))
        except:
            results[mol]['DG_TI_vac'] = float(999.0)

        try:
            results[mol]['DG_FUNC_0'] = readCOULCOR("%s/%s/free/output/freenrg-COULCOR-lam-0.000.dat" % (inputfolder,mol))
        except:
            results[mol]['DG_FUNC_0'] = float(999.0)

        try:
            results[mol]['DG_FUNC_1'] = readCOULCOR("%s/%s/free/output/freenrg-COULCOR-lam-1.000.dat" % (inputfolder,mol))
        except:
            results[mol]['DG_FUNC_1'] = float(999.0)

        try:
            results[mol]['DG_LJ_LRC_0'] = readLJCOR("%s/%s/free/output/freenrg-LJCOR-lam-0.000.dat" % (inputfolder,mol))
        except:
            results[mol]['DG_LJ_LRC_0'] = float(999.0)

        try:
            results[mol]['DG_LJ_LRC_1'] = readLJCOR("%s/%s/free/output/freenrg-LJCOR-lam-1.000.dat" % (inputfolder,mol))
        except:
            results[mol]['DG_LJ_LRC_1'] = float(999.0)


#Save everything
total = open(sys.argv[2],"w")

total.write("morph,VACUUM,FREE\n")

total.write(",TI,TI,FUNC-lam-0.000,FUNC-lam-1.000,LRC-lam-0.000,LRC-lam-1.000\n")

for mol in results:

    outline = "%s," % mol

    outline += "%8.5f," % (results[mol]['DG_TI_vac'])
    outline += "%8.5f," % (results[mol]['DG_TI_free'])
    outline += "%8.5f," % (results[mol]['DG_FUNC_0'])
    outline += "%8.5f," % (results[mol]['DG_FUNC_1'])
    outline += "%8.5f," % (results[mol]['DG_LJ_LRC_0'])
    outline += "%8.5f" % (results[mol]['DG_LJ_LRC_1'])


    outline+="\n"

    total.write(outline)
    print(mol)
    print(results[mol])
