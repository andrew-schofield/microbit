# Add your Python code here. E.g.
from microbit import *


while True:
    temp = temperature()
    display.scroll(str(temp) + "C", delay=250)
    sleep(2000)
