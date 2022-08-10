'''
Essa é uma introdução à biblioteca Matplotlib, feita para plot de imagens com Python.

É uma biblioteca extremamente versátil, as opções estéticas são muito diversas, limitadas
em geral apenas à inventividade do usuário.
'''

import numpy as np
import matplotlib.pyplot as plt


# Primeiramente, vamos criar alguns dados para serem visualizados:

x = np.linspace(0,7,101)

y1 = np.cos(x)
y2 = np.cos(2*x)
y3 = np.cos(x/2)
y4 = np.sin(2*x + np.pi/3)


# Para criar um gráfico com o Matplotlib, devemos inicialmente criar uma figura 
# a qual conterá os gráficos. Para isso, usamos a função plt.figure, que recebe 
# como argumento um número que será a identificação da figura 
# (caso tenhamos diversas figuras abertas, elas estarão em janelas separadas).
plt.figure(0)

# Agora devemos dar o comando de fazer o gráfico. Vamos usar a função plot, que faz
# pontos de acordo com coordenadas (x, y) e os liga em ordem.
plt.plot(x, y1)

# Agora basta pedirmos ao matplotlib que nos mostre a figura com o comando show:
plt.show()

# Ao terminar de visualizar um gráfico, é boa prática fechar a figura para que
# os dados não permaneçam ocupando espaço na memória:
plt.close()


# Ao longo do tutorial, iremos plotar diversos gráficos, então coloquei algumas 
# marcas de interrupção do código para que ele não execute todas de uma vez. 
# Ao ir avançando, basta comentar os comandos "plt.show()" e "exit()" para que 
# o código continue em frente sem ficar mostrando a mesma imagem repetidas vezes.

#exit() # Marca 1


# Podemos também colocar diversos gráficos em uma única figura:
plt.figure(1) # A figura 0 já foi fechada, então poderíamos tê-la reutilizado aqui
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)

# Podemos também colocar algumas anotações para deixar o gráfico mais claro, 
# como título e legenda dos eixos. Podemos escrever esses termos com o padrão
# do Latex para incluir letras gregas e outros símbolos. 
# (Normalmente deve ser passado como rawstring para que funcione o Latex:)
# "sou uma string" -> string
# r"sou uma raw string" -> rawstring
plt.title("Funções Trigonométricas")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()
#exit() # Marca 2
plt.close()


# O Matplotlib escolhe automaticamente as cores dos gráficos quando há diversos 
# plots juntos, porém podemos fazer isso à mão, além de escolher também o estilo
# do tracejado das linhas (linestyle), dentre diversas outras opções.
# Consulte a documentação do Matplotlib para ver mais exemplos e opções.
# Opção c:  cores 		-> "r", "b", "g", "o", "k", etc ou "red", "blue", "cyan", etc
# Opção ls: linestyle	-> "-", "--", "-.", ":", etc
# Além disso, podemos colocar uma legenda que explica cada um dos plots com a
# opção label.
plt.figure(2)
plt.plot(x, y1, c="b", ls="-", label="$\cos(x)$") 
plt.plot(x, y2, c="g", ls="-.", label=r"$\cos(2x)$")
plt.plot(x, y3, c="c", ls="--", label=r"$\cos(\frac{x}{2})$")
plt.plot(x, y4, c="k", ls=":", label=r"$\cos(2x + \frac{\pi}{3})$")

plt.title("Funções Trigonométricas")
plt.xlabel("x")
plt.ylabel("f(x)")

# Comando para aparecer a caixa de legenda:
plt.legend(loc="best") # podemos definir a sua localização com o argumento loc

plt.show()
exit() # Marca 3
plt.close()


# Existem diversas outras funções de imagens no Matplotlib. Alguns exemplos são
# plt.scatter -> faz o plot mas sem ligar os pontos
# plt.hist -> faz um histograma
# plt.imshow / plt.pcolormesh -> plota imagens 2D


# O Matplotlib também é capaz de fazer plots mais complexos, 
# colocar diversos gráficos em uma única figura, fazer plots 3D, 
# fazer plots animados, dentre outras opções.
# Para essas tarefas, a estrutura de comando é ligeiramente diferente,
# mas segue a mesma lógica que vimos aqui.
