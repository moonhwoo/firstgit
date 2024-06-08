#노트에 정리해둠
import numpy as np
input_data=np.array([[3,5],[1,-1],[0,0],[8,4]])
weight=np.array([[2],[7]])
target=np.array([[33],[-5],[0],[31]])
learning_rate=0.001
bias=0  #편향 추가(원점이 아닌 y축을 지남)

def predict(X,W,b):
    return X.dot(W)+b  #예측값에 +b를 함으로써 원점을 안지날수 있게함
#원점을 지나지 않으면 오차 범위가 작아져서 더 정확도가 올라감

def gradient(X,error):
    return 2*X.T.dot(error),np.sum(error) 
#!!이 함수는 두개의 값을 반환함!!
#np.sum(error)는 편향에 대한 기울기
#=>오차벡터 error의 모든 요소를 더한값

def update(W,b,gd,learning_rate):
    W=W-learning_rate*gd[0] 
    b=b-learning_rate*gd[1]
    #gd[0],gd[1]처럼 두개가 나올수 있는 이유는 함수가 두개의 값을 반환해서
    #배열로 저장되어 있기 때문
   
    return W,b

def cost(error):
    return (error**2).mean()
epoch=20

for i in range(epoch):
    pred=predict(input_data,weight,bias)
    error=pred-target
    print(f"cost at epoch {i}:{cost(error[0]):.4f}")
    gd=gradient(input_data,error)
    weight,bias=update(weight,bias,gd,learning_rate)
print('final prediction:',predict(input_data,weight,bias))