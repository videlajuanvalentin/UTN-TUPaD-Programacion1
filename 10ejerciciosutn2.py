# ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

# ejercicio 2

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# ejercicio 3

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# ejercicio 4

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# ejercicio 5

contraseña = input("Ingrese una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ejercicio 6

consumo = float(input("Ingrese el consumo mensual de energía en kWh: "))

if consumo < 150:
    print("Consumo bajo")
elif consumo <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")

if consumo > 500:
    print("Considere medidas de ahorro energético")

# ejercicio 7

frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"

if frase[-1] in vocales:
    print(frase + "!")
else:
    print(frase)

# ejercicio 8

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 (mayúsculas), 2 (minúsculas) o 3 (primera letra mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

# ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# ejercicio 10

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = int(input("Ingrese el mes del año (1-12): "))
dia = int(input("Ingrese el día del mes: "))

# Determinamos el período según fecha (mes, día)
if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
    periodo = "invierno_norte"
elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
    periodo = "primavera_norte"
elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
    periodo = "verano_norte"
else:
    periodo = "otono_norte"

if hemisferio == "N":
    if periodo == "invierno_norte":
        print("Invierno")
    elif periodo == "primavera_norte":
        print("Primavera")
    elif periodo == "verano_norte":
        print("Verano")
    else:
        print("Otoño")
else:
    if periodo == "invierno_norte":
        print("Verano")
    elif periodo == "primavera_norte":
        print("Otoño")
    elif periodo == "verano_norte":
        print("Invierno")
    else:
        print("Primavera")