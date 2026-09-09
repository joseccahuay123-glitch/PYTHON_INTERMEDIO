## 1. crear una lista de ingredientes ["camote","papa","queso","huevo"] crear un programa que recorra con for los elementos de la lista y me retorne el valor y su indece del igrediente "queso"
ingredientes:list[str]= ["camote","papa","queso","huevo"]
for i in ingredientes:
    if i=="queso"
       print(f "el valor es:",i)
       print(f "su indice es:" ingredientes.index("queso"))


## 2. del siguiente texto"errar es umano dijo el pato bajandose de la gallina" encontrar el error ortoigrafico y corregir por el correcto.
texto:str="errar es umano dijo el pato bajandose de la gallina"
lista_texto:list=texto.split(" ")
for i in lista_texto:
    if i =="umano":
        lista_texto[lista_texto.index("umano")]="humano"
        print (" ".join(lista_texto))

## opcion 2
texto_correjido:str=texto.replace("umano","humano")
print(texto_correjido)