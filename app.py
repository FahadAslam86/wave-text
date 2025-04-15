import math
import time
from IPython.display import clear_output

def ascii_wave(text, width=40, height=12, speed=0.1, cycles=2):
    for t in range(int(width * cycles)):
        clear_output(wait=True)
        for y in range(height):
            line = ""
            for i, char in enumerate(text):
                wave_y = int((math.sin((i + t) * 0.5) + 1) * (height / 2))
                if y == wave_y:
                    line += char
                else:
                    line += " "
            print(line)
        time.sleep(speed)

# 👇 Change this to anything you want!
your_text = input("Enter your text: ")
ascii_wave(your_text)
