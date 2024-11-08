
inventory = {}
while True:
    item = input("Enter Item : ")
    quantity = float(input("Enter quantity : "))
    price = float(input("Enter Price : "))

    qc=[]

    qc.append(quantity)
    qc.append(price)
    inventory[item] = qc

    #updating quantity
    up_= input("Want to update price or quantity : ")
    if up_ == "yes":
        up_wht = input("Enter what to update : ")
        if up_wht == "price":
            item_name = input("Enter item name to update :")
            up_price = input("Enter updated Price : ")

            price_l = list(inventory[item_name])
            price_l[1] = up_price
            inventory[item_name]= price_l

        if up_wht == "quantity":
            item_name = input("Enter item name to update :")
            up_quantity = input("Enter updated Quantity : ")

            quantity_l = list(inventory[item_name])
            quantity_l[0] = up_quantity
            inventory[item_name] = quantity_l

    #total value of inventory
    sum =0
    for i in inventory:
        vals= list(inventory[i])
        sum = sum + (float(vals[0])*float(vals[1]))

    print(inventory)
    print("Total value : ",sum)







