class Shoe:

    # Initializes instance attributes.
    def __init__(self, country: str, code: int, product: str, cost: float, quantity: int):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Represents objects as strings.
    def __repr__(self) -> str:   
        return (f'''\n\t\tShoe name: {self.product}
        \tCountry: {self.country}
        \tCost: {self.cost}
        \tQuantity: {self.quantity}''')