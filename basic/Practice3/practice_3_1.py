maxnum=9
def mult(num):
    org=num+1
    for i in range(maxnum):
        multi =i+1
        print(f'{org} * {multi} = {org*multi}')

for i in range(maxnum):
    mult(i)