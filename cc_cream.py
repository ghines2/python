class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

'''class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue(shop)

    def take_order(self, customer, flavor, scoops):
        self.customer = customer
        self.flavor =  flavor
        self.num_scoops = 0
        if self.flavor is not None and scoops <= 3:
            print("Order Created")
        else:
            print("INVALID ORDER")

        order = {"customer": customer, "flavor": flavor, "scoops": int(scoops)}
        self.orders = Queue(order)

def show_all_orders():
        print(Queue())

    def dequeue(next_order):

class IceCreamShop:
    def __init__(self):
            self.items = []
        

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()'''