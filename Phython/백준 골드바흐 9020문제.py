def is_prime(n):
    if n<=1:
        return False
    for i in range (2,int(n**0.5)+1): #사이의 모든 소수이면TRUE
        if n%i==0:
            return False
    return True
        
    
def find_prime_pair(n):
    primes=[i for i in range(2,n) if is_prime(i)]
    pairs=[]
    for i in primes:   
        if is_prime(n-i) and i<=n-i: #이미 i가 소수이기때문에 
            #n-i도 소수이고 중복을 없애기 위해 i<=n-i를씀
            pairs.append((i,n-i))
    return pairs
            
        
def goldbahh(n): #약수 중 차이 적은것을 구하는 함수
    pairs = find_prime_pair(n)
    if not pairs:
        return None
    result = pairs[0]
    min_diff = abs(result[1] - result[0])
    for pair in pairs:
        diff = abs(pair[1] - pair[0])
        if diff < min_diff:
            result = pair
            min_diff = diff
    return result

number=int(input("받을갯수:"))
a=[]
for i in range (number):
    n=int(input())
    a.append(goldbahh(n))
for i in a:
    print(i[0],i[1])