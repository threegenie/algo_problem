import random, timeit

##
## 여기에 세 가지 정렬함수를 위한 코드를...
##

def quick_sort(A, begin, end):
   if begin >= end : return

   global Qs, Qc
   #피봇과 left, right 값의 설정
   #피봇은 일반적으로 mid 값으로 하지만 어떤것으로해도 무관함
   pivot = begin
   left, right = begin + 1, end

   while left<=right:
       #left가 가르키는 값이 피봇보다 크다면 left가 증가
       while left<=end and A[left] <= A[pivot]:
           left+=1
           Qc+=1
       #right가 가르키는 값이 피봇보다 작다면 right가 증가
       while right>begin and A[right] >= A[pivot]:
           right-=1
           Qc+=1

       #left, right가 교차함
       #피봇과 right값의 교체
       if left>right:
           A[pivot], A[right] = A[right], A[pivot]
           Qs+=1
       #그렇지 않다면 left와 right의 교체
       else:
           A[left], A[right] = A[right], A[left]
           Qs+=1

   quick_sort(A, begin, right - 1)
   quick_sort(A, right + 1, end)


def merge_sort(B, begin, end):
    if begin >= end : return

    global Ms, Mc
    #변수 값의 설정
    mid = (begin + end) //2
    temp, left, right = begin, begin, mid +1
    #병합된 데이터를 임시로 받을 리스트 v
    v = []
    
    #두 파트씩 재귀적으로 쪼개기
    merge_sort(B, begin, mid)
    merge_sort(B, mid+1, end)

    while left <= mid and right <= end:
        #left와 right를 비교해서 순차적으로 v에 추가
        if B[left] < B[right]: 
            v.append(B[left])
            left+=1
        else:
            v.append(B[right])
            right+=1
        Mc+=1

    #left에 남은 부분 모두 v에 추가
    while left <= mid :
        v.append(B[left])
        left+=1
        Ms+=1

    #right에 남은 부분 모두 v에 추가
    while right <= end:
        v.append(B[right])
        right+=1
        Ms+=1

    #v의 모든 데이터를 B에 넣어서 교체
    i=begin
    for k in v:
        B[i] = k
        i+=1
        Ms+=1

def heapify(arr, index, heap_size):
    global Hs, Hc

    # 완전이진트리는 배열 하나로 트리 구현가능
    largest = index
    left = index * 2 + 1
    right = index * 2 + 2

    # 왼쪽 자식이 현재 요소보다 크면 인덱스 교체
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
        Hc+=1
    # 오른쪽 자식이 현재 요소보다 크면 인덱스 교체
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
        Hc+=1

    # 교체된적이 있다면 교체된 index와 largest 요소값 교체
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        Hs+=1
        # 변경되었으면 변경된 부분을 중심으로 다시 한번 heapify 실행
        return heapify(arr, largest, heap_size)

def heap_sort(C):
    global Hs, Hc
    n = len(C)

    # 트리의 절반부터 거꾸로 올라가며 heapify
    for i in range(n // 2 - 1, -1, -1):
        heapify(C, i, n)

    # 힙을 정렬하고 가장 큰 값(루트) 를 가장 끝 값으로 이동한 후 힙 생성.
    for i in range(n - 1, 0, -1):
        C[0], C[i] = C[i], C[0]
        heapify(C, 0, i)
        Hs+=1

    

# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
cnt = 0

print("n=", end='')
n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))
print("---------------------------------------------------\n")

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
