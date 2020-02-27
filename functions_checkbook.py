import os
import json
from datetime import datetime, date
from pprint import pprint

def add_json_entry(number, time, category):
    '''This function creates the dictionary that each transaction will fill'''
    transaction_dict = {}
    transaction_dict['amount'] = number
    transaction_dict['time'] = time
    transaction_dict['category'] = category
    return transaction_dict

def open_new_account():
    '''This function checks to see if a file named my_current_balance.txt already exists, and if not it creates it, adding a single initializing transaction'''
    if not os.path.exists('my_current_balance.json'):
        with open('my_current_balance.json', 'a+') as f:
            date_time = datetime.today().strftime('%m %d %Y %H:%M:%S')
            new_entry = add_json_entry('0', date_time, 'initial')
            x = json.dumps([new_entry], default=str)
            f.write(x)

def get_balance():
    '''This function finds the sum of all historical transactions and returns it'''
    transactions = json.load(open('my_current_balance.json'))
    balances  = [float(transaction['amount']) for transaction in transactions]
    return sum(balances)

def withdraw(number):
    '''This function pulls historical data from a json file and appends a withdrawal transaction to it, then writes it back to the json file. It checks if the user entered a number, and if that number is less than the current balance. If not, it goes back to the menu'''
    if number.replace('.','',1).isdigit():
        if get_balance() > float(number):
            transactions = json.load(open('my_current_balance.json'))
            with open('my_current_balance.json', 'w') as f:
                date_time = datetime.today().strftime('%m %d %Y %H:%M:%S')
                new_entry = add_json_entry(str(float(number) * -1), date_time,'withdrawal')
                transactions.append(new_entry)
                z = json.dumps(transactions, default=str)
                f.writelines(z)
            return new_entry
        else:
            print("You do not have the required funds for this transaction")
    else:
        print('You must enter a valid monetary value\n') 


def deposit(number):
    '''This function pulls historical data from a json file and appends a deposit transaction to it, then writes it back to the json file.'''
    if number.replace('.','',1).isdigit():
        transactions = json.load(open('my_current_balance.json'))
        with open('my_current_balance.json', 'w') as f:
            date_time = datetime.today().strftime('%m %d %Y %H:%M:%S')
            new_entry = add_json_entry(number, date_time,'deposit')
            transactions.append(new_entry)
            z = json.dumps(transactions, default=str)
            f.writelines(z)
    else:
        print('You must enter a valid monetary value\n')

def view_balance():
    '''This function prints the result of get_balance'''
    print(f'\nYour current balance is ${get_balance():,.2f}\n')

def view_all_transactions():
    '''This function prints all historical transactions'''
    transactions = json.load(open('my_current_balance.json'))
    transactions  = [transaction for transaction in transactions]
    entries = [entry for entry in transactions]
    pprint(entries)


def view_all_in_category():
    '''This function prints all historical transactions within a user-specified category and checks the user inputs'''
    user_choice = input('Which category do you wish to see?'
                            + '\nWithdrawal or Deposit\n' )
    if user_choice.lower() == 'withdrawal' or \
                user_choice.lower() == 'deposit':
        transactions = json.load(open('my_current_balance.json'))
        transactions  = [transaction for transaction in transactions if transaction['category'] == user_choice]
        for item in transactions:
            pprint(item)
    else:
        print('You must enter a valid category\n')

# def view_all_on_day():
#     '''This function prints all historical transactions within a user-specified day'''
#     user_choice = input('Which day do you wish to view? ')
#     transactions = json.load(open('my_current_balance.json'))
#     transactions = [transaction for transaction in transactions]
#     transaction_dates  = [transaction['time'] for transaction in transactions]
#     dates = [str(day[:10]) for day in transaction_dates]
#     # print(dates)
#     for i in range(len(transactions)):
#         if user_choice == dates[i]:
#             print(transactions[i])
#         else:
#             print('You must enter a date in the format MM DD YYYY')
#             break
