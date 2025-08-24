#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int *board;
int solutions = 0;

bool isSafe(int row, int col, int n) {
    for (int i = 0; i < row; i++) {
        if (board[i] == col || abs(board[i] - col) == abs(i - row)) {
            return false;
        }
    }
    return true;
}

void placeQueen(int row, int n) {
    if (row == n) {
        solutions++;
        for (int i = 0; i < n; i++) {
            printf("%d ", board[i] + 1);
        }
        printf("\n");
        return;
    }

    for (int i = 0; i < n; i++) {
        if (isSafe(row, i, n)) {
            board[row] = i;
            placeQueen(row + 1, n);
        }
    }
}

int main() {
    int n;
    printf("Enter the number of queens: ");
    scanf("%d", &n);
    board = malloc(n * sizeof(int));

    placeQueen(0, n);
    printf("Total solutions: %d\n", solutions);
    free(board);
    return 0;
}
