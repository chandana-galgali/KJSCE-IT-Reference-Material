#include <stdio.h>
#include <limits.h>

int dist[10][10]; // Adjust the size as needed, keeping practical limits in mind
int dp[1<<10][10]; // Adjust based on the maximum expected number of cities
int N; // Number of cities

int VISITED_ALL;

int tsp(int mask, int pos) {
    if (mask == VISITED_ALL) {
        return dist[pos][0];
    }
    if (dp[mask][pos] != -1) {
       return dp[mask][pos];
    }

    int ans = INT_MAX;

    // Try to go to an unvisited city
    for (int city = 0; city < N; city++) {
        if ((mask & (1 << city)) == 0) {
            int newAns = dist[pos][city] + tsp(mask | (1 << city), city);
            ans = ans < newAns ? ans : newAns;
        }
    }

    return dp[mask][pos] = ans;
}

int main() {
    printf("Enter the number of cities: ");
    scanf("%d", &N);

    VISITED_ALL = (1<<N) - 1;

    printf("Enter the distances between the cities:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &dist[i][j]);
        }
    }

    // Initialize dp array
    for (int i = 0; i < (1<<N); i++) {
        for (int j = 0; j < N; j++) {
            dp[i][j] = -1;
        }
    }

    printf("The minimum cost of visiting all the cities: %d\n", tsp(1, 0));
    return 0;
}
