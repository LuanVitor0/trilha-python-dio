menu = """ 

[1] Depositar 
[2] Sacar 
[3] Extrato 
[0] Sair 

---> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
Limite_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input(">> Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
            print(">> Valor informado foi invalidado, tente de novo.")

    elif opcao == "2":
        valor = float(input(">> Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= Limite_SAQUES

        if excedeu_saldo:
            print("! Operação invalida! Você provavelmente tem o saldo insuficiente. !")
        
        elif excedeu_limite:
            print("! Operação invalida! Provavelmente o valor do saque excedeu o limite. !")

        elif excedeu_saque:
            print("! Operação invalida! Provavelmente o numero máximo de saque foi excedido. !")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("!!!FALHA!!! Valor informado é inválido")

    
    elif opcao == "3":
        print("\n**************************EXTRATO******************************")
        print(">> Não foi realizado nenhuma movimentação." if not extrato else extrato)
        print(f"\n >> Saldo: R$ {saldo:.2f}")
        print("*****************************************************************")

    elif opcao == "0":
        print("Obrigado por ser nosso cliente fiel")
        break
    
    else:
        print("!!!! A sua operação foi invalidada, devido a operação não encontrada, por favor volte no sistema e selecione uma opção valida.!!!")