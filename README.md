# KEDL

Kyocera has implemented vendor commands in EDL, let's use them!

> [!WARNING]
> The vendor commands are implemented inside SBL1, as such erasing it will render this tool useless.

> [!WARNING]
> DO NOT ERASE RANDOM PARTITIONS. DO NOT DISCONNECT THE DEVICE WHEN A FLASHING PROCEDURE STARTED.

## What this tool can do:

- Device Info: Read SecureBoot status and print the GPT.
- Dump: Extract individual partitions or create full-disk (sector by sector) eMMC dumps.
- Flashing: Flash specific partitions or flash a complete eMMC backup.
- Hardware Operations: Clear write protection (`0xAB`), run region erasures (`0xA5`), and issue hardware resets (`0x0D`).
- Integrity Verification: Calculate and compare local file dynamic checksums directly against hardware-calculated partition checksums (`0xA7`).
- Sector Peek: Read an arbitrary byte count from the start of a raw eMMC sector (`0xA3`), without a full-sector aligned read.

---

## Prerequisites

Ensure you have Python 3.8+ installed along with `libusb` dependencies required by `pyusb` / `usblib`.

Generally, in Linux:

```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pyusb usblib
```

## Entering RAMDUMP mode:

To enter RAMDUMP mode, you have 2 methods:

1. Create a FAT/FAT32 formatted SD Card with a file named `NOTPUSH`, with the contents `DEVKEYDL` inside it. This SD card trigger is _persistent RAMDUMP mode_ (i.e across reboots)

> [!NOTE]
> On Linux/MacOS, you can run `echo "DEVKEYDL" > "NOTPUSH"` in the root directory of the SD card.

2. use a deepflash cable.

It will connect with a device `KYOCERA_Android Android` and the notification LED will be green (if LED exists).

### To exit from RAMDUMP, remove the SD card and reboot the phone.

# Usage:

1. View GPT mapping and secureboot status:

   `python kedl.py info`

2. Dump entire eMMC:

   `python kedl.py dump --full -o full_emmc.img`

3. Dump a single partition:

   `python kedl.py dump -p system -o system.img`

4. Flash a single partition:

   `python kedl.py flash -p system -i system.img`

5. Flash an entire raw eMMC image:

   `python kedl.py flash --full -i full_emmc.img`

6. Peek at the first N bytes of a raw sector:

   `python kedl.py peek --lba 1 --count 32`

> [!NOTE]
> Your device may have a different VID/PID, and may not be detected. For such cases use `lsusb -v` to check your specific IDs.
> For example on KYF31 the output is as such: `ID 0482:0a7f Kyocera Corp. KYOCERA_Android` which would mean you'd specify `--vid 0482 --pid 0a7f` in the commands. (this is the default VID/PID)

---

# Credits

Original reverse engineering efforts, research and code by [@leobuskin](https://xdaforums.com/m/leobuskin.13248532/#recent-content).

This project uses code derived from or inspired by [bkerler/edl](https://github.com/bkerler/edl) by Bjoern Kerler, and as such is also licensed under GPLv3.

This repository is based on a fork-clone of [sonic011gamer/kedl](https://github.com/sonic011gamer/kedl)
