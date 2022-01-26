#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
	//RESERVA DINAMICA DE MEMORIA
	char aux[10];
	int longitud;
	char *lista[3];
	int cont;
	for(cont=0;cont<3;cont++){
    	printf("\nDime el nombre de un rey %d: ",cont);
	    scanf("%s",aux);
	    longitud=strlen(aux);
	    lista[cont]=(char *)malloc(longitud*sizeof(char));
	    strcpy(lista[cont],aux);
	}
	printf("\nLOS TRES REYES MAGOS SON: ");
	for(cont=0;cont<3;cont++){
		printf("\n %s",lista[cont]);
	}

	

	return(0);
}
