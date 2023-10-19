import turtle

def zeichnen_yannick():
    turtle.write("Yannick", font=('Arial', 60, 'normal'))
    
    turtle.color('yellow')
    turtle.width(10)

    turtle.circle(100)
    turtle.up()
    turtle.color('orange')
    turtle.forward(150)
    turtle.down()
    turtle.circle(100)

def main():
    print("Zeichenprogramm")
    zeichnen_yannick()
    input()

if __name__ == "__main__":
    main()