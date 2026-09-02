##
temperatura:float=40.0
if temperatura > 20:
    print("alta temperatura")
##
temp:int=40
if temp>35:
    print("temperatura alta")
else:
    print("temperatura normal")

##
temp:int=20
if temp < 30:
    if temp <10:
        print("nuvel azul mucho frio")
    else:
        print("nivel verde normal")
else:
    if temp < 30:
        print("nivel naranja")
    else:
        print("nivel rojo")

## 
temp:int=40
if temp>35:
    print("temperatura alta")
else:
    print("temperatura normal")

## 
temp:int=20
if temp < 30:
    if temp <10:
        print("nuvel azul mucho frio")
    else:
        print("nivel verde normal")
elif temp < 30:
    print("nivel naranja")
else:
    print("nivel rojo")

    ##
vocal:str=input("ingrese una letra")
match vocal:
    case "a":
        print("es una vocal")
    case "e":
        print("es una vocal")
    case "i":
        print("es una vocal")
    case "o":
        print("es una vocal")
    case _:
        print("es una consonate")

vocal:str=input("ingrese una letra: ")
match vocal:
    case "a"| "e" | "i" |"o" | "u" :
        print("es una vocal")
    case _:
        print("es una consonante")

###

salir:str="N"
while salir=="N":
    print("hola que tal")
    salir=input("deseo salir (S/N):")
print("adios")

## usando while crear un programa que me de una pregunta para responder y que solo 3 oportunidades para dar con la respuesta correcta
intentos:int=0
respuesta_correcta:str="ayacucho"
while intentos<3:
    respuesta_usuario:str=input("capital ayacucho: ")
    if respuesta_correcta==respuesta_usuario:
        print("respuesta correcta")
        break
    else:
        print("error sigue intentando")
    intentos=intentos-1
    print(intentos)