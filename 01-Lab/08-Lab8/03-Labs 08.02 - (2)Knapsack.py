"""Labs 08.02 - (2)Knapsack"""
class Item :
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def Item(self, name, price, weight) :
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self) :
        return self.__name
    
    def get_price(self) :
        return self.__price
    
    def get_weight(self) :
        return self.__weight
    
    def get_cost(self) :
        return self.__price / self.__weight

def knapsack(itemList, amount) :
    totalPrice = 0
    tmp = []
    itemList.sort(key=lambda item :item.get_cost(),reverse = True)
    print(f"Knapsack Size: {amount:.1f} kg\n===============================")
    for x in itemList :
        if x.get_weight() <= amount:
            totalPrice += x.get_price()
            amount -= x.get_weight()
            tmp.append(x)
    for i in tmp :
        print(f"{i.get_name()} -> {i.get_weight()} kg -> {i.get_price()} THB")
    print(f"Total: {totalPrice} THB")

def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()

# แต่ละข้อคะแนนเท่ากัน ไม่ให้จดเข้า