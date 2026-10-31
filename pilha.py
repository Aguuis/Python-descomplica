#Código da estrutura de dados pilha

class Pilha:

    def __init__(self):

        self.itens = []

    def esta_vazia(self):

        return self.itens == []

    def push(self, item):

        self.itens.append(item)

    def pop(self):

        if not self.esta_vazia():

            return self.itens.pop()
        else:
            print("Erro: não é possível remover elementos. A pilha está vazia!") #Trata o erro de tentar remover elementos de uma pilha vazia

    def peek(self):

        if not self.esta_vazia():

            return self.itens[-1]
        else:
            print("Erro: não é possível mostrar elementos. A pilha está vazia!") #Trata o erro de tentar mostrar elementos de uma pilha vazia

minha_pilha = Pilha()

minha_pilha.push(1) #Adiciona os elementos na pilha

minha_pilha.push(2)

minha_pilha.push(3)

minha_pilha.push(4)

minha_pilha.push(5)

minha_pilha.pop()          # Remove o topo da pilha, que é 5

minha_pilha.pop()          # Remove o topo da pilha, que é 4

print(minha_pilha.peek())  # Agora o topo da pilha é 3