# -*- coding: utf-8 -*-
"""Módulo if - Aula 01.ipynb

# Condições no Python -> If

## Estrutura:

### Uso mais simples:

if condição:
    o que fazer caso a condição seja verdadeira

### Exemplo Real (informações 100% hipotéticas e inventadas):

Digamos que você trabalha na Amazon (que tem centenas de milhares, se não milhões de produtos) e está analisando o resultado de vendas dos produtos.

Você precisa criar um programa que vai analisar o resultado de vendas dos produtos da Amazon em um mês. Para simplificar vamos pensar em um único produto: um Iphone.

Meta de Vendas do Iphone = 50.000 unidades
Quantidade vendida no Mês = 65.300 unidades

O seu programa deve avisar (usaremos o print por enquanto) caso o produto tenha batido a meta do mês. Então devemos fazer:<br>
- Caso o produto tenha batido a meta, devemos exibir a mensagem: "Batemos a meta de vendas de Iphone, vendemos {} unidades" 
- Se ele não bateu a meta do mês, o seu programa não deve fazer nada
"""
meta_venda = 50000
qtd_vendida = 65300

if qtd_vendida > meta_venda:
    print(f"Batemos a meta de vendas! Vendemos {qtd_vendida} unidades.")


"""### Tratando a condição falsa:
Quando usamos o if, nem sempre queremos apenas analisar o caso verdadeiro, em boa parte das vezes queremos fazer alguma coisa caso a condição seja verdadeira e fazer outra coisa caso a condição seja falsa.

Nesse caso usaremos:

if condição:
    o que eu quero fazer caso a condição seja verdadeira
else:
    o que eu quero fazer caso a condição seja falsa

Voltando ao nosso Exemplo Real da Amazon e do Iphone, agora nossa programa deve avisar nos 2 casos:
- Caso o produto tenha batido a meta, devemos exibir a mensagem: "Batemos a meta de vendas de Iphone, vendemos {} unidades" 
- Se ele não bateu a meta do mês, devemos exibir a mensagem: "Infelizmente não batemos a meta, vendemos {} unidades. A meta era de {} unidades"
"""
if qtd_vendida > meta_venda:
    print(f"Batemos a meta de vendas! Vendemos {qtd_vendida} unidades.")
else:
    print(f"Infelizmente não batemos a meta, vendemos apenas {qtd_vendida} unidades. A meta era de {meta_venda} unidades.")