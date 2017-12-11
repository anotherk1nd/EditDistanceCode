def edDiagonalApproximate(s,t,k):
    m=len(s)
    n=len(t)
    x=[0 for x in range(k+1)]
    c=[[0 for x in range(n+1)] for x in range(m+1)]
    if m==0:
        return False
    if n==0:
        return False
    if abs(m-n)>D:
        return False
    for i in range(m+1):
        c[i][0]=i
    for j in range(1,n+1):
        c[0][j]=j
    for i in range(1,m+1):
        x=0
        if i<D+1:
            c[i][i-D-1]=1000
        for j in range(max(i-D,1),min(i+D,n)+1):
            if s[i-1]==t[j-1]:
                c[i][j]=c[i-1][j-1]
            else:
                c[i][j]=1+min(c[i-1][j],c[i][j-1],c[i-1][j-1])
            if c[i][j]<=D:
                x=x+1
        if j<n:
            c[i][j]=1000
        if x<=0:
            return False
    if c[m][n]<=D:
        return True
    else:
        return False
    
s = 'abdee'
t = 'ade'

edDiagonalApproximate(s,t,1)


