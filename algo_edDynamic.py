import numpy as np
import math

def edDynamic(x, y):
    # M records is the score array
    # P stores the path information, inside of Path:
    # d denotes: diagnal
    # u denotes: up
    # l denotes: left
    # s denotes : substitute
    lenx = len(x)
    leny = len(y)

    M = np.zeros((lenx + 1, leny + 1))
    P = np.empty((lenx + 1, leny + 1), dtype=object)


    for i in range(1, lenx+1):
        M[i][0] = i
    for j in range(1, leny+1):
        M[0][j] = j
    for i in range(1, lenx + 1):
        for j in range(1, leny + 1):
            if x[i-1] == y[j-1]:
                M[i][j] = M[i-1][j-1]
                P[i][j] =  "d"
            else:
                M[i][j] = 1+ min(M[i-1][j-1], M[i-1][j], M[i][j-1])
                if M[i][j] == 1+ M[i-1][j-1]:
                    P[i][j] =  "s"
                elif M[i][j] == 1+M[i-1][j]:
                    P[i][j] = "u"
                else:
                    P[i][j] = "l"

    print("Edit_distance:",int(M[lenx][leny]))

    #Building the alignment
    i = lenx
    j = leny

    align1 = ''
    mark = ''
    align2 = ''
    while i != 0 and j != 0:
        if P[i][j] == "d":#same
            align1 = x[i-1] + align1
            mark = "|" + mark
            align2 = y[j-1] + align2
            i -= 1
            j -= 1
        elif P[i][j] == "s":#substitution
            align1 = x[i-1] + align1
            mark = " " + mark
            align2 = y[j-1] + align2
            i -= 1
            j -= 1
        elif P[i][j] == "u":#deletion
            align1 = x[i-1] + align1
            mark = " " + mark
            align2 = "-" + align2
            i -= 1
        else:#insertion
            align1 = "-" + align1
            mark = " " + mark
            align2 = y[j-1] + align2
            j -= 1

    print("ALIGNMENT:\n" +
    align1 + "\n" +
    mark + "\n" +
    align2)

	#return M[lenx] 
	#return M[lenx][leny]
    return M,P



x= "sunrise"
y= "sunshine"

edDynamic(x, y)

import time

startTime = time.time()

edDynamic('pretty','protein')

elapsedTime = time.time() - startTime
print("the time use is ", elapsedTime*1000,"ms")


