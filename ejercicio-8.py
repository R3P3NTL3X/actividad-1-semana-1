
peso = int(input("Cual es tu peso en kilogramos  (kg): "))
altura = float(input("Cual es tu estatura en metros (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Tu IMC es {imc:.2f}. Bajo peso.")
elif 18.5 <= imc < 25:
    print(f"Tu IMC es {imc:.2f}. Normal.")
elif 25 <= imc < 30:
    print(f"Tu IMC es {imc:.2f}. Sobrepeso.")
else:
    print(f"Tu IMC es {imc:.2f}. Obesidad.")
