'''
Expanda o exercício anterior adicionando o atributo `tipo_combustivel` na classe `Carro` e
`cilindradas` na classe `Moto`. Sobrescreva o método `informacoes()` para exibir detalhes
específicos de cada classe filha.
'''


class Veiculo:
    

    def __init__(self,marca,modelo):
        self.__marca = marca
        self.__modelo = modelo


    def informacoes(self):
        return f"Marca do Veiculo is {self.__marca} e modelo is {self.__modelo}"

    '''
    @property a way to define getters and setters (pythonic)
    '''
    @property #getter
    def marca(self):
        return self.__marca
    
    @marca.setter #setter
    def marca(self,marca):
        self.__marca = marca

    @property 
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self,modelo):
        self.__modelo= modelo
 

class Carro(Veiculo):

   

    def __init__(self,marca,modelo,num_portas,tipo_combustivel):
       
        super().__init__(marca, modelo) #accessa metodo init da superclasse
        self.__num_portas =  num_portas
        self.__tipo_combustivel =tipo_combustivel
        
    def informacoes(self):
        """
        Reutiliza o método informacoes da classe base e adiciona detalhes específicos do carro.
        """
        return f"{super().informacoes()}, Portas: {self.__num_portas}, Combustivel:{self.__tipo_combustivel}"
    
    @property
    def num_portas():
        return self.__num_portas
    
    @num_portas.setter
    def num_portas(self,num_portas):
        self.__num_portas = num_portas

    @property
    def tipo_combustivel():
        return self.__tipo_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self,tipo_combustivel):
        self.__tipo_combustivel =  tipo_combustivel

class Moto(Veiculo):

    
    def __init__(self,marca,modelo,nums_cilindradas):

        super().__init__(marca,modelo)
        self.__nums_cilindradas = nums_cilindradas

    @property
    def nums_cilindradas():
        return self.__nums_cilindradas
    
    @nums_cilindradas.setter
    def nums_cilindradas(self,nums_cilindradas):
        self.__nums_cilindradas =  nums_cilindradas
    
    def informacoes(self):
        return f"{super().informacoes()}, Numero cilindradas: {self.__nums_cilindradas}"


car = Carro("Wolkswagem","polo 2024",4,"flex")
print(car.informacoes())

moto = Moto("Yamaha", "Fazer", 150)
print(moto.informacoes())

car.modelo="pol0 2025"
car.num_portas = 6
print(car.informacoes())

