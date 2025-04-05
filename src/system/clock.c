#include "system/clock.h"
#include "sam.h"

void clock_init(void) {
    // GCLK0: CPU, GCLK1: USB, GCLK2: I2C/Timer

    // OSC32K aktivieren
    OSC32KCTRL->OSC32K.bit.ENABLE = 1;

    // DPLL96M für 96 MHz USB/Core
    GCLK->GENCTRL[0].reg = GCLK_GENCTRL_SRC_DPLL0 | GCLK_GENCTRL_GENEN;
    GCLK->PCHCTRL[USB_GCLK_ID].reg = GCLK_PCHCTRL_GEN_GCLK1 | GCLK_PCHCTRL_CHEN;

    // NVM Waitstates setzen (empfohlen für 96 MHz)
    NVMCTRL->CTRLA.bit.RWS = 3;
}
