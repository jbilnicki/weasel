#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>


// Function to generate a random character
char randomChar() {
    int r = rand() % 27; // 26 letters + space
    return r == 26 ? ' ' : 'A' + r;
}

// Function to calculate fitness (number of matching characters with the target)
int fitness(const char *candidate, const char *target) {
    int score = 0;
    for (int i = 0; i < strlen(target); i++) {
        if (candidate[i] == target[i]) {
            score++;
        }
    }
    return score;
}

// Function to mutate a string
void mutate(char *candidate, const char *target, double mutation_rate) {
    for (int i = 0; i < strlen(target); i++) {
        if ((double)rand() / RAND_MAX < mutation_rate) {
            candidate[i] = randomChar();
        }
    }
}

// Function to reproduce a new candidate from the best match
void reproduce(const char *parent, char *child, const char *target, double mutation_rate) {
    strcpy(child, parent);
    mutate(child, target, mutation_rate);
}

int main() {
    srand(time(NULL));

    // Get target sequence from user
    char target[100]; // Adjust size for longer sequences
    printf("Enter target sequence (uppercase letters and spaces only): ");
    fgets(target, sizeof(target), stdin);
    printf("\n");
    // Remove newline character
    target[strcspn(target, "\n")] = '\0';


    // Get mutation rate from user
    double mutation_rate;
    printf("Enter mutation rate (e.g., 0.05 for 5%%): ");
    scanf("%lf", &mutation_rate);
    printf("\n");

    // Get population size from user
    int population_size;
    printf("Enter population size: ");
    scanf("%d", &population_size);
    printf("\n");

    char population[population_size][strlen(target) + 1];
    char bestCandidate[strlen(target) + 1];
    int bestFitness = 0;

    // Initialize population with random strings
    for (int i = 0; i < population_size; i++) {
        for (int j = 0; j < strlen(target); j++) {
            population[i][j] = randomChar();
        }
        population[i][strlen(target)] = '\0';
    }

    int generation = 0;
    while (bestFitness < strlen(target)) {
        generation++;

        // Find the best candidate in the population
        for (int i = 0; i < population_size; i++) {
            int score = fitness(population[i], target);
            if (score > bestFitness) {
                bestFitness = score;
                strcpy(bestCandidate, population[i]);
            }
        }

        // Output progress
        printf("Generation %d: %s (Fitness: %d)\n", generation, bestCandidate, bestFitness);

        // Stop program for 1s for output to be more readible
        sleep(1);

        // Reproduce the next generation based on the best candidate
        for (int i = 0; i < population_size; i++) {
            reproduce(bestCandidate, population[i], target, mutation_rate);
        }
    }

    printf("Target reached in %d generations!\n", generation);
    return 0;
}
