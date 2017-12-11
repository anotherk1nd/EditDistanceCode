
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn.cross_validation import train_test_split


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
     return M[len(x)][len(y)]


 def most_common(lst):
    return max(set(lst), key=lst.count)

def KNN(x,X,y,k):
    x_c=[] 
    for j in range(len(x)):
        order=[]# list of (distance, index) 
        for i in range(len(X)):
            edist=edDynamic(x[j],X[i])
            order.append((edist,i))
        order.sort()
        klass=[]
        for element in order[:k]:
            index = element[1]
            klass.append(y[index])
        x_class=most_common(klass)
        x_c.append(x_class)
    return x_c

def getAccuracy(y_test, y_predict):
    correct_sum = 0
    for i in range(len(y_test)):
        if y_test[i] == y_predict[i]:
            correct_sum += 1
    accuracy=correct_sum/float(len(y_test)) * 100.0
    return accuracy


X_train, X_cv, y_train, y_cv = train_test_split(X, y, test_size=0.33, random_state=42)

def getBestk(X_train, X_cv, y_train, y_cv):   # cv:cross-validation
    acc=[]
    for k in range(1,11):
        print("progress=",k*100/10,"%")
        y_predict=KNN(X_cv,X_train,y_train,k)
        accuracy=getAccuracy(y_cv,y_predict)
        acc.append((k,accuracy))
    return acc



#k = np.arange(1,11,1)
#acc = [94,88,76,76,76,76,73,73,73,64]
#plt.plot(k, acc)
#plt.xlabel('number of k')
#plt.ylabel('accuracy(%)')
#plt.title('Find the optimal k')
#plt.grid(True)
#plt.savefig("test.png")
#plt.show()
