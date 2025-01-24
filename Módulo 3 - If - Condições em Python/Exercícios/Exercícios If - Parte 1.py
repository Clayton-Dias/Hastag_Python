# -*- coding: utf-8 -*-
"""05.04.01 Exercícios if.ipynb

# Exercícios com if

## 1. Cálculo de Bônus

- Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:

A meta é 1000 vendas.<br> 
Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.<br>
Caso contrário o valor de bônus do funcionário é 0.<br>
Print o bônus dos 3 funcionários
"""

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

meta = 1000

if vendas_funcionario1 >= meta:
    bonus = 0.1 * vendas_funcionario1
    print(f"Funcionário 1 bateu a meta, e ganhou um bônus de R${bonus:.2f}")
else:
    print("Funcionário 1 não bateu a meta.")
    
if vendas_funcionario2 >= meta:
    bonus = 0.1 * vendas_funcionario2
    print(f"Funcionário 2 bateu a meta, e ganhou um bônus de R${bonus:.2f}")
else:
    print("Funcionário 2 não bateu a meta.")
    
if vendas_funcionario3 >= meta:
    bonus = 0.1 * vendas_funcionario3
    print(f"Funcionário 3 bateu a meta, e ganhou um bônus de R${bonus:.2f}")
else:
    print("Funcionário 3 não bateu a meta.")

"""Resposta:
O funcionário 1 ganhou 100 de bônus
O funcionário 2 ganhou 0 de bônus
O funcionário 3 ganhou 270 de bônus

## 2. Cálculo de bônus com uma nova regra

- Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:

A meta é 1000 vendas<br>
Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:<br>

- Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
- Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
- Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.

Use as mesmas variáveis de vendas_funcionários
"""
#obs: há 2 formas de fazer, com if dentro de if ou então com if e elif. Escolha a que você preferir
if vendas_funcionario1 >= 2000:
    bonus = 0.15 * vendas_funcionario1
    print(f"Funcionário 1 vendeu acima da meta, e ganhou um bônus de R${bonus:.2f}")
elif vendas_funcionario1 >= 1000 and vendas_funcionario1 < 2000:
    bonus = 0.1 * vendas_funcionario1
    print(f"Funcionário 1 bateu a meta, e ganhou um bônus de R${bonus:.2f}")
else: 
    print("Funcionário 1 não bateu a meta.")
    
if vendas_funcionario2 >= 2000:
    bonus = 0.15 * vendas_funcionario2
    print(f"Funcionário 2 vendeu acima da meta, e ganhou um bônus de R${bonus:.2f}")
elif vendas_funcionario2 >= 1000 and vendas_funcionario2 < 2000:
    bonus = 0.1 * vendas_funcionario2
    print(f"Funcionário 2 bateu a meta, e ganhou um bônus de R${bonus:.2f}")
else:
    print("Funcionário 2 não bateu a meta.")
    
if vendas_funcionario3 >= 2000:
    bonus = 0.15 * vendas_funcionario3
    print(f"Funcionário 3 vendeu acima da meta, e ganhou um bônus de R${bonus:.2f}")
elif vendas_funcionario3 >= 1000 and vendas_funcionario3 < 2000:
    bonus = 0.1 * vendas_funcionario3
    print(f"Funcionário 3 bateu a meta, e ganhou um bônus de R${bonus:.2f}")
else:
    print("Funcionário 3 não bateu a meta.")

"""Resposta:
O funcionário 1 ganhou 100 de bônus
O funcionário 2 ganhou 0 de bônus
O funcionário 3 ganhou 405 de bônus
"""