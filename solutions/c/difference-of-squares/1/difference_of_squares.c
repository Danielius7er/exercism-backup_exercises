#include "difference_of_squares.h"

unsigned int square_of_sum(unsigned int number) {
    unsigned long long n = number;
    unsigned long long sum = n * (n + 1) / 2;      // soma de Gauss
    return (unsigned int)(sum * sum);
}

unsigned int sum_of_squares(unsigned int number) {
    unsigned long long n = number;
    return (unsigned int)(n * (n + 1) * (2 * n + 1) / 6);
}

unsigned int difference_of_squares(unsigned int number) {
    return square_of_sum(number) - sum_of_squares(number);
}