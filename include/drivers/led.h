#ifndef LED_H
#define LED_H
#include <stdint.h>

void led_init(void);
void led_set(uint8_t pad, uint8_t r, uint8_t g, uint8_t b, uint8_t effect);

#endif
