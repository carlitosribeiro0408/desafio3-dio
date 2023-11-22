# Classes de Jogo

## Hero

### Método de Inicialização

A classe `Hero` é definida para representar um herói no jogo. Possui um método de inicialização que recebe dois parâmetros: `nome` e `idade`. O objeto herói é inicializado com as características fornecidas.

```python
def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
```

Além disso, a classe possui um dicionário chamado `tipo`, que mapeia diferentes classes de heróis a seus respectivos estilos de ataque.

```python
self.tipo = {
    "mago" : "magia",
    "guerreiro" : "espada",
    "monge" : "artes marciais",
    "ninja": "shuriken"
}
```

### Função Atacar

A classe possui um método chamado `atacar` que aceita como parâmetro a classe do oponente. Se a classe fornecida estiver presente no dicionário `tipo`, exibirá uma mensagem indicando que o herói atacou usando o método associado a essa classe.

```python
def atacar(self, classe):
    if classe in self.tipo:
        print(f"O {classe} atacou usando {self.tipo[classe]}")
```

## Exemplo de Uso

Um objeto `Hero` é criado com o nome "Carlos" e a idade 20.

```python
a = Hero("Carlos", 20)
```

A função `atacar` é então chamada, passando "monge" como argumento.

```python
a.atacar("monge")
```

Isso resultaria na impressão da mensagem "O monge atacou usando artes marciais".
