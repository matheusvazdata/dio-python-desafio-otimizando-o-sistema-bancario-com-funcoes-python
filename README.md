# 💸 Sistema Bancário em Python

Bem-vindo ao **Sistema Bancário**! Este projeto simula as principais operações bancárias, como criar usuários, abrir contas correntes, fazer depósitos, saques e consultar extratos. 📊💰

## 🔧 Funcionalidades

O sistema oferece as seguintes funcionalidades:

- 👤 **Criar Usuário**: Crie um novo usuário fornecendo nome, data de nascimento, CPF e endereço.
- 🏦 **Abrir Conta Corrente**: Crie uma conta corrente vinculada a um usuário existente (através do CPF).
- 💵 **Realizar Depósitos**: Permite ao usuário adicionar dinheiro em sua conta.
- 💸 **Realizar Saques**: Saque valores respeitando o limite de saques diários e o saldo disponível.
- 📄 **Exibir Extrato**: Veja o histórico das movimentações realizadas e o saldo atual.

---

## 🚀 Como executar o projeto

Siga os passos abaixo para rodar o sistema bancário em sua máquina:

### 1️⃣ Clonando o repositório

Primeiro, clone o repositório para a sua máquina local usando o comando:

```bash
git clone https://github.com/matheusvazdata/dio-python-desafio-otimizando-o-sistema-bancario-com-funcoes-python.git
```

### 2️⃣ Navegando até o diretório

Entre no diretório do projeto:

```bash
cd sistema-bancario
```

### 3️⃣ Executando o sistema

Com o Python instalado na sua máquina, basta rodar o arquivo principal:

```bash
python sistema_bancario.py
```

🎉 **Pronto!** Agora o sistema está rodando, e você pode criar usuários, contas e realizar operações bancárias!

---

## 💻 Estrutura do Projeto

O projeto é composto pelas seguintes funções principais:

- **`criar_usuario()`**: Cria um novo usuário com nome, data de nascimento, CPF e endereço.
- **`criar_conta_corrente()`**: Cria uma conta corrente associada a um usuário com um CPF já cadastrado.
- **`realizar_operacoes()`**: Permite ao usuário realizar depósitos, saques ou consultar o extrato.
- **`saque()`**: Executa o saque, verificando limites diários e saldo.
- **`depositar()`**: Função para adicionar saldo à conta do usuário.
- **`exibir_extrato()`**: Exibe o histórico de movimentações e o saldo da conta.

---

## 📌 Requisitos

Para rodar este projeto, você precisa ter o **Python** instalado na sua máquina.

- **Python 3.x**
  
Você pode fazer o download do Python [aqui](https://www.python.org/downloads/).

---

## 🏗️ Como o sistema funciona

### 1. 👤 Criar Usuário

Para cadastrar um usuário, o sistema solicita as seguintes informações:

- Nome completo
- Data de nascimento (no formato `dd/mm/aaaa`)
- CPF (somente números)
- Endereço (no formato `logradouro, número - bairro - cidade/sigla estado`)

⚠️ **Importante**: Um CPF não pode ser cadastrado mais de uma vez.

### 2. 🏦 Criar Conta Corrente

Após cadastrar um usuário, você pode criar uma conta corrente para ele. Cada conta corrente possui:

- **Agência**: O número da agência é sempre `0001`.
- **Número da Conta**: Gerado automaticamente de forma sequencial.
- **Usuário**: A conta é vinculada a um CPF já cadastrado.

### 3. 💸 Operações Bancárias

Com a conta corrente criada, o sistema permite as seguintes operações:

- **Depósitos**: Adicionar saldo à conta.
- **Saques**: Retirar dinheiro, respeitando o limite de saques diários e o saldo disponível.
- **Extrato**: Consultar o saldo e o histórico de transações realizadas.

### 4. 📝 Regras de Negócio

- O usuário pode realizar até **3 saques diários**.
- O valor de cada saque não pode ultrapassar **R$500,00**.
- O saldo precisa ser suficiente para realizar o saque.

---

## 📂 Estrutura de Diretórios

```plaintext
dio-python-desafio-otimizando-o-sistema-bancario-com-funcoes-python/
├── sistema_bancario.py  # Arquivo principal do projeto
└── README.md            # Arquivo de documentação
```

---

## 🤝 Contribuição

Sinta-se à vontade para contribuir com o projeto! Você pode fazer isso das seguintes maneiras:

1. **Abrindo issues** para relatar bugs ou sugerir melhorias.
2. **Enviando pull requests** com novas funcionalidades ou correções.

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---

**Desenvolvido com 💻 e ☕ por Francisco Matheus Vaz dos Santos**

---

### 🎯 Dicas Finais

- Sempre mantenha seu ambiente de desenvolvimento atualizado.
- Verifique se os usuários foram cadastrados corretamente antes de criar contas.
- Divirta-se enquanto aprende Python com este projeto simples e prático! 🎉

---

Se você gostou desse projeto, deixe uma ⭐ no repositório! 😄