
#calculation based on item and item price
def cali(item,itemp):
    money = int(input("How much money do you have: "))
    input_count = input('How many kgs do you want?: ')
    count = int(input_count)
    total_price = itemp * count

    print('You will buy ' + str(count) + ' '+ item)
    print('The total price is  ' + str(total_price) + ' dollars')


    # Add control flow based on the comparison of money and total_price
    if money > total_price:
        print('You have bought ' + str(count) + ' ' + item)
        leftmoney = money - total_price
        print('You have ' + str(leftmoney) + ' dollars left')
    elif money == total_price:
        print('You have bought ' + str(count) + ' ' + item )
        print('Your wallet is now empty')
    else:
        print('Your wallet is now empty')
        print('You cannot buy that many ' + item)


def user_choice():
    choice = input("What do you want to buy \n"
                   "FOR,\n"
                   "Apple : Enter A \n"
                   "Banana : Enter B \n"
                   "Kivi : Enter K \n"
                   "Grapes : Enter G \n"
                   "Enter -- ")
    return choice

while True:
    choice = user_choice()
    apple_price = 140
    banana_price = 50
    kivi_price = 30
    grapes_price = 50


    if choice == 'A':
        itemp = apple_price
        item = "APPLE"
        res = True


    elif choice == 'B':
        itemp = banana_price
        item = "BANANA"
        res = True


    elif choice == "K":
        itemp = kivi_price
        item = "KIVI"
        res = True


    elif choice == "G":
        itemp = grapes_price
        item = "Grapes"
        res = True


    else:
        itemp = 00
        item = "invalid"
        res = "False"


    if res == True:
        cali(item, itemp)
        i = input('Want to continue shopping - y/n ')
        if i == 'y' or i == 'Y':
            pass
        else:
            print("Thank You")
            break
    else :
        i = input('Invalid Input , Want to continue? - y/n')
        if i == 'y' or i == 'Y':
            pass
        else:
            print("Thank You")
            break


