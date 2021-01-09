year = int(input("년도 입력:"))
if(year%4==0):
    if(year%100):
        if(year%400):
            print("윤년입니다.")
        else:
            print("평년입니다.")
    else:
        print("윤년입니다.")
else:
    print("평년입니다.")