import time

#Naive computation of the edit distance
def edNaive(s,t,m,n):
    #empty s,insert t
    # m=len(s)
    # n=len(t)

    if m==0 and n==0:
        return 0,[],[]
    if m==0:
        return n, ["-" for i in range(n)], [t[i] for i in range(n)]
    #empty t,delete s
    if n==0:
        return m, [s[i] for i in range(m)], ["-" for i in range(m)]


    #last characters of s and t match
    if s[m-1]==t[n-1]:
        sed, as1, as2 = edNaive(s,t,m-1,n-1)
        #building the alignment when the characters match
        as1 += [s[m-1]]
        as2 += [t[n-1]]
        return sed, as1, as2
    #last characters of s and t don't match
    else:
        ied, ai1, ai2 = edNaive(s,t,m,n-1) #insertion
        ded, ad1, ad2 = edNaive(s,t,m-1,n) #deletion
        ced, ac1, ac2 = edNaive(s,t,m-1,n-1) #substitution

        min_op = min(ied, ded, ced)

        if (min_op == ied):
            ai1 += ["-"]
            ai2 += [t[n-1]]
            return (1+ ied), ai1, ai2
        elif (min_op == ded):
            ad1 += [s[m-1]]
            ad2 += ["-"]
            return (1 + ded), ad1, ad2
        else:
            ac1 += [s[m-1]]
            ac2 += ["-"]
            return (1 + ced), ac1, ac2



#Printing utility
#For convenience issues, prints edit distance and alignment
def the_printer(editDist, al1, al2):
    print("Edit distance:", editDist)

    l = len(al1)
    al1 = ''.join(al1)
    al2 = ''.join(al2)
    mark = ''
    for i in range(l):
        if al1[i] == al2[i]:
            mark += "|"
        else:
            mark += " "

    print("\nALIGNMENT: \n"
          + al1 + "\n"
          + mark + "\n"
          + al2)










s= "sun"
t= "sunshine"

edit_distance, a1, a2 = edNaive(s,t,len(s),len(t))
the_printer(edit_distance, a1, a2)

startTime = time.time()

edNaive('sunrise','sunshine',len('sunrise'),len('sunshine'))

elapsedTime = time.time() - startTime
print("the time use is ", elapsedTime*1000,"ms")

