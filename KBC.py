# import random
point=0
q1='''How many contients are in the world
A: 6
B: 8
C: 7
D: 9'''
q2='''Which lang is a obejct oriented lang
A: CPP
B: C#
C: Ruby
D: Python'''
q3='''What is the mass of the electron
A: 8.85*10^-31
B: 6.66*10-27
C: 1.6*10-19
D: 9.1*10-31'''
ques=[q1,q2,q3]
lis=["C","D","D"]
for i in range(0,len(ques)):
    print(ques[i])
    ans=input("What is your answer: ")
    if ans==lis[i]:
        print("You Won!!")
        point+=1
        print("Your point is:",point)
        if point==len(ques):
            break
    else:
        print("You Lose ")
        life=input("Do you still want to continue[y/n]: ")
        if life=="n":
            break
        else:
            continue