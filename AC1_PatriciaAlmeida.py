"""
AC1 - Aluna: Patricia Almeida Marquett
Matrícula: 202302989527
"""
# Exercício 1
# Enunciado:Elabore um código em Python que resolva uma equação do segundo grau ax² + bx + c = 0
# O programa deve ler os parâmetros a, b e c da equação e deve calcular as raízes pela fórmula de Bhaskara.
# Considere que as raízes dadas pelo usuário são sempre reais, e os valores passados pelo usuário são sempre numéricos.

a = float(input("Informe o parâmetro a da equação:"))
b = float(input("Informe o parâmetro b da equação:"))
c = float(input("Informe o parâmetro c da equação:"))
delta = b**2-4*a*c
x1 = float(((-1)*b + delta**0.5)/(2*a))
x2 = float(((-1)*b - delta**0.5)/(2*a))
print("A primeira raiz da equação é", x1)
print("A segunda raiz da equação é", x2)

print("-" * 30)

#Exercicio 2
#Enunciado:Elabore um programa em Python que leia uma variável inteira ano.
#Exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto.
#Um ano é bissexto se ele é múltiplo de quatro.
#Anos múltiplos de 100 que não são múltiplos de 400 não são bissextos.
#Utilizar apenas as funções print(), input() e int(),
#Além dos operadores lógicos and, or ou not e comparações
ano = int(input("Informe o ano:"))
print((ano%4==0 and ano%100!=0) or ano%400==0)


