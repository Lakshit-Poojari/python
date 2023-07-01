import random
words = ["cricket","hockey","football","basketball","shotput","batminton","tennis"]
choosen_word=random.choice(words)
#print(choosen_word)
chance = len(choosen_word) -1
print(f"You have {chance} chance to guess the word")
word = "_"*len(choosen_word)
while chance !=0:
    print(word)
    alphabet = input("Guess the alphabet for word ")
    if alphabet in choosen_word:
        for i in range(len(choosen_word)):
            if choosen_word[i]==alphabet:
                word = word[:i]+alphabet+word[i+1:]
                print(word)
        if word == choosen_word:
            print("You guessed the correct word")
            break        
    else:
        chance -= 1
        print("Alphabet not matched")
        print(f"Total chance remaining is {chance}")
else:
    print("Gameover")