print("Apka phela sawal \nYe kounsa programing language hai ?")
Question = [["Ye kounsa programing language hai ?",
             "A.  c++", "B. Java" ,"C. python" ,"D. Non of the above"],
             ["Aap kounsa game khel rahe ho ?",
              "A.  Ludo ", "B. X and Zero" ,
              "C. Koun Banega corepati" ,"D. Non of the above"],
             ["Capital of India ?","A.  Pune", "B. Mumbai" ,"C. Delhi" ,"D. Non of the above"]]

Answer = "C" and "c"

for i in range(0, len(Question)): 
    option = (Question[i])
    print(option)
    Jawab = input("jawab dijiye  Write only option (eg. A, B, C, D)\n")
    
    if(Jawab == Answer ):
      print("7 core")
    else:
      print("Afsos apka jawab galat hai")
      break