#sys모듈 : 파이썬 인터프리터 제어 방법 제공

#os : 운영체제 제어

#string : 기본적인 문자열 연산 제공

#re : string보다 좀 더 전문적으로 문자열을 다룰 수 있는모듈.

#random: 난수 생성
import random

#0~1사이의 난수 생성
print(random.random())

#(a,b) a이상 b미만의 무작위 정수 생성
print(random.randrange(1,7))

#원소를 무작위로 뽑아주는 choice()
menu = "왈","랄","라"
print(random.choice(menu))

#matplotib을 이용해서 하트 그리기
from pylab import *

x = linspace(-1.6, 1.6, 10000)
#linspace함수는 주어진 숫자범위 내에서 동일한 간격으로 떨어진 숫자들을 만들어준다.
f = lambda x: (sqrt(cos(x)) * cos(200 * x) + sqrt(abs(x)) - 0.7) * \
    pow((4 - x * x), 0.01)
#람다 함수를 생성하였고 제곱을 구하였다. sqrt는 제곱근을 cos는 코사인을 구하는 함수로 이는 pylab에서 import하여 사용할 수 있다.
plot(x, list(map(f, x)))
#plot을 생성하여
show()
#화면에 보여준다.