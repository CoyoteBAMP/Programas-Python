texto = input("Introduce el mensaje: ").upper()
n= int(input("Introduce la clave: "))
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cifrado=""
print("1= Cifrar")
print("2= Descifrar")
des=int(input("¿Que quieres hacer?"))
if des ==1:
    for l in texto:
        if l in abc:
            pos_letra = abc.index(l)
            nueva_pos= (pos_letra + n) % len(abc)
            cifrado+= abc[nueva_pos]
        else:
            cifrado+=l

    print("Mensaje cifrado: ", cifrado)
elif des ==2:
    descifrado=""
    for l in texto:
        if l in abc:
            pos_letra= abc.index(l)
            nueva_pos= (pos_letra - n) %len(abc)
            descifrado+= abc[nueva_pos]
        else:
            descifrado+=l
       
    mensaje = (descifrado)
    print(mensaje)
            
