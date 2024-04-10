
def main():
    a = int(input("Ingrese la base\n"))
    b = int(input("Ingrese el exponente \n"))
    print("es ", potencia(a,b))

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return(base * potencia(base, exponente - 1))

main()