# pickle

users = {'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
f = open('users.txt', 'w')
import pickle
pickle.dump(users, f)
#users라는 리스트의 내용을 파일 f에 쏙아붓는 역할./ 모양이 좀 지저분함
#?? 안담기는데 ㅇㅅㅇ??
f.close()

#원래대로 되돌리기(이전 모습이 어떤지는 모르겠지만)
f = open('users.txt')
a = pickle.load(f)
print(a)


#glob : 파일들의 리스트를 뽑을 때 사용함.
from glob import glob
glob('*.exe')               # 현재 디렉터리의 .exe 파일
glob('*.txt')               # 현재 디렉터리의 .txt 파일

#glob() 함수는 인자로 받은 패턴과 이름이 일치하는 모든 파일과 디렉토리의 리스트를 반환 *=> 모든 파일과 디렉토리



