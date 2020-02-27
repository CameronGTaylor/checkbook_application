import functions_checkbook as funcs

print('\n~~~ Welcome to your terminal checkbook ~~~')

funcs.open_new_account()

options = '''
    1) View current balance
    2) Make a withdrawal
    3) Make a deposit
    4) View past transactions
    5) View transactions by category
    6) Exit this terminal
        '''
# 6) View transactions by day
print(f'{options}')
user_input  = input("What would you like to do? ")


while True:
    if user_input in ['1','2','3','4','5','6']:
        if user_input == '1':
            funcs.view_balance()
            user_input = input(f'\nWhat would you like to do?' \
                f'\n{options}\nYour choice? ')
            
        elif user_input == '2':
            number = input('How much would you like to withdraw? $')
            funcs.withdraw(number)
            user_input = input(f'\nWhat would you like to do?' \
                f'\n{options}\nYour choice? ')

        elif user_input == '3':
            number = input("How much would you like to deposit? $")
            funcs.deposit(number)
            user_input = input(f'\nWhat would you like to do?' \
                f'\n{options}\nYour choice? ')
        
        elif user_input == '4':
            funcs.view_all_transactions()
            user_input = input(f'\nWhat would you like to do?' \
                f'\n{options}\nYour choice? ')

        elif user_input == '5':
            funcs.view_all_in_category()
            user_input = input(f'\nWhat would you like to do?' \
                f'\n{options}\nYour choice? ')

        # elif user_input == '6':
        #     funcs.view_all_on_day()
        #     user_input = input(f'\nWhat would you like to do?' \
        #         f'\n{options}\nYour choice? ')

        elif user_input == '6':
            print('\nThank you, have a wonderful day')
            break
        

    else:
        print(f'{options} \n\nYour choice? {user_input}' \
        + f'\nInvalid choice: {user_input}\n')
        user_input = input('Your choice? ')
