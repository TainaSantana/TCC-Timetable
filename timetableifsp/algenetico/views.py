from django.shortcuts import render
from random import random

def algGenetico(request):
    return render(request, 'algenetico/algoritmo.html', {})


class Produto():
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor

class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0):
        # espacos utilizados pelos produtos
        self.espacos = espacos
        #valores totais
        self.valores = valores
        # limite de espaco que pode ser transportado no caminhao
        self.limite_espacos = limite_espacos
        #cada individuo tem uma nota, para comparacao
        self.nota_avaliacao = 0
        self.espaco_usado = 0
        self.geracao = geracao
        # onde esta contido a solucao
        self.cromossomo = []
        
        # faz inicializacao aleatoria das solucoes
        for i in range(len(espacos)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
        
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
            
        for i in range(len(self.cromossomo)):
            # valida se o produto sera add no caminhao
            if self.cromossomo[i] == '1':
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
        if soma_espacos > self.limite_espacos:
            nota = 1
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos
        
    def crossover(self, outro_individuo):
        # pega um numero randomico entre 0 e 1 e multiplica pelo tamanho
        # do cromossomo para gerar o numero de corte
        corte = round(random() * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1),
                  Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1)]
        
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos
    
    def mutacao(self, taxa_mutacao):
        print("Antes %s" % self.cromossomo)
        
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo =='1'
        print("Depois %s" % self.cromossomo)
        return self
        
class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0

    def inicializa_populacao(self, espacos, valores, limite_espacos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos, valores, limite_espacos))                    
        self.melhor_solucao = self.populacao[0]
    
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao, 
                                key=lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
    
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
    
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
        return soma
    
if __name__ == '__main__':
    #p1 = Produto("Iphone 6", 0.0000899, 2199.7)
    lista_produtos = []
    lista_produtos.append(Produto("Iphone 6", 0.0000899, 2199.7))
    lista_produtos.append(Produto("Geladeira Dako", 0.75, 999.90))
    lista_produtos.append(Produto("TV 55 ", 8.4000, 4346.99))
    lista_produtos.append(Produto("TV 50", 8290, 3999.90))
    lista_produtos.append(Produto("TV 42", 8200, 2999.00))
    lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
    lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
    lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
    lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
    lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
    lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
    lista_produtos.append(Produto("Geladeira Consult", 0.870, 1199.89))
    lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
    lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))
    
    #for produto in lista_produtos:
     #   print(produto.nome)
    
    espacos = []
    valores = []
    nomes = []
    
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)
    limite = 3
    
    tamanho_populacao = 20
    ag = AlgoritmoGenetico(tamanho_populacao)
    ag.inicializa_populacao(espacos, valores, limite)
    for individuo in ag.populacao:
        individuo.avaliacao()
    ag.ordena_populacao()
    ag.melhor_individuo(ag.populacao[0])
    soma = ag.soma_avaliacoes()
    print("Soma das avaliações: %s" % soma)
    
    
