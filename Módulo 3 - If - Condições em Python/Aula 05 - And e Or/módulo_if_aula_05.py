# -*- coding: utf-8 -*-
"""Módulo if - Aula 05.ipynb

# Casos com várias condições/comparações

### Estrutura:

Quando temos várias comparações, ao invés de criar if dentro de if podemos usar os operadores "and" e "or" para tratar essas condições.

Funciona assim:

if condicao_1 and condicao_2:
    vai ser executado se as 2 condições forem verdadeiras ao mesmo tempo

outro caso:

if condicao_1 or condicao_2:
    vai ser executado se pelo menos uma das condições forem verdadeiras

### Exemplo

Vamos voltar ao exemplo de cálculo de meta de vendas dos funcionários. Muitas empresas atribuem bonificação do salário dos funcionários de acordo com o resultado do funcionário e também com o resultado da empresa como um todo.

Nesse caso, a regra funciona da seguinte forma:
- Se o funcionário vendeu mais do que a meta de vendas e a loja bateu a meta de vendas da loja, o funcionário ganha 3% do que ele vendeu em forma de bônus.
- Caso o funcionário tenha batido a meta de vendas individual dele, mas a loja não tenha batido a meta de vendas da loja como um todo, o funcionário não ganha bônus.
"""
meta_vendedor = 10000
meta_loja = 1000000

vendas_vendedor = 10000
vendas_loja = 800000

if (vendas_vendedor >= meta_vendedor) and (vendas_loja >= meta_loja):
    bonus = vendas_vendedor * 0.03
    print(F"Parabéns, você bateu a meta de vendas e receberá um bônus de R$ {bonus:.2f}")
else:
    print("Infelizmente as meta de vendas não foram atingidas.")


"""### Outro exemplo

Agora vamos levar essa análise mais a fundo.

Nessa empresa, existe um outro caso também que garante que o funcionário ganhe um bônus, independente das vendas que ele fez naquele mês.

Todo mês os diretores da empresa fazem uma avaliação qualitativa de todos os funcionários. Nessa avaliação os diretores dão uma nota de 0 a 10 para cada funcionário. Se a nota do funcionário for 9 ou 10, ele também ganha o bônus de 3% do valor de vendas. (os bônus não são cumulativos)
"""

nota_funcionario = 7.5
meta_nota = 9

if nota_funcionario >= meta_nota or ((vendas_vendedor >= meta_vendedor) and (vendas_loja >= meta_loja)):
    bonus = vendas_vendedor * 0.03
    print(f"Parabéns, receberá um bônus de R$ {bonus:.2f} por sua avaliação.")
else:
    print("Infelizmente sua nota não foi suficiente para receber o bônus.")