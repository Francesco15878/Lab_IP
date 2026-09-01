numero,hexadecimal= 10, "" #se define que numero es 8 y hexadecimal una cadena
if numero == 0:    print("0") #verifica si numero es igual a 0 en caso de si imprime 0
while numero > 0: 
    residuo=numero%16
    if residuo == 1:
        hexadecimal= "1" + hexadecimal
    elif residuo == 2:
        hexadecimal= "2" + hexadecimal
    elif residuo == 3:
        hexadecimal= "3" + hexadecimal
    elif residuo == 4:
        hexadecimal= "4" + hexadecimal
    elif residuo == 5:
        hexadecimal= "5" + hexadecimal
    elif residuo == 6:
        hexadecimal= "6" + hexadecimal
    elif residuo == 7:
        hexadecimal= "7" + hexadecimal
    elif residuo == 8:
        hexadecimal= "8" + hexadecimal
    elif residuo == 9:
        hexadecimal= "9" + hexadecimal
    elif residuo == 10:
        hexadecimal= "A" + hexadecimal
    elif residuo == 11:
        hexadecimal= "B" + hexadecimal
    elif residuo == 12:
        hexadecimal= "C" + hexadecimal
    elif residuo == 13:
        hexadecimal= "D" + hexadecimal
    elif residuo == 14:
        hexadecimal= "E" + hexadecimal
    elif residuo == 15:
        hexadecimal= "F" + hexadecimal
    numero= numero//16      

print("Número convertido:",hexadecimal) #Se imprime el numero convertido a hexadecimal