# n 번째 피보나치 수 구하는 알고리즘

# 조건 1. fibo(0) = 1이며, fibo(1)이다.
# 조건 2. fibo(n)을 계산할 때 리스트나 재귀(recursion)을 쓰면 안되며
# 오로지 while 루프와 새로운 변수 3개 이하로 사용해야 한다.

def fibo(n):
    if n == 0 or n == 1: return 1

    a = 1; b = 1; temp = 0
    i = 2
    while i <= n:
        temp = a + b
        a = b
        b = temp
        i += 1

    return b


# n을 입력받은 후
n = int(input())
# fibo(n) 호출!
res = fibo(n)
# 리턴값을 출력함
print(res)
