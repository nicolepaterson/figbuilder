#figbuilder/figbuild.py
#@nicolepaterson
#!usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import argparse

#print("Usage for HA SNP figure builder: "./figbuild.py -l 1 56 78 566 -f figure_name")
parser = argparse.ArgumentParser()

parser.add_argument("-l", "--snplist", nargs='+', type=int, dest="snp_input", help="List of amino acid position for desired SNPS in csv format: 1 2 23 87 566", required=True)
parser.add_argument("-f", "-figname", dest="fig_name", help="Figure name", required=True)

args = parser.parse_args()

fig, ax = plt.subplots(figsize=(11.5, 1.5))
fig.subplots_adjust(top=0.6)
fig.subplots_adjust(bottom=0.4)

cmap = (mpl.colors.ListedColormap(['gold','moccasin', 'teal', 'antiquewhite', 'thistle', 'tomato','lightcoral'])
        .with_extremes(over='0.25', under='0.75'))

#deep mutational scanning sites identified for H3 hemagglutinin, doi: 10.1073/pnas.1806133115.

#Location of functional domains of HA protein, doi: 10.2183/pjab.88.226

#HA1=([1:329], "HA1 domain")
#HA2=([330:566], "HA2 Domain")

fig.suptitle('DMS Sites Associated with Decreased Neutralization Mapped onto Hemagglutinin Domain Architecture', fontsize=12, fontweight='bold')
domains = [0,63, 114, 263, 276, 324, 329, 566]
#glycosylation sites

plt.grid(False)
norm = mpl.colors.BoundaryNorm(domains, cmap.N)
fig.colorbar(
    mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
    cax=ax,
    boundaries=[0] + domains + [566], 
    ticks=domains,
    spacing='proportional',
    orientation='horizontal',
    label='Amino acid position'
)
#"Enter SNP sites as csv list by aa position: 1 2 ...566"))]

#conv_list=int(args.snp_input)
x=args.snp_input
print(x)

#Plot the SNPs entered
for int in x:
    ax.plot([int], [0.8], color='black', marker='v', markersize=15)

#for i in list:
    #ax.plot([i], [0.5], color='red', marker='|', markersize=15)
    #print(i)

ax.annotate("F1",xy=(40, 1))
ax.annotate("RBD",xy=(175, 1))
ax.annotate("cleavage site",xy=(312, 1))

#plt.plot(145, 0,'--','w')

hifold = [153,154,155,156]
lofold = [125,127,129,163]
#deep mutational scanning sites identified for H3 hemagglutinin, doi: 10.1073/pnas.1806133115.


for int in hifold:
    ax.plot([int], [0.5], color='orange', marker='1', markersize=12,label="4-8 fold titer change")
for int in lofold:
    ax.plot([int], [0.5], color='lightblue', marker='2', markersize=12,label="2-4 fold titer change")

plt.xticks(rotation=90)
plt.show()
#plt.legend(loc="upper left")
#rando = np.random.rand()
figname = (args.fig_name+'.png')

#randofigname = (rando+'.pdf')
plt.savefig(figname, dpi=350, format='png', pad_inches=0.1
)
exit()
