import json
'''data = [{"air freshener": 5, "bulb": 56, "dash cam": 68},    ### UNCOMMENT THIS TO CREATE DATA.JSON ###
{"tire": 16, "window tint": 10},
{
    "air freshener":{
        "cost": 2,          #how much we sell them for
        "stock": 100,       #how much we have (in the warehouse)
        "product_code": "FBJ3ND",   
        "quantity_per_unit": 30,    #how many of an item you get when you buy 1 unit
        "sold": 43
    },
    "bulb":{
        "cost": 4,
        "stock": 130,
        "product_code": "JNV2HR",
        "quantity_per_unit": 12,
        "sold": 64
    },
    "dash cam":{
        "cost": 70,
        "stock":20,
        "product_code": "DBK6NS",
        "quantity_per_unit": 1,
        "sold": 52
    },
    "tire":{
        "cost": 40,
        "sotck": 40,
        "product_code": "JYD9NY",
        "quantity_per_unit":1,
        "sale": 40
    },
    "window tint":{
        "cost": 18,
        "stock": 0,
        "product code": "AKN5JD",
        "quantity_per_unit": 10,
        "sale": 4
    }
},
["Add stock", "Move stock", "Sale / remove stock", "save", "Stock shortages", "Stock breakdown", "Change product values", "add product value"]]
with open ("data.json", "w") as file:
    json.dump(data, file)'''
with open ("data.json", "r") as file:           #all basic setup created by: Ben McManus
    data= json.load(file)
    shop_item_quantity = data[0]# quantity of items found in the shop
    garage_item_quantity = data[1]# quantity of items found in the garage
    warehouse = data [2]# all other items in storage, ALL other data asociated with items will be found here too
    menu = data[3]

while True:                         
    count = 1
    for items in menu:
        print(f"{count}) {items}")
        count = count + 1
    choice = input("Please enter your choice: ")
    choice = choice.strip(" ")
    while choice.isdigit() == False or int(choice) < 1 or int(choice) > count:
        choice = input("Unrecognised input, please choose again: ")
    choice = int(choice)



    #if choice == 1:                        #created by:
    #adding stock to warehouse, all new stock must go through this


    #elif choice == 2:                        #created by:
    #moving stock around the 3 different storage areas, the variable names are warehouse, shop_item_quantity and garage_item_quantity


    #elif choice == 3:                      #created by:
    # this is to log a sale, and to remove stock out of inventory, for if it broke ect, there should be a different statement for each


    #elif choice ==4:                       #created by:
    #this should be to save all changes made to data.json


    #elif choice == 5:                      #created by:
    #this section is to show any recomendations of what stock should be bought if we are running low


    #elif choice == 6:                      #created by:
    #this section is for showing infomation associated, this could be showing where how much stock is located, an item as a percentage of the whole stock value ect
    #it should also have a way to display items added if choice == 7


    #elif choice == 7:                      #created by:
    #this is to change values asociated with values, such as the price or quantity_per_unit


    #elif choice == 8:                      #created by:
    #this is to add another value that isnt included already, such as buy in price