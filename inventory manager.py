import json  #Fixed up the data and json loading, should work properly now. Updated by: Dan Caveney
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
     "Stock breakdown", "Change product values", "add product value", "Exit"]
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
    #moving stock around the 3 different storage areas, the variable names are warehouse, shop_item_quantity and garage_item_quantity

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
        if shop_item_quantity[choice] > 0:
            has_items.append("shop")

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







    


    #elif choice == 3:                      #created by:
    # this is to log a sale, and to remove stock out of inventory, for if it broke ect, there should be a different statement for each


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


    #elif choice == 7:                      #created by: Aaron Rielly?
    #this is to update an items value, which involves changing the name, price & quantity_per_unit

 
    #elif choice == 8:                      #created by:
    #this is to add another value that isnt included already, such as buy in price


    #allows for the user to exit the program during the choice selection
    elif choice == 9:                       #created by: Dan Caveney
        print("=== Have a good day! Be sure that you saved everything and there aren't any problems ===")
        print("=== Come back again some day! ===")
        exit()
















