# 거듭제곱 연산 (a^b)

# (2진법)
# 1101 / 2 = 110 ... 1
# 110 / 2 = 11 ... 0
# 11 / 2 = 1 ... 1
# 1 / 2 = 0 ... 1

# a^13 = a * a^4 * a^8

def pow_custom(a, b):
    ret = 1
    while b:
        if b % 2 == 1: ret *= a
        a = a*a
        b //= 2
    return ret

a, b = map(int, input().split())
result = pow_custom(a, b)
print(result)



# 거듭제곱 후 나머지 계산 (a^b % mod)

# 비효율적인 방법 - 거듭제곱 다 계산한 후 그 값에 mod 계산
# (큰 수의 연산 -> 연산량 많음) 
def pow_custom(a, b, mod)
    ret = 1 
    while b:
        if b % 2 == 1: ret *= a
        a *= a
        b //= 2
    return ret % mod

# 효율적인 방법 - 연산을 할 때마다 mod 계산
def pow_custom(a, b, mod):
    ret = 1
    while b:
        if b % 2 == 1: ret = ret * a % mod
        a = a * a % mod
        b //= 2
    return ret

a, b, mod = map(int, input().split())
result = pow_custom(a, b, mod)
print(result)
