# 하노이의 탑 - 판을 옮기는 모든 과정을 출력

def hanoi(st, ed, sz):
    if sz == 1: return print(st, ed)
    hanoi(st, 6-st-ed, sz-1)
    print(st, ed)
    hanoi(6-st-ed, ed, sz-1)

n = int(input())
print(2**n-1) # 총 판 이동 횟수 = 2^n-1
hanoi(1, 3, n)