#include <stdint.h>

extern int main(void);
extern void SystemInit(void);

void Reset_Handler(void) {
    SystemInit();
    main();
}

// Schwacher Alias für ISR (nicht belegt)
void Default_Handler(void) {
    while (1);
}

// Vektortabelle
__attribute__((section(".vectors")))
void (* const vector_table[])(void) = {
    (void (*)(void))(0x20030000), // Initial Stack Pointer
    Reset_Handler,                // Reset Handler
    Default_Handler,              // NMI
    Default_Handler,              // HardFault
    // ...
};
