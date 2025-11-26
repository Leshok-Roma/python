class CoffeeShopError(Exception):
    pass

class CoffeeNotFoundError(CoffeeShopError):
    pass

class CoffeeExistsError(CoffeeShopError):
    pass

class InvalidSizeError(CoffeeShopError):
    pass

class Coffee(): 
    
    def __init__(self, name='', coffee_type='', base_price=0.0, available_sizes=None): 
        self.name = name
        self.coffee_type = coffee_type
        self.base_price = base_price
        self.available_sizes = available_sizes if available_sizes else []
    
    def get_info(self):
        sizes_prices = ", ".join([f"{size}ml (${self.calculate_price(size):.2f})" 
                                for size in self.available_sizes])
        return f"{self.name} ({self.coffee_type}) - {sizes_prices}"
        
    
    def calculate_price(self, size):
        size_multiplier = {200: 1.0 , 300: 1.1 ,400: 1.2, 500: 1.3}
        return self.base_price * size_multiplier.get(size, 1.0)

class CoffeeOrder(): 
    
    def __init__(self, number=0): 
        self.number = number
        self.items = []  
    
    def add_item(self, coffee, size, quantity):
        if quantity <= 0:
            raise InvalidSizeError("quantity should be positive")
        if size not in coffee.available_sizes:
            raise InvalidSizeError(f"size {size}ml isn't available for {coffee.name}")
        
        self.items.append({'coffee': coffee,'size': size, 'quantity': quantity })
    
    def remove_item(self, index):
        if index < 0 or index >= len(self.items):
            raise CoffeeNotFoundError("item not found in order")

        del self.items[index]
    
    def get_total(self):
        total = 0.0
        for item in self.items:
            price = item['coffee'].calculate_price(item['size'])
            total += price * item['quantity']
        return total
    
    def show_order(self):
        if not self.items:
            print("order is empty")
            return
        
        print(f"Order N{self.number}:")
        for i, item in enumerate(self.items, 1):
            coffee = item['coffee']
            size = item['size']
            quantity = item['quantity']
            price = coffee.calculate_price(size)
            total = price * quantity
            print(f"  {i}. {coffee.name} {size}ml x {quantity} - ${total:.2f}")
        print(f"Total: ${self.get_total():.2f}")


class CoffeeShop(): 
    def __init__(self, name=''): 
        self.name = name
        self.espresso_drinks = {}
        self.milk_drinks = {}
        self.special_drinks = {}
        self.order_counter = 1
    
    def add_coffee(self, name, coffee_type, base_price, available_sizes):
        name = name.lower()
        coffee_type = coffee_type.lower()
        
        
        if (name in self.espresso_drinks or 
            name in self.milk_drinks or 
            name in self.special_drinks):
            raise CoffeeExistsError(f"coffee '{name}' already exists")
        
        if base_price <= 0:
            raise ValueError("base_price have to be positive")        
        if not available_sizes:
            raise InvalidSizeError("available_sizes cannot be empty")        
        coffee = Coffee(name, coffee_type, base_price, available_sizes)        
        if coffee_type == 'espresso':
            self.espresso_drinks[name] = coffee
        elif coffee_type == 'milk':
            self.milk_drinks[name] = coffee
        elif coffee_type == 'special':
            self.special_drinks[name] = coffee
        else:
            raise ValueError("coffee_type must be espresso, milk or special")
    
    def remove_coffee(self, name):
        name = name.lower()        
        if name in self.espresso_drinks:
            del self.espresso_drinks[name]
        elif name in self.milk_drinks:
            del self.milk_drinks[name]
        elif name in self.special_drinks:
            del self.special_drinks[name]
        else:
            raise CoffeeNotFoundError(f"coffee '{name}' not found")
    
    def find_coffee(self, coffee_name):        
        coffe_name = coffee_name.lower()
        if coffee_name in self.espresso_drinks:
            return self.espresso_drinks[coffee_name]
        elif coffee_name in self.milk_drinks:
            return self.milk_drinks[coffee_name]
        elif coffee_name in self.special_drinks:
            return self.special_drinks[coffee_name]
        else:
            return None
    
    def show_menu(self):
        print(f"{self.name} MENU:")
        if self.espresso_drinks:
            print("Espresso drinks:")
            for coffe in self.espresso_drinks.values():
                print(f' {coffe.get_info()} ')        
        if self.milk_drinks:
            print("Milk drinks:")
            for coffee in self.milk_drinks.values():
                print(f"  {coffee.get_info()}")
        
        if self.special_drinks:
            print("Special drinks:")
            for coffee in self.special_drinks.values():
                print(f"  {coffee.get_info()}")
    
    def create_order(self):
       pass
    
    def print_receipt(self, order):
        filename = f'coffee_receipt_{order.number}.txt'        
        with open(filename, 'w') as f:
            f.write(f" {self.name} receipt ")            
            f.write(f"Order: N{order.number}")
            
            for item in order.items:
                coffee = item['coffee']
                size = item['size']
                quantity = item['quantity']
                price = coffee.calculate_price(size)
                total = price * quantity
                f.write(f"{coffee.name} {size}ml * {quantity} - ${total:.2f}\n")
            
            f.write(f"\nTOTAL: ${order.get_total():.2f}\n")
            f.write("Enjoy your coffee!")
        
        print(f'receipt saved to {filename}')

coffee_shop = CoffeeShop("CoffeeShop")
try:
    coffee_shop.add_coffee("espresso", "espresso", 2.00, [200, 300])
    coffee_shop.add_coffee("americano", "espresso", 2.50, [300, 400, 500])
    coffee_shop.add_coffee("cappuccino", "milk", 2.70, [300, 400])
    coffee_shop.add_coffee("latte", "milk", 3.00, [300, 400, 500])
    
    coffee_shop.add_coffee("raf", "special", 4.00, [300, 400, 500])
except CoffeeShopError as e:
    print(f'Error: {e}')

while True: 
    print("\ncoffee shop")
    print("1: show menu")
    print("2: add coffee")
    print("3: remove coffee")
    print("4: create order")
    print("0: exit")
    choice = input("choose action: ") 
    try:
        if choice == "1": 
            coffee_shop.show_menu()
        
        elif choice == '2': 
            name = input("coffee name: ")
            coffee_type = input("type (espresso/milk/special): ")
            base_price = float(input("base price for 200ml: "))
            sizes_input = input("available sizes: (200,300,400): ")
            available_sizes = [int(size.strip()) for size in sizes_input.split(',')]            
            coffee_shop.add_coffee(name, coffee_type, base_price, available_sizes)
            print("coffee added successfully")
        
        elif choice == '3': 
            name = input("coffee name: ")
            coffee_shop.remove_coffee(name)            
            print(f"{name} coffee removed ")

        elif choice == '4': 
            coffee_shop.create_order()
        
        elif choice == '0':
            print("HAPPY END")
            break
        else: 
            print("incorrect input")
            
    except (CoffeeShopError, ValueError) as e: 
        print(f'Error: {e}')    