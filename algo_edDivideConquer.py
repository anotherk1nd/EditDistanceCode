def edLinearSpace(s,t):
    m=len(s)
    n=len(t)
    c=[[0 for x in range(n+1)] for x in range(2)]
    for j in range(n+1):
        c[0][j]=j
    for i in range(m):
        c[1][0]=i+1
        for j in range(n):
            if s[i]==t[j]:
                c[1][j+1]=c[0][j]
            else:
                c[1][j+1]= 1+ min(c[0][j],c[1][j],c[0][j+1])
        for j in range(n+1):
            c[0][j]=c[1][j]
            
    return c[0]


def edDivideConquer(x,y):
    Path=[]
    m=len(x)
    n=len(y)
    xmid=math.floor(m/2)
    print(xmid, m, n, x,y)
    #print(edLinearSpace(x,y))
    
    if m<=1 or n<=1:
        #edDynamic(x, y)
        #Path.append(edDynamic(x, y)
            return x,y
    else:  
        for i in range(m): 
            for j in range(n):
                c1=edLinearSpace(x[0:xmid],y[0:n])
                c2=edLinearSpace((x[xmid:m])[::-1],(y[0:n])[::-1])
                cost=np.array(c1)+np.array(c2[::-1])       
        q=np.argmin(cost)
        print("q=",q)
        Path.append((xmid,q))
        #print("first=",edDivideConquer(x[1:xmid],y[1:q]))
        #print("sec=",edDivideConquer(x[xmid+1:m],y[q+1:n]))
        Path.append(edDivideConquer(x[0:xmid],y[0:q]))
        Path.append(edDivideConquer(x[xmid:m],y[q:n]))
        
    return Path

