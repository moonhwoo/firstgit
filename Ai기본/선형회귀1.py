#노트에 정리해둠
import numpy as np
input_data=np.array([[3,5],[1,-1],[0,0],[8,4]]) #데이터 행렬 =>x
weight=np.array([[2],[7]])  #가중치 행렬    =>w
target=np.array([[33],[-5],[0],[31]])  #목표값
learning_rate=0.001  #러닝레이트

def predict(X,W):   #예측값구하는 함수
    return X.dot(W) #데이터 행렬과 가중치 행렬 을 곱함

def gradient(X,error):   #기울기 함수   
    return 2*X.T.dot(error)  #y=x^2을 미분하면 y'=2x처럼 앞에 2* 가 나오고 X.T는 행렬곱을 할수 없을때 전치하는 기능

def update(W,gd,learning_rate): #여기서gd는 구해진 기울기 
    W=W-learning_rate*gd #새로운 가중치=기존 가중치-러닝레이트*기울기
    return W

def cost(error): #오차를 받아 비용(cost)를 계산
    return (error**2).mean() #비용함수=평균 제곱오차(mse)
#오차**2 .mean() mean()이 평균을 구하게함 즉 오차제곱의 평균을 구해줌
epoch=20 

for i in range(epoch):
    pred=predict(input_data,weight) #예측값을 구하기위해 함수에 넣음
    error=pred-target  #오차값=예측값-목표값
    print(f"cost at epoch {i}:{cost(error[0]):.4f}")
    gd=gradient(input_data,error) #기울기 구하기
    weight=update(weight,gd,learning_rate) #가중치 구하기
print('final prediction:',predict(input_data,weight))