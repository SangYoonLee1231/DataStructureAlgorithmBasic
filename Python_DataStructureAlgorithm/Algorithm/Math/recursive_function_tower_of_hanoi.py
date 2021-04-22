# 하노이의 탑 - 판을 옮기는 모든 과정을 출력

# F(N) = F(N+1) + 1 + F(N+1)
# F(N) = 2**N - 1

def hanoi(st, ed, sz):
    # 판의 개수가 1일 때
    if sz == 1: return print(st, ed)

    hanoi(st, 6-st-ed, sz-1) # F(N+1)
    print(st, ed) # 1
    hanoi(6-st-ed, ed, sz-1) # F(N+1)

n = int(input()) # 판의 개수 n의 값 입력
print(2**n-1) # 총 판 이동 횟수 = 2^n-1
hanoi(1, 3, n) # hanoi 함수 호출