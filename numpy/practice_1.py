import numpy as np
# 넘파이 패키지를 import하는데 넘파이는 np라는 이름으로 import하는 것이 관례이다.

#1차원 배열 만들기
ar = np.array([0,1,2,3,4,5,6,7,8,9])

#list와 비슷해보이지만 type 명령으로 자료형을 살펴보면 numpy.ndarray임을 알 수 있다.
#print(type(ar)) => <class 'numpy.ndarray'>
# array 객체는 list와 다르게 각각의 원소가 모두 같은 자료형이여야 한다. (list는 자료형 여러개)


# 벡터화 연산 : 배열 객체는 배열의 각 원소에 대한 반복 연산을 하나의 명령어로 처리하느 ㄴ벡터화 연산을 지원한다.
# ex) 여러개의 데이터를 모두 2배 해야하는 경우
data = [0,1,2,3,4,5,6,7,8,9]
x = np.array(data)
print(2*x) #  => data 값이 2배가 되어서 출력됨.

# 일반적인 리스트 객체에 정수를 곱하면 객체의 크기가 정수배 만큼으로 증가한다
#ex) print(data*2) => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#벡터화 연산은 비교 연산과 논리 연산을 포함한 모든 종류의 수학 연산에 대해 적용된다.
a = np.array([1,2,3])
b = np.array([10,20,30])

print(2*a+b)  # => 12 24 36 출력

print(a==2) # => f t f 출력
print(b>10) #=> f t t 출력


#2차원 배열 만들기
#ndarray는 n-diensional Array의 약자.
c = np.array(([0,1,2], [3,4,5])) #=> 2x3 array

#2차원 배열의 행의 개수 구하기 : len(arrayname)
print("행의 개수 :",len(c))

#2차원 배열의 열의 개수 구하기 : len(arrayName[0])
print("열의 개수 :",len(c[0]))

#practice_1
p_array_1 = np.array(([10,20,30,40],[50,60,70,80])) # 괄호 두개있어야 함.
print(p_array_1)


#3차원 배열 만들기
d = np.array([[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]],
              [[11, 12, 13, 14],[15, 16, 17, 18],[19, 20, 21, 22]]])
# 위의 배열은 2x3x4배열이다. 이는 높이x행x열 을 나타낸다.
# 깊이 => len(d) / 행 => len(d[0]) / 열 =>len(d[0][0])

#배열의 차원과 크기 알아내기
# 차원 : ndim / 크기 : shape
print(d.ndim) # =>3
print(d.shape) # => (2,3,4,)

#배열의 슬라이싱
arr = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])

print(arr[0,:]) # 첫번째 행 전체 => array([0, 1, 2, 3]
print(arr[:,1]) #두 번째 열 전체 => array([1, 5])
print(arr[1,1:]) #두번째 행의 두번째 열부터 끝까지 => array([5, 6, 7])
print(arr[:2,:2]) # =>array([[0, 1],[4, 5]])


#Practce_2
m = np.array([[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14]])
print("연습문제_1 :",m[1,2])
print("연습문제_2 :",m[2,4])
print("연습문제_3 :",m[1,1:3])
print("연습문제_4 :",m[1:,2])
print("연습문제_5 :",m[0:2,3:5])


#배열 인덱싱

#주어진 배열에서 짝수를 찾아낼거임.
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
idx = np.array([True, False, True, False, True, False, True, False, True, False])
# print(a[idx]) => 이렇게 해도 되는데
print(a[a%2==0]) #=> 이렇게 해도 작동이 된다.

arr_1 = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 2, 4, 6, 8])
print(arr_1[idx]) #[11 33 55 77 99]
idx_2 = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
print(arr_1[idx_2]) #[11 11 11 11 11 11 22 22 22 22 22 33 33 33 33 33]

#practice_3
p_array_3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

print("연습문제_3_1 :",p_array_3[p_array_3%3==0])
print("연습문제_3_2 :",p_array_3[(p_array_3%4==1)])
print("연습문제_3_3 :",p_array_3[(p_array_3%3==0)& (p_array_3%4==1)] )