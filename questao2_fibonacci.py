# 2) Dado a sequência de Fibonacci, 
# onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def is_fibonacci(n):
    a, b = 0, 1
    #gera a sequencia fibonacci
    while a < n:
        a, b = b, a + b
    
    if a == n:
        print('pertence a fibonacci')
    else:
        print('nao pertence a fibonacci')

# Número de entrada
number = int(input("Digite um número: "))

is_fibonacci(number)