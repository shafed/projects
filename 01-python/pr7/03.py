class Family:
    def __init__(self, name, money, house) -> None:
        self.name = name
        self.money = money
        self.house = house

    def info(self):
        print(
            "Family name:",
            self.name,
            "\nFamily funds:",
            self.money,
            "\nHaving house:",
            self.house,
        )

    def earn_money(self, plus):
        self.money += plus
        print(f"Earned {plus} money!")
        print("Current value:", self.money)

    def buy_house(self, price, discount=0):
        if self.money >= price * (1 - discount):
            print("House purchased!")
            print("Current money:", self.money)
        else:
            print("Not enough money!")
            print("Try to buy a house again")
