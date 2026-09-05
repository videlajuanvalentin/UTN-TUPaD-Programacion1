# ejercicio 1
print("Hola Mundo!")

# ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# ejercicio 3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# ejercicio 4

import math

radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El área es {area:.2f} y el perímetro es {perimetro:.2f}")

# ejercicio 5

segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# ejercicio 6

numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# ejercicio 7

num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))

print(f"Suma: {num1 + num2}")
print(f"División: {num1 / num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"Resta: {num1 - num2}")

# ejercicio 8

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))

imc = peso / (altura ** 2)
print(f"Su índice de masa corporal es {imc:.2f}")

# ejercicio 9

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit}°F")

# ejercicio 10

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

promedio = (n1 + n2 + n3) / 3
print(f"El promedio es {promedio:.2f}")