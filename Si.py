# Write a program to find simple interest

p=int(input("Enter Principle Amount ="))
r=float(input("Enter Interest rate ="))
n=int(input("Enter Number of years ="))

si=int((p*r*n)/100)
print("Simple Interest =",si)

a=int(p+si)
print("\nTotal Amount with Simple Interest =",a)
