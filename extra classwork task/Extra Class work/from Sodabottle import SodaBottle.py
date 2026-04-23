from sodabottle import SodaBottle

class Main:
    def __init__(self) -> None:
        print("Program Starting")
        bottle_cola = SodaBottle("Cola-cola")
        print("Bottle brand is:", bottle_cola.brand)
        bottle_cola.drink()
        bottle_cola.openBottle()
        bottle_cola.drink()
        print("Program Ending")

if __name__ == "__main__":
    app = Main()

        