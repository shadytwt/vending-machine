# print the main menu first
print("welcome to GalacticGrabs vending machine")

print("Code    item    price    stock")
print("[1]     pepsi    $2         4")
print("[2]     coke     $2         3")
print("[3]     chips    $1         0")
print("[4]     choco    $4         2")
print("[5]     juice    $2         5")
print("[6]     water    $1         8")

# create a variable for items price and stock
pepsiprice = 2
cokeprice = 2
chipsprice = 1
chocoprice = 4
juiceprice = 2
waterprice = 1

pepsistock = 4
cokestock = 3
chipsstock = 0
chocostock = 2
juicestock = 5
waterstock = 8

# insert money command and stock availibilty command
 
def purchase_item(item, price, stock):
    if stock > 0:
        print(f"You chose {item}. Please insert ${price}.")
        money_inserted = float(input())
        if money_inserted >= price:
            stock -= 1
            print(f"Here is your {item}. Enjoy!")
            if money_inserted > price:
                print(f"Here is your change: ${money_inserted - price}")
        else:
            print("Insufficient money. Please try again.")
    else:
        print(f"Sorry, {item} is out of stock.")
    return stock

while True:
 # ask the user to selct a code
    print("please enter a code for an item:")
    userCode = int(input())

# every code category
    if userCode == 1:
        pepsistock = purchase_item("Pepsi", pepsiprice, pepsistock)
    elif userCode == 2:
        cokestock = purchase_item("Coke", cokeprice, cokestock)
    elif userCode == 3:
        chipsstock = purchase_item("Chips", chipsprice, chipsstock)
    elif userCode == 4:
        chocostock = purchase_item("Choco", chocoprice, chocostock)
    elif userCode == 5:
        juicestock = purchase_item("Juice", juiceprice, juicestock)
    elif userCode == 6:
        waterstock = purchase_item("Water", waterprice, waterstock)
    else:
        print("Invalid code. Please try again.")
        continue  
    again = input("Would you like to buy another item? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thank you for using GalacticGrabs vending machine! Goodbye!")
        break