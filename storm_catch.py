# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 14:35:39 2016
program to look at catch before and after storms 
@author: JIM
modified by huimin in January 2018
"""
from datetime import datetime as dt
from storm_catch_functions import getstorm,getcatch
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta as td
#hardcodes
site='BN01'
year=2017
ylim_min=0
ylim_max=3.3
rows=3
cols=2
input_dictionary={'sqldumpfile':'D:/projects/Lobsters/catch_temp/sqldump_2018_01_BN.csv','time_int':14,'starttime':dt(2017,6,1,0,0,0),'endtime':dt(2017,11,1,0,0,0),'lat':42.12,'lon':-69.63,'crit':275,'stormw':10,'stormbreak':3,'crittype':'speed','pot':8.0}
#input_dictionary={'sqldumpfile':'/net/data5/jmanning/fish/lobster/mela/sqldump_2016_01_BN.csv','time_int':50,'starttime':dt(2013,1,0,1,1,0),'endtime':dt(2013,12,30,2,0,0),'lat':42.12,'lon':-69.63,'crit':275,'stormw':16,'stormbreak':3,'crittype':'speed'}
# input_dictionary key: time_int=how many days before and after to average catch, crit=critical slope value, stormw=storm wind criteria in m/s; critical s, stormbreak=hours between critical wind that define a "new" storm
[stormstart,stormend]=getstorm(input_dictionary) #function used to find storm starttimes, stoptimes, and mean speed and/or slope
input_dictionary['stormstart']=stormstart
input_dictionary['stormend']=stormend #appending stormstart and stormend to dict
[before_catch,after_catch,before_times,after_times,mean_bef_catch,mean_aft_catch]=getcatch(input_dictionary) #function used to get lobster average catch value before and after storms 
#diff=mean_bef_catch[0][0]-mean_bef_catch[0][0]
print mean_bef_catch,mean_aft_catch,stormstart
fig,axes=plt.subplots(rows,cols,figsize=(12,8))
for i in range(len(stormstart)):
    if i==0:
        axes[0,0].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        axes[0,0].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        axes[0,0].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        axes[0,0].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days
        if width==0:
            width=1
        axes[0,0].bar(stormstart[i],ylim_max,width)
        axes[0,0].legend(loc='best',fontsize=8,numpoints=1)
        axes[0,0].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        labels=axes[0,0].get_xticklabels()
        for label in labels:
            label.set_rotation(20)
        axes[0,0].set_ylim(ylim_min,ylim_max)
        axes[0,0].set_ylabel('catch/pot',fontsize=13)
        #axes[0,1].yaxis.set_visible(False)
    elif i==1:
        axes[0,1].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        axes[0,1].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        axes[0,1].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        axes[0,1].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days 
        if width==0:
            width=1
        axes[0,1].bar(stormstart[i],ylim_max,width)
        axes[0,1].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        labels=axes[0,1].get_xticklabels()
        for label in labels:
            label.set_rotation(20)
        axes[0,1].set_ylim(ylim_min,ylim_max)
        axes[0,1].get_yaxis().set_visible(False)
    elif i==2:
        #axes[1,0].set_visible(False)
        axes[1,0].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        axes[1,0].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        axes[1,0].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        axes[1,0].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days 
        if width==0:
            width=1
        axes[1,0].bar(stormstart[i],ylim_max,width)
        axes[1,0].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        labels=axes[1,0].get_xticklabels()
        for label in labels:
            label.set_rotation(20)
        axes[1,0].set_ylim(ylim_min,ylim_max)
        axes[1,0].set_ylabel('catch/pot',fontsize=13)
    elif i==3:
        axes[1,1].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        axes[1,1].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        axes[1,1].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        axes[1,1].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days
        if width==0:
            width=1
        axes[1,1].bar(stormstart[i],ylim_max,width)
        axes[1,1].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        labels=axes[1,1].get_xticklabels()
        for label in labels:
            label.set_rotation(20)
        axes[1,1].set_ylim(ylim_min,ylim_max)
        axes[1,1].set_ylabel('catch/pot',fontsize=13)
        axes[1,1].get_yaxis().set_visible(False)
    elif i==4:
        axes[2,0].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        axes[2,0].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        axes[2,0].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        axes[2,0].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days
        if width==0:
            width=1
        axes[2,0].bar(stormstart[i],ylim_max,width)
        axes[2,0].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        labels=axes[2,0].get_xticklabels()
        for label in labels:
            label.set_rotation(20)
        axes[2,0].set_ylim(ylim_min,ylim_max)
        axes[2,0].set_ylabel('catch/pot',fontsize=13)
        axes[2,0].get_yaxis().set_visible(False)
    elif i==5:
        axes[2,1].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        axes[2,1].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        axes[2,1].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        axes[2,1].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days
        if width==0:
            width=1
        axes[2,1].bar(stormstart[i],ylim_max,width)
        axes[2,1].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        labels=axes[2,1].get_xticklabels()
        for label in labels:
            label.set_rotation(20)
        axes[2,1].set_ylim(ylim_min,ylim_max)
        axes[2,1].set_ylabel('catch/pot',fontsize=13)
        axes[2,1].get_yaxis().set_visible(False)
#plt.gcf().autofmt_xdate()
#axes[0,1].set_visible(False)
#axes[1,0].set_visible(False)
#axes[1,1].set_visible(False)
fig.suptitle(site+'-'+str(year)+'-'+str(input_dictionary['time_int'])+'day'+'-'+str(input_dictionary['stormw'])+'m/s_abs_v',fontsize=15)
plt.savefig('storm_catch'+site+str(year)+str(input_dictionary['time_int'])+'day'+str(input_dictionary['stormw'])+'abs_v.png',dpi=200,bbox_inches = "tight")
plt.show()
