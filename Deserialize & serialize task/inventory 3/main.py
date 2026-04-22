from file_handler import FileHandler
from item import Item

filename = "inventory.csv"
inventory_file = FileHandler(filename)
rows = inventory_file.read()

items = []  # it list all items in memory, so we can update them without writing to file immediately

print(f'#####Start: {filename}#####')

#  at First it will  display all items and their prices
for row in rows:
    item = Item.deserialize(row)
    items.append(item)
    item.display_price()

# from this point, this code ask user if they want to update the price of any item.
choice = input("If you want to update a price, press 0: ") 

if choice == "0":  # if user presss 0, then code allow them to select an items value.
    for i, item in enumerate(items): # i is the index number and item is the item objectand enumerate is used to get the index number of each item in the list.
        print(f"{i}: {item.name} (current price: {item.value})") # it will print the index number, item's name and item's price.

    index = int(input("Enter item number to change price: ")) # ask user to select an item's number
    new_price = float(input("Enter new price: "))  # ask user to enter new price of selected item.

    items[index].value = new_price  # update the price of selected item.

    print("\n##### Updated Inventory #####")
    for item in items:
        item.display_price() # it will show the new price 

print(f'#####End: {filename}#####')
