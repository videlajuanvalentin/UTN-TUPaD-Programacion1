# ejercicio 1

# Nombre del cliente (solo letras, no vacío)
nombre = input("Cliente: ")
while not nombre.isalpha():
    print("Error: el nombre solo puede contener letras.")
    nombre = input("Cliente: ")

# Cantidad de productos (entero positivo)
cantidad_str = input("Cantidad de productos: ")
while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
    print("Error: ingrese un número entero mayor a 0.")
    cantidad_str = input("Cantidad de productos: ")
cantidad = int(cantidad_str)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad + 1):
    precio_str = input(f"Producto {i} - Precio: ")
    while not precio_str.isdigit():
        print("Error: ingrese un precio válido (entero).")
        precio_str = input(f"Producto {i} - Precio: ")
    precio = int(precio_str)

    descuento = input("Descuento (S/N): ")
    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Error: ingrese S o N.")
        descuento = input("Descuento (S/N): ")

    total_sin_descuento += precio

    if descuento.lower() == "s":
        precio_final = precio - (precio * 0.10)
    else:
        precio_final = precio

    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print()
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

# ejercicio 2

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and not acceso:
    intentos += 1
    usuario = input(f"Intento {intentos}/3 - Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        print("Error: credenciales inválidas.")

if acceso:
    salir = False
    while not salir:
        print()
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion_str = input("Opción: ")

        while not opcion_str.isdigit():
            print("Error: ingrese un número válido.")
            opcion_str = input("Opción: ")

        opcion = int(opcion_str)

        while opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            opcion_str = input("Opción: ")
            while not opcion_str.isdigit():
                print("Error: ingrese un número válido.")
                opcion_str = input("Opción: ")
            opcion = int(opcion_str)

        if opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")
            confirmacion = input("Confirmar clave: ")
            while confirmacion != nueva_clave:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirmar clave: ")
            clave_correcta = nueva_clave
            print("Clave actualizada con éxito.")
        elif opcion == 3:
            print("¡Vos podés lograrlo, seguí adelante!")
        elif opcion == 4:
            salir = True
            print("Saliendo del sistema...")
else:
    print("Cuenta bloqueada")

# ejercicio 3

# Nombre del operador
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: solo se permiten letras.")
    operador = input("Nombre del operador: ")

# Turnos de lunes (4) y martes (3), inicializados vacíos
lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

salir = False
while not salir:
    print()
    print("1) Reservar  2) Cancelar  3) Ver agenda del día  4) Resumen general  5) Cerrar sistema")
    opcion_str = input("Opción: ")
    while not opcion_str.isdigit() or int(opcion_str) < 1 or int(opcion_str) > 5:
        print("Error: ingrese un número entre 1 y 5.")
        opcion_str = input("Opción: ")
    opcion = int(opcion_str)

    if opcion == 1:
        dia_str = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia_str != "1" and dia_str != "2":
            print("Error: opción inválida.")
            dia_str = input("Elegir día (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            print("Error: solo letras.")
            paciente = input("Nombre del paciente: ")

        if dia_str == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: el paciente ya tiene turno el lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado en Lunes 1.")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado en Lunes 2.")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado en Lunes 3.")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado en Lunes 4.")
            else:
                print("No hay turnos disponibles el lunes.")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: el paciente ya tiene turno el martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado en Martes 1.")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado en Martes 2.")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado en Martes 3.")
            else:
                print("No hay turnos disponibles el martes.")

    elif opcion == 2:
        dia_str = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia_str != "1" and dia_str != "2":
            print("Error: opción inválida.")
            dia_str = input("Elegir día (1=Lunes, 2=Martes): ")

        paciente = input("Nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            print("Error: solo letras.")
            paciente = input("Nombre del paciente a cancelar: ")

        encontrado = False
        if dia_str == "1":
            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True
            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True
            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True
            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True
        else:
            if martes1 == paciente:
                martes1 = ""
                encontrado = True
            elif martes2 == paciente:
                martes2 = ""
                encontrado = True
            elif martes3 == paciente:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado con éxito.")
        else:
            print("Error: no se encontró el turno.")

    elif opcion == 3:
        dia_str = input("Elegir día (1=Lunes, 2=Martes): ")
        while dia_str != "1" and dia_str != "2":
            print("Error: opción inválida.")
            dia_str = input("Elegir día (1=Lunes, 2=Martes): ")

        if dia_str == "1":
            print("--- Agenda del Lunes ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("--- Agenda del Martes ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        print("--- Resumen General ---")
        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} disponibles")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} disponibles")

        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos es: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("El día con más turnos es: Martes")
        else:
            print("Ambos días tienen la misma cantidad de turnos (empate).")

    elif opcion == 5:
        salir = True
        print("Cerrando sistema...")

# ejercicio 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

nombre_agente = input("Nombre del agente: ")
while not nombre_agente.isalpha():
    print("Error: solo se permiten letras.")
    nombre_agente = input("Nombre del agente: ")

forzar_seguidas = 0
bloqueado = False
juego_activo = True

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print()
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1) Forzar cerradura  2) Hackear panel  3) Descansar")
    opcion_str = input("Opción: ")
    while not opcion_str.isdigit() or int(opcion_str) < 1 or int(opcion_str) > 3:
        print("Error: ingrese un número entre 1 y 3.")
        opcion_str = input("Opción: ")
    opcion = int(opcion_str)

    if opcion == 1:
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2

        if forzar_seguidas >= 3:
            print("¡La cerradura se trabó! Se activa la alarma.")
            alarma = True
        else:
            if energia < 40:
                riesgo_str = input("Riesgo de alarma. Elige un número (1-3): ")
                while not riesgo_str.isdigit() or int(riesgo_str) < 1 or int(riesgo_str) > 3:
                    print("Error: ingrese un número entre 1 y 3.")
                    riesgo_str = input("Riesgo de alarma. Elige un número (1-3): ")
                riesgo = int(riesgo_str)

                if riesgo == 3:
                    alarma = True
                    print("¡Se activó la alarma!")
                else:
                    if not alarma:
                        cerraduras_abiertas += 1
                        print("Cerradura abierta con éxito.")
            else:
                if not alarma:
                    cerraduras_abiertas += 1
                    print("Cerradura abierta con éxito.")

    elif opcion == 2:
        forzar_seguidas = 0
        energia -= 10
        tiempo -= 3

        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Progreso hackeo paso {paso}/4 - Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡El hackeo abrió una cerradura automáticamente!")

    elif opcion == 3:
        forzar_seguidas = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
        print("Has descansado.")

    # Verificación de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True

print()
if cerraduras_abiertas == 3:
    print("VICTORIA")
elif bloqueado:
    print("DERROTA (bloqueo)")
else:
    print("DERROTA")

# ejercicio 5

print("--- BIENVENIDO A LA ARENA ---")

nombre_gladiador = input("Nombre del Gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
daño_pesado = 15
daño_enemigo = 12
turno_gladiador = True

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print()
    print(f"{nombre_gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion_str = input("Opción: ")
    while not opcion_str.isdigit() or int(opcion_str) < 1 or int(opcion_str) > 3:
        print("Error: Ingrese un número válido.")
        opcion_str = input("Opción: ")
    opcion = int(opcion_str)

    if opcion == 1:
        if vida_enemigo < 20:
            daño_final = daño_pesado * 1.5
            print(f"¡Golpe Crítico! Atacaste al enemigo por {daño_final} puntos de daño!")
        else:
            daño_final = daño_pesado
            print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")
        vida_enemigo -= daño_final

    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("¡Te has curado 30 puntos de vida!")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= daño_enemigo
        print(f"¡El enemigo te atacó por {daño_enemigo} puntos de daño!")

    print("=== NUEVO TURNO ===")

print()
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

