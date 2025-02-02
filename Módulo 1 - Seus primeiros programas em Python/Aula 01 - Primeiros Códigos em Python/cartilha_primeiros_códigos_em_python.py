# -*- coding: utf-8 -*-
"""Cartilha - Primeiros Códigos em Python.ipynb

# Cartilha para Consulta - 1ºs Códigos em Python

Essa cartilha é para revisão e consulta dor primeiros códigos que aprendemos. Na prática você vai acabar naturalmente decorando esses códigos a medida que formos usando mais no curso, mas essa cartilha pode te ajudar sempre que precisar.

### print(texto) -> Para "imprimir" (exibir) um texto ou uma variável
"""

print('O faturamento da loja foi de R$1.000')


"""### Textos (strings) são sempre entre aspas

'lira@gmail.com' -> é uma string
lira@gmail.com -> vai dar erro porque o Python acha que isso é uma variável (vamos ver como funcionam mais a frente)

### Operações Mateméticas no Python:

1. Adição -> +
2. Subtração -> -
3. Divisão -> /
4. Multiplicação -> *
5. Mod (resto da divisão) -> %
"""

#adição
print(3 + 5)

#subtração
print(5 - 3)

#divisão
print(5 / 3)

#multiplicação
print(5 * 3)

#mod (resto da divisão de 5 por 3)
print(5 % 3)

"""### Operações Básicas com String

1. Concatenar -> +
2. Verificar se um texto está contido dentro do outro -> in
"""

#Concatenar
print('O faturamento da loja foi ' + '1000')

#Verificar se um texto está dentro do outro
print('@' in 'lira@gmail.com')

"""### Variável

variavel = valor
"""

faturamento = 1500
custo = 800
lucro = faturamento - custo 
print(faturamento)
print(lucro)

"""### Pegar informações do Usuário

variavel = input('Texto para o Usuário')
"""

#para cadastrar um cliente
cpf = input('Digite seu cpf (apenas números, sem pontos e traços)')
print('O cpf do cliente é ' + cpf)