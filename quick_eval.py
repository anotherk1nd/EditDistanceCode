import pandas as pd

import edDynamic as dyn
import algo_edDivideConquer as DandC
import branch_and_bound as bb
from algo_edDiagonal import edDiagonalApproximate as diag
from edit_distance_greedy_v2 import GreditDist as gred


df_str = pd.read_csv(r'output 2017-12-11 18-21-40.csv')
str1 = df_str[str1]
str2 = df_str[str2]

counter = 0
for i in range(10):
    for j in range(10):
        counter += 1
        s = str1[i]
        t = str1[j]
        time1 = time.time()
        results = ed(s, t)
        # print results
        time2 = time.time()
        dtime = time2 - time1
        df = pd.DataFrame(columns=('comptime'))
        df.loc[counter] = dtime

print df
