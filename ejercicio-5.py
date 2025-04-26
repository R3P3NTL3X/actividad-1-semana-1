total_cuenta = float(input("digita el monto total de tu cuenta: $"))

print("¿Cuanto porcentaje quieres dejar de propina?")
print("1. 10%")
print("2. 15%")
print("3. 20%")
porcentaje = int(input("Selecciona 1, 2 o 3: "))

if porcentaje == 1:
    propina = total_cuenta * 0.10
elif porcentaje == 2:
    propina = total_cuenta * 0.15
elif porcentaje == 3:
    propina = total_cuenta * 0.20
else:
    print("Esta opción no válida.")
    propina = 0

print(f"La propina  es: ${propina:.2f}")