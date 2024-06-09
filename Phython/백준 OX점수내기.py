number=int(input("받을 갯수 입력:"))#받을 배열의 갯수
a=[]
for i in range(number):
    t = input() #OX문자열 받는 것
    cnt = 0  #점수
    result = 0 #점수 총합   
    for i in range(len(t)) :
        if t[i] == "O" :
            cnt += 1
            result += cnt
        elif t[i] == "X" :
            cnt = 0
    a.append(result)

for p in range(len(a)):
    print(a[p])




