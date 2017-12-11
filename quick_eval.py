import pandas as pd
import time

from edDynamic import edDynamic as ed
import algo_edDivideConquer as DandC
#import branch_and_bound as bb
#from algo_edDiagonal import edDiagonalApproximate as diag
from edit_distance_greedy_v2_return import GreditDist as gred


df_str = pd.read_csv(r'output 2017-12-11 18-21-40.csv')
#print df_str

df = pd.DataFrame(columns=('Str1','Str2','basic_comptime','Gred',''))

str1 = df_str['Str1'][:]
print str1[10]
print type(str1)
str2 = df_str['Str2'][:]

counter = 0
for i in range(99):
    counter += 1
    #s = str1[i]
    print s
    t = str2[i]
    #print t

    #Basic Dynamic
    time1 = time.time()
    #print ed(s,t)
    results = gred(s,t)
    # print results
    time2 = time.time()
    dtime = time2 - time1
    print s
    df.at[counter,'Str1'] = s
    df.at[counter, 'Str2'] = t
    df.at[counter,'comptime'] = dtime

    #Greed
    time1 = time.time()
    # print ed(s,t)
    results = ed(s, t)
    # print results
    time2 = time.time()
    dtime = time2 - time1

print df

"""
counter = 0
for i in range(99):
    for j in range(10):
        counter += 1
        s = str1[i]
        print s
        t = str1[j]
        print t
        time1 = time.time()
        #print ed(s,t)
        results = ed(s,t)
        # print results
        time2 = time.time()
        dtime = time2 - time1
        print s
        df.at[counter,'Str1'] = s
        df.at[counter, 'Str2'] = t
        #df['Str1'].loc[counter] = s
        #df['Str2'].loc[counter] = t
        #df['comptime'].loc[counter] = dtime
"""

