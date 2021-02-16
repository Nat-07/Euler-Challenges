#include <stdlib.h>
#include <stdio.h>

int main(void){

    int i, j, k;

    for(i = 0; i <= 1000; i++){
        for(j = 0; j <= 1000; j++){
            for(k = 0; k <= 1000; k++){
                if((i + j + k == 1000) && (i < j && j < k) && (i*i + j*j == k*k)){
                    printf("Answer: %d\n", j*k*i);
                }
            }
        }
    }

    return 0;
}
