L=list(range(2,30))
num=len(L)
for i in L:
    for j in L:
        if(i!=j and j%i==0):
            L.remove(j)
print(L)