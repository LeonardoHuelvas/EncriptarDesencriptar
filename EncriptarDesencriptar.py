#Encriptar mensaje y Desencriptarlo
from string import ascii_uppercase as alfabeto
def encriptador(mensaje):
    
    mensaje1=list(set(mensaje))
    palabra=list(alfabeto)
    print (alfabeto)

    M= []
    clave={}
    i=0
    while i<len(mensaje1):
        clave[mensaje1[i]]=palabra[i]
        i=i+1

    for i in range(len(mensaje)):
        P = mensaje[i]
        Q = clave[P]
        M.append(Q)
    encriptado=''.join(M)
    print(f'encriptado: {encriptado}')
    
    desencriptador(encriptado,clave)
    return encriptado,clave 
def desencriptador(encriptado,clave):

    T = []
    nuevaclave={}
    encriptado=list(encriptado)
    clave=dict(clave)
    nuevaclave={v:k for k, v in clave.items()}
    for i in range(len(encriptado)):
        R=encriptado[i]
        S=nuevaclave[R]
        T.append(S)
    desencriptado=''.join(T)

    print(desencriptado)
mensaje= "Hola Mundo"
encriptador(mensaje)
