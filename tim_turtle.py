import turtle as t
from random import random

def zeichnung():
    for i in range(100):
        steps = int(random() * 100)
        angle = int(random() * 360)
        t.right(angle)
        t.fd(steps)

if __name__ == '__main__':
    zeichnung()