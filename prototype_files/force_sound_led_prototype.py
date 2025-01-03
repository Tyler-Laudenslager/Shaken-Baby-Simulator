import board
import time
import random
import digitalio
import audiocore
import audiobusio
import adafruit_lis3dh
from adafruit_ht16k33.matrix import Matrix8x8x2

#setup for 3 color matrix
i2c = board.I2C()
matrix = Matrix8x8x2(i2c)
#end setup

#setup for accelerometer
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Set to appropriate CS pin!
int1 = digitalio.DigitalInOut(board.D6) # Set to correct pin for interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_SPI(spi, cs, int1=int1)
#end setup

#audio setup
f = open("StreetChicken.wav", "rb")
wav = audiocore.WaveFile(f)
i2s = audiobusio.I2SOut(board.D1, board.D0, board.D9)

#erase colors from board
matrix.fill(0)


def light_column(matrix, column, color):
    for position in range(0,8):
        matrix[position, column] = color

def light_board(matrix, display_force):
    actual_size = display_force-1
    if actual_size >= 0:
        light_column(matrix, 0, color=matrix.LED_GREEN)
    if actual_size >= 1:
        light_column(matrix, 1, color=matrix.LED_GREEN)
    if actual_size >= 2:
        light_column(matrix, 2, color=matrix.LED_YELLOW)
    if actual_size >= 3:
        light_column(matrix, 3, color=matrix.LED_YELLOW)
    if actual_size >= 4:
        light_column(matrix, 4, color=matrix.LED_YELLOW)
    if actual_size >= 5:
        light_column(matrix, 5, color=matrix.LED_RED)
    if actual_size >= 6:
        light_column(matrix, 6, color=matrix.LED_RED)
    if actual_size == 7:
        light_column(matrix, 7, color=matrix.LED_RED)

def read_force_from_accelerometer(matrix):
    force_read = 1
    if lis3dh.shake(shake_threshold=15):
        force_read = 8
        print("force", force_read)
    elif lis3dh.shake(shake_threshold=12):
        force_read = 6
        print("force", force_read)
    elif lis3dh.shake(shake_threshold=10):
        force_read = 4
        print("force", force_read)
    elif lis3dh.shake(shake_threshold=5):
        force_read = 1
        print("force", force_read)

    light_board(matrix, display_force=force_read)
    time.sleep(0.1)
    matrix.fill(0)


while True:
    start=time.monotonic()
    i2s.play(wav)
    while i2s.playing:
        read_force_from_accelerometer(matrix)
    stop = time.monotonic()
    print("Total lenght = ", stop, "-", start, "=", stop-start)
