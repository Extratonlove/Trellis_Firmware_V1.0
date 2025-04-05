
#include <stdint.h>
#include "drivers/led.h"
#include "drivers/pads.h"
#include "core/usb.h"
#include "board.h"
#include "config.h"
#include "system/clock.h"
#include "system/system_samd51.h"
#include <stdbool.h>
#include <unistd.h>

void startup_animation(void) {
    // Schritt 1: Alle Pads blau
    for (uint8_t i = 0; i < PAD_COUNT; i++) {
        led_set(i, 0, 0, 255, 0);
        usleep(3000); // leichte Verzögerung zwischen den Pads
    }

    // Schritt 2: Farbverlauf nach Rot
    for (uint8_t step = 0; step <= 255; step += 5) {
        for (uint8_t i = 0; i < PAD_COUNT; i++) {
            uint8_t r = step;
            uint8_t b = 255 - step;
            led_set(i, r, 0, b, 0);
        }
        usleep(10000);
    }

    // Schritt 3: Alle aus
    for (uint8_t i = 0; i < PAD_COUNT; i++) {
        led_set(i, 0, 0, 0, 0);
        usleep(2000);
    }
}


#include <stdint.h>
#include "drivers/led.h"
#include "drivers/pads.h"
#include "core/usb.h"

int main(void) {
    pads_init();
    led_init();
    usb_init();
    startup_animation();
    while (1) {
        pad_scan();
        usb_poll();
    }
    return 0;
}
