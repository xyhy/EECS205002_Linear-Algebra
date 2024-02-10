//
//  Ans.c
//  Assignment 1 mmm
//
//  Created by 顏浩昀 on 2020/9/25.
//

#include "mmm.h"

// compute C = A*B
void matrixmul(float A[][SIZE], float B[][SIZE], float C[][SIZE]){
    int i, j, k;
    // i: row index for C
    // j: col index for C
    // k: iteration index


    for (i=0; i<SIZE; i++){
        for (j=0; j<SIZE; j++){
            C[i][j] = 0;
            for (k=0; k<SIZE; k++){
                C[i][j] += A[i][k]*B[k][j];
            }
        }
    }
}

// compute C = A*B using blocking
void matrixmul_block(float A[][SIZE], float B[][SIZE], float C[][SIZE], int bSize){
    int i, j, k;
    // i: row index for block
    // j: col index for block
    // k: iteration index

    int bi, bj, bk;
    // bi: block row index for C
    // bj: block col index for C
    // bk: block index

    for (bi=0; bi<SIZE; bi+=bSize){
        for (bj=0; bj<SIZE; bj+=bSize){
            // clean C's value
            for (i=bi; i<bi+bSize; i++){
                for (j=bj; j<bj+bSize; j++){
                    C[i][j] = 0.0;
                }
            }
            // compute the block submatrix C[bi][bj]
            for (bk=0; bk<SIZE; bk+=bSize){
                for (i=bi; i<bi+bSize; i++){
                    for (j=bj; j<bj+bSize; j++){
                        for (k=bk; k<bk+bSize; k++){
                            C[i][j] += A[i][k]*B[k][j];
                        }
                    }
                }
            }
        }
    }
}


// compute C = A*B using blocking
void matrixmul_block2(float A[][SIZE], float B[][SIZE], float C[][SIZE], int p, int q){ // Ai is pxq, Bi is qxp, Ci is pxp.
    // your implementation here
    int row, col, k;
    int brow, bcol, index;
    for(int m = 0; m < SIZE; m++){
        for(int n = 0; n < SIZE; n++){
            C[m][n] = 0;
        }
    }
    for(brow=0; brow<SIZE; brow+=p){
        for(bcol=0; bcol<SIZE; bcol+=q){
            for(index=0; index<SIZE; index+=q){
                for(row=brow; row<(brow+p); row++){
                    for(col=bcol; col<(bcol+q); col++){
                        for(k=index; k<index+q; k++){
                            C[row][col] += A[row][k] * B[k][col];
                        }
                    }
                }
            }
        }
    }
    
}


// verify the correctness of the result
double verify(float X[][SIZE], float Y[][SIZE]){
    float diff = 0.0;
    double accum = 0.0;
    int i, j;

    for (i=0; i< SIZE; i++){
        for (j=0; j<SIZE; j++){
            diff = X[i][j] - Y[i][j];
            accum += diff<0?-diff:diff;
        }
    }
    return accum;
}
