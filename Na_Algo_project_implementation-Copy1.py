
# coding: utf-8

# # Algorithm Edit ditance project

# # Naive version 

# In[7]:


import numpy as np

get_ipython().magic('matplotlib inline')


# In[8]:


def edNaive(s,t,m,n):
    #empty s,insert t
    #m=len(s)
    #n=len(t)
    
    if m==0:
        return n
    #empty t,delete s
    if n==0:
        return m
    #last characters of s and t match
    if s[m-1]==t[n-1]:
        return edNaive(s,t,m-1,n-1)
    #last characters of s and t don't match
    else:
        return 1+ min(edNaive(s,t,m-1,n),
               edNaive(s,t,m,n-1),
               edNaive(s,t,m-1,n-1))



# In[9]:


s= "sun"
t= "sunshine"


# In[10]:


edNaive(s,t,len(s),len(t))


# # classic dynamic programming approach
# 

# In[11]:


def edDynamicProgramming(s,t,m,n):
    
    v=[[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                v[i][j]=j
            
            elif j==0:
                v[i][j]=i  
            elif s[i-1]==t[j-1]:
                v[i][j]=v[i-1][j-1] 
            else:
                v[i][j]=1 + min (v[i-1][j],v[i][j-1],v[i-1][j-1])
    print(v[m])  
    return v[m][n]   


# In[12]:


x= "sunrise"
y= "sunshine"


# In[13]:


print(edDynamicProgramming(s,t,len(s),len(t)))


# # DP-divide and conquer-linear space

# In[14]:


import numpy as np
import math
from operator import add


# In[15]:


def edDynamic(x, y):
  # M records is the score array
  # P stores the path information, inside of Path:
  # d denotes: diagnal
  # u denotes: up
  # l denotes: left
  # s denotes : substitute
     M = np.zeros((len(x) + 1, len(y) + 1))
     P = np.empty((len(x) + 1, len(y) + 1), dtype=object)
     

     for i in range(1, len(x)+1):
        M[i][0] = i  
     for j in range(1, len(y)+1):
        M[0][j] = j 
     for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
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

  
     #return M[len(x)] 
     return M,P


# In[16]:


x= "sunrise"
y= "sunshine"


# In[17]:


edDynamic(x, y)


# In[18]:


def printedDynamic(P,x,i,j):
     
    if i==0 or j==0:
        return 
    
    if P[i][j]=="d":
        printedDynamic(P,x,i-1,j-1)
        print(x[i])
    elif P[i][j]=="u":
        printedDynamic(P,x,i-1,j)
    else:
        printedDynamic(P,x,i,j-1)


# In[19]:


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


# In[20]:


s= "sunrise"
t= "sunshine"


# In[21]:


print(edLinearSpace(s,t))


# In[22]:


def edDivideConquer(x,y):
    Path=[]
    m=len(x)
    n=len(y)
    xmid=math.floor(m/2)
    print(xmid, m, n, x,y)
    
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
        #print("q=",q)
        Path.append((xmid,q))
        #print("first=",edDivideConquer(x[1:xmid],y[1:q]))
        #print("sec=",edDivideConquer(x[xmid+1:m],y[q+1:n]))
        Path.append(edDivideConquer(x[0:xmid],y[0:q]))
        Path.append(edDivideConquer(x[xmid:m],y[q:n]))
        
    return Path
    
 
    


# In[23]:


y= "sunrise"
x= "sunshine"
print(edLinearSpace(x,y))


# In[24]:


edDivideConquer(x,y)


# In[25]:


def edDiagnonalApproximate(s,t,D):
    m=len(s)
    n=len(t)
    x=[0 for x in range(D+1)]
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
    
    
            
            
        
    


# In[26]:


s="approximate"
t="appropriate"


# In[27]:


edDiagnonalApproximate(s,t,3)


# In[28]:


s="approximate"
t="appropriate"


# In[29]:


##to think about and add substitution
def edDiagnonalsub(s,t):
    m=len(s)
    n=len(t)
    maxi=m+n
    x=[0 for x in range(2*(maxi+1))]
    v=[[0 for x in range(2*(maxi+1))] for x in range(2*(maxi+1))]
    v[1]=0
    for D in range(0,maxi+1):
        for k in range(-D,D+1,2):
            if k==-D or k!=D and v[k-1]<v[k+1]:
                x = v[k+1]
            else:
                x =v[k-1]+1
            y=x-k
            while x<m and y<n and s[x]==t[y]:
                x=x+1
                y=y+1
            v[k]=x
            if x==m and y==n:
                return D


# In[30]:


s="approximate"
t="appropriate"


# In[31]:


edDiagnonalsub(s,t)


# In[32]:


## same with edDiagonalsub
def edDiagnonalGreedy(s,t):
    m=len(s)
    n=len(t)
    max=m+n
    x=[0 for x in range(2*(max+1))]
    v=[[0 for x in range(2*(max+1))] for x in range(2*(max+1))]
    v[1]=0
    for D in range(0,max+1):
        for k in range(-D,D+1,2):
            if k==-D or k!=D and v[k-1]<v[k+1]:
                x = v[k+1]
            else:
                x =v[k-1]+1
            y=x-k
            while x<m and y<n and s[x]==t[y]:
                x=x+1
                y=y+1
            v[k]=x
            if x==m and y==n:
                return D
    


# In[33]:


s="approximate"
t="appropriate"


# In[34]:


edDiagnonalGreedy(s,t)


# In[526]:


def edDiagnonalGreedyhalfmemory(s,t):
    m=len(s)
    n=len(t)
    maxi=m+n
    x=[0 for x in range(2*(maxi+1))]
    v=[[0 for x in range(2*(maxi+1))] for x in range(2*(maxi+1))]
    v[1]=0
    for D in range(0,maxi+1):
        for k in range(-D+2*max(0,D-m),D-2*max(0,D-n)+1,2):
            if k==-D or k!=D and v[k-1]<v[k+1]:
                x = v[k+1]
            else:
                x =v[k-1]+1
            y=x-k
            while x<m and y<n and s[x]==t[y]:
                x=x+1
                y=y+1
            v[k]=x
            if x==m and y==n:
                return D


# In[527]:


s="sunrise"
t="sunshine"


# In[528]:


edDiagnonalGreedyhalfmemory(s,t)


# In[ ]:


### branch and bound A star algo sample

def A*-GRAPH-SEARCH(start):
  Let pq be an empty min priority queue
  Let closed be an empty set
  
  g(start) = 0
  f(start) = h(start)
  path(start) = []
  pq.push(start, f(start))
  
  while not pq.empty():
    top = pq.pop()
    if isGoal(top):
      return f(top), path(top)
    closed.add(top)
    foreach next in succ(top):
      if next not in closed:
        g(next) = g(top) + cost(top, next)
        f(next) = g(next) + h(next)
        path(next) = path(top).append(next)
        pq.push(next, f(next))


# In[155]:


# according to WIKI NW+HIRSCHBURG ALGO, needs to adjust and test

def edDivideandConquer(s,t):
    z=""
    w=""
    m=len(s)
    n=len(t)
    c=[[0 for x in range(n+1)] for x in range(2)]
    if m==0:
        for j in range(1,n+1):
            z=z+'-'
            w=w+t[j]
        
    elif n==0:
        for i in range(1,m+1):
            z=z+s[i]
            w=w+'-'
        
    elif m==1 or n==1:
        for i in range(m):
            for j in range(n):
                if s[i]==t[j]:
                    z=s[i+1]+z
                    w=t[j+1]+w              
                else:
                    if 
                    c[1][j+1]=c[0][j+1]+1: 
                    z=s[i+1]+z
                    w='-'+w
                    elif c[1][j+1]=c[0][j]+1: 
                    z=s[i+1]+z
                    w=t[j+1]+w
                    else:
                    c[1][j+1]=c[1][j]+1  
                    z='-'+z
                    w=t[j+1]+w  
                    
    else:
        for i in range(m):
            for j in range(n):
                smid=math.floor(m/2)
                return edLinearSpace(s[1:smid],t)
        cu=edLinearSpace(s[1:smid],t)
        cd=edSpaceEfficient(s[smid+1:m],t)
        tmid=np.argmin (cu + cd)
        
        (z,w)= edDivideandConquer(s[1:smid],t[1:tmid])+edDivideandConquer(s[smid+1:m],t[tmid+1:n])
    return (z,w)


# In[ ]:


s= "sweet"
t= "sunshine"

