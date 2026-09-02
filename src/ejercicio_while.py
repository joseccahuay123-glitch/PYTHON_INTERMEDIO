## crear un programa de login que mientras que la persoma no ponga el usuario/contraceña correcto le sigue pidiendo esa informacion, si el usuario/contraceña son correctos entonces darle un mensaje de vienvenida y salir derl programa
usur_correcto:str="Admin"
pass_correcto:str="Admin1234"
WHILE TRUE
    usur:str=imput("ingrese el usuruario")
    pass:str=imput("ingrese la contraceña")
    if usur==usur_correcto and password==pass_correcto:
        print("Bienvenido a mi sistema")
        break
    else:
        print("usuario/ontraceña incorrectos sigue intentando")
        