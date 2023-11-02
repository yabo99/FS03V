import turtle as t
from random import random

def zeichnung():
    tmp = "j"
    while (tmp == "j"):
        for i in range(10):
            steps = int(random() * 100)
            angle = int(random() * 360)
            t.right(angle)
            t.fd(steps)
        tmp = input("Willst du noch mehr gezeichnet bekommen? (j/n) ")
        


if __name__ == '__main__':
    zeichnung()