# Selection + Heap (힙 + 선택 알고리즘) - (학교 과제)
# 배열 A애서 k번째로 작은 값 출력

import heapq

def heapify_down(A, k, n):
    while 2*k+1 < n:
        L, R = 2*k+1, 2*k+2
        if A[L] < A[k] and L < n:
            min = L
        else:
            min = k
        if A[R] < A[min] and R < n:
            min = R

        if min != k:
            A[k], A[min] = A[min], A[k]
            k = min
        else: break



def solve(A, k):
    n = len(A)
    heapq.heapify(A)

    print(A)

    for i in range(n-1, n-k-1, -1):
        A[0], A[n-1] = A[n-1], A[0]
        n = n - 1
        heapify_down(A, 0, n)

    print(A)

    n = len(A)

    return A[n-k]
    '''
    for i in range(k):
		min = heapq.heappop(A)
	return min
    '''


k = int(input())
A = [int(x) for x in input().split()]
heapq.heapify(A)
print(solve(A, k))


# 1. 알고리즘 설명

# 입력받은 리스트 A를 heapify함수를 통해 min힙으로 만든 후,
# min힙 성질 중 'root node엔 리스트의 최솟값이 온다'는 성질을 통해
# root node에 해당하는 리스트 요소와 마지막 요소를 바꾸는 과정을 k번 반복한다. (k번째로 작은 수만 찾으면 되므로)

# 이 떼 바꾸고 나면은 힙 성질이 깨지게 되므로, heapify_down함수를 통해 root node에 있는 값을 제 위치로 보내주어야 한다.
# 또한, heapify_down 함수의 한 사이클을 마치면, 마지막 요소는 다음 사이클 때 제외해주어야 한다. (line 25 : n = n - 1)

# 사이클을 모두 마치면, 리스트 A는 마지막 요소부터 n-k번째 요소까지 뒤에서부터 작은 숫자대로 정렬된다.
# 이때, 이 A 리스트에서 n-k번째 요소가 k번째로 작은 값이므로 이 값을 리턴하여 출력한다.



# 2. 수행시간 분석
# (1) heapify_down함수 수행 시간: logn + c = O(logn)

# (2) 알고리즘 수핸 시간: T(n) = klogn + c = O(nlogn)



# 3. 알고리즘의 장단점

# - 장점 : Sort, Quick, Mom 알고리즘과 달리 추가적인 메모리가 필요하지 않는다.
# - 단점 : O(nlogn)시간이 필요하며, 데이터의 정렬 상태에 수행 시간이 영향을 받는 불안정(unstable)한 알고리즘이다.
