# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule
# a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

number = int(input())
antes = 0
depois = 0
proximo = antes
fibonacci = False
while antes <= number:
    antes = depois
    if antes == number:
        fibonacci = True
        break
    depois = proximo + depois
    proximo = antes
    if antes == 0:
        depois = 1
if fibonacci:
    print('O número pertence à sequência')
else:
    print('Esse número não pertence à sequência')