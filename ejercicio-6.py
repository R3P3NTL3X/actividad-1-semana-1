numero_secreto = 7

adivina = int(input("Adivina cual es el numero que estoy pensando: "))

if adivina > numero_secreto:
    print("uy! calente tu numero es mayor al numero que pienso =c")
elif adivina < numero_secreto:
    print("uy! mas caliente hay tu numero es menor al que pienso =c")
else:
    print("¡Felicidades! Adivinaste el numero en el que estaba pensando =).")
