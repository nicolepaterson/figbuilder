#figbuilder/figbuild.py
#Plots a set of mutations against sites identified to be important for recognition of broadly neutralizing antibody C585
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

#C585 broadly neutralizing antibody H3 epitope sites DOI: 10.1128/JVI.01035-19

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
    ax.plot([int], [0.8], color='black', marker='v', markersize=15)

#for i in list:
    #ax.plot([i], [0.5], color='red', marker='|', markersize=15)
    #print(i)

ax.annotate("F1",xy=(40, 1))
ax.annotate("RBD",xy=(175, 1))
ax.annotate("cleavage site",xy=(312, 1))

#Plotting the epitope binding sites 

#plt.plot(145, 0,'--','w')
highcon = [119,123,168,169,171,174,176,257,259]
varsites = [121,122,124,172,173]
#C585 broadly neutralizing antibody H3 epitope sites DOI: 10.1128/JVI.01035-19


for int in highcon:
    ax.plot([int], [0.5], color='blue', marker='o', markersize=5,label="highly conserved sites")
for int in varsites:
    ax.plot([int], [0.5], color='red', marker='v', markersize=8,label="variable sites")

#plt.legend(loc="upper left")
plt.xticks(rotation=90)
plt.show()

#rando = np.random.rand()
figname = (args.fig_name+'.png')

#randofigname = (rando+'.pdf')
plt.savefig(figname, dpi=350, format='png', pad_inches=0.1
)
exit()
