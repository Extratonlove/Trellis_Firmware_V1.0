#include "core/usb.h"
#include "drivers/led.h"

void usb_init(void) {
    // USB-Stack starten
}

void usb_poll(void) {
    uint8_t buffer[64];
    int len = usb_receive(buffer); // Annahme: eigene Funktion
    if (len > 0 && buffer[0] == 0xF0 && buffer[len - 1] == 0xF7) {
        if (buffer[1] == 0x7D && buffer[2] == 0x01) {
            uint8_t pad_id = buffer[3];
            uint8_t r = buffer[4] * 2;
            uint8_t g = buffer[5] * 2;
            uint8_t b = buffer[6] * 2;
            uint8_t fx = buffer[7];
            led_set(pad_id, r, g, b, fx);
        }
    }
}
