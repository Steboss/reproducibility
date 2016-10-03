#FEB 2016 Stefano Bosisio
#Script to analyze in one shot all the reproducibility project molecules
#Usage: python  collect_results  run_numb ( e.g run001)
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
    try: 
        LJCOR = reader[len(reader)-1].split()[2]
    except:
        LJCOR = 999.0

    return float(LJCOR)

#####


run_numb = sys.argv[1]
path = os.getcwd()
dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path,d))]
excluded = ["collect_results.py","inputfiles","methane","neopentane","run001.csv","run002.csv","run003.csv"]

results = {}

print("Extracting results")

for mol in dirs:
    if mol in excluded:
        continue
    else:
        print(mol)
        #path = str(path) + "/" + str(mol)
        #print(path)
        results[mol] = {}
        
        try:
            results[mol]['DG_TI_free'] = readTI("%s/%s/%s/free/analysis_gro/results.txt" % (path,mol,run_numb))
        except:
            results[mol]['DG_TI_free'] = float(999.0)
        
        try:
            results[mol]['DG_TI_vac'] = readTI("%s/%s/%s/vacuum/analysis_gro/results.txt" % (path,mol,run_numb))
        except:
            results[mol]['DG_TI_vac'] = float(999.0)

        try:
            results[mol]['DG_FUNC_0'] = readCOULCOR("%s/%s/%s/free/freenrg-COULCOR_lam-0.000.dat" % (path,mol,run_numb))
        except:
            results[mol]['DG_FUNC_0'] = float(999.0)

        try:
            results[mol]['DG_FUNC_1'] = readCOULCOR("%s/%s/%s/free/freenrg-COULCOR_lam-1.000.dat" % (path,mol,run_numb))
        except:
            results[mol]['DG_FUNC_1'] = float(999.0)

        try:
            results[mol]['DG_LJ_LRC'] = readLJCOR("%s/%s/%s/free/freenrg-LJCOR.dat" % (path,mol,run_numb))
        except:
            results[mol]['DG_LJ_LRC'] = float(999.0)
        


#Save everything
name_total = run_numb + ".csv"
total = open(name_total,"w")

total.write("morph,VACUUM,FREE\n")

total.write(",TI,TI,FUNC-lam-0.000,FUNC-lam-1.000,LRC\n")

for mol in results:
    
    outline = "%s," % mol

    outline += "%8.5f," % (results[mol]['DG_TI_vac'])
    outline += "%8.5f," % (results[mol]['DG_TI_free'])
    outline += "%8.5f," % (results[mol]['DG_FUNC_0'])
    outline += "%8.5f," % (results[mol]['DG_FUNC_1'])
    outline += "%8.5f" % (results[mol]['DG_LJ_LRC'])
 
    outline+="\n"

    total.write(outline)


