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

#Glycosylation sites, doi: 10.2183/pjab.88.226

#Location of functional domains of HA protein, doi: 10.2183/pjab.88.226

#HA1=([1:329], "HA1 domain")
#HA2=([330:566], "HA2 Domain")

fig.suptitle('Hemagglutinin Domain Architecture', fontsize=14, fontweight='bold')
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
    ax.plot([int], [0.5], 'rx', markersize=15)

#for i in list:
    #ax.plot([i], [0.5], color='red', marker='|', markersize=15)
    #print(i)

ax.annotate("F1",xy=(40, 1))
ax.annotate("RBD",xy=(175, 1))
ax.annotate("cleavage site",xy=(312, 1))

#plt.plot(145, 0,'--','w')

plt.annotate('2x glyc',xy=(129, 1),xytext=(129, 1.7),
             arrowprops=dict(facecolor='deeppink'),
             )
plt.annotate('2x glyc',xy=(131, 1),xytext=(129, 1.7),
             arrowprops=dict(facecolor='black'),
             )
plt.annotate('2x glyc',xy=(163, 1),xytext=(163, 1.7),
             arrowprops=dict(facecolor='deeppink'),
             )
plt.annotate('2x glyc',xy=(165, 1),xytext=(163, 1.7),
             arrowprops=dict(facecolor='black'),
             )

plt.xticks(rotation=90)
plt.show()

rando = np.random.rand()
figname = (args.fig_name+'.pdf')

#randofigname = (rando+'.pdf')
plt.savefig(figname, dpi=350, format='pdf', pad_inches=0.1
)
exit()