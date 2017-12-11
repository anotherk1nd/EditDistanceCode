import numpy as np

def edDynamic(x, y):
    # M records is the score array
    # P stores the path information, inside of Path:
    # d denotes: diagnal
    # u denotes: up
    # l denotes: left
    # s denotes : substitute
    M = np.zeros((len(x) + 1, len(y) + 1))
    P = np.empty((len(x) + 1, len(y) + 1), dtype=object)

    for i in range(1, len(x) + 1):
        M[i][0] = i
    for j in range(1, len(y) + 1):
        M[0][j] = j
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                M[i][j] = M[i - 1][j - 1]
                P[i][j] = "d"
            else:
                M[i][j] = 1 + min(M[i - 1][j - 1], M[i - 1][j], M[i][j - 1])
                if M[i][j] == 1 + M[i - 1][j - 1]:
                    P[i][j] = "s"
                elif M[i][j] == 1 + M[i - 1][j]:
                    P[i][j] = "u"
                else:
                    P[i][j] = "l"

    # return M[len(x)]
    return M[i][j]

s = 'sunrise'
t = 'sunshine'

print edDynamic(s,t)