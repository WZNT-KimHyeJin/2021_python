def sumOfDigit(num):
    numList =map(int,list(str(num)))
    return sum(numList)
if __name__=='__main__':
    print(sumOfDigit(6666))