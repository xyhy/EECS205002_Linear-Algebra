//
//  main.c
//  Assignment 1 mmm
//
//  Created by 顏浩昀 on 2020/9/25.
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mmm.h"

float A[SIZE][SIZE], B[SIZE][SIZE], C[SIZE][SIZE], D[SIZE][SIZE];

int main(){
    int i, j;
    int p, q;
    clock_t t1, t2, t3;
    double d1, d2;
    
    for (i=0; i<SIZE; i++) {
        for (j=0; j<SIZE; j++){
            A[i][j] = rand()%10;
            B[i][j] = rand()%10;
        }
    }
    for(p=4; p<512; p*=2){
        for(q=4; q<512; q*=2){
            //t1 = clock();
            //matrixmul(A, B, C);
            t2 = clock();
            matrixmul_block2(A, B, D, p, q);
            t3 = clock();
            

            //d1 = ((double) (t2 - t1)) / CLOCKS_PER_SEC;
            d2 = ((double) (t3 - t2)) / CLOCKS_PER_SEC;
            printf("%f  ",d2);
            //printf("%f, diff=%f\n",d2, verify(C, D));
        }
        printf("\n");
    }
    return 0;
}
