print("_____________________Mark.Sheet_____________________")
english = int(input("Enter the number of english subject : "))
urdu = int(input("Enter the number of urdu subject : "))
sindhi = int(input("Enter the number of sindhi subject : "))
islamiat = int(input("Enter the number of islamiat subject : "))
mathematics = int(input("Enter the number of mathematics subject : "))
physics = int(input("Enter the number of physics subject : "))
chemistry = int(input("Enter the number of chemistry subject : "))

obtain_marks = int(input("Enter the obtain marks : "))

total_marks = int(input("Enter the total marks : "))

percentage = ((obtain_marks/total_marks)*100)

if (percentage>=80) :
    print("Grade : A+")
    
elif (percentage>=70) :
    print("Grade : A")
    
elif (percentage>=60) :
    print("Grade : B")
    
elif (percentage>=50) :
    print("Grade : C")
    
elif (percentage>=40) :
    print("Grade : D")
    
else :
    print("Fail")
