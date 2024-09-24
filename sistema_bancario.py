# Lista para armazenar os usuários
usuarios = []

# Lista para armazenar as contas correntes
contas_correntes = []
numero_conta = 1  # Inicia a contagem das contas a partir de 1

# Função para criar um usuário
def criar_usuario():
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Informe o CPF (somente números): ").replace(".", "").replace("-", "").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Verifica se o CPF já está cadastrado
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Erro: Já existe um usuário com esse CPF cadastrado.")
        return
    
    # Cria o dicionário do usuário
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }

    # Adiciona o usuário à lista
    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso!")

# Função para criar uma conta corrente
def criar_conta_corrente():
    global numero_conta
    cpf = input("Informe o CPF do usuário para criar a conta: ").replace(".", "").replace("-", "").strip()

    # Verifica se o CPF está cadastrado
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    if usuario:
        conta = {
            'agencia': '0001',
            'numero_conta': numero_conta,
            'usuario': usuario['nome']
        }
        contas_correntes.append(conta)
        numero_conta += 1
        print(f"Conta criada com sucesso! Agência: 0001, Conta: {conta['numero_conta']}, Titular: {usuario['nome']}")
    else:
        print("Erro: CPF não cadastrado. Por favor, crie um usuário primeiro.")

# Função para encontrar uma conta pelo CPF
def encontrar_conta(cpf):
    contas_usuario = [conta for conta in contas_correntes if conta['usuario'] == cpf]
    return contas_usuario

# Função para realizar operações bancárias (depositar, sacar, extrato)
def realizar_operacoes():
    cpf = input("Informe o CPF cadastrado: ").replace(".", "").replace("-", "").strip()
    
    # Verifica se há uma conta associada ao CPF
    contas = encontrar_conta(cpf)
    if not contas:
        print("Nenhuma conta encontrada para este CPF.")
        return

    # Exibe as contas associadas ao CPF e permite escolher uma
    print("Contas encontradas:")
    for i, conta in enumerate(contas, start=1):
        print(f"[{i}] Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']}")

    opcao_conta = int(input("Selecione o número da conta para realizar operações: ")) - 1
    conta_selecionada = contas[opcao_conta]

    saldo = 1400
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    print(f"Bem-vindo(a), {conta_selecionada['usuario']}! Sua conta é {conta_selecionada['numero_conta']} na agência {conta_selecionada['agencia']}.")

    while True:
        opcao = input("""
Digite a letra com a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """).lower()

        if opcao == "d":
            valor_deposito = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "s":
            valor_saque = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Por favor, tente novamente.")

# Funções para saque, depósito e exibição de extrato
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print(f'Você atingiu o limite de {limite_saques} saques diários. Para mais saques, volte amanhã!')
        return saldo, extrato, numero_saques

    if valor <= 0 or valor > limite:
        print(f'O valor deve ser maior que R$ 0,00 e menor ou igual a R$ {limite:.2f}.')
        return saldo, extrato, numero_saques

    if valor > saldo:
        print(f'Você não tem saldo suficiente. Seu saldo é de: R$ {saldo:.2f}')
        return saldo, extrato, numero_saques

    saldo -= valor
    extrato += f'(-) Saque: R$ {valor:.2f}\n'
    numero_saques += 1
    print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato):
    if valor <= 0:
        print(f'O valor do depósito precisa ser maior que R$ 0,00.')
        return saldo, extrato

    saldo += valor
    extrato += f'(+) Depósito: R$ {valor:.2f}\n'
    print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    print(f'Extrato detalhado:\n')
    if not extrato:
        print('Não foi realizada movimentação alguma!\n')
    else:
        print(extrato)
    print(f'Saldo atual: R$ {saldo:.2f}')


# Testando a criação de usuários, contas e operações bancárias
while True:
    opcao_principal = input("\nEscolha uma opção:\n[u] Criar Usuário\n[c] Criar Conta Corrente\n[o] Realizar Operações\n[q] Sair\n=> ")

    if opcao_principal == "u":
        criar_usuario()
    elif opcao_principal == "c":
        criar_conta_corrente()
    elif opcao_principal == "o":
        realizar_operacoes()
    elif opcao_principal == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")