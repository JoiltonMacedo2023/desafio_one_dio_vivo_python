import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def saudacao():
    hora_atual = datetime.datetime.now().hour
    if 6 <= hora_atual < 12:
        return "Bom dia"
    elif 12 <= hora_atual < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

saudacao_atual = saudacao()
agora = datetime.datetime.now()
data_hora = agora.strftime("%A, %d de %B de %Y %H:%M:%S")

menu = f"""
{str(saudacao_atual)}, Seja bem-vindo(a)!
Hoje é {data_hora}

Selecione a operação que deseja realizar:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")    


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo_excedido = valor > saldo

        limite_excedido = valor > limite  

        saque_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Operação falhou! Você não possui saldo suficiente.")

        elif limite_excedido:
            print("Operação falhou! O valor do saque excede o limite.") 

        elif saque_excedido:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato +=f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
                     
    elif opcao == "e":
        print("\n===================Extrato========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================")
      
    elif opcao == "q":
        print("Agradecemos pela preferência, Volte sempre!") 
        break    

    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")

