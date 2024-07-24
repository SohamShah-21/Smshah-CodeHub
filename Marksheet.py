phy=int(input("Enter marks of physics : "))
che=int(input("Enter marks of chemistry : "))
bio=int(input("Enter marks of biology : "))

total=phy+che+bio
per=(total)/3
print("Percentage obtained = %",per)

if(per>=70):
    print("Distinction class achieved")
elif(per>=60 and per<70):
    print("First class achieved")
elif(per>=50 and per<60):
    print("Second class achieved")
elif(per>=40 and per<50):
    print("PASS")
else:
    print("FAIL") 