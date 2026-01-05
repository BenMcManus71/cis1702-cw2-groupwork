import json  #Fixed up the data and json loading, should work properly now. created by Ben McManus. Updated and tested by: Dan Caveney
data = [
    {"air freshener": 5, "bulb": 56, "dash cam": 68, "tire": 16, "window tint": 10},
    {
        "air freshener": {
            "cost": 2,
            "stock": 100,
            "product_code": "FBJ3ND",
            "quantity_per_unit": 30,
            "sold": 43
        },
        "bulb": {
            "cost": 4,
            "stock": 130,
            "product_code": "JNV2HR",
            "quantity_per_unit": 12,
            "sold": 64
        },
        "dash cam": {
            "cost": 70,
            "stock": 20,
            "product_code": "DBK6NS",
            "quantity_per_unit": 1,
            "sold": 52
        },
        "tire": {
            "cost": 40,
            "stock": 40,
            "product_code": "JYD9NY",
            "quantity_per_unit": 1,
            "sold": 40
        },
        "window tint": {
            "cost": 18,
            "stock": 0,
            "product_code": "AKN5JD",
            "quantity_per_unit": 10,
            "sold": 4
        }
    },
    ["Add item", "Move stock", "Sale / remove stock", "save", "Stock shortages",
     "Stock breakdown", "Change product values", "add product value", "Save and Exit"]
]
with open ("data.json", "w") as file:
    json.dump(data, file, indent=4)
    
with open("data.json", "r") as file:
    data = json.load(file)
    shop_item_quantity = data[0]
    garage_item_quantity = data[1]
    menu = data[2]

while True:                         
    count = 1
    for items in menu:
        print(f"{count}) {items}")
        count = count + 1
    choice = input("Please enter your choice: ")
    print("The choices that you can choose from will be shown underneath")
    print("\n")
    #a printed list that displays the choices that the user can choose from 
    #(ensure it in a dictionary so that the user can input a number and not receive an error)
    choice = choice.strip(" ")
    while choice.isdigit() == False or int(choice) < 1 or int(choice) > count:
        choice = input("Unrecognised input, please choose again: ")
    choice = int(choice)


#choices that we must add for the program (Add, Item, View Stock, Update Item, Search, Save & Exit)
    #if choice == 1:                        #created by: Dan Caveney
    #adding stock to warehouse, all new stock must go through this    
    if choice == 1:
        print("\n=== Add items to Warehouse ===")

        print("Current products:")        #prints out the current products inside the inventory (all the info)
        for item in garage_item_quantity:
            print("-", item)

        #new product being made, while loop to prevent duplicate products
        product_item = input("Enter the name of the new product for the inventory: ").strip()

        while product_item in garage_item_quantity:
            product_item = input("Invalid input. That product is already in the inventory: ").strip()

        #these five inputs allow for user to add all the required info, including error invalidation
        cost = (input("Enter cost of the new product: "))
        while not cost.isdigit():
            cost = (input("Invalid, enter a number for the cost: "))

        stock = (input("Enter the stock of the new product: "))
        while not stock.isdigit():
            stock = (input("Invalid, enter a number for the stock: "))

        product_code = input("Enter the 6 digit product code (e.g A17YJF): ").strip()

        quantity = (input("Enter in the Quantity_per_unit: "))
        while not quantity.isdigit():
            quantity = (input("Invalid, enter a number for the quantity: "))

        sold = (input("Enter in the amount sold (if none input 0): "))
        while not sold.isdigit():
            sold = (input("Invalid, enter a number for the sold amount: "))

        #empty dictionary for the program to insert the inputted data
        new_product = {
            "cost": int(cost),
            "stock": int(stock),
            "product_code": product_code,
            "quantity_per_unit": int(quantity),
            "sold": int(sold),
        }

        #adds the new product into the inventory
        garage_item_quantity[product_item] = new_product

        #saves the new item into the json file, allows for the user to also not save incase an error was made
        save = input("Save changes? (y/n): ").lower().strip()
        if save == "y":
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
            print("Changes saved.\n")
        elif save == "n":
            print("Changes not saved")
        else:
            print("Invalid input, enter y or n")
            exit()
    

    elif choice == 2:                        #created by: Ben McManus
    #moving stock around the 2 different storage areas, the variable names are shop_item_quantity and garage_item_quantity

        print("you have chose to move stock from one location to another")
        print("what products would you like to move?:")
        count = 1
        for items in garage_item_quantity:
            print(f"{count}) {items}")
            count = count + 1
        choice = input("\nwhich item would you like to move?: ")
        choice = choice.replace(" ", "")
        while choice.isdigit() == False or int(choice) < 1 or int(choice) > count:
            choice = input("invalid input, please enter again: ")
        choice = int(choice)

        choice = choice - 1
        choice = list(garage_item_quantity.keys())[choice]
        has_items = []
        if garage_item_quantity[choice]["stock"] > 0:
            has_items.append("garage")


        if choice in shop_item_quantity:
            if shop_item_quantity[choice] > 0:
                has_items.append("shop")
        else:
            shop_item_quantity.update({choice: 0})
        
        if len(has_items) == 1:

            if "shop" in has_items:
                to_from = input(f"\nwould you like to move {choice} from the shop (you have {shop_item_quantity[choice]}) to the garage (you have {garage_item_quantity[choice]["stock"]})? ")

                while to_from not in ["y", "n", "yes", "no"]:
                    to_from = input("invalid input, please answer again: ")
                if to_from == "yes":
                    to_from = "shop"
                elif to_from == "no":
                    pass
                
            elif "garage" in has_items:
                to_from = input(f"\nwould you like to move {choice} from the garage (you have {garage_item_quantity[choice]["stock"]}) to the shop (you have {shop_item_quantity[choice]})?")
                while to_from not in ["y", "n", "yes", "no"]:
                    to_from = input("invalid input, please answer again: ")
                if to_from == "yes":
                    to_from = "garage"
                elif to_from == "no":
                    pass

        
        elif len(has_items) ==2:
            print(f"do you want to move {choice} from the shop (you have {shop_item_quantity[choice]}) or from the garage (you have {garage_item_quantity[choice]["stock"]})?")
            to_from = input("please type \"shop\" for shop, or \"garage\" for garage: ")
            to_from = to_from.lower()
            to_from = to_from.replace(" ","")
            while to_from != "shop" and to_from != "garage":
                to_from = input("invalid input, please enter again: ")
                to_from = to_from.lower()
                to_from = to_from.replace(" ","")
            if to_from == "shop":
                print("\nyou have chosen to move stock from the shop to the garage")
                to_from = "shop"

            elif to_from == "garage":
                print("\nyou have chosen to move stock from the garage to the shop")
                to_from = "garage"
           
        else:
            print (f"there is no {choice} in any storage areas")
        

        if to_from == "garage":
            print(f"\nyou currently have {garage_item_quantity[choice]["stock"]} {choice} in the garage")
            quantity = input("how much would you like to move to the shop?: ")
            quantity = quantity.replace(" ","")
            while quantity.isdigit() == False or int(quantity) < 1 or int(quantity) > garage_item_quantity[choice]["stock"]:
                quantity = input("invalid input, please answer again: ")
            quantity = int(quantity)
            garage_item_quantity[choice]["stock"] = garage_item_quantity[choice]["stock"] - quantity
            shop_item_quantity[choice] = shop_item_quantity[choice] + quantity
            print(f"you have successfully moved {quantity} {choice} from the garage to the shop")
        
        elif to_from == "shop":
            print(f"\nyou currently have {shop_item_quantity[choice]} {choice} in the shop")
            quantity = input("how much would you like to move to the garage?: ")
            quantity = quantity.replace(" ","")
            while quantity.isdigit() == False or int(quantity) < 1 or int(quantity) > shop_item_quantity[choice]:
                quantity = input("invalid input, please answer again: ")
            quantity = int(quantity)
            shop_item_quantity[choice] = shop_item_quantity[choice] - quantity
            garage_item_quantity[choice]["stock"] = garage_item_quantity[choice]["stock"] + quantity
            print(f"\nyou have successfully moved {quantity} {choice} from the shop to the garage\n")







    


    #elif choice == 3:                      #created by: Mia Watabe
    # this is to log a sale, and to remove stock out of inventory, for if it broke ect, there should be a different statement for each
    elif choice == 3:
        print("You have chosen to log sale or remove stock.")
        log = input("Would you like to log a sale? (y/n)").strip().lower()

        if log == 'n':
            # ================= REMOVE STOCK =================
            print("You have chosen to remove stock.")
            removeItem = input("What item would you like to remove? ").strip().lower()

            if removeItem in shop_item_quantity:
                print("Item found.")
                removeQty = input("How many would you like to remove?")

                if not removeQty.isdigit():
                    print("Please use numbers only")
                    continue

                removeQty = int(removeQty)
                shopQty = shop_item_quantity[removeItem]

                if removeQty <= shopQty:
                    newQty = shopQty - removeQty
                    shop_item_quantity[removeItem] = newQty
                else:
                    print("Error: Not enough Stock")

            elif removeItem in garage_item_quantity:
                print("Item found.")
                removeQty = input("How many would you like to remove?")

                if not removeQty.isdigit():
                    print("Please use numbers only")
                    continue

                removeQty = int(removeQty)
                garageQty = garage_item_quantity[removeItem]["stock"]

                if removeQty <= garageQty:
                    newQty = garageQty - removeQty
                    garage_item_quantity[removeItem]["stock"] = newQty
                    print("Stock updated.")
                else:
                    print("Error: Not enough Stock")

            else:
                print("Item not found.")

        elif log == 'y':
        # ================= LOG SALE =================

            print("You have chosen to log a sale.")
            removeItem = input("What item was sold? ").strip().lower()

            if removeItem in shop_item_quantity:
                print("Item found.")
                removeQty = input("How many were sold?")

                if not removeQty.isdigit():
                    print("Please use numbers only")
                    continue

                removeQty = int(removeQty)
                shopQty = shop_item_quantity[removeItem]
                garageSold = garage_item_quantity[removeItem]["sold"]

                if removeQty <= shopQty:
                    newQty = shopQty - removeQty
                    shop_item_quantity[removeItem] = newQty
                    soldQty = garageSold + removeQty
                    garage_item_quantity[removeItem]["sold"] = soldQty

                else:
                    print("Error: Not enough Stock")

            elif removeItem in garage_item_quantity:
                print("Item found.")
                removeQty = input("How many were sold?")

                if not removeQty.isdigit():
                    print("Please use numbers only")
                    continue

                removeQty = int(removeQty)
                garageQty = garage_item_quantity[removeItem]["stock"]
                garageSold = garage_item_quantity[removeItem]["sold"]

                if removeQty <= garageQty:
                    newQty = garageQty - removeQty
                    garage_item_quantity[removeItem]["stock"] = newQty
                    soldQty = garageSold + removeQty
                    garage_item_quantity[removeItem]["sold"] = soldQty

                    print("Sale logged.")
                else:
                    print("Error: Not enough Stock")

            else:
                print("Item not found.")

        else:
            print("ERROR Please input only y or n.")



    elif choice == 4:                       #created by: Dan Caveney
        def save_changes():
            print("=== You have selected the Save option ===")
            print("\n=== Here you can choose to save every change made to the inventory ===\n")

            save = input("Do you want to save all your changes? (y/n)").lower().strip()
            if save == "y":
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
                print("Your changes have been successfully changed")
            elif save == "n":
                print("You have decided to not save your changes")
                print("Make sure you look over your changes before saving it")
            else:
                print("\nInvalid input, enter y or n. \n")
        save_changes()
    #this should be to save all changes made to data.json


    
    elif choice == 5:                      #created by: Aaron Rielly
    #this section is to show any recomendations of what stock should be bought if we are running low

        print("\n===================================")
        print("       STOCK SHORTAGE REPORT       ")
        print("===================================\n")

        low_stock_limit = 10                                            # Defines the low stock level as 10

        low_stock_items_found = False                                   # Tracks whether any low stock items are found

        print("Low stock criteria:")
        print(f"- Stock equal to 0")
        print(f"- Stock less than or equal to {low_stock_limit} units\n")

        for product_name in garage_item_quantity:                       # Loops through every product in the inventory
            product_details = garage_item_quantity[product_name]

            current_stock = product_details.get("stock", 0)
            units_sold = product_details.get("sold", 0)
            product_code = product_details.get("product_code", "UNKNOWN")

            if current_stock == 0 or current_stock <= low_stock_limit:  # Checks if the item is below the low stock limit

                low_stock_items_found = True

                print("-----------------------------------")
                print(f"Product Name   : {product_name}")
                print(f"Product Code   : {product_code}")
                print(f"Stock Remaining: {current_stock}")
                print(f"Units Sold     : {units_sold}")

                if current_stock < 0:                                     # If stock is below 0:
                    print("Status         : STOCK LEVEL BELOW 0")
                    print("Recommendation : Check the wearhouse immediately for stock levels & update the stockfile.")
                elif current_stock == 0:                                  # If low-stock items were detected:
                    print("Status         : OUT OF STOCK")
                    print("Recommendation : Reorder immediately.")
                else:
                    print("Status         : LOW STOCK")
                    print("Recommendation : Consider reordering soon.")

                print("-----------------------------------\n")

        if not low_stock_items_found:                                   # If no low-stock items were detected:
            print("All products currently have sufficient stock levels.")
            print("No reordering is required at this time.\n")
            

        input("Press Enter to return to the main menu...")


    
    #elif choice == 6:                      #created by:
    #this section is for showing infomation associated, this could be showing where how much stock is located, an item as a percentage of the whole stock value etc
    #it should also have a way to display items added if choice == 7


    elif choice == 7:                      # created by: Aaron Rielly
    # this is to update an items value, which involves changing the name, price & quantity_per_unit

        print("\n===================================")
        print("\n=== CHANGE PRODUCT VALUES ===\n")
        print("\n===================================")

        # list current products
        print("Current products:")
        count = 1
        for product_name, product_details in garage_item_quantity.items():
            product_id = product_details.get("product_code", "UNKNOWN")
            print(f"{count}) ID: {product_id} | Name: {product_name}")
            count += 1

        choice_item = input("\nSelect a product number to update: ")
        while not choice_item.isdigit() or int(choice_item) < 1 or int(choice_item) >= count:
            choice_item = input("Invalid input, please choose again: ")

        choice_item = int(choice_item) - 1
        product_name = list(garage_item_quantity.keys())[choice_item]
        product = garage_item_quantity[product_name]

        print(f"\nYou are currently making changes to: {product_name}")
        print("Press Enter to keep the current value of a product.\n")

        # update name
        new_name = input(f"New name [{product_name}]: ")
        if new_name and new_name not in garage_item_quantity:                           #Checks to make sure the new name isnt already being used.
            garage_item_quantity[new_name] = garage_item_quantity.pop(product_name)
            shop_item_quantity[new_name] = shop_item_quantity.pop(product_name, 0)
            product_name = new_name
            product = garage_item_quantity[product_name]

        # update cost
        new_cost = input(f"New cost [{product['cost']}]: ")
        if new_cost:
            while not new_cost.isdigit():                                           #Checks value enetered is a digit
                new_cost = input("Invalid input. Enter a number: ")                 #If not a digit, user prompted again
            product["cost"] = int(new_cost)                                         

        # update stock value
        new_stock = input(f"New stock [{product['stock']}]: ")
        if new_stock:
            while not new_stock.isdigit():                                          #Checks value enetered is a digit
                new_stock = input("Invalid input. Enter a number: ")                #If not a digit, user prompted again
            product["stock"] = int(new_stock)

        # update quantity per unit
        new_quantity_per_unit = input(f"New quantity per unit [{product['quantity_per_unit']}]: ")
        if new_quantity_per_unit:
            while not new_quantity_per_unit.isdigit():                                      #Checks value enetered is a digit
                new_quantity_per_unit = input("Invalid input. Enter a number: ")            #If not a digit, user prompted again
            product["quantity_per_unit"] = int(new_quantity_per_unit)

        # update product code
        new_product_code = input(f"New product code [{product['product_code']}]: ")
        if new_product_code:
            product["product_code"] = new_product_code


        # update sold value
        new_sold = input(f"New sold amount [{product['sold']}]: ")
        if new_sold:
            while not new_sold.isdigit():
                new_sold = input("Invalid input. Enter a number: ")
            product["sold"] = int(new_sold)

        # save option value
        save = input("\nSave changes? (y/n): ").lower()                         #.lower() means any capital letters are lowered to pass the next function
        if save == "y":
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
            print("Changes saved.\n")
        elif save == "n":
            print("Changes not saved.\n")
        else:
            print("Invalid input, Changes not saved. Please try again.\n")
            save = input("\nSave changes? (y/n): ").lower() 

 
    #elif choice == 8:                      #created by:
    #this is to add another value that isnt included already, such as buy in price


    #allows for the user to exit the program during the choice selection
    elif choice == 9:                       #created by: Dan Caveney
        def exit_program():
            print("=== You have selected the Save and Exit option. Make sure everything is as it should before saving and exiting the program ===")
            print("\n=== Before you leave, would you like to save your changes? ===\n")

            save = input("Would you like to save all changes made to the program before exiting (input y or n)?: ").lower().strip()
            
            if save == 'y':
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)

                print("\nChanges saved successfully!\n")

                save_confirm = input("You've chosen to save your changes, and now you're exiting the program with the changes made, is this what you want?: ")
                if save_confirm == 'y':
                    print("You have decided to not save your changes.")
                    print("\n=== Come back again some day! ===\n")
                    exit()
                elif save_confirm == 'n':
                    print("\nVery well, you've chosen not to exit the program yet\n")

            elif save == 'n':
                save_confirm = input("You've chosen to not save your changes, meaning you're exiting the program without the changes, is this what you want?: ")
                if save_confirm == 'y':
                    print("You have decided to not save your changes.")
                    print("\n=== Come back again some day! ===\n")
                    exit()
                elif save_confirm == 'n':
                    print("\nVery well, you've chosen not to exit the program yet\n")
            else:
                ("\nInvalid input! enter y or n\n")
        exit_program()


























