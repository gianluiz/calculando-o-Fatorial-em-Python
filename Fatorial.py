while True: #tratamento de erros inicial, caso o usuário não digite um número.
    try:
        n = int(input("Qual o número de Fatorial você quer ver?"))
        break
    except ValueError:
        print("Tem certeza que você digitou um número?Tente novamente, pois houve um erro...")

#abaixo começa o programa principal
c = n
multiplicador = 1 #se fosse somador ou subtrator, seria 0, mas em divisão e multiplicação, é 1..Essa variável é fundamental para o cálculo do exercício
print(f"Fatorial de {n}:")
while c != 0:
    if c == 1:
        print(f"1 = ", end=(""))
    else:
        print(f"{c} X ", end=(""))
    multiplicador = multiplicador * c #oque importa mesmo é o cálculo desta variável e o debaixo, onde o 'c' foi perdendo 1 a cada loop, para o fatorial dar certo..
    c = c - 1                         #o resto é visual...ou seja, os 'prints' dentro do "while' servem para demonstrar o raciocínio do Fatorial
print(multiplicador)
