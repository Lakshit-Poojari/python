import random
user = input("Select Snake/Water/Gun \n")
choise = "Snake"
choise_1 ="Water"
choise_2 = "Gun"
program = ["Snake","Water","Gun"]
computer = random.choice(tuple(program))
print(computer)
if user == computer :
    print("Draw")
elif choise != program[0] and program[2]:
    print("User won")
elif choise_1 != program[1] and program[0]:
    print("User won")
elif choise_2 != program[2] and program[1] :
    print("User won")
else :
    print("Program won")