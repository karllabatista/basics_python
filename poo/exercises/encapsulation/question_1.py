'''
Crie uma classe `ContaBancaria` com atributos privados `saldo` e `titular`. Implemente métodos
para depositar, sacar e consultar o saldo. Não permita saques com valor superior ao saldo.
'''

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
            raise ValueError("O valor de saque dever ser maior que zero")
        if valor_saque > self.__saldo:
            raise Exception("Insufficient amount for withdraw!")

        self.__saldo -= valor_saque
        
        
    def consultar_saldo(self):
        return f"Consulta de Saldo do sra/o {self.__titular}:{self.__saldo}"

       
    def consultar_titular(self):
        return f"Titular da conta: {self.__titular}"

conta = ContaBancaria("Karlla")
conta.depositar(400)
print(conta.consultar_saldo())
#conta.sacar(1000)
#conta.depositar(400)
#print(conta.consultar_saldo())
