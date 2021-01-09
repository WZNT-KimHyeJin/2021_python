class StrayKids:
    birthday=''
    def sing(self):
        return print("탐험을 떠나갈거야 right now")
    def bd(self,newBirthday):
        self.birthday=newBirthday
LeeKnow = StrayKids()
LeeKnow.sing()
LeeKnow.bd('19981025')
print(LeeKnow.birthday)