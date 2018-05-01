
# coding: utf-8

# In[28]:


from Operations import *
from numpy import random


class Three_NETWORK():
    def __init__():
        batch_size=100
        W_array=[]
        b_array=[]
        return
    
    def Three_NETWORK(X,W_array,b_array,y,test,learning_rate):
        Z1,acache1=Affine_Forward(A,W_array[0],b_array[0])
        A1,rcache1=ReLU_Forward(Z1)
        Z2,acache2=Affine_Forward(A1,W_array[1],b_array[1])
        A2,rcache3=ReLU_Forward(Z2,W_array[1],b_array[1])
        F,acache3=Affine_Forward(A2,W_array[2],b_array[2])
        if test== true:
            #need update
            classifications=0
            return classification
        loss,dF=cross_entropy(F,y)
        dA2,dW2,db3=Affine_Backward(dZ2,acache2)
        dZ1=ReLU_Backward(dA1,rcache1)
        dX,dW1,db1=Affine_Backward(dZ1,acache1)
        W_array[0]-=learning_rate*dW1
        W_array[1]-=learning_rate*dW2
        W_array[2]-=learning_rate*dW3
    
        return loss


    def MinibatchGD(data,num_epoch):
        random.seed(1)
        W_array[0]=random.random((5,100))
        W_array[1]=random.random((5,100))
        W_array[2]=random.random((5,100))
        b_array[0]=np.zeros(batch_size).T
        b_array[1]=np.zeros(batch_size).T
        b_array[2]=np.zeros(batch_size).T
        for epoch in range(num_epoch):
            shuffle(data)
            for i in range(10000/batch_size):
                #X has features and y has targets
                X,y=data[i*batch_size:i*(batch_size+batch_size),0:5],(data[i*batch_size:i*(batch_size+batch_size),5]).T
                loss=Three_NETWORK(X,W_array,b_array,y,test)
    


# In[23]:




