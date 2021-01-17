import numpy as np

#배열의 연산

#%%time : 셀 코드의 실행 시간을 측정하는 IPython 매직 명령어

#벡터화 연산을 사용하여 벡터 계산
x = np.arange(1, 10001)
y = np.arange(10001, 20001)

z = x+y
print(z[:10])

#사칙 연산 뿐만 아니라 비교 연산과 같은 논리 연산도 벡터화 연산이 가능하다
a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
print(a==b)
print(a>=b)

#배열의 각 원소들을 일일히 비교하는 것 이 아니라 배열의 모든 원소가 다 같은지 알고싶다면 all 명령을 사용하면 된다.
c = np.array([1,2,3,4])
print(np.all(a==b)) # 모든 원소를 비교하여 같은 원소를 가진 array인지에 대하여 비교한 값을 출력한다. => false
print(np.all(a==c)) # 두 array가 같은 array인지에 대하여 판단한다. => true


#스칼라와 벡터/행렬의 곱셈 : 선형대수에서 사용하는 식과 넘파이 코드가 일치한다.

x=np.arange(10)
print(100*x) # => [ 0 100 200 300 400 500 600 700 800 900]

x = np.arange(12).reshape(3,4)
print(x)
print(100*x)

#브로드캐스팅
#벡터끼리 덧셈 혹은 뺄셈을 하려면 두 벡터의 크기가 같아야 하는데 넘파이에서는 서로 다른 크기를 가진 두 배열의 사칙연산도 지원한다.
#벡터와 스칼라를 더하는 경우 스칼라를 벡터와 같은 크기로 확장시켜서 덧셈을 계산한다.
#브로드 캐스팅은 1차원 외에 더 차원이 높은 경우도 적용된다.
x =np.arange(5)
y=np.ones_like(x)

print("array 동일 여부 판단 :",np.all((x+y) == (x+1)))

#2차원 + 1차원
x = np.vstack([range(7)[i:i+3]] for i in range(5))
print("arrya x 출력 :\n",x)
y=np.arange(5)[:,np.newaxis]
print("array Y 출력:\n",y)

print("x+y 출력 :\n",x+y)

#차원 축소 연산

#최대 /최소 : min, max, argmin, argmax
#통계 : sum, mean, median, std, var
#불린 : all, any

x=np.array([1,2,3,4])
print("np.sum(x) :",np.sum(x),"같은 표현 x.sum() :",x.sum())
print("x.min() :",x.min())
print("x.max()",x.max())
print("최솟값의 위치 == x.argmin() :",x.argmin())
print("최댓값의 위치 == x.argmax() :",x.argmax())
print("평균 :",x.mean())
print("np.median(x) :",np.median())
print("np.all :",np.all([True,True,True]))
print("np.any() :",np.any(True,True,True))

#연산의 대상이 2차원 이상인 경우에는 어느 차원으로 계산을 할지를 axis 인수를 사용하여 지시한다.
#axis =0인 경우는 열연산, axis=1인 셩우는 행연산이다. 디폴트값은 axis=0이다.  axis인수는 대부분의 차원 축소 명령에 적용할 수 있다.
x=np.array([[1,1],[2,2]])
print(x)
print("x.sum() :",x.sum())
print("열 합계 x.sum(axis=0) : ",x.sum(axis=0))
print("행 합계 x.sum(axis=1) : ",x.sum(axis=1))


#정렬
#sort 함수나 메소드를 사용하여 배열 안의 원소를 크기에 따라 정렬하여 새로운 배열을 만들 수도 있다.
#2차워 ㄴ이상인 경우에는 행이나 열을 각각 따로정렬하는데 axis 인수를 사용하여 행을 정렬할 것인지 열을 정렬할것인지 결정한다.
#axis=0이면 각각의 행을 따로 정렬
#axis=1이면 각각의 열을 따로 정렬
#default 값은 -1로 가장 안쪽의 차원을 가리킨다.

a = np.array([[4,  3,  5,  7],
              [1, 12, 11,  9],
              [2, 15,  1, 14]])
print(np.sort(a)) #axis=-1 | axis=1과 동일하다.
print(np.sort(a,axis=0))

#자룔를 정렬하는 것이 아닌 순서만 알고 싶을 경우 argsort명령을 사용한다.
a = np.array([42, 38, 12, 25])
print("argsort",np.argsort(a))
