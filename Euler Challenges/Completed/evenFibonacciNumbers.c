#include <stdio.h>
#include <stdlib.h>

int main(){

    int arr[3] = {0,1,2};

    int sum = 0;

    while((arr[0] + arr[1]) < 4000000){

        // summing even terms
        if (arr[2] % 2 == 0){
            sum = arr[2] + sum;
        }
        
        // shifting values in array & getting new
        arr[0] = arr[1];
        arr[1] = arr[2];
        arr[2] = arr[0] + arr[1];
    }
    
    printf("Answer: %d\n", sum);
    
    return 0;
}