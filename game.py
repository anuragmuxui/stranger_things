score=0
funnyQuestions = {
  "question1": "Cow gives milk and chicken lays egg, so who is the one who gives both milk and egg",
  "question2":"If Oxygen ever fall in love with magnesium by mistake, What would we call there relationship?",
  "question3":"wht is in between 1 nad 3"
}
answer = {
    "question1":["shopkeeper" , "hen" ,"milk"],
    "question2":["oh my god","omg","oh my love"],
    "question3":["and","2","3"],
}
print("simple game")
print(" do you want to start 'yes'/'no' ")
userChoice=str(input("Your option = "))
if(userChoice=="yes"):
    print(funnyQuestions["question1"])
    print(answer["question1"])
    useranswer=(input("your answer"))
    
    if(useranswer=="shopkeeper"):
        print("correct")
        score=score+1
        
    else:
        print("your anser is wrong")
        print("congratulations your score is :",score)
        exit()
    print(funnyQuestions["question2"])
    print(answer["question2"])
    useranswer2=(input("your answer="))
    if(useranswer2=="omg"):
        print("correct")
        score=score+1
    else:
        print("your anser is wrong")
        print("congratulations your score is :",score)
        exit()
    print(funnyQuestions["question3"])
    print(answer["question3"])
    useranswer3=(input("your answer="))
    if(useranswer3=="and"):
        print("correct")
        score=score+1
        print("correct you have ished the question your score is:",score)
    else:
        print("sorry  wrong")
        print("congratulations your score is :",score)
        exit()
        
    
        
       
else :
    print("appo sheri bye")
