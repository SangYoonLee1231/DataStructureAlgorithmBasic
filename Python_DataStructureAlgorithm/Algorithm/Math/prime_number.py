# 소수 판별법

# 비효율적인 방법
def isPrime(N):
    if N == 1: return False
    if N == 2: return True
    for i in range(2, N):
        if N % i == 0: return False
    return True

# 효율적인 방법
def isPrime(N):
    if N == 1: return False
    if N == 2: return True
    i = 2
    while i*i <= N:
        if N % i == 0: return False
        i += 1
    return True

n = int(input())
answer = isPrime(n)
print(answer)



# 에라토스테네스의 체
# 1 ~ N까지의 소수를 찾는 방법 -> (1, 2 제외) sqrt(N)까지 수들의 배수를 지워나가는 방식
def era(N):
    