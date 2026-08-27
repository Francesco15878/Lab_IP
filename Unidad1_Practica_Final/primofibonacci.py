numero=int(input("Ingresa un numero: "))
es_primo = True
if numero <= 1:
    es_primo = False
else:
    i=2
    while i<numero:
        if numero %i ==0:
            es_primo=False
        i+=1

if es_primo == True:
    print("El numero es primo")
    a=0
    b=1
    while a<numero:
        siguiente=a+b
        a=b
        b=siguiente
    if a == numero:
        print("Esta en fibonacci")
    else:
        print("No esta en fibonacci")  
if es_primo==False:
    print("EL numero no es primo")