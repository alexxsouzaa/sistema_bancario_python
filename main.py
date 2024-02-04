from datetime import datetime

def menu():
    global opcao
    print(' MENU '.center(74, '='))
    print('[1] Depositor\n[2] Saque\n[3] Saldo\n[4] Sair\n')
    opcao = int(input('Digite a opção desejada: '))
    print('=' * 74)

def deposito():
    print(' DEPOSITO '.center(74, '-'))
    print('[1] Deposita na minha conta\n[2] Deposita em outra conta')
    opcao_deposito = int(input('\nDigite a opção desejada: '))
    if opcao_deposito == 1:
        global saldo
        print(' DEPOSITO EM MINHA CONTA '.center(74, "-"))
        print('\nQual valor deseja deposita?')
        valor_deposito_conta = float(input('Valor: '))
        saldo = saldo + valor_deposito_conta
        hora_deposito_conta = datetime.now()
        print('-' * 74)
        print('\nDeposito realizado com sucesso!\n')
        print(' COMPROVANTE DE DEPOSITO '.center(74, '-'))
        print('Banco DevCred')
        print(f'\nData é hora do deposito: {hora_deposito_conta.strftime("%d-%m-%Y - %H:%M:%S")}')
        print(f'Agencia: {agencia}')
        print(f'Conta: {conta}')
        print(f'Valor: {valor_deposito_conta}')
        print(f'Saldo atual: {saldo}')
        print('-' * 74)
    elif opcao_deposito == 2:
        print('\n')
        print(' DEPOSITO EM OUTRA CONTA '.center(74, "-"))
        print('\nDADOS DE DEPOSITO')
        print('')
        print(f'SALDO: {saldo}')
        agencia_deposito = int(input('\nAgencia: '))
        conta_deposito = int(input('Conta: '))
        valor_deposito = float(input('Valor do deposito: '))
        saldo = saldo - valor_deposito
        hora_deposito = datetime.now()
        if valor_deposito <= saldo:
            print(' ')
            print('-' * 74)
            print('\nDeposito realizado com sucesso!\n')
            print(' COMPROVANTE DE DEPOSITO '.center(74, '-'))
            print('Banco DevCred')
            print(f'\nData é hora do deposito: {hora_deposito.strftime("%d-%m-%Y - %H:%M:%S")}')
            print(f'Agencia: {agencia_deposito}')
            print(f'Conta: {conta_deposito}')
            print(f'Valor: {valor_deposito}')
            print(f'Saldo atual: {saldo}')
            print('-' * 74)
        elif valor_deposito > saldo:
            print('\nSaldo em conta insuficiente!\nVerifique o seu saldo é tente novamente.')

def saque():
    global saldo
    print(' SAQUE '.center(74, '-'))
    valor_saque = float(input('\nInforme o valor que deseja sacar: '))
    saldo = saldo - valor_saque
    hora_deposito_saque = datetime.now()
    print('-' * 74)
    print(' COMPROVANTE DE SAQUE '.center(74, '-'))
    print('Banco DevCred')
    print(f'\nData é hora do saque: {hora_deposito_saque.strftime("%d-%m-%Y - %H:%M:%S")}')
    print(f'Valor do saque: {valor_saque}')
    print(f'Saldo atual: {saldo}')
    print('-' * 74)
    
           
def saldo():
    global saldo
    print(' SALDO '.center(74, '-'))
    print(f'Saldo atual: {saldo}')


if __name__=='__main__':
    
    saldo = 1000.00
    resposta = 'S'
    
    print('\n')
    print(' Seja Bem-Vindo(a) ao Banco DevCred '.center(74, '#'))
    print('\nInforme sua agência e conta para continuar:\n')
    agencia = int(input('Agência: '))
    conta = int(input('Conta: '))
    print(' ')
    print('#' * 74)


    if (agencia == 1) and (conta == 1):
        menu()
        if opcao == 1:
            while resposta == 'S':
                deposito()
                print('\nDeseja realiza outro saque?')
                resposta = input('Digite \'S\' para continua e \'N\' para sair: ').upper()
                print('-' * 74)
            menu()
        elif opcao == 2:
            saque()
        elif opcao == 3:
            saldo()
    else:
        print('Agência e conta invalidas!')
