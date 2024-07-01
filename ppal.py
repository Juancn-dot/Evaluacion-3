registrados = []
reg_fifa = []
reg_valorant = []
reg_fortnite = []
while True:
    print('''
    :---Bienvenido a eShirlitos esports---:
    1.- Registrar puntajes torneo
    2.- Listar todos los puntajes
    3.- Imprimir por tipo
    4.- Salir del programa
        ''')
    try:
        opc = ""
        opc = int(input("Ingrese su opcion (1-4):\n --> "))
    except:
        print("Solo valores numéricos!")
    if opc == 1: #Registrar puntajes
        id = input("Ingresa tu ID:\n --> ")
        nombre = input("Ingresa tu Nombre:\n --> ")
        registrados.append(id)
        registrados.append(nombre)
        print('''
    --Juegos Registrables--
    1.- Valorant
    2.- Fortnite
    3.- Fifa
            ''')
        try:
            valorant = int(input("Ingrese el puntaje de Valorant:\n --> "))
            fortnite = int(input("Ingrese el puntaje de Fortnite:\n --> "))
            fifa = int(input("Ingrese el puntaje de Fifa:\n --> "))
        except:
            print("Opcion Inexistente!")
        if valorant >= 0: #Valorant
            reg_valorant = valorant
        if fortnite >= 0: #Fortnite
            reg_fortnite = fortnite
        if fifa >= 0: #Fifa
            reg_fifa = fifa
        registrados.append(reg_valorant)
        registrados.append(reg_fortnite)
        registrados.append(reg_fifa)
        print('''
    --Categoria--
    1.- Principiante
    2.- Avanzado
    3.- Exeperto
              ''')
        categoria = int(input("Ingrese la categoria a registrarse:\n --> "))
        if categoria == 1:
            registrados.append("Principiante")
        elif categoria == 2:
            registrados.append("Avanzado")
        elif categoria == 3:
            registrados.append("Experto")
    elif opc == 2: #Listar Puntajes
        if registrados[5] == "Principiante":
            print(f"Id Jugador: {registrados[0]}")
            print(f"Nombre: {registrados[1]}")
            print(f"Valorant: {registrados[2]}")
            print(f"Fortnite: {registrados[3]}")
            print(f"Fifa: {registrados[4]}")
            print(f"Tipo:{registrados[5]}")
        if registrados[5] == "Avanzado":
            print(f"Id Jugador: {registrados[0]}")
            print(f"Nombre: {registrados[1]}")
            print(f"Valorant: {registrados[2]}")
            print(f"Fortnite: {registrados[3]}")
            print(f"Fifa: {registrados[4]}")
            print(f"Tipo:{registrados[5]}")
        if registrados[5] == "Experto":
            print(f"Id Jugador: {registrados[0]}")
            print(f"Nombre: {registrados[1]}")
            print(f"Valorant: {registrados[2]}")
            print(f"Fortnite: {registrados[3]}")
            print(f"Fifa: {registrados[4]}")
            print(f"Tipo:{registrados[5]}")
    elif opc == 3: #Imprimir puntajes
        print('''
    --Categorias--
    1.- Principiante
    2.- Avanzado
    3.- Experto
            ''')
        try:
            opc_2 = int(input("Eliga la categoria (1-3):\n --> "))
        except:
            print("Categoria Inexistente!")
        if opc_2 == 1:
            print
        elif opc_2 == 2:
            print
        elif opc_2 == 3:
            print
    elif opc == 4: #Salir del programa
        print("Saliendo...")
        break
    else:
        print("Opcion Inexistente!")