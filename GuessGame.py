import random
guesstaken=0
print("Welcome To Guess the Number game!")
print("Enter Your Name to Continue!")
name=str(input())
print("Hi! "+name+" I am Thinking Of A Number Between 1 and 20")
number=random.randint(1,20)
print("Enter The Number You Have Guessed")
enterednum=int(input())
while(guesstaken<4):
    guesstaken += 1
    if(enterednum<number):
        print("The Number You Have Entered is Too Low")
        enterednum=int(input("One More Chance is Given To You"))
        continue
    elif(enterednum>number):
        print("The Number You Have Entered is Too High")
        enterednum = int(input("One More Chance is Given To You"))
        continue
    elif(enterednum==number):
        break
if(enterednum==number):
        print("You Have Guessed it Right")
        print("The Number is=",number)
else:
    print("You Loose!")




