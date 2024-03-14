"""AC2 - Aluna: Patricia Almeida Marquett
Matrícula: 202302989527
"""

#1. Função para retornar as raízes de uma equação de segundo grau
def raizes_eq(a, b, c):
    delta = b ** 2 - 4 * a * c
    return ((-b + delta ** 0.5) / (2 * a)) , ((-b - delta ** 0.5) / (2 * a))
#teste
print(raizes_eq(1, -6, 8))
print(raizes_eq(2, 16, 3))

print("-"*30)

#2. Função para informar se o ano é bissexto ou não
def ano_bisexto(ano):
    return (ano%4==0 and ano%100!=0) or ano%400==0
#teste
print(ano_bisexto(1995))
print(ano_bisexto(2012))
print(ano_bisexto(1900))
print(ano_bisexto(2000))

print("-"*30)

#3. Função para calcular salário
def calcula_salario(valor_hora, num_horas):
    bruto = valor_hora * num_horas
    irpf = 0.275*bruto
    return bruto - irpf

#teste
print(calcula_salario(100,10))











