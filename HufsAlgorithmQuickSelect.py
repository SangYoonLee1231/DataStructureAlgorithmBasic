# 퀵 정렬 알고리즘
# (n개의 리스트 중 k번째로 작은 값을 구하는 코드)

def QuickSelect(L, k):
    A, B, M = [], [], []
    p = L[0]

    for i in L:
        if i < p: A.append(i)
        elif i > p: B.append(i)
        else: M.append(i)

    if len(A) >= k: return QuickSelect(A, k)
    elif len(A) + len(M) < k: return QuickSelect(B, k - len(A) - len(M))
    else: return p


n, k = map(int, input().split())
L = list(map(int, input().split()))

ans = QuickSelect(L, k)
print(ans)
