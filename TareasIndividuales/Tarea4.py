
def main():
    n = int(input("Dame un numero\n"))
    binario(n)

def binario(num):
    if num == 0:
        return print("0")
    else:
        binario(num//2)
    print(num%2, end="") 
        
main()