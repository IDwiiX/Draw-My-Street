from facade import facade
from random import randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle


def etage(x, y_sol, couleur, niveau):
    """
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    """
    # dessin des murs

    facade(x, y_sol, couleur, niveau)
    i = randint(1, 2)
    if i == 1:
        fenetre(x + 15, y_sol + 60 * niveau + 15)
    else:
        fenetre_balcon(x + 15, y_sol + 60 * niveau + 55)

    i = randint(1, 2)
    if i == 1:
        fenetre(x + 60, y_sol + 60 * niveau + 15)
    else:
        fenetre_balcon(x + 60, y_sol + 60 * niveau + 55)

    i = randint(1, 2)
    if i == 1:
        fenetre(x + 105, y_sol + 60 * niveau + 15)
    else:
        fenetre_balcon(x + 105, y_sol + 60 * niveau + 55)


if __name__ == '__main__':
    etage(0, 0, "red", 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
