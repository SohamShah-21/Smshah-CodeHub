cs=int(input("Enter your amount :"))
if(cs>100):
         Discount=(cs*10)/100
         Price=cs*(1-10/100)
         print("Discounted Price = ",Price)
else:
    print("No Discount Available on this product")
