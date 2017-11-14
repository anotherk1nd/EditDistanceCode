#Implentation of pseudocode found at https://www.google.fr/search?q=wagner+fischer+algorithm&gws_rd=cr&dcr=0&ei=4eAKWuz6JIfNwAKvkouoBw

import scipy as sp


def EditDistance(s,t): # s,t are our 2 strings
    #For all i and j, d[i,j] will hold the Levenshtein distance between
    #the first i characters of s and the first j characters of t.
    #s has dimension m and t has dimension n
    #Note that d has (m+1) x (n+1) values.
    print len(s)
    m = len(s)
    n = len(t)
    print m,n
    d = sp.zeros(m,n)
    for i in range(m):
        d[i,0] = i
    for j in range(n):
        d[0,j] = j
    for j in range(n):
        for i in range(m):
            if s[i] == t[j]:
                d[i,j] = d[i-1,j-1]
            else:
                d[i,j] = min((d[i-1,j]+1),
                             (d[i,j-1]+1),
                             (d[i-1,j-1]+1)
                             )
    return d[m,n]

#Trial
s= 'abdee'

t= 'ade'
EditDistance(s,t)
print type(s)
print m,n