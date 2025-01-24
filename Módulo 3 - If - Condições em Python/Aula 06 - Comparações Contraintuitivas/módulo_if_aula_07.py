# -*- coding: utf-8 -*-
"""Módulo if - Aula 06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KOJUk6_6xh-cNA_19hC2WQV1SKQ7w96W

# Comparações Contraintuitivas

Existem algumas comparações no Python que não são tão intuitivas quando vemos pela primeira vez, mas que são muito usadas, principalmente por programadores mais experientes.

É bom sabermos alguns exemplos e buscar sempre entender o que aquela comparação está buscando verificar.

### Exemplo 1:

Digamos que você está construindo um sistema de controle de vendas e precisa de algumas informações para fazer o cálculo do resultado da loja no fim de um mês.
"""
faturamento = input('Qual foi o faturamento da loja nesse mês?')
custo = input('Qual foi o custo da loja nesse mês?')

if faturamento == '' or custo == '':
    print('Por favor, preencha os campos corretamente')
else:    
    lucro = int(faturamento) - int(custo)
    print("O lucro da loja foi de {} reais".format(lucro))
    
"""
Outra forma de fazer o código é a seguinte:

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print("O lucro da loja foi de {} reais".format(lucro))
else:    
    print('Por favor, preencha os campos corretamente')
"""    

"""## Resumo

Algumas comparações contraintuitivas muito usadas:

If 0:

If '':

Temos outras também, mas que são usadas para verificar listas vazias, dicionários vazios, objetos vazios e assim vai. Quando chegarmos nesses módulos vamos relembrar esse conceito, mas o importante é saber dessa possibilidade e entender seu uso.
"""