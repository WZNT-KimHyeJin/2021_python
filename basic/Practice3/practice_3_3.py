#람다 사용 방법
print((lambda x,y:x+y)(10,20))

# map()
print(list(map(lambda x:x**2, range(5))))

# reduce() // reduce(함수, 순서형 자료)
from functools import reduce
print(reduce(lambda x,y: (x+1)*y,range(5)))
print(reduce(lambda x, y: x+y, 'abcde'))
# 문자열 자체를 배열로인식하나봉가

#filter // filter(함수, 리스트)
print(list(filter(lambda x: x%3, range(10))))