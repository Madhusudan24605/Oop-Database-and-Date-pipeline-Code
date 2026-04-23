class sodabottle:
    brand:str
    caponen:bool

    def _init_(self, brand) -> None:
        self.brand = brand
        self.caponen = False
    
    def openbottle(self) -> None:
        if not self.caponen:
            print("Sihhh.....")
       
    def drink (self) -> None:
        if not self.caponen:
            print("You need to open the bottle first!")
        else:
            print(f"Glug glug glug... {self.brand}")