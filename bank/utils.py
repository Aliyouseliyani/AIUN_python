import os
import json


class DataBase():
    def __init__(self, file_name='data.json'):
        self.path = os.path.join('db', file_name)

    def open_json(self):
        try:
            with open(self.path, 'r', encoding='UTF-8') as f:
                return json.load(f)
        except Exception as e:
            print(e)

    def save_json(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)


class Bank(DataBase):
    def __init__(self, account_name):
        super().__init__()

        self.ac_name = account_name

        self.account = self.create_get_account()

    def len_accounts(self):
        return len(self.account.values())

    def create_get_account(self):
        data = self.open_json()

        data = dict(data)
        if self.ac_name in data.keys():
            return data[self.ac_name]
        else:
            new_ac = {self.ac_name: {}}
            data.update(new_ac)
            self.save_json(data)
            return data[self.ac_name]

    def all_accounts(self):
        return self.account

    def deposit_account(self, account_number, amount):
        data = self.open_json()

        try:
            int(amount)
        except:
            return '\033[91mEnter amount correctly\033[0m'

        try:
            data[self.ac_name][account_number]
        except:
            return '\033[91mChosen account does not exists\033[0m'

        current_balance = int(data[self.ac_name][account_number])
        data[self.ac_name][account_number] = int(current_balance) + int(amount)

        self.save_json(data)

        return '\033[92mDeposit operation was successfully\033[0m'

    def withdrawal_account(self, account_number, amount):
        data = self.open_json()

        try:
            int(amount)
        except:
            return '\033[91mEnter amount correctly\033[0m'

        try:
            data[self.ac_name][account_number]
        except:
            return '\033[91mChosen account does not exists\033[0m'

        current_balance = int(data[self.ac_name][account_number])
        if int(amount) <= current_balance:
            data[self.ac_name][account_number] = current_balance - int(amount)
        else:
            return "\033[91mbalance is not enough for withdrawal\033[0m"

        self.save_json(data)

        return '\033[92mWithdrawal operation was successfully\033[0m'

    def all_accounts_with_above_avg(self):
        balances = self.account

        total = [x for x in balances.values()]
        avg = sum(total) / len(balances)

        result = {}
        for k, v in balances.items():
            if v >= avg:
                result.update({k: v})

        return result

    def create_accounts(self, accounts_dic):

        data = self.open_json()

        try:
            data[self.ac_name].update(accounts_dic)
        except Exception as e:
            return f'\033[91{e}\033[0m'

        self.save_json(data)
        return "\033[92mCreating accounts was successful\033[0m"
