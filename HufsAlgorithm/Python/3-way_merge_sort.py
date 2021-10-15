def merge(A, first, m1, m2, last):
    # i <= j and j < k <= l
    # 정렬된 두 부분 A[i..j]와 A[k..l]을 merge하는 함수

    i, j = first, m2
    B, C = [], []

    while i <= m1-1 and j <= last:
        if A[i] >= A[j]:
            B.append(A[j])
            j += 1
        else:
            B.append(A[i])
            i += 1
    print(B)

    for k in range(i, m1):
        B.append(A[k])
    for k in range(j, last+1):
        B.append(A[k])

    print(B)

    i, j = m1, 0

    while i <= m2-1 and j <= len(B)-1:
        if A[i] >= B[j]:
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1

    for k in range(j, len(B)):
        C.append(B[k])
    for k in range(i, m2):
        C.append(A[k])

    for i in range(first, last+1):
        A[i] = C[i - first]


def m_sort(A, first, last):
    if first >= last:
        return  # 바닥 조건
    
    # m1, m2 구하는 부분이 잘못되면 오류가 나는데 아직 그 이유는 잘 모르겠다.
    m1 = first + ((last - first) // 3)
    m2 = first + 2 * ((last - first) // 3) + 1

    m_sort(A, first, m1-1)
    m_sort(A, m1, m2-1)
    m_sort(A, m2, last)

    # 3-way merge sort - merge 함수를 이용해 적절히 합병한다
    merge(A, first, m1, m2, last)


A = [10, 9, 7, 8, 6, 1, 3, 5, 2, 4]
m_sort(A, 0, len(A)-1)
print(A)
