
# coding: utf-8

# In[77]:


import numpy as np
from numpy import exp,array,random,dot

        
class Operation():
    def __init__():
        return
        
    
    def Affine_Forward(A,W,b):
    
        Z= np.dot(A, W) + b
        cache=(A,W,b)
        return cache,Z
    

    
    def Affine_Backward(dZ,cache):
    
        A,W,b=cache
        dA=dot(dZ,W.T) 
        dW=dot(A.T,dZ)
        db=dot(Z.T,np.ones(dZ.shape[0]))
        return dA,dW,db

    
    
    def ReLU_Forward(Z):
        A=np.maxium(0,Z)
        cache=Z
        return A,cache




    def ReLU_Backward(dA,cache):
        Grad_Z=np.array(dA,copy=True)
        Grad_Z[cache<=0]=0
        return Grad_Z


    def softmax(F):
        exps=np.exp(F)
        return exps/np.sum(exps)

    def Cross_Entropy(F,y):
        m=y.shape[0]
    
        Loss=-np.sum(F-log_likelihood)/m
        dF=None
    
        p=softmax(F)
        
        return Loss,dF
    
        

        
        
 
        
        
        







