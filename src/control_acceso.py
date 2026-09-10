*Ejercicio CONTROL_ACCESO:* Control de Acceso con Intentos (Bucle while y break)
Escribe un programa que simule el acceso a una cuenta personal mediante una contraseña previamente definida (por ejemplo, "python123").
- El usuario tiene un máximo de 3 intentos para ingresar la clave correcta.
- Si ingresa la contraseña correcta, el programa debe mostrar "Acceso concedido" y terminar inmediatamente con break.
- Si se equivoca, debe mostrar cuántos intentos le quedan.
- Si agota los 3 intentos sin éxito, debe imprimir "Cuenta bloqueada por seguridad".

CONTRASENA_CORRECTA = "python123"
intentos_restantes = 3

while intentos_restantes > 0:
    clave_ingresada = input("Introduce la contraseña: ")
    
    if clave_ingresada == CONTRASENA_CORRECTA:
        print("Acceso concedido")
        break
    else:
        intentos_restantes -= 1
        if intentos_restantes > 0:
            print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos.")
        else:
            print("Cuenta bloqueada por seguridad")