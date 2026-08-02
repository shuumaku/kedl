import struct

from io import BytesIO


def write_object(definition, *args):
    """ Unpacks a structure using the given data and definition. """
    obj = {}
    object_size = 0
    data = b""
    i = 0
    for (name, stype) in definition:
        object_size += struct.calcsize(stype)
        arg = args[i]
        try:
            data += struct.pack(stype, arg)
        except Exception as e:
            print("Error:" + str(e))
            break
        i += 1
    obj['object_size'] = len(data)
    obj['raw_data'] = data
    return obj


class structhelper_io:
    pos = 0

    def __init__(self, data: BytesIO = None, direction='little'):
        self.data = data
        self.direction = direction

    def setdata(self, data, offset=0):
        self.pos = offset
        self.data = data

    def qword(self):
        dat = int.from_bytes(self.data.read(8), self.direction)
        return dat

    def dword(self):
        dat = int.from_bytes(self.data.read(4), self.direction)
        return dat

    def dwords(self, dwords=1):
        dat = [int.from_bytes(self.data.read(4), self.direction) for _ in range(dwords)]
        return dat

    def short(self):
        dat = int.from_bytes(self.data.read(2), self.direction)
        return dat

    def shorts(self, shorts):
        dat = [int.from_bytes(self.data.read(2), self.direction) for _ in range(shorts)]
        return dat

    def bytes(self, rlen=1):
        dat = self.data.read(rlen)
        if dat == b'':
            return dat
        if rlen == 1:
            return dat[0]
        return dat

    def string(self, rlen=1):
        dat = self.data.read(rlen)
        return dat

    def getpos(self):
        return self.data.tell()

    def seek(self, pos):
        self.data.seek(pos)
