"""
    in this, we will see an example of user defined exception

    example is withdraw money from bank
    1) balance in an account must not be less than 1000
    2) the account will be blocked for 1 hour if user
       put 3 times wrong pin

"""
import time

class WithdrawExceptionError(Exception):
    pass

class AttemptExceptionError(Exception):
    pass

attempts = 1
def withdraw():
    global attempts
    saved_PIN = 1243
    balance = 10000
    
    pin = int(input('Enter PIN: '))
    if pin == saved_PIN:
        try:
            amount = float(input('Enter amount to withdraw: '))
            temp_bal = balance-amount
            if temp_bal < 1000:
                raise WithdrawExceptionError("Insufficient balance ------------\n")
            else:
                balance = temp_bal
                print(f'\nRemained Balance = {balance}\n')
        except Exception as err:
            print('\n------------', err)
    else:
        print('\n------------ Wrong PIN ------------')
        responce = input('Do you want to continue(y/n): ')
        if responce.lower() == 'y':
            attempts += 1
            try:
                if attempts == 4:
                    raise AttemptExceptionError("Too many attempts, your account is blocked for 1 hour ------------\n")
            except Exception as err:
                print('\n------------',err)
                time.sleep(3600)
            else:
                withdraw()
        else:
            print('\n------------ tu ja yahan se ------------\n')

withdraw()
