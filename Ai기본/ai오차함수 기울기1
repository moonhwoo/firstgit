#y=x^2(오차함수) 을 미분하는것  y'=2x  (x는error)
input_data=3#입력
weight=2#가중치
target=10#목표값
learning_rate=0.01
pred=weight*input_data  #pred(예상)=입력*가중치
error=pred-target  #오차=예상-목표값 -->하지만 나중에 어차피 제곱하기 때문에 순서 바뀌어도 상관없음!!
print("original error",error)
slope=2*error*input_data#slope=기울기
print("slope",slope)

new_weight=weight-learning_rate*slope
print("new weight",new_weight)

new_pred=new_weight*input_data
print("new prediction",new_pred)

new_error=new_pred-target
print("new error",new_error)