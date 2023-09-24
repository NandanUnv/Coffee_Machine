import time

print("# Welcome to coffee cafe #")
dct = {"Milk(ml)":70, "Water(ml)":200, "Coffee(g)":75, "Money(RS.)":150}

def myfun(pric,a):
    print("Please insert coins")
    b = int(input("How many 5Rs. coins:"))
    c = int(input("How many 10Rs. coins:"))
    d = int(input("How many 20Rs. coins:"))
    price = pric
    pc = (5 * b + 10 * c + 20 * d)
    if(pc>=price):
        r_c = pc - price
        print(f'Here is your Rs.{r_c} in change')
    else:
        print("sorry, no enough money")
    print(f"Here is your '{a}' ☕")

def fun(a):
    if a=='latte':
        myfun(100,a)
    elif a=='cappuccino':
        if (dct['Milk(ml)']>40):
            myfun(150,a)
            dct['Milk(ml)']-=20
        else:
            print("Not enough milk")
    elif a=='espresso':
        myfun(125,a)
    else:
        print('This flavour is not available')

while True:
    a = input("Enter your flavour of coffee(latte/espresso/cappuccino):")
    fun(a)
    v = input("Do you want to order anything?(Y/N):")
    if v=='y' or v=='Y':
        time.sleep(2)
        pass
    else:
        break

print("// Thank you for visiting //")
