#Implentation of pseudocode found at https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm

import scipy as sp # After my own experiments I found that we need to import necessary packages within the module, else it won't


def EditDistance(s,t): # s,t are our 2 strings
    #For all i and j, d[i,j] will hold the Levenshtein distance between
    #the first i characters of s and the first j characters of t.
    #s has dimension m and t has dimension n
    #Note that d has (m+1) x (n+1) values.
    #print len(s)
    m = len(s)
    n = len(t)
    #print m,n
    d = sp.zeros((m,n))
    for i in range(0,m):
        d[i,0] = i
    for j in range(n):
        d[0,j] = j
    for j in range(1,n):
        for i in range(1,m):
            if s[i] == t[j]:
                d[i,j] = d[i-1,j-1]
            else:
                d[i,j] = min((d[i-1,j]+1),
                             (d[i,j-1]+1),
                             (d[i-1,j-1]+1)
                             )
    #print d[i,j] #This was to check it works
    return int(d[m-1,n-1])




