import textwrap

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")


def menu():
    menu_text = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_text))


def criar_usuario():
    cpf = input("Informe o CPF (somente número): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    return Usuario(nome, cpf, data_nascimento, endereco)


def criar_conta(usuarios):
    usuario = None
    while not usuario:
        cpf = input("Informe o CPF do usuário: ")
        usuario = next((u for u in usuarios if u.cpf == cpf), None)
        if not usuario:
            print("\n@@@ Usuário não encontrado, por favor crie um novo usuário primeiro! @@@\n")
    
    agencia = "0001"  # Supondo agência fixa para simplificação
    numero_conta = len(contas) + 1
    conta = ContaBancaria(agencia, numero_conta, usuario)
    contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")


def listar_contas():
    for conta in contas:
        print("=" * 100)
        print(f"Agência:\t{conta.agencia}")
        print(f"C/C:\t\t{conta.numero_conta}")
        print(f"Titular:\t{conta.usuario.nome}")


usuarios = []
contas = []


def main():
    while True:
        opcao = menu()

        if opcao == "d":
            if not contas:
                print("\n@@@ Crie uma conta primeiro! @@@\n")
                continue
            valor = float(input("Informe o valor do depósito: "))
            conta = contas[-1]
            conta.depositar(valor)

        elif opcao == "s":
            if not contas:
                print("\n@@@ Crie uma conta primeiro! @@@\n")
                continue
            valor = float(input("Informe o valor do saque: "))
            conta = contas[-1]
            conta.sacar(valor)

        elif opcao == "e":
            if not contas:
                print("\n@@@ Crie uma conta primeiro! @@@\n")
                continue
            conta = contas[-1]
            conta.exibir_extrato()

        elif opcao == "nu":
            usuario = criar_usuario()
            usuarios.append(usuario)

        elif opcao == "nc":
            criar_conta(usuarios)

        elif opcao == "lc":
            listar_contas()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
