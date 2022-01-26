#include<stdio.h>

int main(){
	float suma=0;
	float media;
	float x[10];
	int cont;
	for(cont=0;cont<=10;cont++){
		printf("Dame un numero: ");
		scanf("%f",&x[cont]);
	}
	for(cont=0;cont<10;cont++){
		printf("\n%.2f",x[cont]);
		suma+=x[cont];
	}
	media=suma/cont;
	printf("\nLA MEDIA MEDIA VALE= %.2f",media);
	
	return(0);
}
