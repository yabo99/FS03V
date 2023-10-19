import turtle

def zeichnung_sascha():
    turtle.bgcolor('black') 
    turtle.goto(-200,-200)
    turtle.color('blue')         
    turtle.write("Turtle von Sascha")
    turtle.up()
    r = 100
    x = 10

    turtle.goto(5,5)
    turtle.down()

    for i in range(3):
        turtle.color('yellow')
        turtle.width(10)
        turtle.circle(50)
        turtle.goto(x,x)
        x = x + 5 
        turtle.color('orange')
        turtle.width(10)
        turtle.circle(50)
        turtle.goto(x,x)
        x = x + 5 

    turtle.up()
    turtle.goto(r,r)
    turtle.down()

    for i in range(3):
        turtle.color('green')
        turtle.width(10)
        turtle.circle(50)
        r = r + 5 
        turtle.goto(r,r)
        turtle.color('purple')
        turtle.width(10)
        turtle.circle(50)
        r = r + 5 
        turtle.goto(r,r)
        


def main():
    print("Turtle-Action")
    zeichnung_sascha()



if __name__ == '__main__':
    main()