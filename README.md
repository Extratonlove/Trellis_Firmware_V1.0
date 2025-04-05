# Trellis Firmware V1.0

Firmware für das Adafruit NeoTrellis M4 (SAMD51), zur vollständigen Ansteuerung von RGB-Pads und Kommunikation mit einem PC über USB.

---

## 🎯 Ziel der Firmware

- 🔹 Erkennen von Pad-Interaktionen (Pressed / Released)
- 🔹 Steuerung der NeoPixel-Farben pro Pad über USB-Kommandos
- 🔹 Optional: Ausgabe von MIDI- und HID-Signalen
- ❌ Keine Makros, Gruppen oder Logik auf dem Gerät – alle Profile werden am PC verwaltet

---

## ⚙️ Hardware

- **Board**: Adafruit NeoTrellis M4 Express  
- **Chip**: ATSAMD51J19A  
- **Matrix**: 4x8 RGB-Pads (32 Stück)  
- **Kommunikation**: USB (für PC-Kommandos), I2C (für Seesaw: LED + Pad)

---

## 🗂️ Projektstruktur

```bash
Trellis_Firmware/
├── Makefile                     # Buildsystem für GCC ARM
├── linker/samd51_flash.ld      # Speicherdefinitionen (FLASH/RAM)
├── tools/uf2conv.py            # Konvertierung BIN → UF2
├── src/
│   ├── main.c                  # Mainloop, Startanimation
│   ├── startup/startup.c       # Vektortabelle & Reset-Handler
│   ├── system/clock.c          # GCLK / DPLL / Waitstates
│   ├── system/system_samd51.c  # FPU, Cache, PowerInit
│   ├── drivers/                # i2c, led, pads
│   ├── core/                   # usb, midi, hid
├── include/                    # Headerstruktur
│   ├── board.h, config.h
│   ├── core/, drivers/, system/
