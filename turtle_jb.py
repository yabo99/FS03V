import turtle

tr = turtle


def main():
    draw_janeck()

def f():#forward
    y = tr.ycor()
    tr.sety(y+100)

def b():#backward
    y = tr.ycor()
    tr.sety(y-100)

def l():#left
    x = tr.xcor()
    tr.setx(x-100)

def r():#right
    x = tr.xcor()
    tr.setx(x+100)

def draw_janeck():
    wn = turtle.Screen()
    tr = turtle.Turtle().hideturtle()
    txt = turtle.Turtle()

    txt.penup()
    txt.hideturtle()
    txt.goto(0, 260)
    txt.write("Mit Pfeiltasten bedienen", align="center", font=("courier", 14, "normal"))   
    wn.listen()
    wn.onkeypress(f, "Up")  
    wn.onkeypress(b, "Down")  
    wn.onkeypress(l, "Left")  
    wn.onkeypress(r, "Right")
    turtle.mainloop()



if __name__ == "__main__":
    main()

