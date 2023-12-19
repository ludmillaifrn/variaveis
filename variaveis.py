from turtle import Turtle,onscreenclick, onkey, listen, Screen, color
turtle = Turtle ()
tela = Screen()

def circulo(): 
    r = 50
    turtle.pendown()
    turtle.circle(r)

def quadrado(): 
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70) 

escolher = ''

while(escolher != 0 ):

    print("escolha um numero")
    print("2 circulo" )
    print("4 quadrado")
    escolher = int(input())
    cor = input("escolha uma cor ")
    turtle.color(cor)
    pincel = input("diga a largura ")
    velocidade = input("escolha a velocidade ")
    if escolher == 2 :
        circulo()
    if escolher == 4 :
        quadrado()

tela.onscreenclick()

listen()
tela.mainloop()