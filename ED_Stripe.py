"""
Implements the approximated version of the classical dynamic programming approach where one fills only a stripe of
size k around the diagonal of the matrix. Takes as argument the 2 strings to be compared, s and t, and the strip size k.
NEED TO FIND OUT IF WE CAN USE A SPARSE MATRIX OR ARRAY MUST BE SIZED BY STRIP
"""

import scipy as sp


def ED_Stripe(s,t,k):
    strip = sp.zeros((len(s),k))
    return strip

s = 'abdee'
t = 'ade'

strip = ED_Stripe(s,t,1) #Problem with filling matrix due to different indices, suggest filling with sparse matrix
#strip[0,0] = 0 #Using zeros so corner is initialised to zero obvs!
#print len(strip)
print strip

k = 2
for i in range(len(s)+1):
    for j in range(i,i+k):
        print i,j
        #strip[i,j] = s[i]
        if s[i - 1] == t[j - 1]:
            strip[i, k-1] = strip[i - 1, j - 1]  # If they are same, get value from subproblems of strings excluding that value
            print strip
        else:
            strip[i, k-1] = min((strip[i - 1, j] + 1),
                          # If they are different, choose subprob with lowest value, add 1 to indicate operation is necessary
                          (strip[i, j - 1] + 1),
                          (strip[i - 1, j - 1] + 1))
            print strip
#print strip