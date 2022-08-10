'''
Essa é uma introdução à biblioteca Numpy, feita para análise de dados com Python.
'''

import numpy as np # aqui estamos dizendo que iremos chamar a biblioteca com "np."

print("\n\nIntrodução: Arrays\n")

# Listas em Python não são feitas para cálculos matemáticos.
# Ex.: soma e multiplicação.
lista1 = [1, 2, 3, 4]
lista2 = [11, 23, 25, 29]

lista3 = lista1+lista2
print("\nSoma das listas {} e {}:".format(lista1, lista2))
print(lista3)

lista4 = 3*lista1
print("\nProduto 3*{}:".format(lista1))
print(lista4)


# As operações não são feitas elemento a elemento, como gostaríamos.
# É aí que entram os arrays do Numpy:

# Podemos fazer um array a partir de uma lista nova que criarmos:
array1 = np.array([3, 4, 5, 7])
# Ou a partir de uma lista já existente:
array2 = np.array(lista1)

array3 = array1+array2
print("\nSoma dos arrays {} e {}:".format(array1, array2))
print(array3)
array4 = 3*array1
print("\nProduto 3*{}:".format(array1))
print(array4)

# Não é possível somar uma lista a um int/float. Porém pode-se fazer isso com um array:
array5 = array1 + 100
print("\nSoma {} + 100:".format(array1))
print(array5)

# De forma geral, os arrays do Numpy são MAIS EFICIENTES do que as listas do Python.
# Então sempre dê preferência para utilizá-los.


print("\n\nNumpy: arange e linspace\n")
# Duas funções se destacam bastante quando se fala em arrays:
# np.arange e np.linspace

# A função arange se comporta exatamente igual ao range do Python:
# range(start, stop, step) produz uma sequência que começa em "start", 
# termina em "stop", e avança em passos de "step" em "step".
# Note que o ponto de stop é excluído da sequência.
start = 10
stop = 30
step = 4
lista_range = list(range(start, stop, step)) # o range não produz uma lista, então devemos usar o comando list() para transformá-lo em uma lista
print("\nLista produzida com start={}, stop={}, step={}:".format(start, stop, step))
print(lista_range)

array_arange = np.arange(start, stop, step)
print("\nArray produzido com start={}, stop={}, step={}:".format(start, stop, step))
print(array_arange)

# A grande diferença é que o arange permite trabalhar com float, enquanto o range permite apenas inteiros!!


# A função linspace é bem parecida, só que ao invés de dar o step, 
# você fornece a quantidade de pontos que deseja que seja produzida, 
# sem se preocupar com o intervalo entre eles. O numpy garante que o espaçamento
# entre os pontos seja constante (daí o nome, linear spacement).
# Note que o ponto do stop aqui é incluído no array.
number = 11 # quantidade de pontos, incluindo final.
array_linspace = np.linspace(start, stop, number)
print("\nArray produzido com start={}, stop={}, number={}:".format(start, stop, number))
print(array_linspace)


print("\n\nTécnicas com arrays\n")
# Existem diversos *métodos* que podem ser aplicados sobre os arrays
# para que possamos obter novos arrays, ou então *atributos* que podemos
# consultar para termos mais informações sobre os arrays.

# Vamos começar com um array simples:
array_basico = np.arange(0,100,5)
print("\nNosso array básico:")
print(array_basico)

# Para sabermos as dimensões de uma lista em Python, usamos a função len().
# Para arrays, podemos consultar o atributo shape:
print("\nShape do array:")
print(array_basico.shape)
# Esse atributo retorna uma lista com as dimensões de um array.
numero_pontos = array_basico.shape[0] # Pegando a primeira dimensão desse array (que é unidimensional, então só tem um número caracterizando seu shape)

# Podemos tamber usar o método reshape para remodelar um array em um novo formato
novas_dimensoes = [4,5]
print("\nNovas dimensões do array:", novas_dimensoes)
array_redim = array_basico.reshape(novas_dimensoes)
print("\nArray redimensionado:")
print(array_redim)
print("Novo shape do array:", array_redim.shape)


print("\n\nOperações Matemáticas\n")
# O Numpy tem variedade de operações matemáticas muito extensa à nossa disposição.
# O mais atrativo delas é que são todas aplicáveis não apenas a números (floats, ints)
# como também a arrays inteiros, o que as torna extremamente práticas.

# Alguns exemplos: log, log10, sin, cos, tan, exp, 
resultado1 = np.log10(100)
print("\nlog10(100):", resultado1)
resultado2 = np.cos(3)
print("\ncos(3) = ",resultado2)


