import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)

        self.pwm.start(0)


    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup(self.gpio_pin)


    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устаннавливаем 0.0 В")
            return 0

        return (voltage / self.dynamic_range * 100)

    
    def number_to_pwm(self, number):
        pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        pwm.start(number)


    def set_voltage(self, voltage):
        number = self.voltage_to_number(voltage)

        self.pwm.ChangeDutyCycle(number)



if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Enter voltage: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("What you've entered is not a number. Try again\n")

    finally:
        dac.deinit()