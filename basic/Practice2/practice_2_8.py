userInput = str(input())
freezing_p,boiling_p = userInput.split()
while True:
    machineInput = int(input())
    if(machineInput>=int(freezing_p) and machineInput<=int(boiling_p)):
        print("Nothing to report")
    elif(machineInput==-999):
        print("stop Operating")
        break
    else:
        print("ALERT!")
        break