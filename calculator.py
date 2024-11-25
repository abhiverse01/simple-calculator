def calculator():
  
 while True:
    print("..SIMPLE CALCULATOR ..")

    num1=float(input("First number: "))
    operator=input("Enter the operator you want to use: ")
    num2=float(input("Second number: "))
    
    if operator== "+":
        Answer=num1+num2
        print(Answer)

    elif operator=="-":
        if num1>num2:
         Answer =num1-num2  
        else:
         Answer=num1-num2
         print(Answer)

    elif operator=="*":
       Answer=num1*num2
       print(Answer)

    elif operator=="/":
       if num1==0: 
          if num2==0:
           print("Invalid.")
          else:
           print("0")

       else:
          Answer=num1/num2
          print("{:.2f}".format( Answer))

    next=input("Do you want to do further calculations?(Yes/No) ").strip().lower()
    if next!="yes":
     print("GoodBye!👋")
    break
     
       
calculator()        

       
            
