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

# Now we can update the price of an item in memory, without writing to file immediately
choice = input("If you want to update a price, press 0: ")

if choice == "0":
    for i, item in enumerate(items):
        print(f"{i}: {item.name} (current price: {item.value})")

    index = int(input("Enter item number to change price: "))
    new_price = float(input("Enter new price: "))

    items[index].value = new_price  # update price in memory

    print("\n##### Updated Inventory #####")
    for item in items:
        item.display_price()

print(f'#####End: {filename}#####')
