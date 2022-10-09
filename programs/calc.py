
def add(a,b):
    print(f"sum of {a}+{b} = ",a+b)
def substract(a,b):
    print(f"substraction of {a}-{b} = ",a-b)
def multiplication(a,b):
    print(f"multiplication of {a}*{b} = ",a*b)
def division(a,b):
    print(f"divided by {a}/{b} = ",a/b)

def main():
    print("\nsimple calculator\n")
            
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    print("1.addition\n2.subtraction \n3.multiplicatrion\n4.division")
    c=int(input("what you want to select: "))   
    if (c==1):
        add(a,b)
    elif(c==2):
        substract(a,b)
    elif(c==3):
        multiplication(a,b)
    elif(c==4):
        division(a,b)
    else :
        print("Invalid Option")
        
while True:   
    main()
        
    
        
        
        
        




  
    
    
    
    
    
        



