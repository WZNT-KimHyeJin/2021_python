import  numpy as np

#넘파이 자료형


# array 명령으로 배열을 만들 때 자료형을 명시적으로 적용하려면 dtype 인수를 사용한다.
# 만약 dtype 인수가 없으면 주어진 데이터를 저장할 수 있는 자료형을 스스로 유추한다.
# 만들어진 배열의 자료형을 알아내려면 dtype 속성을 보면 된다.

x = np.array([1,2,3])
print(x.dtype) # => int32

y = np.array(([1.0,2.0,3.0]))
print(y.dtype) # => float64

# 타입 변경
z = np.array([1, 2, 3], dtype='f') #=> float으로 자료형 변경


#INF와 NAN / np.inf == infinite , np.nan == not a number

#배열 생성_1 모든 원소가 0일 배열
a = np.zeros(5) # => 0 0 0 0 0
b = np.zeros(((2,3))) # 2차원 배열
c = np.zeros((5, 2), dtype="i") # 인수를 명시하여 해당 자료형을 가지는 배열을 생성

#배열 생성_2 모든 원소가 1인 배열
e = np.ones((2, 3, 4))

# 배열의 크기를 튜플로 명시하지 않고 다른 배열과 같은 크기의 배열을 생성하고자 할때
# ones_like, zeros_like
f = np.ones_like(b, dtype="f")

#배열 생성_3 값이 비어있는 배열
g = np.empty((4,3))

#배열 생성_4 특정한 규칙에 따라 증가하는 수열 : arrange
print("수열 :",np.arange(10)) # 0부터 1씩 증가
# print("수열 :",np.arange((3,21,2))) #시작 값, 끝값(미만), 뛰어넘을 단계
# => array([ 3,  5,  7,  9, 11, 13, 15, 17, 19])

#배열 생성_5 선형구간 혹은 로그 구간을 지정한 구간의 수만큼 분할 : linspace, logspace
np.linspace(0,100,5) #시작 ,끝(이하), 갯수 => array([  0.,  25.,  50.,  75., 100.])
np.logspace(0.1, 1, 10)


# 전치연산
#2차원 배열의 전치 연산은 행과 열을 바꾸는 작업이다. : 배열의 T속성으로 구할 수 있음.
# 메소드가 아니라 T 속성임 소 크 성

A = np.array([[1, 2, 3], [4, 5, 6]])
print("변경 전 :\n",A)
print("변경 후 :\n",A.T)


#배열의 크기 변형
B = np.arange(12)
print(B.reshape(3,4)) # array B의 모양을 3x4 형식의 이차원 배열로 변경
# 사용하는 원소의 개수가 정해져 있기 때문에 reshape의 원소 중 하나는 -1이라는 수로 대체가능 하다. 이는 자동적으로 계산된다.
print("\n")
print(B.reshape(2,2,-1))
print("\n")
print(B.reshape(3,-1))

#다차원 배열을 1차원으로 만들기위해서는 flatten이나 ravel 메소드를 사용한다.
print(B.flatten())
print(B.ravel())

#배열 연결 : 행의 수나 열의 수가 같은 두개 이상의 배열을 연결하여 더 큰 배열을 만들 때 사용

#hstack : 행의 수가 같은 두개 이상으 ㅣ배열을 옆으로 연결하여 열의 수가 더 많은 배열을 생성
a1 = np.ones((2,3))
a2 = np.zeros((2,2))

print(np.hstack([a1,a2]))
#[ [1. 1. 1. 0. 0.]
#  [1. 1. 1. 0. 0.] ]

#dstack : 행이나 열이 아닌 깊이 방향으로 배열을 합친다. 가장 안쪽의 원소의 차원이 증가함.

c1 =np.ones((3,4))
c2 = np.zeros((3,4))
print(np.dstack([c1,c2]))
print()
print((np.dstack([c1,c2])).shape) #=> (3,4,2)

np.dstack([c1,c2])

#stack : dstack의 기능을 확장한 것으로 dstack 처럼 마지막 차원으로 연결하는 것이 아니라 사용자가 지정한 차원으로 배열을 연결한다.
# axis인수를 사용하여 연결 후의 회전 방향을 정한다. 디폴트 값은 0이다.
C = np.stack([c1,c2])
print("stack")
print(C)
print(C.shape)

#axis 인수가 1이면 두번째 차원으로 새로운 차원이 삽입된다.
C = np.stack([c1, c2], axis=1)
print(C)
# (3x4) -> (3x2x4)

#indexer : 특수메소드
#r_ : hstack 명령과 비슷하게 배열을 좌우로 연결한다.
# 다만 메소드임에도 불구하고 소괄호를 사용하지 않고 인덱싱과 같이 대괄호를 사용한다.
print(np.r_[np.array([1, 2, 3]), np.array([4, 5, 6])])
#c_ : 배열의 차원을 증가시킨 후 좌우로 연결한다. 1차원 배열 연결 시 2차원 배열이 된다.
print(np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])

#title : 동일한 배열을 반복하여 연결한다.
a = np.array([[0, 1, 2], [3, 4, 5]])
print(np.tile(a, (3, 2)))