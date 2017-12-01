"""
Implements the approximated version of the classical dynamic programming approach where one fills only a stripe of
size k around the diagonal of the matrix. Takes as argument the 2 strings to be compared, s and t, and the strip size k.
NEED TO FIND OUT IF WE CAN USE A SPARSE MATRIX OR ARRAY MUST BE SIZED BY STRIP
UPDATE: Can initialise empty array, only care about time complexity, not space
"""

import scipy as sp

def ED_Stripe(s,t,k):
    m = len(s) + 1
    n = len(t) + 1
    """ Tried to take account of which string is longer
    if m>n: 
        s = s1
        t = t1
        t1 = t
        s1 = s"""
    d = sp.zeros((m,n))
    for i in range(m):  # range starts from 0 (maybe can use range k?
        d[i, 0] = i
    for j in range(n):
        d[0, j] = j
    for i in range(1,n):
        for j in range(i, i+k):
            print i, j
            print s[i - 1], t[j - 1]
            if s[i - 1] == t[j - 1]:
                print 'same',s[i-1],t[j-1]
                d[i, j] = d[i - 1, j - 1]  # If they are same, get value from subproblems of strings excluding that value
                print d, i,j
            else:
                d[i, j] = min((d[i - 1, j] + 1),
                              # If they are different, choose subprob with lowest value, add 1 to indicate operation is necessary
                              (d[i, j - 1] + 1),
                              (d[i - 1, j - 1] + 1)
                              )
                print d,i,j

    dist = int(d[m - 1, n - 1])

    #results = pd.DataFrame(columns=('Ed','Ed_Matrix'))
    #results=sp.zeros(2,1)
    #results.loc[0] = [dist, d]
    #print results
    #print results['Ed']
    return dist,d

s = 'abdee'
t = 'ade'
print ED_Stripe(s,t,2)


"""
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
"""