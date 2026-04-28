from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate_cost(self) -> float:
        pass

    def __str__(self):
        return f"{self.name}: ${self.calculate_cost():.2f}"


class ByWeightItem(Item):
    def __init__(self, name: str, weight: float, cost_per_pound: float):
        super().__init__(name)
        self.weight = weight
        self.cost_per_pound = cost_per_pound

    def calculate_cost(self) -> float:
        return self.weight * self.cost_per_pound


class ByQuantityItem(Item):
    def __init__(self, name: str, quantity: int, cost_each: float):
        super().__init__(name)
        self.quantity = quantity
        self.cost_each = cost_each

    def calculate_cost(self) -> float:
        return self.quantity * self.cost_each


class Grapes(ByWeightItem):
    def __init__(self, weight: float):
        super().__init__("Grapes", weight, 2.99) 


class Bananas(ByWeightItem):
    def __init__(self, weight: float):
        super().__init__("Bananas", weight, 0.59)


class Oranges(ByQuantityItem):
    def __init__(self, quantity: int):
        super().__init__("Oranges", quantity, 0.75)


class Cantaloupes(ByQuantityItem):
    def __init__(self, quantity: int):
        super().__init__("Cantaloupes", quantity, 3.50)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def calculate_total(self) -> float:
        return sum(item.calculate_cost() for item in self.items)

    def get_items(self):
        return self.items

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    order = Order()


    order.add_item(Grapes(2.5)) 
    order.add_item(Bananas(3.2)) 
    order.add_item(Oranges(6)) 
    order.add_item(Cantaloupes(2)) 


    print("------ RECEIPT ------")
    for item in order.get_items():
        print(item)

    print("---------------------")
    print(f"Total items: {len(order)}")
    print(f"Total cost: ${order.calculate_total():.2f}")

