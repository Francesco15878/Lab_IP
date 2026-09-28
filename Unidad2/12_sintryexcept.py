"""while True:
    edad = input("Edad: ")
    if not edad.isdigit():
        print("Escribe un número entero.")
    elif not 0 <= int(edad) <= 120:
        print("La edad debe estar entre 0 y 120.")
    else:
        edad = int(edad)
        break

print(f"Edad registrada: {edad}")"""
while True:
        
        edad= int(input("Edad: "))

        if 0<= edad <= 120 and type(edad)==int:
            break

        print("La edad debe estar entre 0 y 120.")

        if type(edad)!=int:
            print("Escribe un numero entero.")

print(f"Edad registrada:{edad}")