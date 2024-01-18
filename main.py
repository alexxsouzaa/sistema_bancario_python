from datetime import datetime

saldo = 1000.00

def menu():
    global opcao
    print(' MENU '.center(74, '='))
    print('[1] Depositor\n[2] Saque\n[3] Saldo\n[4] Sair\n')
    opcao = int(input('Digite a opção desejada: '))
    print('=' * 74)

def deposito():
    global saldo
    print(' DEPOSITO '.center(74, '-'))
    print('[1] Deposita na minha conta\n[2] Deposita em outra conta')
    opcao_deposito = int(input('\nDigite a opção desejada: '))
    if opcao_deposito == 1:
        print('DEPOSITO')
    elif opcao_deposito == 2:
        print('\n')
        print(' DEPOSITO EM OUTRA CONTA '.center(74, "-"))
        print('\nDADOS DE DEPOSITO')
        print('')
        print(f'SALDO: {saldo}')
        agencia_deposito = int(input('\nAgencia: '))
        conta_deposito = int(input('Conta: '))
        valor_deposito = float(input('Valor do deposito: '))
        hora_deposito = datetime.now()
        if valor_deposito <= saldo:
            print(' ')
            print('-' * 74)
            print('\nDeposito realizado com sucesso!\n')
            print(' COMPROVANTE DE DEPOSITO '.center(74, '-'))
            print(f'\nData é hora do deposito: {hora_deposito.strftime("%d-%m-%Y - %H:%M:%S")}')
            print('Banco DevCred')
            print(f'Agencia: {agencia_deposito}')
            print(f'Conta: {conta_deposito}')
            print(f'Valor: {valor_deposito}')
            #saldo = saldo - valor_deposito
            print('\n')
            print('-' * 74)
        elif valor_deposito > saldo:
            print('\nSaldo em conta insuficiente!\nVerifique o seu saldo é tente novamente.')
            
def saldo():
    global saldo
    print(' SALDO '.center(74, '-'))
    print(saldo)


if __name__=='__main__':
    print(' Seja Bem-Vindo(a) ao Banco DevCred '.center(74, '#'))
    print('\nInforme sua agência e conta para continuar:\n')
    agencia = int(input('Agência: '))
    conta = int(input('Conta: '))
    print(' ')
    print('#' * 74)


    if (agencia == 1) and (conta == 1):
        menu()
        if opcao == 1:
            deposito()
        elif opcao == 2:
            print('SAQUE')
        elif opcao == 3:
            saldo()
    else:
        print('Agência e conta invalidas!')
