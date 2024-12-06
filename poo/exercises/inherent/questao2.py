'''
Expanda o exercício anterior adicionando o atributo `tipo_combustivel` na classe `Carro` e
`cilindradas` na classe `Moto`. Sobrescreva o método `informacoes()` para exibir detalhes
específicos de cada classe filha.
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
        self.__tipo_combustivel ='gasosa'
        
    def get_informacoes(self):
        """
        Reutiliza o método informacoes da classe base e adiciona detalhes específicos do carro.
        """
        return f"{super().get_informacoes()}, Portas: {self.__num_portas}, Combustivel:{self.__tipo_combustivel}"



class Moto(Veiculo):

    nums_cilindradas = 0
    
    def __init__(self,marca,modelo,nums_cilindradas):

        super().__init__(marca,modelo)
        self.__nums_cilindradas = nums_cilindradas

    def get_informacoes(self):
        return f"{super().get_informacoes()}, Portas: {self.__nums_cilindradas}"


car = Carro("Wolkswagem","polo 2024",4)
print(car.get_informacoes())

moto = Moto("Yamaha", "Fazer", 150)
print(moto.get_informacoes())
