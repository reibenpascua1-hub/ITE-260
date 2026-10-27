print("Main Menu")
print("1. Add Product")
print("2. View Inventory")
print("3. Update Stock")
print("4. Check Low Stock")
print("5. Exit")
print()

while True:
    num = int(input("Enter Number 1-5: "))

    print()
    if num == 1:
        name = str(input("Enter Product name: "))
        quantity = int(input("Enter Quantity: "))
        inventory=[]
        product = inventory
        stock= product
        quantity1=[]
        quantity2=(quantity)


        inventory.append(name)
        quantity1.append(quantity)

        print("Product added successfully")

    elif num == 2:
        print("INVENTORY")
        print(inventory , quantity1)

    elif num == 3:
        update = (input("Enter Product: "))
        found = False

        for product in inventory:
            if product :
                quantity1 = int(input("Enter New Quantity: "))
                product = quantity1
                print("Stock updated")
                found = True
                break

            if not found:
                print("Product not found")


    elif num == 4:
        found=True


        if quantity2 <=5:
            print("Low stock:", inventory,quantity1)

        elif quantity2 >=6:
            print("No low stock products")












    elif num == 5:
        print("Program ended")
        break

    else:
        print("Please enter a valid number 1-5")






