# 문자열로 된 N진법 수를 정수형 10진수로 변환하는 함수

# 방법 1
def stoi(s, n):
    ret = 0 # ret는 리턴 값
    l = len(s)
    for i in range(l): ret += int(s[i]) * n ** (l-1-i)
    return ret

# 방법 2 (추천)
def stoi(s, n):
    ret = 0
    for i in s: ret = int(i) + ret * n

s = input()
n = int(input())
i = stoi(s, n)
print(i)