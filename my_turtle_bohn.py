import turtle

def zeichne_bohn():
    turtle.write("Bohn", font=('Arial', 50, 'normal'))

   # turtle.Screen.bgcolor("green")

    #pen = turtle.Turtle()
    turtle.speed(3)
    turtle.color  ("blue")

    for _ in range(10):
        turtle.forward(100)
        turtle.right(170)

    #window.exitonclick()

if __name__ == "__main__":
    zeichne_bohn()
