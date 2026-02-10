from dataclasses import dataclass # comes from the standard library module 'dataclasses'. Have to be imported 

@dataclass
class Item:
    SEPARATOR = ","
    name: str
    value: float
    category: str
    weight: float

    @staticmethod
    def deserialize(row):
        columns = row.split(Item.SEPARATOR) # Comme seperated values
        item = Item(
            columns[0], # name
            columns[1], # value
            columns[2], # category
            columns[3],  # weight

        )
        return item
    
    def display_price(self):
        print(f'{self.name} costs {self.value} £.')
        return None
    
        