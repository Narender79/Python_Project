import random
game=["rock","paper","scissors"]
count=0
comp=0
while(True):
    pick=input("Enter what u want from rock,paper,scissors: ")
    sys=random.choice(game)
    if pick==sys:
        print("It's a draw")
    elif pick=="rock" and sys=="scissors":
        print("YOU win this round")
        count+=1
    elif pick=="paper" and sys=="rock":
        count+=1
        print("YOU win this round")
    elif pick=="scissors" and sys=="paper":
        count+=1
        print("YOU win this round")
    elif pick=="scissors" and sys=="rock":
        comp+=1
        print("Computer win this round")
    elif pick=="rock" and sys=="paper":
        comp+=1
        print("Computer win this round")
    elif pick=="paper" and sys=="scissors":
        comp+=1
        print("Computer win this round")
    print("Your Score: ",count)
    print("Computer Score: ",comp)
    if comp==10:
        print("Computer Win!!!")
        break
    elif count==10:
        print("You Win!!!")
        break