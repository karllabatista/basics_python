'''
Implemente uma classe base `FormaGeometrica` com um método `area()` que retorna 0. Crie
classes `Quadrado` e `Circulo` que sobrescrevem o método `area()` para calcular as áreas
corretamente com base nos atributos fornecidos.

'''

'''
Polimorfismo : Permite que codigos com mesmo nome se comportem de maneiras diferentes depe-
dendo da classe

Objetivo: flexibilidade e adaptabilidade
'''
class FormaGeometrica:


    def area(self):
        pass
    
    def informacoes(self):

        pass
    

class Quadrado(FormaGeometrica):

    def __init__(self,lados):

        self.__lados =  lados
    
    def area(self):
        return self.__lados * self.__lados


    @property
    def lados(self):

        return self.__lados

    @lados.setter
    def lados(self,lados):

        self.__lados  = lados

    def informacoes(self):

        return f"Valor da area do quadrado:{self.area()}"


class Circulo(FormaGeometrica):

    pi =  3.14159  #variavel de classe

    def __init__(self,raio):

        self.__raio = raio

    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self,raio):
        self.__raio = raio

    def area(self):
        return self.pi*(self.__raio*self.__raio)

       

    def informacoes(self):

        return f"Valor da area do circulo :{self.area()}"



quad = Quadrado(4)
quad.area()
print(quad.informacoes())

print("Alterando valores do lado do quadrado")
quad.lados = 8
quad.area()
print(quad.informacoes())


print("Calculando area do Ciculo")
circ = Circulo(5)
circ.area()
print(circ.informacoes())