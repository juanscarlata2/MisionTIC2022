def dividir(A,B):
    resultado=A/B
    return resultado



print("Ingrese los dos numeros a dividir\n\n")
A=float(input("Ingrese el primer numero "))
B=float(input("Ingrese el primer numero "))
division=dividir(A, B)
print(f"\n{A}/{B}={division}")