# KEDL, a tool to interact with Kyocera's hidden EDL mode commands.
Kyocera has some hidden commands implemented in EDL, let's use them!


>[!WARNING]
> The vendor commands are implemented inside SBL1, as such erasing it will render this tool useless.

>[!WARNING]
> DO NOT ERASE RANDOM PARTITIONS. DO NOT DISCONNECT THE DEVICE WHEN A FLASHING PROCEDURE STARTED.

## What this tool can do:
* **Device Info**: Read SecureBoot status and print the GPT.
* **Dump**: Extract individual partitions or create full-disk (sector by sector) eMMC dumps.
* **Flashing**: Flash specific partitions or flash a complete eMMC backup.
* **Hardware Operations**: Clear write protection (`0xAB`), execute region erasures (`0xA5`), and issue hardware resets (`0x0D`).
* **Integrity Verification**: Calculate and compare local file dynamic checksums directly against hardware-calculated partition checksums (`0xA7`).
---


## Prerequisites

Ensure you have Python 3.8+ installed along with `libusb` dependencies required by `pyusb` / `usblib`.

## Entering KEDL mode:
To enter KEDL mode, you have 2 methods:
 1. create a FAT/FAT32 formatted SDCard with a text file called ``NOTPUSH``, with the string ``DEVKEYDL`` inside it.
 2. use a deepflash cable.

It will connect with a device `KYOCERA_Android Android` and the notification LED will be green (for KYF31).
### To exit from KEDL, remove the SD card and reboot the phone.
>[!WARNING]
> If your device has Secureboot ON, or you have Android 7+, flashing partitions might result in the system not being able to boot because of verification.

# Usage:
  1. View GPT mapping and secureboot status:

     ```python kedl.py info```
  2. Dump entire eMMC:

     ```python kedl.py dump --full -o full_emmc.img```
  3. Dump a single partition:

     ```python kedl.py dump -p system -o system.img```
  4. Flash a single partition:

     ```python kedl.py flash -p system -i system.img```
  5. Flash an entire raw eMMC image:

     ```python kedl.py flash --full -i full_emmc.img```

>[!NOTE]
> Your device may have a different VID/PID, and may not be detected. For such cases use `lsusb -v` to check your specific IDs.
> For example on KYF31 the output is as such: `Bus 003 Device 011: ID 0482:0a7f Kyocera Corp. KYOCERA_Android` which would mean you'd specify `--vid 0482 --pid 0a7f` in the commands. (this is the default VID/PID)



---
# Credits:
Original reverse engineering efforts, research and code by @leobuskin.

This project uses code derived from or inspired by [bkerler/edl](https://github.com/bkerler/edl) by Bjoern Kerler, and as such is also licensed under GPLv3.
