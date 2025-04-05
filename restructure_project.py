import os
import shutil

wurzel = os.getcwd()

struktur = {
    "linker": ["samd51_flash.ld"],
    "tools": ["uf2conv.py"],
    "src/startup": ["startup.c"],
    "src/system": ["clock.c", "system_samd51.c"],
    "src/drivers": ["i2c.c", "led.c", "pads.c"],
    "src/core": ["usb.c", "midi.c", "hid.c"],
    "src": ["main.c"],
    "include/drivers": ["led.h", "pads.h"],
    "include/core": ["usb.h", "midi.h", "hid.h"],
    "include/system": ["clock.h", "system_samd51.h"],
    "include": ["board.h", "config.h"],
    "": ["Makefile"]
}

finaler_code = {
    "main.c": "#include <stdint.h>\n#include \"drivers/led.h\"\n#include \"drivers/pads.h\"\n#include \"core/usb.h\"\n\nint main(void) {\n    pads_init();\n    led_init();\n    usb_init();\n    while (1) {\n        pad_scan();\n        usb_poll();\n    }\n    return 0;\n}\n",
    "led.c": "#include \"drivers/led.h\"\n\nvoid led_init(void) {\n    // LED-System initialisieren\n}\n\nvoid led_set(uint8_t pad, uint8_t r, uint8_t g, uint8_t b, uint8_t effect) {\n    // GRB-Konvertierung und I2C-Ausgabe\n}\n",
    "led.h": "#ifndef LED_H\n#define LED_H\n#include <stdint.h>\n\nvoid led_init(void);\nvoid led_set(uint8_t pad, uint8_t r, uint8_t g, uint8_t b, uint8_t effect);\n\n#endif\n",
    "pads.c": "#include \"drivers/pads.h\"\n\nvoid pads_init(void) {\n    // Matrix über I2C initialisieren\n}\n\nvoid pad_scan(void) {\n    // Alle Tasten abfragen\n}\n",
    "pads.h": "#ifndef PADS_H\n#define PADS_H\n\nvoid pads_init(void);\nvoid pad_scan(void);\n\n#endif\n",
    "usb.c": "#include \"core/usb.h\"\n\nvoid usb_init(void) {\n    // USB-Verbindung initialisieren\n}\n\nvoid usb_poll(void) {\n    // Eingehende Befehle vom PC verarbeiten\n}\n",
    "usb.h": "#ifndef USB_H\n#define USB_H\n\nvoid usb_init(void);\nvoid usb_poll(void);\n\n#endif\n",
    "midi.c": "#include \"core/midi.h\"\n\nvoid midi_send_note(uint8_t note, uint8_t velocity) {\n    // Beispielhafte MIDI-Note-Ausgabe\n}\n",
    "midi.h": "#ifndef MIDI_H\n#define MIDI_H\n#include <stdint.h>\n\nvoid midi_send_note(uint8_t note, uint8_t velocity);\n\n#endif\n",
    "hid.c": "#include \"core/hid.h\"\n\nvoid hid_send_key(uint8_t keycode) {\n    // Sende Tastencode über HID\n}\n",
    "hid.h": "#ifndef HID_H\n#define HID_H\n#include <stdint.h>\n\nvoid hid_send_key(uint8_t keycode);\n\n#endif\n",
    "clock.c": "#include \"system/clock.h\"\n\nvoid clock_init(void) {\n    // Konfiguriere Taktquellen\n}\n",
    "clock.h": "#ifndef CLOCK_H\n#define CLOCK_H\n\nvoid clock_init(void);\n\n#endif\n",
    "system_samd51.c": "#include \"system/system_samd51.h\"\n\nvoid SystemInit(void) {\n    // MCU-Systemeinstellungen\n}\n",
    "system_samd51.h": "#ifndef SYSTEM_SAMD51_H\n#define SYSTEM_SAMD51_H\n\nvoid SystemInit(void);\n\n#endif\n",
    "i2c.c": "#include \"drivers/i2c.h\"\n\nvoid i2c_init(void) {\n    // Initialisiere I2C-Bus\n}\n",
    "i2c.h": "#ifndef I2C_H\n#define I2C_H\n\nvoid i2c_init(void);\n\n#endif\n",
    "board.h": "#ifndef BOARD_H\n#define BOARD_H\n\n#define PAD_COUNT 32\n\n#endif\n",
    "config.h": "#ifndef CONFIG_H\n#define CONFIG_H\n\n#define ENABLE_USB 1\n#define ENABLE_MIDI 0\n#define MAX_PADS 32\n\n#endif\n",
    "Makefile": "all:\n\t@echo \"Starte Buildprozess...\"\n",
    "samd51_flash.ld": "/* Linkerskript für SAMD51 */\nMEMORY {\n  FLASH (rx) : ORIGIN = 0x00000000, LENGTH = 512K\n  RAM (rwx)  : ORIGIN = 0x20000000, LENGTH = 192K\n}\n",
    "uf2conv.py": "# Platzhalter für UF2-Konvertierungsskript"
}

def schreibe_mit_backup(pfad, inhalt):
    if os.path.exists(pfad):
        shutil.copyfile(pfad, pfad + ".bak")
    with open(pfad, "w", encoding="utf-8") as f:
        f.write(inhalt)

def struktur_erstellen_und_befuellen():
    aktualisiert = []

    print("📁 Starte Strukturprüfung & Codeeinfügen...\n")
    for ordner, dateien in struktur.items():
        pfad = os.path.join(wurzel, ordner)
        os.makedirs(pfad, exist_ok=True)

        for datei in dateien:
            ziel = os.path.join(pfad, datei)
            code = finaler_code.get(datei, f"// {datei} – Platzhalter\n")
            schreibe_mit_backup(ziel, code)
            aktualisiert.append(ziel)

    print("✅ Alle Dateien wurden erstellt oder aktualisiert!\n")
    for pfad in aktualisiert:
        print("  🔄", pfad)

if __name__ == "__main__":
    struktur_erstellen_und_befuellen()
