
#https://docs.circuitpython.org/projects/rgbled/en/latest/
import time
import board
from rainbowio import colorwheel
import adafruit_rgbled

# Pin the Red LED is connected to
RED_LED = board.D11

# Pin the Green LED is connected to
GREEN_LED = board.D12

# Pin the Blue LED is connected to
BLUE_LED = board.D13

# Create the RGB LED object
led = adafruit_rgbled.RGBLED(RED_LED, GREEN_LED, BLUE_LED)

# Optionally, you can also create the RGB LED object with inverted PWM
# led = adafruit_rgbled.RGBLED(RED_LED, GREEN_LED, BLUE_LED, invert_pwm=True)

def rainbow_cycle(wait):
    for i in range(255):
        i = (i + 1) % 256
        led.color = colorwheel(i)
        time.sleep(wait)

while True:
    # setting RGB LED color to RGB Tuples (R, G, B)
    led.color = (255, 0, 0)
    time.sleep(1)

    led.color = (0, 255, 0)
    time.sleep(1)

    led.color = (0, 0, 255)
    time.sleep(1)

    # setting RGB LED color to 24-bit integer values
    led.color = 0xFF0000
    time.sleep(1)

    led.color = 0x00FF00
    time.sleep(1)

    led.color = 0x0000FF
    time.sleep(1)

    # rainbow cycle the RGB LED
    rainbow_cycle(0.1)
