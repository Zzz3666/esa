#include <stdint.h>
#define SIN_WAVE_LENGTH 1000
uint32_t sin_wave_data[SIN_WAVE_LENGTH] = "replace_sin_wave_data";

uint32_t sin_wave_generate(uint32_t time_tick, uint32_t frequency)
{

    return sin_wave_data[(time_tick / 10 * frequency) % SIN_WAVE_LENGTH];
}