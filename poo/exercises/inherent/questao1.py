'''
Crie uma classe base `Veiculo` com atributos `marca` e `modelo`. Crie duas classes filhas `Carro` e
`Moto` que herdam de `Veiculo`. Adicione um método `informacoes()` em `Veiculo` que é reutilizado
pelas classes filhas.

'''

class Veiculo:
    

    def __init__(self,marca,modelo):
        self.__marca = marca
        self.__modelo = modelo


    def get_informacoes(self):
        return f"Marca do Veiculo is {self.__marca} e modelo is {self.__modelo}"

class Carro(Veiculo):

    def __init__(self,marca,modelo,num_portas):
       
        super().__init__(marca, modelo) #accessa metodo init da superclasse
        self.__num_portas =  num_portas
    
    def get_informacoes(self):
        """
        Reutiliza o método informacoes da classe base e adiciona detalhes específicos do carro.
        """
        return f"{super().get_informacoes()}, Portas: {self.__num_portas}"



class Moto(Veiculo):
    
    def __init__(self,marca,modelo,nums_cilindradas):

        super().__init__(marca,modelo)
        self.__nums_cilindradas = nums_cilindradas

    def get_informacoes(self):
        return f"{super().get_informacoes()}, Portas: {self.__nums_cilindradas}"


car = Carro("Wolkswagem","polo 2024",4)
print(car.get_informacoes())

moto = Moto("Yamaha", "Fazer", 150)
print(moto.get_informacoes())
