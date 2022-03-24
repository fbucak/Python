import  random
rps=["rock","paper","scissors"]
firstPlayer=input("please insert first player's name")
secondPlayer=input("please insert second player's name")
count = 1
firstPlayerScore=0
secondPlayerScore=0
while count!=11:

    firstPlayerChoice = random.choice(rps)
    secondPlayerChoice=input(firstPlayer+" made choice.Please insert your choice").casefold()
    if firstPlayerChoice=="rock" and secondPlayerChoice=="paper":
         print(firstPlayer+" chosed "+firstPlayerChoice)
         print(secondPlayer+" won "+str(count)+".round .")
         secondPlayerScore+=1
    elif firstPlayerChoice=="rock" and secondPlayerChoice=="scissors":
         print(firstPlayer + " chosed " + firstPlayerChoice)
         print(firstPlayer + " won " + str(count) + ".round .")
         firstPlayerScore += 1
    elif firstPlayerChoice=="paper" and secondPlayerChoice=="rock":
         print(firstPlayer + " chosed " + firstPlayerChoice)
         print(firstPlayer + " won " + str(count) + ".round .")
         firstPlayerScore += 1
    elif firstPlayerChoice=="paper" and secondPlayerChoice=="scissors":
         print(firstPlayer + " chosed " + firstPlayerChoice)
         print(secondPlayer + " won " + str(count) + ".round .")
         secondPlayerScore += 1
    elif firstPlayerChoice=="scissors" and secondPlayerChoice=="paper":
         print(firstPlayer + " chosed " + firstPlayerChoice)
         print(firstPlayer + " won " + str(count) + ".round .")
         firstPlayerScore += 1
    elif firstPlayerChoice == "scissors" and secondPlayerChoice =="rock":
         print(firstPlayer + " chosed " + firstPlayerChoice)
         print(secondPlayer + " won " + str(count) + ".round .")
         secondPlayerScore += 1
    else:
         print(firstPlayer + " chosed " + firstPlayerChoice)
         print(str(count)+".round is draw")
    count = count + 1
if firstPlayerScore>secondPlayerScore:
    print("Score {}:{} {}:{}, {}won!!!".format(firstPlayer,firstPlayerScore,secondPlayer,secondPlayerScore,firstPlayer))
elif firstPlayerScore<secondPlayerScore:
    print("Score {}:{} {}:{}, {}won!!!".format(firstPlayer,firstPlayerScore,secondPlayer,secondPlayerScore,secondPlayer))
else:
    print("The Game is draw."+firstPlayer+":"+str(firstPlayerScore)+"--"+secondPlayer+":"+str(secondPlayerScore))