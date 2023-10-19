import turtle

def zeichne_muster():
    turtle.write("Bohn", font=('Arial', 50, 'normal'))

    window = turtle.Screen()
    window.bgcolor("green")

    pen = turtle.Turtle()
    pen.speed(3)
    pen.color  ("blue")

    for _ in range(40):
        pen.forward(100)
        pen.right(170)

    window.exitonclick()

if __name__ == "__main__":
    zeichne_muster()
