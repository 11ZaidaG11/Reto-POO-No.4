class MenuItem():
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price

    def total_price(self):
        return self.price

class Beverage(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Appetizer(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class MainCourse(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Order():
    def __init__(self):
        self.food = []

    def add_food(self, food:MenuItem):
        self.food.append(food)

    def price(self):
        suma = 0
        for i in self.food:
            suma += i.total_price()
        return suma

def options(menu:dict, new_order:Order):
    flag = "yes"
    while flag == "yes":
        orr = input("What would you like to order?: ").capitalize()
        match orr:
            case "Beverage":
                for i, p in menu["Beverage"].items():
                    print(f"{i} ${p}")
                or_bev = input("What would you like to eat?: ").capitalize()
                if or_bev in menu["Beverage"]:
                    price = menu["Beverage"][or_bev]
                    new_order.add_food(Beverage(or_bev, price))
                else:
                    print("Not an option")
                    
            case "Appetizer":
                for i, p in menu["Appetizer"].items():
                    print(f"{i} ${p}")
                or_app = input("What would you like to eat to start?: ").capitalize()
                if or_app in menu["Appetizer"]:
                    price = menu["Appetizer"][or_app]
                    new_order.add_food(Appetizer(or_app, price))
                else:
                    print("Not an option")
    

            case "MainCourse":
                for i, p in menu["MainCourse"].items():
                    print(f"{i} ${p}")
                or_main = input("What would you like to eat?: ").capitalize()
                if or_main in menu["MainCourse"]:
                    price = menu["MainCourse"][or_main]
                    new_order.add_food(MainCourse(or_main, price))
                else:
                    print("Not an option")
            case _:
                print("Not an option")

        flag = input("Would you like something else?: ").lower()
    return new_order.price()

if __name__ == "__main__":
    menu = {
        "Beverage": {"Soda": 5, "Limonade": 4, "MilkShake": 7},
        "Appetizer": {"Soup": 12, "Salad": 10, "Wafles": 8},
        "MainCourse": {"Pizza": 15, "Chicken": 18, "Beef": 20, "Sushi": 25}
    }

    new_order = Order()

    print("---Welcome to Zaida & Wafles---")
    print("We can offer you:")
    for i in menu.items():
        print(i[0])

    op = options(menu, new_order)
    print(op)