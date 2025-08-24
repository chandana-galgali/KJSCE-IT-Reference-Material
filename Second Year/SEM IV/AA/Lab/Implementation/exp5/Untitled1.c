#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INF 99999 // Define a large number as infinity
#define MAX_INPUT_LEN 100

// Function prototypes
void printSolution(int **dist, int V);
void floydWarshall(int **graph, int V);

int main() {
    int V, **graph;
    char input[MAX_INPUT_LEN];

    printf("Enter the number of vertices in the graph: ");
    scanf("%d", &V);

    // Allocate memory for the graph
    graph = (int **)malloc(V * sizeof(int *));
    for (int i = 0; i < V; i++) {
        graph[i] = (int *)malloc(V * sizeof(int));
    }

    // Read the adjacency matrix
    printf("Enter the adjacency matrix (use 'INF' for infinity):\n");
    for (int i = 1; i <= V; i++) {
        for (int j = 1; j <= V; j++) {
            printf("Enter the weight of the edge from vertex %d to vertex %d (or 'INF' for no direct edge): ", i, j);
            scanf("%s", input);
            if (strcmp(input, "INF") == 0) {
                graph[i-1][j-1] = INF;
            } else {
                graph[i-1][j-1] = atoi(input);
            }
        }
    }

    // Call the Floyd-Warshall algorithm
    floydWarshall(graph, V);

    // Free the allocated memory for the graph
    for (int i = 0; i < V; i++) {
        free(graph[i]);
    }
    free(graph);

    return 0;
}

void floydWarshall(int **graph, int V) {
    int **dist = (int **)malloc(V * sizeof(int *));
    for (int i = 0; i < V; i++) {
        dist[i] = (int *)malloc(V * sizeof(int));
        for (int j = 0; j < V; j++) {
            dist[i][j] = graph[i][j];
        }
    }

    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] != INF && dist[k][j] != INF && dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    printSolution(dist, V);

    for (int i = 0; i < V; i++) {
        free(dist[i]);
    }
    free(dist);
}

void printSolution(int **dist, int V) {
    printf("The shortest distances between every pair of vertices:\n");
    for (int i = 1; i <= V; i++) {
        for (int j = 1; j <= V; j++) {
            if (dist[i-1][j-1] == INF) {
                printf("%7s", "INF");
            } else {
                printf("%7d", dist[i-1][j-1]);
            }
        }
        printf("\n");
    }
}
