print("welcome to atm !")
b=int(input("enter the balance !"))
m=int(input("enter how much to deduct !"))
if b>1000:
    r=b-m
    if r<1000:
        print("can't deduct.Balance low!")
    else:
        print("money deducted.rem amount:",r)
else:
    print("insufficient balance")