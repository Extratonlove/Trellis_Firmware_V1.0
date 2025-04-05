#ifndef I2C_H
#define I2C_H

#include <stdint.h>

void i2c_init(void);
void i2c_write(uint8_t addr, uint8_t reg, uint8_t* data, uint8_t len);

#endif
