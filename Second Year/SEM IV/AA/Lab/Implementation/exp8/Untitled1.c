#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define N 4
#define MAX_STATES 1000000

typedef struct {
    int state[N][N];
    int x, y;  // Position of the blank tile
    int cost;  // Cost to reach this state + heuristic cost
    int level; // Number of moves from the start
} Node;

int goal[N][N];

// Function to calculate the number of misplaced tiles
int misplacedTiles(int current[N][N]) {
    int misplaced = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (current[i][j] != 0 && current[i][j] != goal[i][j]) {
                misplaced++;
            }
        }
    }
    return misplaced;
}

// Node comparison for the priority queue
int nodeCompare(const void *n1, const void *n2) {
    int l1 = ((Node*)n1)->cost;
    int l2 = ((Node*)n2)->cost;
    return (l1 > l2) - (l1 < l2);
}

// Function to print the board
void printBoard(int board[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%2d ", board[i][j]);
        }
        printf("\n");
    }
}

// Check if (x, y) is a valid board position
bool isSafe(int x, int y) {
    return x >= 0 && x < N && y >= 0 && y < N;
}

// Solves the 15-puzzle problem using branch and bound
void solve(int initial[N][N], int x, int y) {
    // Directions for blank tile movement: down, left, up, right
    int row[] = {1, 0, -1, 0};
    int col[] = {-0, -1, 0, 1};
    char *dir = "DLUR";

    // Priority queue of states (simple implementation)
    Node *pq = (Node *)malloc(MAX_STATES * sizeof(Node));
    int size = 0;

    // Initial state
    Node root;
    memcpy(root.state, initial, sizeof(root.state));
    root.x = x;
    root.y = y;
    root.cost = misplacedTiles(initial);
    root.level = 0;

    // Add root to queue
    pq[size++] = root;

    while (size) {
        // Get the state with the lowest cost
        qsort(pq, size, sizeof(Node), nodeCompare);
        Node min = pq[0];

        // Move the last item to the front (pop from queue)
        pq[0] = pq[--size];

        // If this is the goal state, print the solution
        if (min.cost - min.level == 0) {
            printf("Solution found in %d moves:\n", min.level);
            printBoard(min.state);
            break;
        }

        // Generate children (all possible moves)
        for (int i = 0; i < 4; i++) {
            int newX = min.x + row[i];
            int newY = min.y + col[i];

            if (isSafe(newX, newY)) {
                Node child;
                memcpy(child.state, min.state, sizeof(min.state));
                // Swap values
                child.state[min.x][min.y] = child.state[newX][newY];
                child.state[newX][newY] = 0;
                child.x = newX;
                child.y = newY;
                child.level = min.level + 1;
                child.cost = child.level + misplacedTiles(child.state);

                pq[size++] = child;
            }
        }
    }
    free(pq);
}

int main() {
    int initial[N][N], x, y;

    printf("Enter initial state (use 0 for the blank space):\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &initial[i][j]);
            if (initial[i][j] == 0) {
                x = i;
                y = j;
            }
        }
    }

    printf("Enter goal state (use 0 for the blank space):\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &goal[i][j]);
        }
    }

    solve(initial, x, y);
    return 0;
}
