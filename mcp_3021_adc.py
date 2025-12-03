import smbus
from time import sleep

dynamic_range = 5

class MCP3021:
    def __init__(self, dynamic_range: float,comp_time=0.1, address: bool=0x4d):
        self.__bus = smbus.SMBus(1) 
        self.__address = address
        sleep(1)
        self.__comp_time = comp_time

        self.__dynamic_range = dynamic_range

    def read(self) -> float:
        sleep(self.__comp_time)
        res = self.__bus.read_i2c_block_data(self.__address, 0, 2)
        return ((((res[0] & 0x0F) << 6)|(res[1]>>2))/1023)*self.__dynamic_range

    def deinit(self) -> None:
        self.__bus.close()
           

if __name__ == "__main__":
    try:
        acd = MCP3021(dynamic_range)
        while True:
            print(acd.read())
    finally:
        acd.deinit()
