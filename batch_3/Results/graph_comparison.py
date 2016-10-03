import matplotlib.pyplot as plt
from numpy import *
import math
import re
import os
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sbn

sbn.set_style("whitegrid")
colors=sbn.color_palette()

xticks_name = ["methane~ethane","ethane~methane","ethane~methanol","methanol~ethane",\
                "methane~methanol","methanol~methane","methane~2-methylfuran","2-methylfuran~methane",\
                "methane~toluene","toluene~methane","methane~2-methylindole","2-methylindole~methane",\
                "methane~neopentane","neopentane~methane","methane~neopentane2","neopentane2~methane"]

sire_grom = [0.1703,0.0062,0.0236,0.0146,0.7491,1.0913,0.1551,0.2401,0.1711,0.1720,\
            0.2653,0.1663,0.3408,0.0857, 0.00,0.00]
sire_amber = [0.0267,0.1342,0.1194,0.1596,0.0269,0.0287,0.2491,0.2441,0.4621,0.2840,\
            0.4063,0.0217,0.3038,0.1197,0.0341,0.0296]
sire_amber_nod = [0.1243,0.0192,0.0444,0.0596,0.0521,0.0377,0.1951,0.2891,0.3011,\
            0.2360,0.5673,0.1473,0.8118,0.5417,0.0771,0.0186]

x_lines = linspace(1,16,16)

#print("x dim")
#print(len(x_lines))
#print("sire grom dim")
#print(len(sire_grom))
#print("sire amber dim")
#print(len(sire_amber))
#print("sire amber no dim")
#print(len(sire_amber_nod))
fig,ax = plt.subplots(figsize=[10,7])

ax.plot(x_lines,sire_grom,color=colors[0],marker="o",markersize=10,label="Sire~Gromacs",linestyle="None")
ax.plot(x_lines,sire_amber,color=colors[1],marker="^",markersize=10,label="Sire~Amber",linestyle="None")
ax.plot(x_lines,sire_amber_nod,color=colors[2],marker="s",markersize=10,label="Sire~AmberNoD",linestyle="None")


plt.xticks(arange(min(x_lines), max(x_lines)+1, 1.0))
xTickMarks=[str(x) for x in xticks_name]
xtickNames=ax.set_xticklabels(xTickMarks)

ax.set_ylabel(r'Absolute difference / kcal mol$^{-1}$',fontsize=20)


plt.legend(loc="upper left",fontsize=20)

plt.xticks(rotation=90,fontsize=20)
plt.yticks(fontsize=20)
plt.tight_layout()


plt.savefig("Comparison.png",dpi=600)
plt.savefig("Comparison_trasp.png",dpi=600,transparent=True)
plt.savefig("Comparison.pdf")
