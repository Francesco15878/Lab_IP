numero,octal= 8, "" #se define que numero es 8 y octal una cadena
if numero == 0:    print("0") #verifica si numero es igual a 0 en caso de si imprime 0
while numero > 0:  octal,numero = str(numero%8) + octal, numero//8 #mientras el numero sea mayor a cero se calcula el residuo y se suma a octal y se divide entre 8 el numero 
print("Número convertido:",octal) #Se imprime el numero convertido a octal