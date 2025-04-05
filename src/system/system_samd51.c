#include "system/system_samd51.h"
#include "sam.h"

void SystemInit(void) {
    // FPU aktivieren
    SCB->CPACR |= (0xF << 20);

    // Cache aktivieren
    CMCC->CTRL.bit.CEN = 1;

    // Power Interface & Waitstates
    SUPC->VREG.bit.RUNSTDBY = 1;
    NVMCTRL->CTRLA.bit.RWS = 3;

    // Clock starten
    clock_init();
}
