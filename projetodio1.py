class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.saques_hoje = 0
        self.transacoes = []

    def depositar(self, valor):
        if valor < 0:
            print("Não é possível depositar um valor negativo.")
        else:
            self.saldo += valor
            self.transacoes.append(f"Depósito de R${valor}")
            print(f"Depósito de R${valor} realizado com sucesso.\nSaldo atual: R${self.saldo}")

    def sacar(self, valor):
        if self.saques_hoje >= 3:
            print("Limite de saques diários atingido.")
        elif valor > 1000:
            print("Limite de saque excedido. O máximo é R$1000.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.saques_hoje += 1
            self.transacoes.append(f"Saque de R${valor}")
            print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}")

    def extrato(self):
        print("========= EXTRATO =========")
        for transacao in self.transacoes:
            print(transacao)
        print(f"Saldo atual: R${self.saldo}")
        print("============================")

conta = ContaBancaria()

while True:
    print("\n1. Depositar\n2. Sacar\n3. Extrato\n4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        while True:
            try:
                valor = float(input("Digite o valor do depósito: "))
                conta.depositar(valor)
                break
            except: ValueError
            print("Valor inválido. Tente novamente.")
       
    elif opcao == "2":
        while True:
            try:
                valor = float(input("Digite o valor do saque: "))
                conta.sacar(valor)
                break
            except: ValueError
            print("Valor inválido. Tente novamente.")

        valor = float(input("Digite o valor do saque: "))
        conta.sacar(valor)
    elif opcao == "3":
        conta.extrato()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
