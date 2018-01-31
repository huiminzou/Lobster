# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 10:52:58 2016

@author: JIM
"""

from datetime import datetime as dt
from datetime import timedelta as td
from conversions import uv2sd,r2d
import math
from utilities import haversine, get_nc_data, nearpoint_index, get_wind_ncep
import numpy as np
from numpy import cumsum,diff,mean,isnan
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.dates import date2num, num2date
import netCDF4

#function used to find storm starttimes, stoptimes, and mean speed and/or slope. 
def getstorm(indict):
    [dtimes,u,v]=get_wind_ncep(indict['starttime'],indict['endtime'],indict['lat'],indict['lon'])
    print 'hold on ... getting wind for the year'
    
    # calculate wind speed
    spd=[]
    for k in range(len(u)):
        s=math.sqrt((u[k]**2)+(v[k]**2))
        spd.append(s)
    abs_v=abs(v)   
    if (indict['crittype']=='speed') or (indict['crittype']=='both'):
        #df=pd.DataFrame({'speed':spd},index=dtimes)
        df=pd.DataFrame({'speed':abs_v},index=dtimes)
        storm=df[df['speed']>(indict['stormw'])] #if wind speed is 16 s+, plot
        stormstart=[]
        stormend=[]
        kk=0 # kk is the index of the storm start
        for k in range(1,len(storm)):
            if (storm.index[k]-storm.index[k-1])>td((indict['stormbreak'])): #this defines a new storm when >hour between times
                stormend.append(storm.index[k-1])
                    #meanspeed=mean(df['speed'][kk:k])
                stormstart.append(storm.index[kk])
                kk=k
    if (indict['crittype']=='slope') or (indict['crittype']=='both'):
            # get slope and plot
        sqspd=[]
        for k in range(len(spd)):
            sqspd.append(spd[k]**2)
            cumsqspd=cumsum(sqspd)
            #slope=diff(cumsqspd)
            slopetime=dtimes[0:-1]
        df=pd.DataFrame({'slope':diff(cumsqspd)},index=slopetime)
        storm=df[df['slope']>indict['crit']] #if slope is > 275, plot      
        stormstart=[]
        stormend=[]
        kk=0 # kk is the index of the storm start  
        for k in range(1,len(storm)):
            if (storm.index[k]-storm.index[k-1])>td((indict['stormbreak'])): #this defines a new storm when >day between times
                stormend.append(storm.index[k-1])
                stormstart.append(storm.index[kk])
                kk=k
    return stormstart,stormend

#function used to get lobster catch value before and after storms 
#[stormstart,stormend]=getstorm()
def getcatch(indict):
  # where "indict" is the input dictionary with the following fields:
  # indict key: 
  # time_int=how many days before and after to average catch
  # crit=critical slope value, 
  # stormw=storm wind criteria in m/s; critical s, 
  # stormbreak=hours between critical wind that define a "new" storm
  # stormstart and stormend are the datetimes of storms
  
    variables=['ser_num','num','site_n','lat','lon','time_s','nan','nan','nan','depth','num_traps','catch','egger','short','idepth','nan']
    df2=pd.read_csv(indict['sqldumpfile'],names=variables)
      # convert catch times to datetime
    catcht=[]
    for k in range(len(df2)):
        catcht.append(dt.strptime(df2.time_s[k],'%Y-%m-%d:%H:%M'))
    catcht=np.array(catcht) 
    #print catcht   
      #get start and stop of catch data
    before_catch,after_catch,before_times,after_times,mean_bef_catch,mean_aft_catch=[],[],[],[],[],[]
    indbef,indaft=[],[]
    bc,ac,bt,at,avebc,aveac,=[],[],[],[],[],[]
    for k in range(len(indict['stormstart'])):
        indb=list(np.where((catcht>indict['stormstart'][k]-td(days=indict['time_int'])) & (catcht<indict['stormstart'][k])&(catcht>indict['starttime']))[0])#time focus on summer
        indbef.append(indb)
        inda=list(np.where((catcht>indict['stormend'][k]) & (catcht<indict['stormend'][k]+td(days=indict['time_int']))&(catcht<indict['endtime']))[0])#time focus on early fall season
        indaft.append(inda)
    for i in range(len(indbef)):
        for j in range(len(indbef[i])):
            bc.append(df2['catch'][indbef[i][j]]/indict['pot'])
            bt.append(catcht[indbef[i][j]])       
        before_catch.append(bc)
        before_times.append(bt)
        bc,bt=[],[]
    for i in range(len(before_catch)):
        for j in range(len(before_catch[i])):
            avebc.append(np.mean(before_catch[i]))#the mean of before_catch  
        mean_bef_catch.append(avebc)
        avebc=[]
    for i in range(len(indaft)):
        for j in range(len(indaft[i])):
            ac.append(df2['catch'][indaft[i][j]]/indict['pot'])
            at.append(catcht[indaft[i][j]])
        after_catch.append(ac)
        after_times.append(at)
        ac,at=[],[]
    for i in range(len(after_catch)):
        for j in range(len(after_catch[i])):
            aveac.append(np.mean(after_catch[i]))#the mean of after_catch
        mean_aft_catch.append(aveac)
        aveac=[]
    return before_catch,after_catch,before_times,after_times,mean_bef_catch,mean_aft_catch
