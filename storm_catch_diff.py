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

variables=['times','bef_catch','aft_catch']
files=pd.read_csv('D:/projects/Lobsters/catch_temp/diff_bef_aft_s10_abs_v.csv',names=variables)
time=files['times'].values
times=[]
for i in range(len(time)):
    times.append(datetime.strptime(time[i],'%Y-%m-%d %H:%M'))

bef_catch=files['bef_catch'].values
aft_catch=files['aft_catch'].values
diff=[]
for i in range(len(bef_catch)):
    diff.append(aft_catch[i]-bef_catch[i])
print diff
diffs=np.array(diff)
plt.plot(times,diffs,'or',ms=6)
plt.axhline(0, color='black', lw=2)
plt.title('diff_bef_aft_10m/s_abs_v')
plt.savefig('diff_bef_aft_s10_abs_v.png',dpi=200,bbox_inches = "tight")
plt.show()