import pandas as pd
import time

from edDynamic import edDynamic as ed
import algo_edDivideConquer as DandC
#from branch_and_bound import def_branch as bb
#from algo_edDiagonal import edDiagonalApproximate as diag
from edit_distance_greedy_v2_return import GreditDist as gred
#from algo_edDiagonal import edDiagonalApproximate as kstrip


df_str = pd.read_csv(r'output 2017-12-11 18-21-40.csv')
#print df_str

df = pd.DataFrame(columns=('Str1','Str2','m x n''basic_time','Gred_time','ktime','dctime','b+b'))

string1 = df_str['Str1'][:]
#print str1
print type(string1)
string2 = df_str['Str2'][:]

counter = 0
for i in range(99):
    counter += 1
    s = string1[i]
    #print s
    t = string2[i]
    #print t

    #Basic Dynamic
    time1 = time.time()
    #print ed(s,t)
    print s,t
    results = gred(s,t)
    # print results
    time2 = time.time()
    dtime = time2 - time1
    #print s
    df.at[counter,'Str1'] = s
    df.at[counter, 'Str2'] = t
    df.at[counter,'m x n'] = s*t
    df.at[counter,'basic_time'] = dtime

    #Greed
    time1 = time.time()
    # print ed(s,t)
    results = ed(s, t)
    # print results
    time2 = time.time()
    dtime = time2 - time1
    df.at[counter, 'Gred_time'] = dtime
    """
    #B+B
    time1 = time.time()
    # print ed(s,t)
    results = bb(s, t)
    # print results
    time2 = time.time()
    dtime = time2 - time1
    df.at[counter, 'Gred_time'] = dtime

    #K-strip
    time1 = time.time()
    # print ed(s,t)
    results = ed(s, t)
    # print results
    time2 = time.time()
    dtime = time2 - time1
    df.at[counter, 'Gred_time'] = dtime
"""
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

