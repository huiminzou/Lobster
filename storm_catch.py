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
import math
#hardcodes
site='BD'
num='01'
year=2017
ylim_min=0
ylim_max=3.0#the range of y-axis
ytwin_min=-14
ytwin_max=-10#the range of y-twinx
rows=2
cols=2
input_dictionary={'sqldumpfile':'D:/projects/Lobsters/catch_temp/sqldump_2018_01_'+site+'.csv','time_int':14,'starttime':dt(2017,6,1,0,0,0),'endtime':dt(2017,11,1,0,0,0),'lat':42.33,'lon':-70.87,'crit':275,'stormw':10,'stormbreak':3,'crittype':'speed','pot':8.0}
#input_dictionary={'sqldumpfile':'/net/data5/jmanning/fish/lobster/mela/sqldump_2016_01_BN.csv','time_int':50,'starttime':dt(2013,1,0,1,1,0),'endtime':dt(2013,12,30,2,0,0),'lat':42.12,'lon':-69.63,'crit':275,'stormw':16,'stormbreak':3,'crittype':'speed'}
# input_dictionary key: time_int=how many days before and after to average catch, crit=critical slope value, stormw=storm wind criteria in m/s; critical s, stormbreak=days between critical wind that define a "new" storm
[stormstart,stormend,storm]=getstorm(input_dictionary) #function used to find storm starttimes, stoptimes, and mean speed and/or slope

input_dictionary['stormstart']=stormstart
input_dictionary['stormend']=stormend #appending stormstart and stormend to dict
[before_catch,after_catch,before_times,after_times,mean_bef_catch,mean_aft_catch]=getcatch(input_dictionary) #function used to get lobster average catch value before and after storms 

print mean_bef_catch,mean_aft_catch,stormstart,stormend,storm
#########calculate the average of stormspeed############
ave_speed=[]
stormspeed=storm.speed[0:1].values
sum=0
for i in stormspeed:
    sum+=i
ave_speed.append(sum/len(stormspeed))
stormspeed=storm.speed[1:].values
sum=0
for i in stormspeed:
    sum+=i
ave_speed.append(sum/len(stormspeed))
"""
stormspeed=storm.speed[11:].values
sum=0
for i in stormspeed:
    sum+=i
ave_speed.append(sum/len(stormspeed))

stormspeed=storm.speed[12:13].values
sum=0
for i in stormspeed:
    sum+=i
ave_speed.append(sum/len(stormspeed))
"""
print ave_speed
#########################################################
fig,axes=plt.subplots(rows,cols,figsize=(12,8))
for i in range(len(stormstart)):
    if i==0:
        lns1=axes[0,0].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        lns2=axes[0,0].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        lns3=axes[0,0].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        lns4=axes[0,0].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days
        axes[0,0].bar(stormstart[i],ylim_max,width)
        
        axes[0,0].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        labels=axes[0,0].get_xticklabels()
        for label in labels:
            label.set_rotation(20)
        axes[0,0].set_ylim(ylim_min,ylim_max)
        axes[0,0].set_ylabel('catch/pot',fontsize=13)
        par0 = axes[0,0].twinx()
        lns5=par0.plot(stormstart[i],ave_speed[i],'*y',ms=14,label='speed_wind')
        par0.set_ylim(ytwin_min,ytwin_max)
        par0.set_ylabel('speed of wind')
        lns = lns1+lns2+lns3+lns4+lns5
        labs = [l.get_label() for l in lns]
        axes[0,0].legend(lns, labs, loc='best',fontsize=8,numpoints=1)
        par0.get_yaxis().set_visible(False)
        #axes[0,0].legend(loc='best',fontsize=8,numpoints=1)
    elif i==1:
        axes[0,1].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        axes[0,1].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        axes[0,1].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        axes[0,1].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days 
        axes[0,1].bar(stormstart[i],ylim_max,width)
        axes[0,1].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        labels=axes[0,1].get_xticklabels()
        for label in labels:
            label.set_rotation(20)
        axes[0,1].set_ylim(ylim_min,ylim_max)
        axes[0,1].get_yaxis().set_visible(False)
        par1 = axes[0,1].twinx()
        par1.plot(stormstart[i],ave_speed[i],'*y',ms=14,label='speed_storm')
        par1.set_ylim(ytwin_min,ytwin_max)
        par1.set_ylabel('speed of wind')
    elif i==2:
        
        axes[1,0].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        axes[1,0].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        axes[1,0].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        axes[1,0].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days 
        axes[1,0].bar(stormstart[i],ylim_max,width)
        axes[1,0].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        labels=axes[1,0].get_xticklabels()
        for label in labels:
            label.set_rotation(20)
        axes[1,0].set_ylim(ylim_min,ylim_max)
        axes[1,0].set_ylabel('catch/pot',fontsize=13)
        par2 = axes[1,0].twinx()
        par2.plot(stormstart[i],ave_speed[i],'*y',ms=12,label='speed_storm')
        par2.set_ylim(ytwin_min,ytwin_max)
        par2.set_ylabel('speed of storm (m/s)')
    elif i==3:
        axes[1,1].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        axes[1,1].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        axes[1,1].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        axes[1,1].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days
        axes[1,1].bar(stormstart[i],ylim_max,width)
        axes[1,1].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        labels=axes[1,1].get_xticklabels()
        for label in labels:
            label.set_rotation(20)
        axes[1,1].set_ylim(ylim_min,ylim_max)
        axes[1,1].set_ylabel('catch/pot',fontsize=13)
        axes[1,1].get_yaxis().set_visible(False)
        par3 = axes[1,1].twinx()
        par3.plot(stormstart[i],ave_speed[i],'*y',ms=12,label='speed_storm')
        par3.set_ylim(ytwin_min,ytwin_max)
        par3.set_ylabel('speed of storm (m/s)')
    elif i==4:
        axes[2,0].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        axes[2,0].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        axes[2,0].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        axes[2,0].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days
        axes[2,0].bar(stormstart[i],ylim_max,width)
        axes[2,0].xaxis.set_major_formatter(mdates.DateFormatter('%b-%d'))
        labels=axes[2,0].get_xticklabels()
        for label in labels:
            label.set_rotation(20)
        axes[2,0].set_ylim(ylim_min,ylim_max)
        axes[2,0].set_ylabel('catch/pot',fontsize=13)
        
    elif i==5:
        axes[2,1].plot(before_times[i],before_catch[i],'or',ms=10,label='before_storm')
        axes[2,1].plot(after_times[i],after_catch[i],'^g',ms=10,label='after_storm')
        axes[2,1].plot(before_times[i],mean_bef_catch[i],'-r',linewidth=4,label='average_before')
        axes[2,1].plot(after_times[i],mean_aft_catch[i],'-g',linewidth=4,label='average_after')
        width=(stormend[i]-stormstart[i]).days
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
axes[1,0].set_visible(False)
axes[1,1].set_visible(False)
#fig.suptitle(site+num+'-'+str(year)+'-'+str(input_dictionary['time_int'])+'day'+'-'+str(input_dictionary['stormw'])+'m/s_neg_v',fontsize=15)
#plt.savefig('storm_catch_speed_length'+site+num+str(year)+str(input_dictionary['time_int'])+'day'+str(input_dictionary['stormw'])+'neg_v.png',dpi=200,bbox_inches = "tight")
fig.suptitle('catch before and after storm with winds from the north in 2017',fontsize=15)
plt.savefig('catch before and after storm with winds from the north in 2017',dpi=200,bbox_inches = "tight")
plt.savefig('catch before and after storm with winds from the north in 2017.ps',dpi=200,bbox_inches = "tight")
plt.show()
