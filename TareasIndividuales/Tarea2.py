
def main():
    n = int(input('Ingrese un numero\n'))
    x = fib(n)
    print("El resultado de la serie Fibonacci de ", n, " es: ", x)


def fib(num):
    if (num==0):
        return 1
    elif(num==1):
        return 1
    else:
        return (fib(num-1)+fib(num-2)) #Suma 2 terminos anteriores
    
main()