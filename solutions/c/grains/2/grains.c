#include "grains.h"
#include <stdint.h>

uint64_t square(uint8_t index) {
    if (index < 1 || index > 64) return 0;
    uint64_t grains = 1;
    for (uint8_t i = 1; i < index; i++)
        grains *= 2;
    return grains;
}

uint64_t total(void) {
    uint64_t soma = 0, grains = 1;
    for (uint8_t i = 1; i <= 64; i++) {
        soma += grains;
        grains *= 2;      // na casa 64 dá a volta para 0, mas já não é usado
    }
    return soma;
}