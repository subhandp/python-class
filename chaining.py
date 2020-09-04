data = []
class Cart():
    def __init__(self, data):
        self.data = data
    def showAll(self):
        print (self.data)
        return self
    def addItem(self,value):
        self.data.append(value)
        return self
    def removeItem(self,value):
        for i, val in enumerate(self.data):
            if val['_id'] == value['_id']: 
                del self.data[i]
        return self
    def addDiscount(self,value):
        value = int(value.split('%')[0])
        for i, val in enumerate(self.data):
            self.data[i]['price'] = self.data[i]['price'] - (self.data[i]['price'] * value / 100)
        return self
    @property
    def totalItems(self):
        print("Total Items:", len(self.data))
        return self
    @property
    def totalQuantity(self):
        total = sum(item['quantity'] for item in self.data)
        print("total Quantity:",total)
        return self

    @property
    def totalPrice(self):
        total = sum(item['price'] * item['quantity'] for item in self.data)
        print("Total Price:",total)
        return self
    def checkout(self,filename,ext):
        import json
        f = open(f"{filename}.{ext}", "w")
        f.write(json.dumps(self.data))
        f.close()



cart = Cart(data)
(
cart.addItem({ '_id': 1, 'price': 30000, 'quantity': 3 })
    .addItem({ '_id': 2, 'price': 10000 })              
    .addItem({ '_id': 3, 'price': 5000, 'quantity': 2 })
    .removeItem({'_id': 2})
    .addItem({ '_id': 4, 'price': 400, 'quantity': 6 })
    .addDiscount("50%")
    .showAll()
    .totalItems
    .totalQuantity
    .totalPrice
)