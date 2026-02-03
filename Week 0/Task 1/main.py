from counter import counter

print ("Program starting.")
print("Initializing counter...")
print("Counter initialized.")

counter = counter()

while True:
    print("\nOptions:")
    print("1) Add count")
    print("2) Get count")
    print("3) Zero count")
    print("0) Exit program")

    choice = input("choice: ")

    if choice == "1":
        counter.addCount()
        print("Count increased.")
    elif choice == "2":
        print("Current count:", counter.getCount())
    elif choice == "3":
        counter.zeroCount()
        print("Count zeroed.")
    elif choice == "0":
        print("\nProgram ending.")
        break
    else:
        print("You have entered wrong input, please look back to the options. You have to select 1, 2, 3, or 0.")