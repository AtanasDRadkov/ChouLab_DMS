import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
#%matplotlib inline
import math
import numpy as np
import matplotlib
from matplotlib.colors import LinearSegmentedColormap
matplotlib.rcParams['pdf.fonttype'] = 42

DHFR_seq = "MISLIAALAVDRVIGMENAMPWNLPADLAWFKRNTLNKPVIMGRHTWESIGRPLPGRKNIILSSQPGTDDRVTWVKSVDEAIAACGDVPEIMVIGGGRVYEQFLPKAQKLYLTHIDAEVEGDTHFPDYEPDDWESVFSEFHDADAQNSHSYCFEILERR*"


#print sys.argv[1]

qc_map = pd.read_csv(sys.argv[1], index_col = 'Position  ')
labels = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y','*', '','avg']
qc_map.columns = labels

order = ['*','P','C','G','A','V','I','L','M','W','F','Y','H','K','R','S','T','N','Q','D','E', '','avg']

qc_map = qc_map[order]

locations = []
WT_aas = []
positions = sys.argv[2].split(',')
for pos in positions:
	locations.append(int(pos))
	WT_aas.append(DHFR_seq[int(pos)-1])
locations = [x for _,x in sorted(zip(WT_aas,locations),key=lambda y:order.index(y[0]))]
#locations = sorted(locations, key=lambda x:order.index(x))
locations = sorted(locations)
locations.append(0)
qc_map = qc_map.loc[locations]

sns.set(font_scale=1.2)
sns.set_style({"savefig.dpi": 200})


colormap = cmap = LinearSegmentedColormap.from_list('mycmap', [(0.0, '#555555'),
													(0.025, '#555555'),
													(0.030, '#C3C3C3'),
													(0.08, '#C3C3C3'),
													(0.0825, '#000080'),
													(0.15, '#000080'),
                                                    (0.35, '#0000FF'),
                                                    (0.4985, '#FFFFFF'),
                                                    (0.5015, '#FFFFFF'),
                                                    (0.6, "#FF0000"),
						    (0.70, "#b22222"),
                                                    (1.0, '#b22222')])

colormap.set_bad('black',1.)
fontsize_pt = 18
dpi = 100
matrix_height_pt = fontsize_pt * qc_map.shape[0]
matrix_height_in = matrix_height_pt / dpi
top_margin = 0.04
bottom_margin = 0.04
figure_height = matrix_height_in / (1 - top_margin - bottom_margin)
fig, ax = plt.subplots(
        figsize=(6,figure_height),
        gridspec_kw=dict(top=1-top_margin, bottom=bottom_margin))
ax = sns.heatmap(qc_map, cmap=colormap, linewidths=.1, ax=ax) #vmax = float(sys.argv[2]) vmin = float(sys.argv[3]))
ax.xaxis.tick_top()
ax.set_xticks(np.arange(len(order)))
ax.set_xticklabels(order, fontsize=fontsize_pt*0.8)
ax.set_yticks(np.arange(len(qc_map)))
ax.set_yticklabels(qc_map.index.tolist(), fontsize=fontsize_pt*0.8)
#ax.yaxis.tick_right()
plt.yticks(rotation=0)
#fig = ax.get_figure()
#length = len(qc_map) * 0.175
#fig.set_size_inches(5, length)
figname = sys.argv[1].split(".csv")[0] + "_physiochem_redblue.pdf"
#plt.tight_layout()
fig.savefig(figname)

plt.show() 