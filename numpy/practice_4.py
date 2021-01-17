import numpy as np

#기술 통계

x = np.array([18,   5,  10,  23,  19,  -8,  10,   0,   0,   5,   2,  15,   8,
              2,   5,   4,  15,  -1,   4,  -7, -24,   7,   9,  -6,  23, -13])

#데이터의 개수 : len
print(len(x))

#표본 평균 : np.mean(arrayName)
print("표본 평균 :",np.mean(x))

#표본 분산 : np.var(arrayName)
print("표본 분산 :",np.var(x))

#표본 표준편차 : 분산의 양의제곱근 값 : np.std(x)
print("표본 표준편차 :",np.std(x))

#최댓값과 최솟값 :np.max(x) , np.min(x)
print("최댓값 :",np.max(x))
print("최솟값 :",np.min(x))

#중앙값 : 데이터를 크기대로 정렬하였을 때 가장 가운데에 있는 수. : np.median(x)
# 데이터의 수가 짝수일 경우 가장 가운데에 있는 두 수의 평균을 사용한다.
print("중앙값 :",np.median(x))

#사분위수 : 1/4 , 2/4 , 3/4, 1

print("최소값 :",np.percentile(x,0))
print("1 사분위수 :",np.percentile(x,25))
print("2 사분위수 :",np.percentile(x,50))
print("3 사분위수 :",np.percentile(x,75))
print("4 사분위수 :",np.percentile(x,100))
