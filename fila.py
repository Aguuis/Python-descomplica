#Código da estrutura de dados fila

class Fila:

    def __init__(self):

        self.itens = []

    def esta_vazia(self):

        return len(self.itens) == 0

    def enqueue(self, item):

        self.itens.append(item)

    def dequeue(self):

        if not self.esta_vazia():

            return self.itens.pop(0)
        else:
            print("Erro: não é possível remover elementos. A fila está vazia!") #Trata o erro de tentar remover elementos de uma fila vazia

    def peek(self):

        if not self.esta_vazia():

            return self.itens[0]
        else:
            print("Erro: não é possível mostrar elementos. A fila está vazia!") #Trata o erro de tentar mostrar elementos de uma fila vazia

minha_fila = Fila()

minha_fila.enqueue(1)

minha_fila.enqueue(2)

minha_fila.enqueue(3)

minha_fila.enqueue(4)

minha_fila.enqueue(5)

minha_fila.dequeue()    # Remove 1

minha_fila.dequeue()    # Remove 2

minha_fila.dequeue()    # Remove 3

print(minha_fila.peek())  # Saída: 4