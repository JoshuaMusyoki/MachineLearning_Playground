#include<stdio.h>
#include<stdlib.h>

#define MAX_Q 200
#define MAX_A 400

typedef struct {
    int cost;
    int extra_cost;
}Part;

int main() {
    int Q, A;
    Part repparts[MAX_Q];
    int broken[MAX_A];
    int revealed[MAX_A][MAX_A];
    int n[MAX_A];
    int queue[MAX_A];
    int head = 0, tail = 0;
    int total_cost = 0;

    //Reading the inputs
    scanf("%d", &Q);
    for (int i = 0; i < Q; i++) {
        scanf("%d %d", &repparts[i].cost, &repparts[i].extra_cost);
    }
    scanf("%d",  &A);
    for (int i = 0; i < A; i++) {
        scanf("%d %d", &broken[i], &n[i]);
        for (int j = 0; j < n[i]; j++) {
            scanf("%d", &revealed[i][j]);
        }
    }
//Next I wwill initialize the queue with broken parts
for (int i = 0; i < A; i++) {
        if (n[i] == 0) {
            queue[tail++] = i;
        }
    }


    //The Process Queue
    while (head < tail) {
        int current = queue[head++];

        // Trying to fix current component
        int part = broken[current] - 1;
        if (repparts[part].extra_cost > 0) {
            repparts[repparts[part].extra_cost - 1].extra_cost = 0;
        } else {
            total_cost += repparts[part].cost;
        }
        broken[current] = 0;

        // Then Add components revealed to queue
        for (int i = 0; i < n[current]; i++) {
            int next = revealed[current][i] - 1;
            if (--n[next] == 0) {
                queue[tail++] = next;
            }
        }
    }

    // Print total cost
    printf("%d\n", total_cost);

    return 0;
}



