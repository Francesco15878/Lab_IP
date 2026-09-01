n=input("Proporcione un numero: ")
n=int(n)
if n <= 1:
    print("No es primo")

i=2

while i<= n:
    if n % i == 0 and i != 2:
        print("No es primo")
        break
    elif n % i == 0 and i == n:
        print("Es primo")
        break
    elif n % i != 0 and i < n:
        print("Es primo")
        break
    i= i + 1

    numero=int(input("INgrese un  numero"))
    i=2
    primo=1
    while i<numero:
        if numero %i ==0:
            primo=0
    i+=i
    if primo ==1:
        print("El numero es primo")
    if primo==0:
        print("EL numero no es primo")