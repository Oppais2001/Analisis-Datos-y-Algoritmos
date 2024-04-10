'''
Algoritmo en C
#include <stdio.h>
#include<stdlib.h>
void hanoi(int n,int com, int aux, int fin);

int main(){
	char com='A';
	char aux='B';
	char fin='C';
	int n;
	printf("\nN£mero de discos: ");
	scanf("%d",&n);

	printf("\n\nLos movimientos a realizar son: \n");
	hanoi(n,com,aux,fin);
	return 0;
}

void hanoi(int n,int com, int aux, int fin){
	if(n==1){
		printf("%c->%c",com,fin);
	}
	else{
		hanoi(n-1,com,fin,aux);
		printf("\n%c->%c\n",com,fin);
		hanoi(n-1,aux,com,fin);
	}
}'''

def main():
    com ='A'
    aux ='B'
    fin ='C'
    n = int(input('Ingrese el valor de n:'))
    print('Numero de discos:', n)
    print('Los movimientos a realizar son: ')
    hanoi(n,com,aux,fin)

def hanoi(n, com, aux, fin):
    if(n==1):
        print(com,"-->",fin)
    else:
        hanoi(n-1,com,fin,aux)
        print(com,"->",fin)
        hanoi(n-1,aux,com,fin)

main()