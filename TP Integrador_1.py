#consigna 1:

nombre = input("Por favor ingrese el nombre del cliente: ")

while not nombre.isalpha():
    print("Por favor solo ingrese letras, y su nombre sin espacios")
    nombre=input("Ingrese nuevamente el nombre del cliente: ")

print("Bienvenido/a", nombre)

prod=input("Ingrese cuantos productos quiere comprar: ")
while not prod.isdigit() or int(prod) == 0:
    print("Error,vuelva a intentarlo.")
    prod=input("Ingrese un número entero positivo mayor a 0: ")

prod=int(prod)

con_descuento=0
sin_descuento=0

for i in range (prod):
    print(f"Producto {i+1}")

    precio=input("Ingrese el costo del producto: ")
    while not precio.isdigit():
        print("Ingrese un entero positivo.")
        precio=input("Ingrese el costo del producto: ")

    precio=int(precio)

    descuento=input("el producto posee descuento? S/N ").lower()
    while descuento != "s" and descuento != "n":
        print("Ingrese 's' o 'n'.")
        descuento=input("el producto posee descuento? S/N: ").lower()

    sin_descuento += precio

    if descuento == "s":
        precio_descontado= precio * 0.9
    else:
        precio_descontado = precio

    con_descuento += precio_descontado

ahorros= sin_descuento - con_descuento
promedio= con_descuento / prod

print("Cliente:", nombre)
print("cantidad de productos:",prod)
print(f"total sin descuento:${sin_descuento}")
print(f"total con descuento:${con_descuento:.2f}")
print(f"total ahorrado:${ahorros:.2f}")
print(f"promedio de cada producto:${promedio:.2f}")

#consigna 2:
usuario_correcto="alumno"
contraseña_correcta="python123"
intentos=3

while intentos > 0:
    user=input("Por favor ingrese su usuario: ")
    password=input("Por favor ingrese su contraseña: ")

    if user== usuario_correcto and password==contraseña_correcta:
        print("Acceso exitoso")
        break
    else:
        intentos -= 1
        print(f"Datos incorrectos, intentos restantes: ",intentos)

if intentos == 0:
    print("Cuenta bloqueada")

if intentos > 0:
    opcion=0
        
    while opcion != 4:
        print("""INGRESE UNA DE LAS OPCIONES:
              1)Ver estado de inscripción
              2)Cambiar clave
              3)Mostrar mensaje motivacional
              4)Salir""")
        
        opcion=input("Ingrese una de las opciones: ")

        if not opcion.isdigit():
            print("ingrese una opción valida")
            continue

        opcion=int(opcion)

        if opcion < 1 or opcion > 4:
            print("ingrese una opcion valida")
            continue       

        match opcion:
            case 1:
                print("INSCRIPTO")

            case 2:
                contraseña_actual= input("por favor ingrese su clave actual:")
                if contraseña_actual == contraseña_correcta:
                    while True:
                        nueva= input("Ingrese su nueva contraseña por favor: ")
                        confirmar=input("Ingresela nuevamente: ")

                        if nueva != confirmar:
                            print("Las claves no coinciden")
                            continue
                        
                        if len(nueva) < 6:
                            print("la contraseña debe tener como minimo 6 numeros")
                            continue

                        contraseña_correcta=nueva
                        print("Contraseña cambiada")
                        break
                else:
                    print("Contraseña actual incorrecta")

            case 3:
                print("Estas perfecto, seguí así!!!!")

            case 4:
                print("Hasta luego!")
                

            case _:
                print("ingreso una opción incorrecta, intente nuevamente")

#consigna 3:

lunes_1=""
lunes_2=""
lunes_3=""
lunes_4=""
martes_1=""
martes_2=""
martes_3=""


opciones=0

operador=input("ingrese solo el nombre del operador sin espacios: ")
while not operador.isalpha():
    print("ingrese solo letras por favor")
    operador=input("ingrese el nombre del operador: ")
    continue
else:
    print("Bienvenido",operador)

while opciones != 5:
    print(""" 
        1)Agendar turno
        2)Cancelar turno
        3)Ver agenda del día
        4)Ver resumen general
        5)Cerrar sistema""")
    
    opciones=input ("ingrese una opcion: ")

    if not opciones.isdigit():
        print("ingrese una opcion valida")
        continue

    opciones=int(opciones)
    if opciones < 1 or opciones > 5:
        print("ingrese una opcion valida")
        continue

    match opciones:
        case 1:
            dia=input("Elija que día quiere agendar su turno 1=Lunes 2=Martes: ")
            if not dia.isdigit():
                print("Ingrese una opcion valida")
                continue
            dia=int(dia)

            if dia == 1:
                print("Su turno será agendado el día Lunes")

                paciente=input("ingrese su nombre por favor: ").lower()
                while not paciente.isalpha():
                    print("por favor ingrese letras solamente")
                    paciente=input("ingrese su nombre por favor: ").lower()
                if paciente == lunes_1 or paciente == lunes_2 or paciente == lunes_3 or paciente == lunes_4:
                        print("Ya se encuentra agendado")
                else:
                        if lunes_1=="":
                            lunes_1=paciente
                            print("Su turno se asigno correctamente", paciente)
                        elif lunes_2=="":
                            lunes_2=paciente
                            print("Su turno se asigno correctamente", paciente)
                        elif lunes_3=="":
                            lunes_3=paciente
                            print("Su turno se asigno correctamente", paciente)
                        elif lunes_4=="":
                            lunes_4=paciente
                            print("Su turno se asigno correctamente", paciente)
                        else:
                            print("No tenemos turnos disponibles", paciente)           

            elif dia == 2:
                print("su turno será agendado el día Martes")

                paciente=input("ingrese su nombre por favor: ").lower()
                while not paciente.isalpha():
                    print("Por favor ingrese letras solamente")
                    paciente=input("Ingrese su nombre por favor: ").lower()
                if paciente == martes_1 or paciente == martes_2 or paciente == martes_3:
                        print("Ya se encuentra agendado")
                else:
                        if martes_1=="":
                            martes_1=paciente
                            print("Su turno se asigno correctamente", paciente)
                        elif martes_2=="":
                            martes_2=paciente
                            print("Su turno se asigno correctamente", paciente)
                        elif martes_3=="":
                            martes_3=paciente
                            print("Su turno se asigno correctamente", paciente)
                        else:
                            print("No tenemos turnos disponibles", paciente)
        case 2:
            encontrado=False

            cancelar=input("Ingrese el dia del turno que quiere cancelar 1=Lunes 2=Martes: ")
            if cancelar == "1":
                paciente=input("Ingrese el nombre del paciente para cancelar el turno: ").lower()
                while not paciente.isalpha():
                    print("Por favor ingrese letras solamente")
                    paciente=input("ingrese el nombre el paciente para cancelar el turno: ").lower()

                if paciente==lunes_1:
                    lunes_1=""
                    encontrado=True
                if paciente==lunes_2:
                    lunes_2=""
                    encontrado=True
                if paciente==lunes_3:
                    lunes_3=""
                    encontrado=True
                if paciente==lunes_4:
                    lunes_4=""
                    encontrado=True
                if encontrado:
                    print(f"El turno del paciente: {paciente} fué cancelado correctamente")
                else:
                    print("El paciente no se encuentra registrado en ningun turno.")

            elif cancelar == "2":

                paciente=input("Ingrese el nombre del paciente para cancelar el turno: ").lower()

                while not paciente.isalpha():
                    print("Por favor ingrese letras solamente")
                    paciente=input("ingrese el nombre el paciente para cancelar el turno: ").lower()

                encontrado=False

                if paciente==martes_1:
                    martes_1=""
                    
                    encontrado=True
                if paciente==martes_2:
                    martes_2=""
                    encontrado=True
                if paciente==martes_3:
                    martes_3=""
                    encontrado=True

                if encontrado:
                    print(f"El turno del paciente {paciente} fue cancelado correctamente")
                else:
                    print("El paciente no se encuentra registrado en ningun turno.")

        case 3:
            dia=input("Que día desea consultar 1=Lunes 2=Martes: ")

            if dia =="1":
                print("Agenda del dia Lunes")
                if lunes_1=="":
                    print("Turno n°1 del día lunes se encuentra disponible")
                else:
                    print("Turno n°1 del día lunes se ecuentra ocupado por: ",lunes_1)
                if lunes_2=="":
                    print("Turno n°2 del día lunes se encuentra disponible")
                else:
                    print("Turno n°2 del día lunes se ecuentra ocupado por: ",lunes_2)
                if lunes_3=="":
                    print("Turno n°3 del día lunes se encuentra disponible")
                else:
                    print("Turno n°3 del día lunes se ecuentra ocupado por: ",lunes_3)
                if lunes_4=="":
                    print("Turno n°4 del día lunes se encuentra disponible")
                else:
                    print("Turno n°4 del día lunes se ecuentra ocupado por: ",lunes_4)

            elif dia=="2":
                print("Agenda del dia Martes")
                if martes_1=="":
                    print("Turno n°1 del día Martes se encuentra disponible")
                else:
                    print("Turno n°1 del día Martes se ecuentra ocupado por: ",martes_1)
                if martes_2=="":
                    print("Turno n°2 del día Martes se encuentra disponible")
                else:
                    print("Turno n°2 del día Martes se ecuentra ocupado por: ",martes_2)
                if martes_3=="":
                    print("Turno n°3 del día Martes se encuentra disponible")
                else:
                    print("Turno n°3 del día Martes se ecuentra ocupado por: ",martes_3)
        case 4:
            turnos_lunes=0
            
            if lunes_1 != "":
                turnos_lunes += 1

            if lunes_2 != "":
                turnos_lunes += 1

            if lunes_3 != "":
                turnos_lunes += 1

            if lunes_4 != "":
                turnos_lunes += 1

            turnos_martes=0

            if martes_1 != "":
                turnos_martes += 1

            if martes_2 != "":
                turnos_martes += 1

            if martes_3 != "":
                turnos_martes += 1

            turnos_libres_lunes= 4 - turnos_lunes
            turnos_libres_martes= 3 - turnos_martes
            print("El dia Lunes tiene: ",turnos_libres_lunes," turnos libres, y tiene",turnos_lunes,"turnos ocupados")
            print("El dia Martes tiene:",turnos_libres_martes,"turnos libres, y tiene",turnos_martes,"turnos ocupados")
            if turnos_lunes > turnos_martes:
                print("El día con mas turnos es el Lunes")
            elif turnos_martes > turnos_lunes:
                print("El dia con mas turnos es el Martes")
            else:
                print("la cantidad de turnos en ambos dias es igual")


        case 5:
            print("Hasta luego")
        case _:
            print("ingrese una opcion valida")

#consigna 4:
#Estadisticas del operador
energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = ""
# Anti-spam
forzar_de_seguido = 0

operador = input("ingrese el nombre del operador: ")

while not operador.isalpha():
    print("ingrese solo letras por favor")
    operador = input("ingrese el nombre del operador: ")

print("Bienvenido", operador)

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma == True and tiempo <= 3:
        print("SISTEMA BLOQUEADO PERDISTE")
        break

    print(">>>>>>>ESTADO<<<<<<<")
    print("Energia:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)
    print("Codigo parcial:", codigo_parcial)

    print("""MENU DE ACCIONES
          1)Forzar cerradura (Costo:-20 energia, -2 tiempo)
          2)Hackear panel
          3)Descansar          
          """)
    
    opciones_1 = input("ingrese una opcion: ")

    if not opciones_1.isdigit():
        print("ingrese una opcion valida")
        continue

    opciones_1 = int(opciones_1)

    if opciones_1 < 1 or opciones_1 > 3:
        print("ingrese una opcion valida")
        continue

    match opciones_1:

        case 1:
            energia -= 20
            tiempo -= 2
            forzar_de_seguido += 1

            if forzar_de_seguido == 3:
                alarma = True
                print("forzaste 3 veces seguidas, ALARMA ACTIVADA")
            
            else:
                if energia < 40:
                    num = input("Hay riesgo de activar la alarma, elegí un numero del 1 al 3: ")
                    while not num.isdigit() or int(num) not in range(1, 4):
                        num = input("Error, ingrese un numero valido entre 1 y 3")
                    num = int(num)

                    if num == 3:
                        alarma = True
                        print("Activaste la alarma")
                    else:
                        if not alarma:
                            cerraduras_abiertas += 1
                            print("Felicidades abriste una cerradura")
                else:
                    if not alarma:
                        cerraduras_abiertas += 1
                        print("Felicidades abriste una cerradura")

        case 2:
            print("Vas a hackear el sistema")
            energia -= 10
            tiempo -= 3
            forzar_de_seguido = 0

            for i in range(4):
                letra = input("Ingrese una sola letra: ")

                while not letra.isalpha() or len(letra) != 1:
                    letra = input("ingrese una letra por favor")
                
                codigo_parcial += letra
                print("Codigo parcial hackeado:", codigo_parcial)
                
                if len(codigo_parcial) >= 8:
                    cerraduras_abiertas += 1
                    print("Felicidades abriste una cerradura")
                    codigo_parcial = ""
                    break

        case 3:
            forzar_de_seguido = 0
            energia += 15
            tiempo -= 1

            if energia > 100:
                energia = 100
                
            if alarma:
                tiempo -= 10
                print("La alarma está activada, te cuesta mas energia")

            print("te tomaste un descanso")

        case _:
            print("Ingrese una opcion valida")

if cerraduras_abiertas == 3:
    print("FELICIDADES ABRISTE LA BOVEDA")

elif energia <= 0 or tiempo <= 0 or (alarma and tiempo <= 3):
    print("Te atraparon, PERDISTE!")

#punto 5
#Estadisticas gladidador/Enemigo
HP_gladiador= 100  
HP_enemigo= 100 
potis_vida= 3
ataque_Pesado= 15  
ataque_enemigo= 12  
turno_gladiador= True
opciones= 0

gladiador= input("Por favor ingrese el nombre del gladiador: ")
while not gladiador.isalpha():
    print("Por favor solo ingrese letras, y su nombre sin espacios")
    gladiador=input("Ingrese nuevamente el nombre del gladiador: ")

print("Bienvenido/a", gladiador)

while HP_gladiador > 0 and HP_enemigo > 0:

    print(">>>>>>>ESTADISTICAS<<<<<<<")
    print("Vida Gladiador:", HP_gladiador)
    print("Vida del Enemigo:", HP_enemigo)
    print("Potas de vida:", potis_vida)

    if turno_gladiador:
        print("""Elige una de las acciones disponibles
        1) Ataque Pesado
        2) Rafaga veloz
        3) Curarse""")

        opciones = input("Ingrese una opción: ")

        if not opciones.isdigit():
            print("Ingrese una opción válida")
            continue

        opciones = int(opciones)

        if opciones < 1 or opciones > 3:
            print("Ingrese una opción válida")
            continue

        match opciones:
            case 1:
                if HP_enemigo < 20:
                    daño = int(ataque_Pesado * 1.5)
                    print("GOLPE CRÍTICO!!!")
                else:
                    daño = ataque_Pesado

                HP_enemigo -= daño
                print(f"Atacaste al enemigo por: {daño} puntos de daño")

            case 2:
                print("Lanzaste una ráfaga veloz")
                for i in range(3):
                    HP_enemigo -= 5
                    print("Golpe conectado por 5 de daño")

            case 3:
                if potis_vida > 0:
                    HP_gladiador += 30
                    potis_vida -= 1
                    print("Te curaste!!")
                else:
                    print("No te quedan potas")
                    continue

        turno_gladiador = False

    else:
        print("Turno del enemigo...")
        HP_gladiador -= ataque_enemigo
        print("El enemigo te atacó por:", ataque_enemigo, "de daño")
        turno_gladiador = True

if HP_gladiador <= 0:
    print(f"PERDISTE!! {gladiador} HAS CAIDO EN COMBATE")

elif HP_enemigo <= 0:
    print(f"GANASTE LA BATALLA {gladiador} FELICIDADES!!")







