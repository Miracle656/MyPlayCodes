#include <stdio.h>

int main(){
    int n;
    do{
        printf("Height: ");
        scanf("%d", &n);
    }while(n <= 0);

    for(int i = 0; i < n; i++){
        for(int j = 0; j < i; j++){
            printf("#");
        }
        printf("\n");
    }
}