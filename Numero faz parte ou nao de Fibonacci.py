#Descobrindo se o número escolhido faz parte de Fibonnaci
print("=" * 30)
print("Sequência de Fibonacci")
print("=" * 30)

num = int(input("Digite o número desejado: "))
termo1 = 0
termo2 = 1
termo3 = 0

while termo3 < num:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3

if num == termo3:
    print("O número {} pertence a Sequência de Fibonacci".format(num))
else:
    print("O número {} NÃO pertence a Sequência de Fibonacci".format(num))