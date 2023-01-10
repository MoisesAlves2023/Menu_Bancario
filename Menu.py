from time import sleep

saque_diario = 0
limite_saque = 3
saldo = 0
extrato = []
limite = 500


while True:
    print('''
=========CAIXA ELETRONICO========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

=================================
''')
    opçao = int(input("Digite o número da operação desejada: "))
    if opçao == 1: 
        depositar = float(input("Digite o valor do deposito: "))
        if depositar > 0:
            saldo = saldo + depositar
            print("Fazendo deposito... aguarde alguns segundos")
            sleep(3)
            print("Deposito Realizado")
            extratod = str(f"Foi realizado um deposito de R${depositar:.2f}")
            extrato.append(extratod)
            sleep(1)
        else:
            print("Valor Inválido!")

    elif opçao == 2:
        if limite_saque <=0:
                print("Limite diario de saque atingido, volte amanha.")
        else:
            sacar = float(input("Digite o valor do saque: "))
            if sacar > 500:
                print("Verificando valor...")
                sleep(2)
                print("Valor acima do limite de saque")
                sleep(1)

            elif sacar > saldo:
                print("Verificando valor...")
                sleep(2)
                print("Saldo insuficiente, consulte o seu extrato para ver seu saldo.")

            elif 0 < sacar <=500 and limite_saque <=3 and sacar <= saldo:
                saldo = saldo - sacar
                print("Aguarde o caixa fazer a contagem das notas...")
                sleep(3)
                print("Saque realizado.")
                extratos = str(f"Foi realizado um saque de R${sacar:.2f}")
                extrato.append(extratos)
                limite_saque = limite_saque - 1
                print(f"Saques diarios restante {limite_saque}")
                sleep(2)
            
    elif opçao == 3:
        sleep(1)
        extratot = str(f"Saldo atual R${saldo:.2f}")
        extrato.append(extratot)
        
        for x in extrato:
            print(f"{x}\n")

        sleep(1)


    elif opçao == 4:
        print("Até logo")
        break

    else:
        print("Operação inválida, Selecione uma opção válida!")         