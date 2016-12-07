# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:38:51 2016

@author: GrinevskiyAS
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import matplotlib as mpl
import matplotlib.cm as cm

font_annot = {'family': 'Arial', 'weight': 'normal', 'size':13}
font={'family': 'Arial', 'weight': 'normal', 'size':14}
mpl.rc('font', **font)


def make_cmap(colors, position=None, bit=False):
    '''
    make_cmap takes a list of tuples which contain RGB values. The RGB
    values may either be in 8-bit [0 to 255] (in which bit must be set to
    True when called) or arithmetic [0 to 1] (default). make_cmap returns
    a cmap with equally spaced colors.
    Arrange your tuples so that the first color is the lowest value for the
    colorbar and the last is the highest.
    position contains values from 0 to 1 to dictate the location of each color.
    '''
    import matplotlib as mpl
    import numpy as np
    bit_rgb = np.linspace(0,1,256)
    if position == None:
        position = np.linspace(0,1,len(colors))
    else:
        if len(position) != len(colors):
            sys.exit("position length must be the same as colors")
        elif position[0] != 0 or position[-1] != 1:
            sys.exit("position must start with 0 and end with 1")
    if bit:
        for i in range(len(colors)):
            colors[i] = (bit_rgb[colors[i][0]],
                         bit_rgb[colors[i][1]],
                         bit_rgb[colors[i][2]])
    cdict = {'red':[], 'green':[], 'blue':[]}
    for pos, color in zip(position, colors):
        cdict['red'].append((pos, color[0], color[0]))
        cdict['green'].append((pos, color[1], color[1]))
        cdict['blue'].append((pos, color[2], color[2]))

    cmap = mpl.colors.LinearSegmentedColormap('my_colormap',cdict,256)
    return cmap



#a=np.loadtxt(fname="D:\Projects\Lyayel\Bazalt_totalthk_wellsHRS.txt",skiprows=1)
#a=pd.read_csv("D:\Projects\Lyayel\Bazalt_totalthk_wellsHRS.txt", sep="\t")
#a=pd.read_csv("D:\Projects\Lyayel\CoeffCorr_wellsHRS.txt", sep="\t")
#a=pd.read_csv("D:\Projects\Lyayel\Use_str_wellsHRS.txt", sep="\t")
a=pd.read_csv("D:\Projects\Komandirshor\WellTieCorrCoeff_171116.txt", sep="\t")


#cmap_z=np.loadtxt("E:\HRS\HRS_Files\Colormaps\cmap_zvalue.txt")
#cmap_zv=make_cmap (cmap_z[1:], position=np.linspace(0,1,len(cmap_z)-1))

###cmap_zv=clrs.ListedColormap (cmap_z, name='cmap_zv')

cmap_zv=cm.RdYlGn
minCC=0.4
maxCC=.8
norm = clrs.Normalize(vmin=minCC, vmax=maxCC, clip=True)

f=plt.figure(figsize=(12,10), facecolor='w')
ax=f.add_subplot(111)
sc=ax.scatter(a.X,a.Y,c=a.iloc[:,3],edgecolors='k',marker='o',s=300,cmap=cmap_zv, norm=norm)
#sc=ax.scatter(a.X,a.Y,c=a.iloc[:,3],edgecolors='k',marker='o',s=200,cmap=cmap_zv,norm=norm)

zerowells=a[a.iloc[:,3]==0]
sc2=ax.scatter(zerowells.X,zerowells.Y,c="w",edgecolors='k',s=300,norm=norm)


ax.set_aspect('equal')
cbar = plt.colorbar(sc, shrink=0.65, pad = 0.1, ticks=np.linspace(minCC,maxCC,9))



for ind, well in enumerate(a.iloc[:,0]):
    plt.text(a.iloc[ind,1]+600, a.iloc[ind,2], well, fontdict=font_annot)
    
    
    
seis_border_data=np.loadtxt(fname="D:\Projects\Komandirshor\HRS\kom_border.txt",skiprows=2)
seis_border_data=np.vstack((seis_border_data,seis_border_data[0,:]))
bdp=ax.plot(seis_border_data[:,0],seis_border_data[:,1],c='grey')
    
    