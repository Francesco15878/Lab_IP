#MAnipulando Rangos

for i in range(0,7,1):
    cuadrado= i **2
    print(i,cuadrado)

materias={"Python","Interfaces","Linux"}

for posicion, materia in enumerate(materias, start=1):
    print(f"{posicion},{materia}")

for materia in materias:
    print(materia)

cadena="0123456789ABCDEF"
for letra in cadena:
   print(letra)

for i in range(0,16,2):
    print(cadena[i])