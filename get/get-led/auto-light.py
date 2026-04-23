import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

divide = 6
GPIO.setup(divide, GPIO.IN)

state = 0

while True:
    state = GPIO.input(divide)
    state = not state

    GPIO.output(led, state)