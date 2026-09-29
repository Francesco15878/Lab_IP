def consultar_saldo():
    print("Saldo: $0.00")
def depositar():
    print("Depósito realizado")
def retirar():
    print("Retiro realizado")
def salir():
    print("Saliendo del cajero automático")
def mostrar_menu():
    print("Bienvenido al cajero automático")
    print("1, Consultar saldo")
    print("2, Depositar")
    print("3, Retirar")
    print("4, Salir")
    return input("Opción: ").strip()
def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            salir()
            break
        else:
            print("Opción inválida")
def login():
    USUARIO= "alumno"
    CLAVE= "python123"
    usuario= input("Usuario: ").strip().lower()
    clave= input("Contraseña: ")
    if usuario == USUARIO and clave == CLAVE:
        main()
    else:
        print("Credenciales incorrectas")
login()