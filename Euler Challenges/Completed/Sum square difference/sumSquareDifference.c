#include <stdlib.h>
#include <stdio.h>

int main(void){

    int i;
    int sum1 = 0;
    int sum2 = 0;

    for(i = 1; i <= 100; i++){
        sum1 += i*i; 
        sum2 += i;
    }

    printf("Difference: %d\n", sum2*sum2-sum1);

    return 0;
}