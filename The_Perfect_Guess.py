import random
n=random.randint(1,100)
a=-1
guess=-1
while(a!=n):
    guess+=1
    a=int(input("Guess the number:"))
    if(a>n):
        print("Lower the number please")
    else:
        print("Higher the number please")

print(f"You have gussed the number  {n} correctly in {guess} attempts")