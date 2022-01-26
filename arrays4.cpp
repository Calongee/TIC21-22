#include<stdio.h>

int main(){
	char letras[10];
	int cont;
	
	for(cont=0;cont<=10;cont++){
		printf("Introduce la letra %d: ",cont);
		scanf(" %c",&letras[cont]);
	}
	printf("\nHAS ESCRITO LA PALABRA: ");
	for(cont=0;cont<10;cont++){
		printf("%c",letras[cont]);
	}
	
	
	return(0);
}
