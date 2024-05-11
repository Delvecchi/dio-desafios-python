def menu():
    menu = input("""
    -------------- MENU --------------
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [x]  Sair
    ----------------------------------
    => """)
    
    return menu

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("--- Depósito realizado com sucesso! ---")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("--- Operação falhou! Você não tem saldo suficiente. ---")

    elif excedeu_limite:
        print("--- Operação falhou! O valor do saque excede o limite. ---")

    elif excedeu_saques:
        print("--- Operação falhou! Número máximo de saques excedido. ---")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}"
        numero_saques += 1
        print("--- Saque realizado com sucesso! ---")

    else:
        print("--- Operação falhou! O valor informado é inválido. ---")

    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("-------------- EXTRATO --------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("-------------------------------------")
    
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("--- Já existe usuário com esse CPF! ---")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("--- Usuário criado com sucesso! ---")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("--- Conta criada com sucesso! ---")
        
    else:
        print("--- Usuário não encontrado, fluxo de criação de conta encerrado! ---")

    
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu()
    
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "nc":
            criar_conta(agencia, numero_conta, usuarios)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "x":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
main()