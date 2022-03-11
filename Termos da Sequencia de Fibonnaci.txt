#Posso fazer uma sequância de fibonacci para mostrar a quantidade de termos que eu quiser

print("=" * 40)
print("Sequência de Fibonacci")
print("=" * 40)
num = int(input("Quantos termos você quer mostrar: "))

t1 = 0
t2 = 1
contador = 3
print("{} -> {}".format(t1, t2), end = "")

while contador <= num:
    t3 = t1 + t2
    print(" -> {}".format(t3), end = "")
    t1 = t2
    t2 = t3
    contador = contador + 1
print(" FIM ")
