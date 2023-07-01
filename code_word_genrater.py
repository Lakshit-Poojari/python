word = input("Enter a word \n")              
respond = input("Do you want to encode this word. \n If you want to encode the word type ""yes"".  \n")
order = "yes" 
if (len(word) <= 3):                        
    reversed_word = word[::-1]              
    print("your encoded word is " + reversed_word)            
else:
    if (respond == order) :                
      converted_word = word[1:] + word[0]
      print("Your converted_word is: " + converted_word)
      print("your encoded word is " + "qwe" + converted_word + "iop" )       
    else:
        print(word)

respond_1 = input("Do you weant to dencode this word. \n If you want to dencode the word type ""yes"".  \n")
order_1 = "yes" 

if (respond_1 == order_1) :
      print("Your decoded word is: " + word)

