numero1 = float(input("Cual es tu primer numero: "))
numero2 = float(input("Cual es tu segundo numero: "))

if numero1 > numero2:
    print(f"El número mas grande  es: {numero1}")
elif numero1 < numero2:
    print(f"El número mas grande  es: {numero2}")
else:
    print("Los dos son el mismo numero.")