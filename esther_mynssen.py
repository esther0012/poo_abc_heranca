from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

    @abstractmethod
    def cumprimentar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def cumprimentar(self):
        print(f"Olá, eu sou o aluno {self.nome} e minha matrícula é {self.matricula}.")

    def estudar(self, materia):
        print(f"Estou estudando {materia}.")

    def fazer_prova(self):
        print("Estou fazendo a prova.")


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} feito. Novo saldo: {self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de {valor} feito. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: {self.saldo}")


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo=0, taxa_juros=0.02):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros

    def calcular_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f"Juros calculados e adicionados. Novo saldo: {self.saldo}")

    def transferir(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.depositar(valor)
            print(f"Transferência de {valor} realizada para {destino.titular}.")
        else:
            print("Saldo insuficiente para a transferência.")

class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def cumprimentar(self):
        print(f"Olá, eu sou o professor {self.nome} e meu salário é {self.salario}.")

    def lecionar(self, disciplina):
        print(f"Estou lecionando a disciplina de {disciplina}.")

    def corrigir_prova(self):
        print("Estou corrigindo provas.")

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0, limite=1000):
        super().__init__(titular, saldo)
        self.limite = limite

    def get_limite(self):
        return self.limite

    def set_limite(self, novo_limite):
        self.limite = novo_limite

    def transferir(self, destino, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            destino.depositar(valor)
            print(f"Transferência de {valor} realizada para {destino.titular}.")
        else:
            print("Saldo insuficiente para a transferência.")

    def pagar_conta(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Pagamento de conta no valor de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente para efetuar o pagamento.")

# Criando objetos das classes
aluno1 = Aluno("João", 20, "A123")
professor1 = Professor("Maria", 35, 5000)
conta_poupanca = ContaPoupanca("Alice", 1000)
conta_corrente = ContaCorrente("Carlos", 2000)

# Testando os métodos da classe Aluno
aluno1.apresentar()
aluno1.cumprimentar()
aluno1.estudar("Matemática")
aluno1.fazer_prova()

# Testando os métodos da classe Professor
professor1.apresentar()
professor1.cumprimentar()
professor1.lecionar("História")
professor1.corrigir_prova()

# Testando os métodos da classe ContaPoupanca
conta_poupanca.depositar(500)
conta_poupanca.calcular_juros()
conta_poupanca.consultar_saldo()
conta_poupanca.transferir(conta_corrente, 300)

# Testando os métodos da classe ContaCorrente
conta_corrente.depositar(100)
conta_corrente.consultar_saldo()
conta_corrente.pagar_conta(150)
conta_corrente.consultar_saldo()
conta_corrente.transferir(conta_poupanca, 500)