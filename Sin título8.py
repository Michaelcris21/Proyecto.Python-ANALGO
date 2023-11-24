# Crear un diccionario para llevar un registro de las transacciones de cada cliente
transacciones = {}

# Diccionario para mantener los saldos iniciales de los clientes
saldos_iniciales = {}


# Diccionario para mantener la cantidad de billetes en el dispensador
dispensador = {
    200: 50,  # Cantidad inicial de billetes de 200 soles
    100: 100,  # Cantidad inicial de billetes de 100 soles
    50: 200,  # Cantidad inicial de billetes de 50 soles
    20: 300,  # Cantidad inicial de billetes de 20 soles
    10: 500  # Cantidad inicial de billetes de 10 soles
}

# Definir una base de datos de usuarios y contrase�as para clientes y administradores
usuarios = {
    "cliente1": "clavecliente1",
    "cliente2": "clavecliente2",
    "admin": "claveadmin"
}

# Definir los saldos iniciales para los clientes
saldos = {
    "cliente1": 1000,
    "cliente2": 1500
}

# Diccionario para mantener el estado de los clientes
estado_clientes = {
    "cliente1": "ACTIVO",
    "cliente2": "ACTIVO"
}

# Historial de movimientos de los clientes
movimientos = {
    "cliente1": [],
    "cliente2": []
}



pagos_servicios = {}
# Funci�n para iniciar sesi�n
def login():
    while True:
        usuario = input("Usuario: ")
        contrasena = input("Contrase�a: ")

        if usuario in usuarios and usuarios[usuario] == contrasena:
            return usuario
        else:
            print("Credenciales incorrectas. Int�ntelo de nuevo.")

# Funci�n para mostrar el men� principal del cliente
def mostrar_menu_cliente(usuario):
    print("=" * 30)
    print(f"Bienvenido, {usuario} (Cliente).")
    print("1. Consultar saldos")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Transferir")
    print("5. Pagar servicios")
    print("6. Consultar movimientos")
    print("7. Cerrar sesi�n")
    
# Funci�n para mostrar el men� principal del administrador
def mostrar_menu_admin(usuario):
    print("=" * 30)
    print(f"Bienvenido, {usuario} (Administrador).")
    print("1. Gestionar clientes")
    print("2. Gestionar dispensadores")
    print("3. Salir (regresar a cajero autom�tico)")
    print("=" * 30)
    
# Función para consultar el saldo
def consultar_saldos(usuario):
    print("=" * 30)
    print(f"Saldo disponible: ${saldos[usuario]}")
    print("=" * 30)
    
# Funci�n para registrar una transacci�n
def registrar_transaccion(usuario, descripcion, monto):
    if usuario in transacciones:
        transacciones[usuario].append((descripcion, monto))
    else:
        transacciones[usuario] = [(descripcion, monto)]
        
# Funci�n para agregar clientes
def agregar_cliente():
    print("=" * 30)
    usuario = input("Ingrese el nombre de usuario: ")
    if usuario in usuarios:
        print("El cliente ya existe.")
        return

    contrasena = input("Ingrese la contrase�a: ")
    monto_inicial = float(input("Ingrese el monto inicial: $"))
    usuarios[usuario] = contrasena
    saldos[usuario] = monto_inicial
    saldos_iniciales[usuario] = monto_inicial
    estado_clientes[usuario] = "ACTIVO"
    print(f"Cliente {usuario} agregado con �xito.")
    
    
# Funci�n para modificar el saldo de un cliente
def modificar_cliente():
    print("=" * 30)
    usuario = input("Ingrese el nombre de usuario a modificar: ")
    if usuario in usuarios:
        nuevo_saldo = float(input(f"Ingrese el nuevo saldo para {usuario}: $"))
        saldos[usuario] = nuevo_saldo
        print(f"Saldo de {usuario} modificado con �xito.")
    else:
        print("El cliente no existe.")
        
        
# Funci�n para listar clientes
def listar_clientes():
   print("=" * 30)
   print("Listado de clientes:")
   for cliente, saldo in saldos.items():
        if cliente != "admin":
            print(f"{cliente} - Saldo original: ${saldo}, Saldo actual: ${saldos.get(cliente, 0)}")


# Funci�n para ordenar clientes por saldo
def ordenar_clientes():
    print("=" * 30)
    print("Clientes ordenados por saldo:")
    clientes_ordenados = sorted(saldos, key=lambda x: saldos[x], reverse=True)
    for cliente in clientes_ordenados:
        print(f"{cliente} - Saldo: ${saldos[cliente]}")

# Funci�n para buscar un cliente
def buscar_cliente():
    print("=" * 30)
    usuario = input("Ingrese el nombre de usuario a buscar: ")
    if usuario in usuarios:
        print(f"El cliente {usuario} existe.")
    else:
        print("El cliente no existe.")

# Funci�n para cambiar el estado de un cliente
def cambiar_estado_cliente():
    print("=" * 30)
    usuario = input("Ingrese el nombre de usuario a cambiar de estado: ")
    if usuario in usuarios:
        nuevo_estado = input("Ingrese el nuevo estado (ACTIVO/BAJA): ").upper()
        if nuevo_estado in ["ACTIVO", "BAJA"]:
            estado_clientes[usuario] = nuevo_estado
            if nuevo_estado == "BAJA" and usuario == usuario_activo:
                print(f"Estado de {usuario} actualizado a BAJA. Su cuenta ha sido desactivada.")
                print("SU CUENTA EST� DE BAJA, INT�NTELO M�S TARDE.")
                salir = input("Presione 'S' para salir: ")
                if salir.upper() == "S":
                    return
            else:
                print(f"Estado de {usuario} actualizado a {nuevo_estado}.")
        else:
            print("Estado no v�lido.")
    else:
        print("El cliente no existe.")

# Función para depositar dinero
def depositar(usuario):
    print("=" * 30)
    monto_deposito = float(input("Ingrese el monto a depositar: $"))
    if monto_deposito <= 0:
        print("Monto inv�lido. El monto debe ser mayor que cero.")
    else:
        saldos[usuario] += monto_deposito
        registrar_movimiento(usuario, "Dep�sito", monto_deposito)
        print("Dep�sito exitoso.")
        consultar_saldos(usuario)
    print("=" * 30)

def retirar(usuario):
    print("=" * 30)
    monto_retiro = float(input("Ingrese el monto a retirar: $"))
    if monto_retiro <= 0:
        print("Monto inv�lido. El monto debe ser mayor que cero.")
    elif monto_retiro > saldos[usuario]:
        print("Saldo insuficiente.")
    else:
        saldos[usuario] -= monto_retiro
        registrar_movimiento(usuario, "Retiro", monto_retiro)
        print("Retiro exitoso.")
        consultar_saldos(usuario)
    print("=" * 30)

def transferir(usuario):
    print("=" * 30)
    usuario_destino = input("Ingrese el usuario de destino: ")
    if usuario_destino in saldos and usuario_destino != usuario:
        monto_transferencia = float(input("Ingrese el monto a transferir: $"))
        if monto_transferencia <= 0:
            print("Monto inv�lido. El monto debe ser mayor que cero.")
        elif monto_transferencia > saldos[usuario]:
            print("Saldo insuficiente.")
        else:
            saldos[usuario] -= monto_transferencia
            saldos[usuario_destino] += monto_transferencia
            registrar_movimiento(usuario, f"Transferencia a {usuario_destino}", monto_transferencia)
            registrar_movimiento(usuario_destino, f"Transferencia de {usuario}", monto_transferencia)
            print(f"Transferencia a {usuario_destino} exitosa.")
            consultar_saldos(usuario)
    else:
        print("Usuario de destino no v�lido. Intente de nuevo.")
    print("=" * 30)

# Funci�n para registrar movimientos
def registrar_movimiento(usuario, tipo, monto):
    movimiento = f"{tipo}: ${monto}"
    if usuario in movimientos:
        movimientos[usuario].append(movimiento)
    else:
        movimientos[usuario] = [movimiento]

# Funci�n para consultar movimientos
def consultar_movimientos(usuario):
    print("=" * 30)
    if usuario in movimientos and movimientos[usuario]:
        print("Movimientos recientes:")
        for movimiento in movimientos[usuario]:
            if "Retiro" in movimiento or "Pago" in movimiento or "Transferencia a" in movimiento:
                print(chr(27) + "[1;31m" + movimiento + chr(27) + "[0m")  # Rojo para movimientos negativos
            else:
                print(chr(27) + "[1;32m" + movimiento + chr(27) + "[0m")  # Verde para movimientos positivos
    else:
        print("No hay movimientos registrados para este cliente.")
    print("=" * 30)


def gestionar_clientes():
    while True:
        print("=" * 30)
        print("Men� de gesti�n de clientes:")
        print("1. Agregar clientes")
        print("2. Modificar clientes")
        print("3. Listar clientes")
        print("4. Ordenar clientes")
        print("5. Buscar clientes")
        print("6. Cambiar estado de clientes (activo/baja)")
        print("7. Salir (regresar a men� administrador)")
        opcion = input("Seleccione una opci�n: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            modificar_cliente()
        elif opcion == "3":
            listar_clientes()
        elif opcion == "4":
            ordenar_clientes()
        elif opcion == "5":
            buscar_cliente()
        elif opcion == "6":
            cambiar_estado_cliente()
        elif opcion == "7":
            break
        else:
            print("Opci�n no v�lida. Intente de nuevo.")

# Funci�n para pago de servicios
def pagar_servicios(usuario):
    print("=" * 30)
    print("Pago de servicios:")
    print("1. Agua")
    print("2. Luz")
    print("3. Internet")
    print("4. Gas")
    print("5. Universidad")
    print("6. Cerrar (regresar a menu cliente)")
    opcion_servicio = input("Seleccione el servicio a pagar: ")

    if opcion_servicio in ["1", "2", "3", "4", "5"]:
        monto_pago = float(input("Ingrese el monto a pagar: $"))
        if monto_pago <= 0:
            print("Monto inv�lido. El monto debe ser mayor que cero.")
        elif monto_pago > saldos[usuario]:
            print("Saldo insuficiente.")
        else:
            servicio = obtener_nombre_servicio(opcion_servicio)
            saldos[usuario] -= monto_pago
            registrar_movimiento(usuario, f"Pago de {servicio}", monto_pago)
            print(f"Pago de {servicio} exitoso.")
            consultar_saldos(usuario)
    elif opcion_servicio == "6":
        return
    else:
        print("Opci�n no v�lida. Intente de nuevo.")

    print("=" * 30)

# Funci�n para obtener el nombre del servicio
def obtener_nombre_servicio(opcion_servicio):
    servicios = {
        "1": "Agua",
        "2": "Luz",
        "3": "Internet",
        "4": "Gas",
        "5": "Universidad"
    }
    return servicios.get(opcion_servicio, "Servicio no v�lido")


# Funci�n para modificar la cantidad de billetes en el dispensador
def modificar_cantidad_billetes():
    print("=" * 30)
    print("Modificar cantidad de billetes en el dispensador:")
    print("Denominaciones disponibles: 200, 100, 50, 20, 10")
    denominacion = int(input("Ingrese la denominaci�n del billete a modificar: "))
    if denominacion in dispensador:
        cantidad = int(input(f"Ingrese la nueva cantidad de billetes de {denominacion} soles: "))
        dispensador[denominacion] = cantidad
        print(f"Cantidad de billetes de {denominacion} soles modificada con �xito.")
    else:
        print("Denominaci�n no v�lida. Intente de nuevo.")
    print("=" * 30)
    
    
    
# Funci�n para ver las cantidades actuales de billetes en el dispensador
def ver_cantidad_billetes():
    print("=" * 30)
    print("Cantidades actuales de billetes en el dispensador:")
    for denominacion, cantidad in dispensador.items():
        print(f"{denominacion} soles: {cantidad} billetes")
    print("=" * 30)
    
    
    
# Funci�n para gestionar dispensadores (opci�n del administrador)
def gestionar_dispensadores():
    while True:
        print("=" * 30)
        print("Men� de gesti�n de dispensadores:")
        print("1. Modificar cantidad de billetes")
        print("2. Ver cantidades actuales de billetes")
        print("3. Salir (regresar a men� administrador)")
        opcion = input("Seleccione una opci�n: ")

        if opcion == "1":
            modificar_cantidad_billetes()
        elif opcion == "2":
            ver_cantidad_billetes()
        elif opcion == "3":
            break
        else:
            print("Opci�n no v�lida. Intente de nuevo.")



# Diccionario para relacionar opciones de pago de servicios con su descripci�n
opciones_servicios = {
    "1": "Agua",
    "2": "Luz",
    "3": "Internet",
    "4": "Gas",
    "5": "Universidad"
}



usuario_activo = None

# Ciclo principal del programa
while True:
    print("=" * 30)
    print("=== Cajero Autom�tico ===")
    print("1. Iniciar sesi�n como Cliente")
    print("2. Iniciar sesi�n como Administrador")
    print("3. Cerrar")
    print("=" * 30)

    opcion = input("Seleccione una opci�n: ")

    if opcion == "1":
        usuario = login()
        if estado_clientes.get(usuario, "ACTIVO") == "BAJA":
            print("SU CUENTA EST� DE BAJA, INT�NTELO M�S TARDE.")
            salir = input("Presione 'S' para salir: ")
            if salir.upper() == "S":
                break
            else:
                continue

        usuario_activo = usuario
        while True:
            mostrar_menu_cliente(usuario)
            opcion_cliente = input("Seleccione una opci�n: ")
            if opcion_cliente == "1":
                consultar_saldos(usuario)
            elif opcion_cliente == "2":
                depositar(usuario)
            elif opcion_cliente == "3":
                retirar(usuario)
            elif opcion_cliente == "4":
                transferir(usuario)
            elif opcion_cliente == "5":
                pagar_servicios(usuario)
            elif opcion_cliente == "6":
                consultar_movimientos(usuario)
            elif opcion_cliente == "7":
                usuario_activo = None
                break

    elif opcion == "2":
        usuario = login()
        while True:
            mostrar_menu_admin(usuario)
            opcion_admin = input("Seleccione una opci�n: ")
            if opcion_admin == "1" and usuario == "admin":
                gestionar_clientes()
            elif opcion_admin == "2" and usuario == "admin":
                gestionar_dispensadores()
            elif opcion_admin == "3":
                break

    elif opcion == "3":
        print("=" * 30)
        print("Gracias por utilizar nuestro cajero autom�tico. Hasta luego.")
        print("=" * 30)
        break

    else:
        print("Opci�n no v�lida. Intente de nuevo.")