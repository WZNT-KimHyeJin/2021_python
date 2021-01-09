def sumOfDigits(num):
    if num>0:
        temp = num%10
        return temp+sumOfDigits(num//10)
    else:
        return num

userInput = int(input("수를 입력하시오:"))
print(sumOfDigits(userInput))
