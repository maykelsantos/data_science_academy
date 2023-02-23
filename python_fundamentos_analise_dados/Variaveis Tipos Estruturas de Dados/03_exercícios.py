# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
ex_01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ex_01)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
ex_02 = ['Objeto 1', 'Objeto 2', 'Objeto 3', 'Objeto 4', 'Objeto 5']
print(ex_02)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
str1, str2 = 'Um', 'Dois'
print(str1 + str2 + 'Três')

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
ex_04 = (1, 2, 2, 3, 4, 4, 4, 5)
print(ex_04.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
ex_05 = {
    
}
print(ex_05)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
ex_06 = {
    'Chave 1': 'Valor 1',
    'Chave 2': 'Valor 2',
    'Chave 3': 'Valor 3'
}
print(ex_06)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
ex_06['Chave 4'] = 'Valor 4'
print(ex_06)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
ex_08 = {
    'Chave 1': 'Valor 1',
    'Chave 2': 'Valor 2',
    'Chave 3': [1, 2]
}
print(ex_08)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
ex_09 = [
    'string',
    (
        'Elemento 1',
        'Elemento 2'
    ),
    {
        'Chave 1': 'Valor 1',
        'Chave 2': 'Valor 2'
    },
    64.9
]
print(ex_09)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
# frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
ex_10 = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(ex_10[0:18])