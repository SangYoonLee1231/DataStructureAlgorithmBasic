# 최대 공약수 (GCD)

# 비효율적인 방법1
def gcd(a, b):
    ret = 0
    for i in range(min(a, b)):
        if a % i == 0 and b % i == 0:
            ret = i
    return ret

# 비효율적인 방법2 (1보다 간단)
def gcd(a, b):
    ret = 0
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            ret = i
    return i

# 유클리드 호제법 알고리즘 이용한 방법
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a%b)


# 최소 공배수 (LCM)
# LCM(A,B) = AB / GCD(A,B)
def lcm(a, b):
    return int(a * b / gcd(a, b))

a, b = map(int, input().split())
gcd_val = gcd(a, b)
lcm_val = lcm(a, b)
print(gcd_val, lcm_val)