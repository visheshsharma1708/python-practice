marks=int(input("enter your marks here :"))

if(marks>=90):
    print("grade:A+")
elif(marks<90 and marks>=80):
    print("grade:A")    
elif(marks<80 and marks>=70):
    print("grade:B")    
elif(marks<70 and marks>=60):
    print("grade:C+")    
elif(marks<60 and marks>=50):
    print("grade:C")    
elif(marks<50 and marks>=40):
    print("grade:D")    
elif(marks<40 and marks>=36):
    print("grade:E") 
else:
    print("you have failed in exam !")       
