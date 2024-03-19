"""AC2 - Aluna: Patricia Almeida Marquett
Matrícula: 202302989527
"""

#1.Triângulos

def determina_tipo_triangulo (a, b, c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        if  (a==b) and (b==c):
            return "Equilátero"
        elif (a==b) or (b==c) or (c==a):
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é um triângulo"


def testa_triangulo():
    print(determina_tipo_triangulo(4,4,4)) # Equilátero
    print(determina_tipo_triangulo(2,4,4)) # Isósceles
    print(determina_tipo_triangulo(3,4,5)) # Escaleno
    print(determina_tipo_triangulo(1,1,4)) # Não é um triângulo

testa_triangulo()

print("-"*30)

#2. Dias da Semana

def dia_semana(dia):
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-Feira"
        case 3:
            return "Terça-Feira"
        case 4:
            return "Quarta-Feira"
        case 5:
            return "Quinta-Feira"
        case 6:
            return "Sexta-Feira"
        case 7:
            return "Sábado"
        case _:
            return ""


def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

testa_dia_semana()

print("-"*30)

#3 Calculadora simples

"""Desenvolva funções de operações aritméticas soma, subtracao, multiplicacao e divisao,
que recebem dois números cada uma e retornam o resultado da operação indicada.
Em seguida, crie uma função que elabora uma interface por linha de comando (CLI),
que lê dois números e uma operação e exibe na tela o valor do resultado,
ou exibe "operação inválida" se o usuário inserir uma mensagem diferente das quatro operações"""

def som (x1,x2):
    return x1 + x2

def sub(x1,x2):
    return x1 - x2

def mult (x1, x2):
    return x1*x2

def div (x1, x2):
    return x1/x2

def calculadora():
    a = float(input("Informe um número:"))
    b = float(input("Informe outro número:"))
    op = input("Informe a operação:")
    match op:
        case "soma":
            print ("Resultado:", a+b)
        case " subtração":
            print ("Resultado:", a-b)
        case "multiplicação":
            print ("Resultado:", a*b)
        case "divisão":
            print ("Resultado:", a/b)
        case _:
            print ("operação inválida")

calculadora()


