accountMurat = {
    'name':'Murat Keskin',
    'accountNumber':'123',
    'balance' : 2000,
    'addition': 1000
}

accountAli = {
    'name':'Ali Ucar',
    'accountNumber':'321',
    'balance' : 5000,
    'addition': 250
}

accountAhmet = {
    'name':'Ahmet Kacar',
    'accountNumber':'111',
    'balance' : 2500,
    'addition': 1250
}

def withdrawMoney(account, amount):
    print(f"Hello {account['name']}")

    if account['balance'] >= amount:
        account['balance'] -= amount
        print('You can take your money.')
    else:
        total = account['balance'] + account['addition']
        if total >= amount:
            usageOfAddition = input('Do you want to use your additional money (y/n): ')
            if usageOfAddition == 'y':

                usageOfAddition= amount- account['balance']
                account['balance']=0
                account['addition']-=usageOfAddition
                print('You can take your money.')
            else:
                print(f"In account number {account['accountNumber']}, you have {account['balance']} available.")
        else:
            print('Not enough balance.')


withdrawMoney(accountMurat, 2020)  
withdrawMoney(accountMurat, 500)  
