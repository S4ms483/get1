import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

leds = [24, 22,  23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
dynamic_range = 3.3


def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устаннавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)


def number_to_dac(number):
    GPIO.output(leds, [int(element) for element in bin(number)[2:].zfill(8)])

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()

