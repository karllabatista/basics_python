'''
Adicione validações no método de saque da classe `ContaBancaria`. Caso o valor seja negativo ou
superior ao saldo, lance uma exceção personalizada chamada `SaldoInsuficienteError`.
'''

class SaldoInsuficienteError(Exception):
    def __init__(self, message="Saldo insuficiente para realizar a operação"):
        super().__init__(message)

class ContaBancaria:

    def __init__(self,titular):
        self.__saldo = 0 #private attributes
        self.__titular = titular

    def depositar(self,valor_atual):
        if valor_atual < 0:
            raise ValueError("O valor de deposito dever ser maior que zero")
            
        self.__saldo += valor_atual

    def sacar(self,valor_saque):
        if valor_saque < 0:
           raise SaldoInsuficienteError("O valor do saque nao pode ser negativo")
        if valor_saque > self.__saldo:
           raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque")

        self.__saldo -= valor_saque
        
        
    def consultar_saldo(self):
        return f"Consulta de Saldo do sra/o {self.__titular}:{self.__saldo}"

       
    def consultar_titular(self):
        return f"Titular da conta: {self.__titular}"

if __name__ == '__main__':

    try:
        #titular
        conta = ContaBancaria("Karlla")

        #deposito
        print("novo deposito ..")       
        conta.depositar(400)
        print(conta.consultar_saldo())
        print("-----------------------\n")

        #saque invalido
        print("Novo saque ..")
        conta.sacar(-900)
        print(conta.consultar_saldo())
        print("-----------------------\n")

    except SaldoInsuficienteError as erro:
        print(erro)