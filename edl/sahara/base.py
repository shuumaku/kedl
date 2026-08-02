from enum import IntEnum
from dataclasses import dataclass


ErrorDesc = {
    0x00: "Invalid command received in current state",
    0x01: "Protocol mismatch between host and target",
    0x02: "Invalid target protocol version",
    0x03: "Invalid host protocol version",
    0x04: "Invalid packet size received",
    0x05: "Unexpected image ID received",
    0x06: "Invalid image header size received",
    0x07: "Invalid image data size received",
    0x08: "Invalid image type received",
    0x09: "Invalid tranmission length",
    0x0A: "Invalid reception length",
    0x0B: "General transmission or reception error",
    0x0C: "Error while transmitting READ_DATA packet",
    0x0D: "Cannot receive specified number of program headers",
    0x0E: "Invalid data length received for program headers",
    0x0F: "Multiple shared segments found in ELF image",
    0x10: "Uninitialized program header location",
    0x11: "Invalid destination address",
    0x12: "Invalid data size received in image header",
    0x13: "Invalid ELF header received",
    0x14: "Unknown host error received in HELLO_RESP",
    0x15: "Timeout while receiving data",
    0x16: "Timeout while transmitting data",
    0x17: "Invalid mode received from host",
    0x18: "Invalid memory read access",
    0x19: "Host cannot handle read data size requested",
    0x1A: "Memory debug not supported",
    0x1B: "Invalid mode switch",
    0x1C: "Failed to execute command",
    0x1D: "Invalid parameter passed to command execution",
    0x1E: "Unsupported client command received",
    0x1F: "Invalid client command received for data response",
    0x20: "Failed to authenticate hash table",
    0x21: "Failed to verify hash for a given segment of ELF image",
    0x22: "Failed to find hash table in ELF image",
    0x23: "Target failed to initialize",
    0x24: "Failed to authenticate generic image",
    0x25: "Invalid ELF hash table size.  Too bit or small.",
    0x26: "Invalid IMG Hash Table Size",
    0x27: "Enumeration failed",
    0x28: "Hardware Bulk transfer error"
}


class SaharaCmd(IntEnum):
    HELLO_REQ = 0x1
    HELLO_RSP = 0x2
    READ_DATA = 0x3
    END_TRANSFER = 0x4
    DONE_REQ = 0x5
    DONE_RSP = 0x6
    RESET_REQ = 0x7
    RESET_RSP = 0x8
    MEMORY_DEBUG = 0x9
    MEMORY_READ = 0xA
    CMD_READY = 0xB
    SWITCH_MODE = 0xC
    EXECUTE_REQ = 0xD
    EXECUTE_RSP = 0xE
    EXECUTE_DATA = 0xF
    MEMORY_DEBUG_64BIT = 0x10
    MEMORY_READ_64BIT = 0x11
    MEMORY_READ_DATA_64BIT = 0x12
    RESET_STATE_MACHINE_ID = 0x13


class SaharaExecCmd(IntEnum):
    # Only one exec subcmd is implemented in sbl1
    SERIAL_NUM_READ = 0x01


class SaharaMode(IntEnum):
    IMAGE_TX_PENDING = 0x0
    IMAGE_TX_COMPLETE = 0x1
    MEMORY_DEBUG = 0x2
    COMMAND = 0x3


@dataclass
class CmdHeader:
    cmd: SaharaCmd
    len: int


@dataclass
class SaharaPacket:
    cmd: SaharaCmd
    len: int

    def __repr__(self):
        return f"SAHARA_UNKNOWN_PKT(cmd={self.cmd}, len={self.len}"

    def __str__(self):
        return self.__repr__()


@dataclass
class HelloRequest(SaharaPacket):
    version: int
    version_supported: int
    cmd_packet_length: int
    mode: SaharaMode
    reserved1: int
    reserved2: int
    reserved3: int
    reserved4: int
    reserved5: int
    reserved6: int

    def __repr__(self):
        return (f"SAHARA_HELLO_REQ(cmd={self.cmd}, "
                f"len={self.len}, version={self.version}, "
                f"version_supported={self.version_supported}, "
                f"cmd_packet_length={self.cmd_packet_length}, "
                f"mode={self.mode})")


@dataclass
class ExecuteResponse(SaharaPacket):
    client_cmd: int
    data_len: int


@dataclass
class ImageEnd(SaharaPacket):
    image_id: int
    image_tx_status: int
