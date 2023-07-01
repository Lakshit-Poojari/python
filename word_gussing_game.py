import random
program = ["Hello","World","Laptop","Mobile","House","Table"]
computer = random.choice(tuple(program))
print(computer)
print("Given word is", program)
i = 1
while i < 6 :
    user = input("Enter your word\n")

    if (user!=computer):
        print("Try again")
        i += 1
    else:
        print("Congratulation you have gussed the correct word")
        break
else:
    print("Gameover")