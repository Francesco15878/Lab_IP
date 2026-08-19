numero= 8
if numero == 0:
    print("0")

hexadecimal=""
while numero > 0:
    residuo = numero%16
    if residuo == 1:
        hexadecimal= "1" + hexadecimal
    if residuo == 2:
        hexadecimal= "2" + hexadecimal
    if residuo == 3:
        hexadecimal= "3" + hexadecimal
    if residuo == 4:
        hexadecimal= "4" + hexadecimal
    if residuo == 5:
        hexadecimal= "5" + hexadecimal
    if residuo == 6:
        hexadecimal= "6" + hexadecimal
    if residuo == 7:
        hexadecimal= "7" + hexadecimal
    if residuo == 8:
        hexadecimal= "8" + hexadecimal
    if residuo == 9:
        hexadecimal= "9" + hexadecimal
    if residuo == 10:
        hexadecimal= "A" + hexadecimal
    if residuo == 11:
        hexadecimal= "B" + hexadecimal
    if residuo == 12:
        hexadecimal= "C" + hexadecimal
    if residuo == 13:
        hexadecimal= "D" + hexadecimal
    if residuo == 14:
        hexadecimal= "E" + hexadecimal
    if residuo == 15:
        hexadecimal= "F" + hexadecimal
    numero= numero//16        

print("Número convertido:",hexadecimal)