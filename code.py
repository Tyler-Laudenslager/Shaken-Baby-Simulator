mport board
import time
import random
from adafruit_ht16k33.matrix import Matrix8x8x2

i2c = board.I2C()
matrix = Matrix8x8x2(i2c)


matrix.fill(0)


def light_column(matrix, column, color):
    for position in range(0,8):
        matrix[position, column] = color
        
def light_board(matrix, size):
    actual_size = size-1
    if actual_size >= 0:
        light_column(matrix, 0, color=matrix.LED_GREEN)
    if actual_size >= 1:
        light_column(matrix, 1, color=matrix.LED_GREEN)
    if actual_size >= 2:
        light_column(matrix, 2, color=matrix.LED_GREEN)
    if actual_size >= 3:
        light_column(matrix, 3, color=matrix.LED_YELLOW)
    if actual_size >= 4:
        light_column(matrix, 4, color=matrix.LED_YELLOW)
    if actual_size >= 5:
        light_column(matrix, 5, color=matrix.LED_YELLOW)
    if actual_size >= 6:
        light_column(matrix, 6, color=matrix.LED_RED)
    if actual_size == 7:
        light_column(matrix, 7, color=matrix.LED_RED)
    
while True:
    light_board(matrix, random.randint(1,7))
    time.sleep(0.4)
    matrix.fill(0)
