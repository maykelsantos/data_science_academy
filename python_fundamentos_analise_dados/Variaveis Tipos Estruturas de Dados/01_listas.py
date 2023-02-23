# criando a lista com único elemento
lista_do_mercado = ['ovos, farinha, leite, maças']
print(lista_do_mercado)

# criando outra lista com vários elementos
lista_do_mercado_2 = ['ovos', 'farinha', 'leite', 'maças']
print(lista_do_mercado_2)

# extraindo o primeiro elemento de cada lista
print(lista_do_mercado[0])
print(lista_do_mercado_2[0])

# criando outra lista
lista_3 = [12, 100, 'Universidade']
print(lista_3)

# atribuindo cada valor da lista a uma variável
item_1 = lista_3[0]
item_2 = lista_3[1]
item_3 = lista_3[2]
print(item_1, item_2, item_3)

# atualizando um item da lista
lista_do_mercado_2[2] = 'chocolate'
print(lista_do_mercado_2)

# remover um item da lista
del lista_do_mercado_2[3]
print(lista_do_mercado_2)

# criando uma lista aninhada (lista dentro de lista)
listas_aninhadas = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]
print(listas_aninhadas)

# atribuindo um item da lista a uma variável
a = listas_aninhadas[0]
b = a[0]
print(a, b)

#atribuindo à variável o primeiro valor da primeira lista
c = listas_aninhadas[1][1]
print(c)

# operações matemáticas com as listas aninhadas
d = listas_aninhadas[2][0] + listas_aninhadas[2][1]
e = listas_aninhadas[2][0] * 10
print(d, e)

# imprimindo com novas operações matemáticas
print('A varrável D é ', d)
print('A variável E é ', e)
print('A soma é ', d + e)
print('A subtração é ', d - e)
print('A divisão é ', d / e)
print('A multiplicação é ', d * e)

# concatenando listas
lista_concatenada = listas_aninhadas[0] + listas_aninhadas[1]
print(lista_concatenada)

# verificando se um valor pertence a lista (True ou False)
verificando_lista = [100, 2, -5, 3.4]
print(10 in verificando_lista)
print(100 in verificando_lista)

# contando elementos da lista
print(len(verificando_lista))

# maior valor da lista
print(max(verificando_lista))

# menor valor da lista
print(min(verificando_lista))

# adicionado um elemento à lista
verificando_lista.append('carne')
print(verificando_lista)

# contando quantas vezes o elemento aparece na lista
print(verificando_lista.count('carne'))

# inserindo elemento na lista numa posição específica
verificando_lista.insert(1,'*&¨&%')
print(verificando_lista)