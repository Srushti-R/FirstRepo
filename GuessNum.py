import random


target = random.randint(1 , 100)

while True:
    userNum = input("Enter any No.Or Quit(Q) =")
    if(userNum == "Q"):
        break

    userNum = int(userNum)
    
    if (userNum == target):
        print("\nCongrats !! You Guess the Right Number")
        break
    elif(userNum < target):
        print("Your Number is too Small ,Take bigger Number")
    else:
        print("Your Number is too big ,Take small Number")


print("\n--**--**--Game Over--**--**--\n")
              