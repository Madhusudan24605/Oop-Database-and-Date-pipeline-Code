from counter1 import Counter

counter = Counter()

while True:
    print("\n1. Add count")
    print("2. Get count")
    print("3. Zero count")
    print("4. Exit program")

    choice = input("Choose an option: ")

    if choice == "1":
        counter.addCount()
        print("Count increased.")
    elif choice == "2":
        print("Current count:", counter.getCount())
    elif choice == "3":
        counter.zeroCount()
        print("Count reset to zero.")
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")