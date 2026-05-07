import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("Only integers allowed as input numbers")
            return

        if not (0 <= number <= 4095):
            print("The number is out of range for MCP4752(12 bits)")
            return


        first_byte = self.wm | self.pds | (number >> 8)
        second_byte = number & 0xFF
        self.bus.write_i2c_block_data(self.address, first_byte, [second_byte])

        if self.verbose:
            print(f"Number: {number}, data sent by I2C: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")


    def set_voltage(self, voltage):
        if not (0 <= voltage <= self.dynamic_range):
            print("The number exceeds range")
            return

        number = int((voltage / self.dynamic_range) * 4095)
        self.set_number(number)



if __name__ == "__main__":
    try:
        mcp = MCP4725(5, 0x61, True)

        while True:
            try:
                voltage = int(input("Enter voltage: "))
                mcp.set_voltage(voltage)

            except ValueError:
                print("What you've entered is not a number. Try again\n")

    finally:
        mcp.deinit()