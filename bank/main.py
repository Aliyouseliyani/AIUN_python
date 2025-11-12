from utils import Bank

print("Welcome to the Bank app!")

account_name = input("For start enter your account name: ").strip()
account = Bank(account_name)

while True:
    print(
        f"How many accounts do you want\nyou already have {account.len_accounts()} accounts"
        f"\n\033[33mto continue without adding account enter 0:\033[0m ")

    new_accounts_number = input("Enter: ")
    if int(new_accounts_number) > 0:
        new_accounts_dic = {}
        for x in range(int(new_accounts_number)):
            new_account_balance = input(f'enter the balance of account: {x + account.len_accounts() + 1}: ')
            try:
                new_account_balance = int(new_account_balance)
                if new_account_balance < 0:
                    new_account_balance = 0
            except:
                new_account_balance = 0

            new_accounts_dic.update({x + account.len_accounts() + 1: new_account_balance})
        print(account.create_accounts(new_accounts_dic))
        break
    elif new_accounts_number == "0":
        break
    else:
        print('\033[92mto Enter number of accounts correctly 0:\033[0m ')


while True:
    account = Bank(account_name)
    print("\nPlease choose an option:")
    print("\n1. Balance of all accounts")
    print("\n2. Deposit into account")
    print("\n3. Withdrawal from account")
    print("\n4. Show all accounts with above average balance")
    print("\n5. Exit")

    status = input("\nEnter your choice (1-5):")

    if status == '5':
        print("\nThank you for using the To Do List Application. \nComeback soon!")
        break

    if status == '1':

        balances = dict(account.all_accounts())

        for k, v in balances.items():
            print(f'account number : \033[92m{k}\033[0m with \033[91m{v}\033[0m Rial balance \n')

    elif status == '2':
        balances = dict(account.all_accounts())

        while True:
            print('Choose a bank account to continue')
            print("To exit to main menu enter exit")

            for k, v in balances.items():
                print(f"\n {int(k)} : {v} \n")

            chosen_balance = input('Enter account number: ')
            if chosen_balance == 'exit':
                break
            deposit_amount = input('Enter deposit amount: ')

            print(account.deposit_account(chosen_balance, deposit_amount))

            break

    elif status == '3':
        balances = dict(account.all_accounts())
        while True:
            print('Choose a bank account to continue')
            print("To exit to main menu enter exit")

            for k, v in balances.items():
                print(f"\n {int(k)} : {v} \n")
            chosen_balance = input('Enter account number: ')
            if chosen_balance == 'exit':
                break
            deposit_amount = input('Enter amount: ')

            print(account.withdrawal_account(chosen_balance, deposit_amount))

            break

    elif status == '4':

        balances = dict(account.all_accounts_with_above_avg())

        for k, v in balances.items():
            print(f'account number : \033[92m{k}\033[0m with \033[91m{v}\033[0m Rial balance \n')
