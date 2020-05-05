import time, random

def prefixSum1(X, n):
	# code for prefixSum1
    for i in range(n):
        S = 0
        for j in range(i+1):
            S += X[j]
	
def prefixSum2(X, n):
	# code for prefixSum2
    S = X[0]
    for i in range(1, n):
        S += X[i]
	
random.seed()		# random 함수 초기화

n = int(input()) # n 입력받음
X = [random.randint(-999, 999) for _ in range(n)] 
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움

before = time.clock()
prefixSum1(X, n) # prefixSum1 호출
after = time.clock()
print('prefixSum1이 수행된 시간 : %f 초' % (after-before)) # 수행시간 출력

before = time.clock()
prefixSum2(X, n) # prefixSum1 호출
after = time.clock()
print('prefixSum2이 수행된 시간 : %f 초' % (after-before)) # 수행시간 출력


#수행시간 비교
runtime = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

for i in runtime: 
	X = [random.randint(-999, 999) for _ in range(i)]
	
	before = time.clock()
	prefixSum1(X, i)
	after = time.clock()
	run1 = after - before
	
	before = time.clock()
	prefixSum2(X, i)
	after = time.clock()
	run2 = after - before
	print("n이 %s일 때 O(n^2)의 수행시간은 O(n)의 수행시간의 %s배" %(i, run1/run2))
