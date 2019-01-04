#create quiz
quiz = {
    "question": " If x = 8, then what is the value of 4(x + 3)? " ,
    "answer" : [35 , 36 , 40 , 44 , ] ,
    "correct": 44 ,
}

while True :
    print(quiz["question"])
    #print answer
    for index,item in enumerate(quiz["answer"]):
        print(index+1,item,sep=". ")
    guest = int(input("you choice :"))-1
    #check condition
    if quiz["answer"][guest] == quiz["correct"]:
        print("bingo")
        break
    else :
        print(":(")