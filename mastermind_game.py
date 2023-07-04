import random
num  = random.randint(1,10)
#print(f"Computer gussed number {num}")      PROGRAM RANDOMLY SELECTED THE NUMBER FROM 1-10
gusse_num = "_"*len(str(num))
print(f"Computer has gussed the number {gusse_num}")
number = ''
number_1 =int(input("Give number\n"))
num_1 = ""
chance = 0
while number != num :
    number =  int(input("Guess the number\n"))
    chance += 1
    if number == num :
        print ("match")
        print(f"You have taken {chance} chances")
    else :
        print("try again")
        print(f"You have taken {chance} chances")
    
    chance_1 = 0
while number_1 != num_1:
       
    num_1 = random.randint(1,10)
    print(num_1)
    chance_1 += 1
    if num_1 == number_1:
        print("Coputer won")
        print(f"Computer has taken {chance_1} chances")
    else:
        print("Computer should try again")
        print(f"Computer has taken {chance_1} chances")

if chance > chance_1:
    print ("Computer is Mastrmind!!")
elif chance_1 > chance:
    print ("You are Mastermind!!")
else :
    print("Both are Mastermind!!")