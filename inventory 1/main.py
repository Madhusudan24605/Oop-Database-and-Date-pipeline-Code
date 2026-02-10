from file_handler import FileHandler


filename = "inventory.csv"
inventory_file = FileHandler(filename) # create an object
rows = inventory_file.read() # use read method for the previously created object
print(f'#####Start: {filename}#####')
for row in rows:
    print(row)

print(f'#####End: {filename}#####')