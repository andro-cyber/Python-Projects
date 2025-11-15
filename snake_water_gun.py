import random

computer=random.choice([1,0,-1])
user=input("Enter your choice(s for Snake,w for Water,g for Gun):").strip().lower()
you={"s":1,"snake":1,
"w":-1,"water":-1,
"g":0,"Gun":0}
reverse={1:"Snake",-1:"Water",0:"Gun"}
option=you[user]
f=open("game.txt","a")
f.write(f"User choice: {reverse[option]}\n")
f.write(f"Computer choice: {reverse[option]}\n")

print(f" You chose: {reverse[option]}\nComputer chose {reverse[computer]}")
f.write(f"Score:")
if (computer==option):
    result="draw"
    print("Its a draw")
else:
    if(computer==-1 and option==1):
        result="Win"
        print("You win!")

    elif(computer==-1 and option==0):
        result="Lose"
        print("You Lose!")

    elif(computer==1 and option==-1):
        result="Lose"
        print("You Lose!")
    elif(computer==1 and option==0):
        result="Win"
        print("You win!")
    elif(computer==0 and option==-1):
        result="Lose"
        print("You Lose!")

    elif(computer==0 and option==1):
        result="Win"
        print("You win!")
    else:
        print("Something went wrong")
f.write(result,"\n")
f.close()

    