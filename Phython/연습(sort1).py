"""개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.(단 중복없음)"""
number=int(input("받을갯수:"))
number_list=[]
for _ in range(number):
    number_list.append(int(input()))
    
sort_list=set(sorted(number_list)) #다른 변수로 받아서 할때는 sorted 그러나 안받고 바로하려면 
#이렇게 사용number_list.sort()
for i in  sort_list:
    print(i)