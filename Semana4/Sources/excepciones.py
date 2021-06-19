def dividir(A,B):
    try:
        resultado=A/B
    except Exception as err:
        print(f"Se ha dado un error: {err}")
        return "tiende a infinito"
    else:
        return resultado



print("Ingrese los dos numeros a dividir\n\n")

try:
    A=float(input("Ingrese el primer numero "))
    B=float(input("Ingrese el primer numero "))
except Exception as err:
    print("No se puede convertir en numero")
    A=float(input("Ingrese el primer numero "))
    B=float(input("Ingrese el primer numero "))

   
division=dividir(A, B)

print(f"\n{A}/{B}={division}")