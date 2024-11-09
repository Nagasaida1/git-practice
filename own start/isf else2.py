pen=int(input("enter a number:"))

if pen % 3==0 & pen%5==0:
    print("AZ")
elif pen % 3==0:
    print("A")
elif pen % 5==0:
    print("Z")
else:
    print("Invalid")