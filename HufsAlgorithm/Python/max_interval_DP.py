# 최대 구간 합 계산 알고리즘 - Dynamic Programming(동적 계획법)으로 구현

# Q. 리스트 내 정수 값을 (index 순으로) 연속적으로 더하여 그 합이 최대가 되는 구간의 값 구하기

def max_interval_DP(A):
    S = [0] * len(A)
    S[0] = A[0]

    for k in range(1, n):
        S[k] = max(S[k-1] + A[k] , A[k])

    return max(S)


n = int(input())
A = list(map(int, input().split()))

print(max_interval_DP(A))
