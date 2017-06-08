# Add your Python code here. E.g.
from microbit import *

unit = "C"
offset = -2

while True:
    if button_a.is_pressed():
        unit = "C"
    elif button_b.is_pressed():
        unit = "F"
    temp = temperature() + offset
    if unit == "F":
        temp = int(temp * 9/5 + 32)
    display.scroll(str(temp) + unit, delay=200, wait=False)
    sleep(5000)
