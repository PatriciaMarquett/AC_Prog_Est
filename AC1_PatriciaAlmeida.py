"""
AC1 - Aluna: Patricia Almeida Marquett
Matrícula: 202302989527
"""
# Exercício 1
# Enunciado:Elabore um código em Python que resolva uma equação do segundo grau ax² + bx + c = 0
# O programa deve ler os parâmetros a, b e c da equação e deve calcular as raízes pela fórmula de Bhaskara.
# Considere que as raízes dadas pelo usuário são sempre reais, e os valores passados pelo usuário são sempre numéricos.
# Baskara: x1=(-b+(b^2-4*a*c)^1/2)/2*a e x2=(-b-(b^2-4*a*c)^1/2)/2*a

a = float(input("Informe o parâmetro a da equação:"))
b = float(input("Informe o parâmetro b da equação:"))
c = float(input("Informe o parâmetro c da equação:"))
print("A primeira raiz da equação é", round((-b+(b^2-4*a*c)^1/2)/2*a))
print("A segunda raiz da equação é", round((-b-(b^2-4*a*c)^1/2)/2*a))
