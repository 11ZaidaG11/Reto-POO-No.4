class MenuItem():
    def __init__(self, name:str, price:float):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name
    
    def total_price(self):
        return self._price

class Beverage(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_beverage(self):
        return self.get_name()
    
    def set_beverage(self):
        for i in menu["Beverage"]:
            print(f"{i.get_beverage()} ... ${i.total_price()}")

        or_bev = input("What would you like to drink?: ").capitalize()
        if or_bev == "Nothing":
            return
        for b in menu["Beverage"]:
            if b.get_beverage() == or_bev:
                new_order.add_food(Beverage(or_bev, b.total_price()))
                print(f"{or_bev} added to your order.")
                return
            else:
                print("Not an option")

class Appetizer(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_appetizer(self):
        return self.get_name()
    
    def set_appetizer(self):
        for i in menu["Appetizer"]:
            print(f"{i.get_appetizer()} ... ${i.total_price()}")

        or_app = input("What would you like to eat to start?: ").capitalize()
        if or_app == "Nothing":
            return
        for a in menu["Appetizer"]:
            if a.get_appetizer() == or_app:
                new_order.add_food(Appetizer(or_app, a.total_price()))
                return
            else:
                print("Not an option")

class MainCourse(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_main_course(self):
        return self.get_name()
    
    def set_main_course(self):
        for item in menu["MainCourse"]:
            print(f"{item.get_main_course()} ... ${item.total_price()}")

        or_main = input("What would you like to eat?: ").capitalize()
        if or_main == "Nothing":
            return
        for m in menu["MainCourse"]:
            if m.get_main_course() == or_main:
                new_order.add_food(MainCourse(or_main, m.total_price()))
                return
            else:
                print("Not an option")

class Order():
    def __init__(self):
        self.food = []

    def add_food(self, food:MenuItem):
        self.food.append(food)

    def price(self):
        sum = 0
        for i in self.food:
            sum += i.total_price()
        return sum

def options(menu:dict, new_order:Order):
    flag = "yes"
    while flag == "yes":
        orr = input("\nWhat would you like to order?: Beverage, Appetizer or Main Course: ").capitalize()
        match orr:
            case "Beverage":
                Beverage("", 0).set_beverage()
            case "Appetizer":
                Appetizer("", 0).set_appetizer()
            case "Maincourse":
                MainCourse("", 0).set_main_course()
            case _:
                print("Not an option")
        flag = input("Would you like something else? (yes/no): ").lower()
    return new_order.price()

class PayForm:
    def __init__(self):
        pass
    def pay(self, money):
        pass

class Cash(PayForm):
    pass
class Card(PayForm):
    pass
    
def user_pay():
    total = options(menu, new_order)
    print(f"\nYour total is: ${total}")
    user = input("How would you like to pay cash or card?: ")
    if user == "card":
        pass
    elif user == "cash":
        pass
    else:
        print("Not an option")

if __name__ == "__main__":
    menu = {
        "Beverage": [
            Beverage("Soda", 5),
            Beverage("Lemonade", 4),
            Beverage("Milkshake", 7)
        ],
        "Appetizer": [
            Appetizer("Soup", 12),
            Appetizer("Salad", 10),
            Appetizer("Waffles", 8)
        ],
        "MainCourse": [
            MainCourse("Pizza", 15),
            MainCourse("Chicken", 18),
            MainCourse("Beef", 20),
            MainCourse("Sushi", 25)
        ]
    }

    new_order = Order()

    print("--- Welcome to Zaida & Waffles ---")
    print("We can offer you:")
    for i in menu:
        print(f"-{i}")