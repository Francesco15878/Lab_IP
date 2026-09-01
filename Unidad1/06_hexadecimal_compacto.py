numero,hexadecimal=10,"" ## define el numero y añade un str vacio
if numero==0:print("0") ## si el numero ess 0 imprime 0
while numero>0:hexadecimal,numero="0123456789ABCDEF"[numero % 16] + hexadecimal,numero//16 ##y de pendiendo de que residuo tenga en la division de 16 se elige el numero o la letra
print("Número convertido:",hexadecimal) ##Imprime el numero en hexadecimal