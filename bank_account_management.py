def get_balance(account_number: str) -> float:
    with open('account.txt', 'r') as file:
        for line in file:
            acc_num, balance = line.strip().split(',')
            if acc_num == account_number:
                return float(balance)
    return 0.0

def update_account(account_number: str, balance: float):
    lines = []
    with open('account.txt', 'r') as file:
        lines = file.readlines()
    
    with open('account.txt', 'w') as file:
        for line in lines:
            acc_num, bal = line.strip().split(',')
            if acc_num == account_number:
                file.write(f"{account_number},{balance}\n")
            else:
                file.write(line)

def deposit(account_number: str, amount: float):
    balance = get_balance(account_number)
    balance += amount
    update_account(account_number, balance)

def withdraw(account_number: str, amount: float):
    balance = get_balance(account_number)
    if balance >= amount:
        balance -= amount
        update_account(account_number, balance)
    else:
        print("Insufficient balance")

deposit('12345', 800.0)
print(get_balance('12345'))
withdraw('67890', 200.0)
print(get_balance('67890'))
