# Escrevendo as classes de um jogo
#Definindo classe
class Hero:
    #metódo de inicialização da classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
      
        self.tipo = {
            "mago" : "magia",
            "guerreiro" : "espada",
            "monge" : "artes marciais",
            "ninja": "shuriken"
            }
        
    #função atacar
    def atacar(self, classe):
        if classe in self.tipo:
            print(f"o {classe} atacou usando {self.tipo[classe]}")


#criando objeto
a = Hero("carlos", 20)
#chamando função
a.atacar("monge")