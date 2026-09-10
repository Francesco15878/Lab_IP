total_cuenta=float(input("Ingrese el total de su cuenta: "))
porcentaje_propina=float(input("Ingrese el porcentaje: "))
num_personas=int(input("Ingrese el total de personas: "))
total=(total_cuenta)+((porcentaje_propina/100)*total_cuenta)
propina=(porcentaje_propina/100)*total_cuenta
cuenta_individual=(total_cuenta+propina)/num_personas

print("Subtotal: ",total_cuenta)
print("Propina: ",propina)
print("El total es: ",total)
print("Cada persona debe pagar: ", cuenta_individual)