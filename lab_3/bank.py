class BankError(Exception):
    pass

class AccountNotFoundError(BankError):
    pass

class InsufficientFundsError(BankError):
    pass

class AccountExistsError(BankError):
    pass


class Client(): 
    
    def __init__(self, first_name, surname, passports_index): 
        self.first_name = first_name
        self.surname = surname 
        self.accounts = {} 
        self.passport_index = passports_index 
    
    def get_info(self):
        if not self.accounts: 
            print("You dont have accounts ")
        for cur, val in self.accounts.items(): 
            print(f"currency :{cur}, balance: {val}")  
    
    def open_account(self, currency): 
        currency = currency.upper()
        if currency not in self.accounts:
            self.accounts[currency] = 0.0
        else: 
             raise AccountExistsError(f"account in {currency} already exists")
    
    def deposit(self, currency, amount):  
        if currency in self.accounts:
            if amount > 0: 
                self.accounts[currency] += amount
            else: 
                  raise ValueError("amount have to be positiv")
        else: 
          raise AccountNotFoundError("can't find this account")
    
    def withdraw(self, currency, amount): 
        if currency in self.accounts:
            if amount > 0:
                if self.accounts[currency] >= amount:  
                    self.accounts[currency] -= amount
                else:
                    raise InsufficientFundsError("Insufficient funds")
            else: 
                raise ValueError("amount have to be positiv")
        else: 
            raise AccountNotFoundError("can't find this account")
        
    def show_accounts(self): 
        if not self.accounts: 
            print("accounts don't exist")
            return
        for cur, val in self.accounts.items(): 
            print(f"currency: {cur}, value: {val:.2f}")
        print(f'total: {self.total_value()}')
    
    def transfer_accounts(self, from_curr, to_curr, amount): 
        rate = {  
        "BYN": 1.0,
        "USD": 3.00,
        "EUR": 3.4900
        }
        from_currency = from_curr.upper() 
        to_currency = to_curr.upper()     
        if from_currency not in self.accounts:
            raise AccountNotFoundError("can't find this account")
        if to_currency not in self.accounts:
            raise AccountNotFoundError("can't find this account")
        if amount <= 0:
            raise ValueError("amount have to be positiv")
        if self.accounts[from_currency] < amount:  
            raise InsufficientFundsError("Insufficient funds")
        self.accounts[from_currency] -= amount
        if from_currency == to_currency:
            converted = amount
        else:
            in_byn = amount * rate[from_currency]  
            converted = in_byn / rate[to_currency] 
        self.accounts[to_currency] += converted
    
    def get_accounts(self): 
        return self.accounts
    
    def total_value(self): 
        rates = {
            "BYN": 1.0,
            "USD": 3.00,
            "EUR": 3.4900
        }
        sum = 0
        for cur, val in self.accounts.items():
            rate = rates.get(cur.upper(), 1)
            sum += val * rate 
        return sum 
    
    def statement(self): 
        if not self.accounts: 
            print("accounts don't exist")
            return
        filename = f'statement of {self.first_name} {self.surname} {self.passport_index}.txt'
        with open(filename, 'w') as f: 
            f.write(f"first name: {self.first_name}\n")
            f.write(f'surname: {self.surname}\n')
            f.write(f'passports_index: {self.passport_index}\n')  
            for cur, val in self.accounts.items(): 
                f.write(f'currency: {cur}, value: {val:.2f}\n')
            f.write(f"total(BYN): {self.total_value():.2f}\n")
        print(f'statement in {filename}')

class Bank(): 
    def __init__ (self): 
        self.clients = {} 

    def add_client(self, first_name, surname, passports_index):
            if passports_index in self.clients:
                print(f'client with passports_index: {passports_index} already exist')
            else: 
                self.clients[passports_index] = Client(first_name, surname, passports_index)
    
    def get_client(self, passports_index):
        return self.clients.get(passports_index)
    
    def transfer(self, sender_id, receiver_id, amount, sender_currency, receiver_currency): 
        sender = self.get_client(sender_id)
        receiver = self.get_client(receiver_id) 
        rate = {
        "BYN": 1.0,
        "USD": 3.00,
        "EUR": 3.4900    
        }
        sender_currency = sender_currency.upper()
        receiver_currency = receiver_currency.upper()
        if not sender or not receiver:
            raise BankError("clients don't exist")
        if sender_currency not in sender.accounts:
            raise AccountNotFoundError("sender doesn't have account in this currency")
        if receiver_currency not in receiver.accounts:
            raise AccountNotFoundError("receiver doesn't have account in this currency")
        if amount <= 0:
            raise ValueError("amount have to be positiv")
        if sender.accounts[sender_currency] < amount:  
            raise InsufficientFundsError("Insufficient funds")
        sender.withdraw(sender_currency, amount)
        if sender_currency == receiver_currency:
            converted_amount = amount
        else:
            amount_in_byn = amount * rate[sender_currency]
            converted_amount = amount_in_byn / rate[receiver_currency]
        receiver.deposit(receiver_currency, converted_amount)





bank = Bank()
while True: 
    print("1: add client")
    print("2: open account")
    print("3: deposit")
    print("4: withdraw")
    print("5: transfer between clients")
    print("6: transfer between accounts")
    print("7: show accounts")
    print("8: statement")
    print("9: list of clients")
    print("q: exit")

    choice = input("choose action: ") 

    try:
        if choice == "1": 
            first_name = input("first_name: ")
            surname = input("surname: ")
            passports_index = input("passports_index: ")
            bank.add_client(first_name, surname, passports_index)
        
        elif choice == '2': 
            passports_index = input("passports_index: ")
            cur = input("currency: ")
            client = bank.get_client(passports_index)
            if client: 
                client.open_account(cur)
            else: 
                raise BankError("Client not found")

        
        elif choice == '3': 
            passports_index = input("passports_index: ")
            cur = input("currency: ")
            amount = float(input("amount: "))
            client = bank.get_client(passports_index)
            if client: 
                client.deposit(cur, amount)
            else:
                raise AccountNotFoundError("can't find this account")

        elif choice == '4': 
            passports_index = input("passports_index: ")
            cur = input("currency: ")
            amount = float(input("amount: "))
            client = bank.get_client(passports_index)
            if client: 
                client.withdraw(cur, amount)
            else: 
                raise AccountNotFoundError("can't find this account")
        
        elif choice == '5': 
            sender_passport_index = input('sender_passport_index: ')
            receiver_passport_index = input("receiver_passport_index: ")
            amount = float(input("amount: "))
            sender_currency = input('sender_currency: ')
            receiver_currency = input('receiver_currency: ')
            bank.transfer(sender_passport_index, receiver_passport_index, amount, sender_currency, receiver_currency) 
        
        elif choice == '6': 
            passports_index = input("passports_index: ")
            client = bank.get_client(passports_index)
            if client:
                from_ac = input("from account: ")
                to_ac = input("to_ac: ")
                amount = float(input("amount: "))
                client.transfer_accounts(from_ac, to_ac, amount)  
            else:
                raise AccountNotFoundError("can't find this account")
            
        elif choice =='7': 
            passports_index = input("passports_index: ")
            client = bank.get_client(passports_index)
            if client: 
                client.show_accounts()
            else: 
                raise AccountNotFoundError("can't find this account")

        elif choice == '8': 
            passports_index = input("passports_index: ")
            client = bank.get_client(passports_index)
            if client: 
                client.statement()
            else: 
                raise AccountNotFoundError("can't find this account")
        
        elif choice == '9':
            print("ALL CLIENTS:")
            for passports_ind, cl in bank.clients.items():
                print(f"{passports_ind}: {cl.first_name} {cl.surname}")
                if cl.accounts:
                    print("Accounts:")
                    for currency, balance in cl.accounts.items():
                        print(f"  - {currency}: {balance:.2f} {currency}")
                else:
                  print("Accounts: No accounts")
                
                total = cl.total_value()
                print(f"Total balance: {total:.2f} BYN")
                

        elif choice == 'q':
            print("THE END")
            break
        else: 
            print("incorrect input")
    except (BankError, ValueError) as e: 
          print(f'Error : {e}')