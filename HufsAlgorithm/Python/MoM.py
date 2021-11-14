# Median of Medians 알고리즘

def find_median_five(A):
    #L의 다섯 개 이하의 값 중에서 중간값을 찾아 리턴하는 코드
    #파이썬의 man,min 함수 사용해도 됨 (단, sort 등 정렬하면 안됨)
	max = A[0]
	max_idx = 0

	n = len(A)
	mid_idx =  // 2

	for _ in range(mid_idx + 1):
		for i in range(n):
			if max < A[i]:
				max = A[i]
				max_idx = i
		A[max_idx], A[n-1] = A[n-1], A[max_idx]
		n = n-1

	return A[max_idx]
    
    #A.sort()
    #return A[len(A)//2]
    

def MoM(A, k): # L의 값 중에서 k번째로 작은 수 리턴
    if len(A) == 1: # no more recursion
	    return A[0]
    i = 0
    S, M, L, medians = [], [], [], []
    while i+4 < len(A):
        medians.append(find_median_five(A[i: i+5]))
        i = i + 5
		
    if i < len(A) and i+4 >= len(A): # 마지막 그룹으로 5개 미만의 값으로 구성
        medians.append(find_median_five(A[i:]))

    mom = MoM(medians, len(medians)//2 + 1)
    for v in A:
        if v < mom:
            S.append(v)
        elif v > mom:
            L.append(v)
        else:
            M.append(v)

    if k <= len(S) : return MoM(S, k)
    elif k > len(S) + len(M): return MoM(L, k-len(S)-len(M))
    else: return mom

# n과 k를 입력의 첫 줄에서 읽어들인다
n, k = map(int, input().split())
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
L = list(map(int, input().split()))
print(MoM(L, k))
