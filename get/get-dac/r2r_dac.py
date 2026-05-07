import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение {voltage} выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устаннавливаем 0.0 В")
            return 0

        return int(voltage / self.dynamic_range * 255)

    def number_to_dac(self, number):
        GPIO.output(self.gpio_bits, [int(element) for element in bin(number)[2:].zfill(8)])

    
    def set_number(self, number):
        if not (0 <= number <= 255):
            if self.verbose:
                print("error - nnumber should be from 0 to 255")
            return
        self.number_to_dac(number)
        # GPIO.output(self.gpio_bits, [int(element) for element in bin(number)[2:].zfill(8)])

    def set_voltage(self, voltage):
        number = self.voltage_to_number(voltage)

        self.set_number(number)




if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("вы ввели не число. Попробуйте еще раз\n")
    
    finally:
        dac.deinit()