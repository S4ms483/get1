import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

divide = 6
GPIO.setup(divide, GPIO.IN)

state = 0

while True:
    if GPIO.input(divide):
        state = 0

    else:
        state = 1
    GPIO.output(led, state)