import backend.account_manager

manager = backend.account_manager.AccountManager('accounts.json')

templateAcc = {
    'name' : 'Max Mustermann',
    'picture' : 'standard.png',
    'pin' : '0000',
    'adress' : 'Test'
    }

for p in manager.accountList['accounts'] :
    print(p)

print('-----------------------')

manager.addAccount(templateAcc)

for p in manager.accountList['accounts'] :
    print(p)

print('-----------------------')

templateAcc2 = {
    'name' : 'Max Mustermann',
    'picture' : 'standard.png',
    'pin' : '0000',
    'adress' : 'Hamburg'
    }

manager.changeAccount('Max Mustermann', templateAcc2)

for p in manager.accountList['accounts'] :
    print(p)

print('-----------------------')

manager.selectAccount('Max Mustermann')

print(manager.selectedAccount)

print('-----------------------')

if manager.checkPin('0000') :
    print('Pin korrekt')
else :
    print('Pin inkorrekt')

print('-----------------------')

manager.deselectAccount()

print(manager.selectedAccount)

print('-----------------------')

manager.deleteAccount('Max Mustermann')

print(manager.accountList)
