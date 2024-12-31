import turtle


def fenetre(x, y):
    """
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    """

    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(30)
        turtle.left(90)
    turtle.end_fill()


if __name__ == '__main__':
    fenetre(0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
