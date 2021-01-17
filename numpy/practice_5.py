import numpy as np

#난수 발생과 카운팅

#시드 설정하기
#파이썬에서 시드를 설정하는 함수는 seed이다. 인수로는 0과 같거나 큰 정수를 넣어준다.
np.random.seed(0)

#rand 함수는 0과 1 사이의 난수를 발생시키는 함수로 인수로 받은 횟수만큼 난수를 발생시킨다.
print(np.random.rand(5))

#데이터의 순서 바꾸기 : 데이터의 순서를 바꾸려면 shuffle 함수를 사용한다.
#shuffle 함수도 자체 변환 함수로 한 번 사용하면 변수의 값이 바뀌므로 사용에 주의해야 한다.
x=np.arange(10)
print("변경 전 :",x)
np.random.shuffle(x) # 변수 위치 변경
print("변경 후 :",x)

#데이터 샘플링 : 이미 있는 데이터의 집합에서 일부를 무작위로 선택하는 것. == 표본 선택 == 샘플링
#choice 함수 사용.
#numpy.random.choice(a,size=None, replace=True,p=None)
# a : 배열이라면 원래의 데이터, 정수이면 arange(a)명렬으로 데이터를 생성
#size : 정수. 샘플 숫자
#replace : 불린, True일 경우 한번 선택한 데이터를 다시 선택 가능
#p : 배열. 각 데이터가 선택될 수 있는 확률

print("replace = False :",np.random.choice(5,5,replace=False)) #shuffle 명령과 같음.
print("3개만 선택 :",np.random.choice(5,3,replace=False))
print("반복해서 10개 선택 :",np.random.choice(5,10))
print("선택 확률을 다르게 해서 10개 선택 :",np.random.choice(5,10,p=[0.1,0,0.3,0.6,0]))

#난수 생성
#rand :0부터 1사이의 균일 분포
#randn : 표준 정규 분포
#randint : 균일분포의 정수 난수

#난수 설정 2차원 배열
print(np.random.rand(3,5)) #3x5의 행렬 생성

#randn 함수는 기댓값이 0이교 표준편차가 1인 표준 정규분포를 따르는 난수를 생성
print(np.random.randn(10))
#2차원 배열
print(np.random.randn(3,5))

#randint : 인수 => numpy.random.randint(low, high=none, size=None)
#high를 입력하지 않으면 0과 low 사이의 수를, high를 입력하면 low와 hihg의 수를 출력한다. size는 난수의 개수이다.
np.random.randint(10,size=10)
np.random.randint(10,20,size=10)
np.random.randint(10,20,size=(3,5))