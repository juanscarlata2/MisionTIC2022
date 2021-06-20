from util import palabras,grafico

"""
1. obtener una palabra para adivinar
2. mostrar con __ las letras que conforman la palabra
3. preguntar por una letra al usuario
4. validar si la letra esta en la palabra
5. mostrar las letras en la palabra
6. preguntar por la palabra
7.validar si ha ganado o no 

"""
obj_palabra=palabras()

palabra_secreta=obj_palabra.get_palabra()

def codificar_palabra(palabra):
    longitud=len(palabra) - 1
    caracter='__'

    for i in range(longitud):
        print(caracter, end='  ')
    print()


def validar_letra(letra):
    if letra in palabra_secreta:
        return True
    else:
        return False


codificar_palabra(palabra=palabra_secreta)

letra=input("Ingrese una letra")

esta_en_la_palabra=validar_letra(letra=letra)

print(esta_en_la_palabra)












