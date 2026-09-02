# cotrol de flujo 
## condicionales
### la sentencia if 
esta sentencia al igual que en otros lenguajes de programacion en su escritura debemos añadir una exprecion de comparacio,terminanbdo en dos puntos`:`
```python
temperatura:float=40.0
if temperatura > 20:
    print("alta temperatura")
```
en esta caso solo se ejecuta el bloque if si la condicion es verdadera, para controlar si la condicion es falso debemos usar la sentencia else
```python
temp:int=40
if temp>35:
    print("temperatura alta")
else:
    print("temperatura normal")
```
podriamos tener muchas condiciones, lo que se llamaria tecnicamente *condiciones anidada*:
```python
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
```
python ofrece una mejora en la escritura de condiciones anidadas, para ello podemos usar la sentencia elif.
```python
temp:int=40
if temp>35:
    print("temperatura alta")
else:
    print("temperatura normal")
```
podriamos tener muchas condiciones, lo que se llamaria tecnicamente *condiciones anidada*:
```python
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
```

## sentencia match-case
Esta es una nueva centencia condiional, similar a los if anidados:
```python
vocal:str= "a"
match vocal:
case "a":
    print("es una vocal")
case "e":
    print("es iun vocal")
case "i":
    print("es una vocal")
case "o":
    print("es iun vocal")
case "u":
    print("es una vocal")
```

una manera de hacer codigo mas corto es :
```python
    vocal:str=input("ingrese una letra: ")
case "a"| "e" | "i" |"o" | "u" :
    print("es una vocal")
case _:
    print("es una consonante")
```

## bucles
### la sentencia while
es el primer mecanismo que existe en python para repetir instrucciones
la semantica tras esat sentencia es:mientras se cumpla la condicion has algo
ejemplo:
```python
salir:str="N"
while:salir=="N":
    print("hola que tal")
    salir=input("deseo salir (S/N):")
print("adios")
```
se puede contar la ejecucion de un white haciendo use de un break
```python
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
```