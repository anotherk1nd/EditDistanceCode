#Import different modules here
from editdistancefromwikiUPDATE import EditDistance as ed
#from edit_distance_greedy_v2 import GreditDist as gd
import datetime
import time
import os # For exporting file in manner compatible with different OS
import scipy as sp
from RSG import RSG
import pandas as pd
pd.set_option('display.max_colwidth', -1)


"""
s= 'abdee'
t= 'ade'
s1 = RSG(4)
print s1
s2 = RSG(4)
print s2
"""
#t0=time.time()

#print s1,s2,ed(s1,s2)
#t1 = time.time()

#time = float(t1-t0)
#print 'Time to run is %.6f seconds' % (time)
#s1 = RSG(5)
#s2 = RSG(6)
#print s1,s2
#print ed(s1,s2)

df = pd.DataFrame(columns=('ref','Str1','Str2','Ed','Ed_Matrix','comptime')) #=str(),Str2=str(),Time=int(),stringsAsFactors=FALSE)
#print df
counter = 0
for i in range(1,10):
    for j in range(1,10):
        counter += 1
        str1 = RSG(i)
        str2 = RSG(j)
        #print str1,str2
        #print ed(str1, str2)
        time1 = time.time()
        results = ed(str1,str2)
        #print results
        time2 = time.time()
        dtime = time2-time1
        #print results.loc(i,['d'])
        #df.loc[i] = [time1,str1,str2,results.loc[0,'Ed'],results.loc[0,'Ed_Matrix'],dtime]
        #df = pd.DataFrame([time1,str1,str2,results.loc[0,'Ed'],results.loc[0,'Ed_Matrix'],dtime])
        df.loc[counter] = [time1,str1,str2,results.loc[0,'Ed'],results.loc[0,'Ed_Matrix'],dtime]
        #dftemp = pd.DataFrame()

        #print dftemp
        #df = df.append(dftemp)
        #print df

print df
root = 'EditDistanceCode'
os.path.join(root,) #Use this to work independent of operating system
path = r'Results/'
name = 'output '+str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+'.csv'
df.to_csv(path+name)

#print s,t,ed(s,t)