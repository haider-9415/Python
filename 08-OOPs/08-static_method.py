class Bank:
    bank_name = 'BOB'
    rate_of_interest = 12.25

    @staticmethod
    def simple_interest(p, n):
        si = (p*n*Bank.rate_of_interest)/100
        print('.....................................................\n')
        print('Simple Interest = ', si)
        print('.....................................................\n')


p = float(input('Enter principle amount: '))
n = int(input('Enter no. of years: '))

# Bank.simple_interest(p, n)


# we can acces it with object
ob1 = Bank()
ob1.simple_interest(p, n)