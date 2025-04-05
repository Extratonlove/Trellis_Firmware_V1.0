# Projektname
TARGET = trellis_firmware

# Toolchain
CC = arm-none-eabi-gcc
LD = arm-none-eabi-ld
OBJCOPY = arm-none-eabi-objcopy
SIZE = arm-none-eabi-size

# Pfade
BUILD_DIR = build
SRC_DIR = src
INC_DIR = include
LINKER = linker/samd51_flash.ld

# Flags
CFLAGS = -Wall -Werror -Os -mcpu=cortex-m4 -mthumb -std=c11 -ffunction-sections -fdata-sections
LDFLAGS = -T$(LINKER) -nostartfiles -Wl,--gc-sections

# Dateiendungen
ELF = $(BUILD_DIR)/$(TARGET).elf
BIN = $(BUILD_DIR)/$(TARGET).bin
UF2 = $(BUILD_DIR)/$(TARGET).uf2

# Quellcodedateien automatisch finden
C_SOURCES := $(shell find $(SRC_DIR) -name "*.c")
OBJ_FILES := $(C_SOURCES:%.c=$(BUILD_DIR)/%.o)

# Inkludeverzeichnisse
INCLUDES := -I$(INC_DIR) \
            -I$(INC_DIR)/drivers \
            -I$(INC_DIR)/core \
            -I$(INC_DIR)/system

# Targets
all: $(UF2)

$(BUILD_DIR)/%.o: %.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

$(ELF): $(OBJ_FILES)
	$(CC) $(OBJ_FILES) $(LDFLAGS) -o $@
	$(SIZE) $@

$(BIN): $(ELF)
	$(OBJCOPY) -O binary $< $@

$(UF2): $(BIN)
	python tools/uf2conv.py $< -o $@

clean:
	rm -rf $(BUILD_DIR)

flash: $(UF2)
	cp $(UF2) /e/  # ⚠️ Passe das Laufwerk deines NeoTrellis M4 hier an

.PHONY: all clean flash
