# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:20:38 2018
plot difference before and after storm
@author: huimin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import time
###########get catch difference#################
site='BN'
num='01'
fig,ax=plt.subplots()
variables_catch_diff=['times','bef_catch','aft_catch']
files=pd.read_csv('D:/projects/Lobsters/catch_temp/diff_bef_aft_s13_neg_v.csv',names=variables_catch_diff)
times=files['times'].values
dates=[]
for i in range(len(times)):
    dates.append(datetime.strptime(times[i],'%Y-%m-%d %H:%M'))
bef_catch=files['bef_catch'].values
aft_catch=files['aft_catch'].values
diff=[]
for i in range(len(bef_catch)):
    diff.append(aft_catch[i]-bef_catch[i])
print diff
diffs=np.array(diff)
##########get length of storm#####################
file_length_storm=pd.read_csv('D:/projects/Lobsters/catch_temp/lenth_stormtime_BN01_s13_neg_v.csv',names=['stormstart','stormend'])
stormstart=file_length_storm['stormstart'].values
stormend=file_length_storm['stormend'].values
starttime,endtime=[],[]
for i in range(len(stormstart)):
    starttime.append(datetime.strptime(stormstart[i],'%Y-%m-%d %H:%M'))
    endtime.append(datetime.strptime(stormend[i],'%Y-%m-%d %H:%M'))
width,timedel=[],[]
for i in range(len(starttime)):
    timedel.append(endtime[i]-starttime[i])
for i in range(len(timedel)):
    width.append((timedel[i].days+timedel[i].seconds/60/60/6*0.25)*100)
for i in range(len(width)):
    if width==0:
        width+=1
######################################################
###################get speed of storm####################
file_speed=pd.read_csv('D:/projects/Lobsters/catch_temp/speed_BN01_s13_neg_v.csv',names=['stormtimes','ave_speed'])
stormtimes=file_speed['stormtimes'].values

ave_speed=file_speed['ave_speed'].values
#ax.plot(starttime,ave_speed,'*b',ms=12)
ax.bar(starttime,[3,3,3,3,3],width)
lns1=ax.plot(dates,diffs,'or',ms=12,label='catch differ')
ax.axhline(0, color='black', lw=2)
ax.set_title(site+num+'_diff_length_speed_13m/s_neg_v')
ax.set_ylabel('catch differ')
ax1=ax.twinx()
lns2=ax1.plot(starttime,ave_speed,'*y',ms=12,label='wind_speed')
ax1.set_ylabel('speed of wind')

lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0,numpoints=1)

plt.savefig(site+num+'_diff_length_speed_s13_neg_v.png',dpi=200,bbox_inches = "tight")
plt.show()