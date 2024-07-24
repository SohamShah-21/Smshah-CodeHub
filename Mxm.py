num1=int(input("Enter your value : "))
num2=int(input("Enter your value : "))
num3=int(input("Enter your value : "))

if(num1>num2):
    if(num1>num3):
        print("Num 1 is greater than num 3")
    else:
        print("Num 3 is greater than num 1")
else:
    if(num2>num3):
        print("Num 2 is greater than num 3")
    else:
        print("Num 3 is greater than num 2")
