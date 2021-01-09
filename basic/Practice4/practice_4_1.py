characters = []
sentence = 'Be happy!'
for char in sentence:
    characters.append(char)
print(characters)

# 위의 과정과 동일한 역할을 하는 함수
print(list(sentence))

# str(int) => 정수형 문자열 변경 함수

#list의 합
ont_to_ten = list(range(1,11))
print(sum(ont_to_ten))

#############################################
def sumOfDigits(num):
    sum=0
    for i in list(num):
        sum+=int(i)
    return sum

userInput = input("수를 입력하시오")
print(sumOfDigits(userInput))
