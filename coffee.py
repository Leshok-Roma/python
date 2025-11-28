class CoffeeError(Exception):
    pass

class CoffeeNotFoundError(CoffeeError):
    pass

class InvalidInputError(CoffeeError):
    pass

class SizeNotFoundError(CoffeeError):
    pass


class Coffee:
    def __init__(self, name):
        self.name = name
        self.prices = {}  
    
    def add_size(self, size, price):
        if price <= 0:
            raise InvalidInputError("Price must be positive")
        self.prices[size] = price
    
    def get_info(self):
        info = f"{self.name}: "
        sizes_info = []
        for size, price in self.prices.items():
            sizes_info.append(f"{size}ml - ${price:.2f}")
        return info + ", ".join(sizes_info)
    
    def get_price(self, size):
        if size not in self.prices:
            raise SizeNotFoundError(f"Size {size}ml doesn't available for {self.name}")
        return self.prices[size]
    
class Order:
    
    def __init__ (self, number):
        self.number = number 
        self.items = []

    def add_coffee(self, coffee_name, size , quantity , price):
        if quantity <= 0  : 
            raise InvalidInputError("Quantity must be positive")
        self.items.append({
            "coffee": coffee_name,
            "size": size, 
            "quantity" : quantity , 
            "price": price 
        })
    
    def remove_coffee(self, index ):
        if index < 0 or index >= len(self.items):
            raise CoffeeNotFoundError("Coffee wasn't found in order")
        del self.items[index]

    def get_total(self): 
        total    = 0.0 
        for item in self.items:
            total += item['quantity'] * item['price']
        return total
    
    def show_order(self):
        if not self.items:
            print("Order is empty")
            return
        print(f'Order N{self.number}: ')
        total_sum = 0.0 
        for i , item in enumerate(self.items, 1 ):
            item_total = item['price'] * item['quantity'] 
            total_sum += item_total
            print(f"{i}. {item['coffee']} {item['size']}ml x {item['quantity']} - ${item_total:.2f}")  # ИСПРАВЛЕНО: кавычки и символ $
        print(f'Total: ${total_sum:.2f}')  
    
    def is_empty(self):
        return len(self.items) == 0
class CoffeeShop:
    
    def __init__(self, name):
        self.name = name
        self.menu  = {}
        self.order_counter = 1 
    
    def add_coffee_to_menu(self, name):
        # if name in self.menu:  
        #     raise CoffeeError(f"Coffee {name} already exists") 
        self.menu[name] = Coffee(name)
        print(f"Coffee {name} was added to menu")

    def add_size_to_coffee(self, coffee_name, size, price):
        if coffee_name not in self.menu:
            raise CoffeeNotFoundError(f"Coffee {coffee_name} wasn't found in menu")
        self.menu[coffee_name].add_size(size, price)
        print(f'Size {size}ml was added for coffee {coffee_name}')    
    
    def remove_coffee_from_menu(self, coffee_name):
        if coffee_name not in self.menu:
            raise CoffeeNotFoundError(f"Coffee '{coffee_name}' not found in menu")
        
        del self.menu[coffee_name]
        print(f"Coffee '{coffee_name}' removed from menu")
    
    def show_menu(self):
        if not self.menu:
            print("Menu is empty")
            return
        print("Menu:")
        for coffee in self.menu.values():
            print(f'  {coffee.get_info()}') 
    
    def create_order(self):
        order = Order(self.order_counter)
        self.order_counter += 1
        
        while True:
            print(f"\nOrder {order.number}")  
            order.show_order()
            print("\n1. Add coffee")
            print("2. Remove coffee")
            print("3. Finish order")
            print("4. Cancel order")
            choice = input("Choose action: ")           
            try:
                if choice == "1":
                    self.show_menu()
                    coffee_name = input("Coffee name: ")
                    
                    if coffee_name not in self.menu:
                        raise CoffeeNotFoundError("Coffee wasn't found in menu")  
                    
                    coffee = self.menu[coffee_name]
                    print(f"Available sizes for {coffee_name}:")
                    for size, price in coffee.prices.items():
                        print(f"  {size}ml - ${price:.2f}")  
                    
                    size = int(input("Size (ml): "))
                    quantity = int(input("Quantity: "))
                    
                    price = coffee.get_price(size)
                    order.add_coffee(coffee_name, size, quantity, price)
                    print(f"Added {quantity} x {coffee_name} {size}ml")
                
                elif choice == "2":
                    if order.is_empty():
                        print("Order is empty")
                        continue
                    
                    order.show_order()
                    index = int(input("Item number to remove: ")) - 1
                    removed_item = order.items[index]
                    order.remove_coffee(index)
                    print(f"Removed: {removed_item['coffee']} {removed_item['size']}ml")
                
                elif choice == "3":
                    if not order.is_empty():
                        self.save_receipt(order)
                        print("Order completed successfully")
                        break
                    else:
                        print("Order is empty, cannot finish empty order")
                        continue  
                
                elif choice == "4":
                    print("Order cancelled")
                    break                      
                else:
                    print("Invalid choice")
            
            except (CoffeeError, ValueError) as e:
                print(f"Error: {e}")
    
    def save_receipt(self, order):
        filename = f"order_receipt_{order.number}.txt"
        with open(filename, 'w') as f: 
            f.write(f"{self.name}\n")
            f.write(f"Order N{order.number}\n\n")
            for item in order.items:
                total = item["price"] * item['quantity']
                f.write(f"{item['coffee']} {item['size']}ml x {item['quantity']} - ${total:.2f}\n")  # ИСПРАВЛЕНО: кавычки и символ $
            f.write(f"\nTotal: ${order.get_total():.2f}\n")  
        print(f'Receipt was saved to file: {filename}')

def main():
    coffee_shop = CoffeeShop("Coffee Time")
    coffee_shop.add_coffee_to_menu("Espresso")
    try:
        coffee_shop.add_coffee_to_menu("Espresso")
        coffee_shop.add_coffee_to_menu("Americano")
        coffee_shop.add_coffee_to_menu("Cappuccino")
        coffee_shop.add_coffee_to_menu("Latte")              
        coffee_shop.add_size_to_coffee("Espresso", 200, 1.00)
        coffee_shop.add_size_to_coffee("Espresso", 300, 1.50)        
        coffee_shop.add_size_to_coffee("Americano", 300, 2.0)
        coffee_shop.add_size_to_coffee("Americano", 400, 2.50)
        coffee_shop.add_size_to_coffee("Americano", 500, 3.00)        
        coffee_shop.add_size_to_coffee("Cappuccino", 300, 3.00)
        coffee_shop.add_size_to_coffee("Cappuccino", 400, 3.50)        
        coffee_shop.add_size_to_coffee("Latte", 300, 3.50)
        coffee_shop.add_size_to_coffee("Latte", 400, 4.00)
        coffee_shop.add_size_to_coffee("Latte", 500, 4.50)
        
    except CoffeeError as e:
         print(f"Error: {e}")   
    
    while True:
        print("\nCoffee Shop")  
        print("1. Show menu")
        print("2. Add coffee to menu")
        print("3. Add size to coffee")
        print("4. Remove coffee from menu")
        print("5. Create order")
        print("6. Exit")
        
        choice = input("Choose action: ")        
        try:
            if choice == "1":
                coffee_shop.show_menu()            
            elif choice == "2":
                name = input("Coffee name: ")
                coffee_shop.add_coffee_to_menu(name)            
            elif choice == '3':
                coffee_name = input("Coffee name: ")
                size = int(input("Size (ml): "))
                price = float(input("Price: ")) 
                coffee_shop.add_size_to_coffee(coffee_name, size, price)  
            elif choice == "4":
                name = input("Coffee name to remove: ")
                coffee_shop.remove_coffee_from_menu(name)            
            elif choice == "5":
                coffee_shop.create_order()            
            elif choice == "6":
                print("Happy end!")
                break
            
            else:
                print("Incorrect choice. Try again")
        
        except (CoffeeError, ValueError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()