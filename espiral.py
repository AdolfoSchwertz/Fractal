import turtle

#Expessura da linha
turtle.pensize(5)

#Desenha um Quadrado em espiral
step = 10
angle = 90
distance = 0
for i in range(20):
    turtle.forward(distance)
    distance += step
    turtle.left(angle)

#Abre a tela do desenho e fecha com um click
turtle.Screen().exitonclick()