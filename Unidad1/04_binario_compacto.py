numero,binario= 8, "" #se define que numero es 8 y binario una cadena
if numero == 0:    print("0") #verifica si numero es igual a 0 en caso de si imprime 0
while numero > 0:  binario,numero = str(numero%2) + binario, numero//2 #mientras el numero sea mayor a cero se calcula el residuo y se suma a binario y se divide entre 2 el numero 
print("Número convertido:",binario) #Se imprime el numero convertido a binario