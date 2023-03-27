import turtle

turtle.bgcolor('black')

def arvore(t, comprimento, nivel, cores):
    if nivel == 0:
        return
    cor = cores[nivel % len(cores)]
    t.color(cor)
    t.pensize(nivel/3)
    t.forward(comprimento)
    t.left(45)
    arvore(t, 0.6*comprimento, nivel-1, cores)
    t.right(90)
    arvore(t, 0.6*comprimento, nivel-1, cores)
    t.left(45)
    t.backward(comprimento)

t = turtle.Turtle()
t.left(90)
cores = ['brown', 'green', 'red']
arvore(t, 100, 6, cores)
turtle.done()