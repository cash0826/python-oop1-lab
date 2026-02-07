#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    
    def get_size(self):
        return self._size
    
    def set_size(self, input):
        if isinstance(input, str) and input in ("Small", "Medium", "Large"):
            self._size = input
        else:
            print("size must be Small, Medium, or Large")
            
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
        
    size = property(get_size, set_size)

latte = Coffee("Medium", 2.99)
print(latte.size)
latte.size = "no size"
black = Coffee("Medium", 1.99)
black.size = "Small"
black.price = 1.50
print("Black", black.size, black.price)