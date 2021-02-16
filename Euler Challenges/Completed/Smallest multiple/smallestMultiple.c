#include <stdio.h>
#include <stdlib.h>

int main(void){

    int i, j;

    for (i = 1; i <= 1000000000; i++){

        for (j = 1; j <= 20; j++){
            if (i % j != 0){
                // break out of single for loop
                break;
            
            // if j has succeeded up to 20, we found an answer
            }else if (j == 20){
                printf("Answer : %d\n", i);
                exit(0);
            }
            
        }
        
    }

    return 0;
}
