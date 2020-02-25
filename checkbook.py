print('\n~~~ Welcome to your terminal checkbook ~~~\n\n')

user_input  = input("What would you like to do? ")

options = '''
            1) View current balance
            2) Make a withdrawal
            3) Make a deposit
            4) Exit this terminal
        '''
while user_input.isalpha() or int(user_input) < 1 or int(user_input) > 4:
    print(f'{options} \n\nYour choice? {user_input}' \
    + f'\nInvalid choice: {user_input}')
    user_input = input('Your choice? ')

# def withdraw(number):

# def deposit(number):

# def view_balance():

