#   -*- coding: utf-8 -*-

# Les imports
import pygame
import random
pygame.init()
# Les variables et fonctions globales
longueurPlateforme = 70
largeurJoueur = 66
display_width, display_height = 800, 600
# couleurs
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
pygame.display.set_caption('Endless Arena')
clock = pygame.time.Clock()
pygame.display.set_caption('Endless Arena')

gameDisplay = pygame.display.set_mode((display_width, display_height))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, display, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        gameDisplay.blit(textSurf, textRect)

def quitter():
    print("quitter")
    pygame.QUIT()

def menu():
    print("[*]: Lancement du menu")
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        carImg = pygame.image.load('fichiers/images/bg.png')
        gameDisplay.blit(carImg, (0, 0))
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Endless Arena", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Quitter", 550, 450, 100, 50, red, bright_red, gameDisplay, quitter)
        button("Jouer", 150, 450, 100, 50, green, bright_green, gameDisplay, jouer)

        pygame.display.update()
        clock.tick(15)


def jouer():
    "Jouer une partie"
    print("[*]: Début d'une partie")
    # initialisation des variables de partie
    scoreJoueur1 = 0
    scoreJoueur2 = 0

    # variables de personnages
    hauteurJoueur = 92

    sensJoueur1 = 1  # bool, 1 tourné vers la droite,
    sensJoueur2 = 1  # 0 tourné vers la gauche

    xJoueur1 = 15
    yJoueur1 = 380
    xJoueur2 = 785
    yJoueur2 = 380

    vitXJoueur1 = 0
    vitXJoueur2 = 0
    nbSautJoueur1 = 0
    nbSautJoueur2 = 0

    respawnX = 15
    respawnY = 380

    # variables de plateformes
    vitessePlateforme = 1

    xPlateforme1 = 0
    yPlateforme1 = 15

    xPlateforme2 = 160
    yPlateforme2 = 65

    xPlateforme3 = 220
    yPlateforme3 = 125

    xPlateforme4 = 380
    yPlateforme4 = 400

    xPlateforme5 = 540
    yPlateforme5 = 500

    # création des sprites et objets
    # L'arrière plan
    arrierePlan = pygame.image.load('fichiers/images/bgPartie.png')
    gameDisplay.blit(arrierePlan, (0, 0))

    # Les joueurs
    imgJoueur1 = pygame.image.load('fichiers/images/joueur1.png')
    gameDisplay.blit(imgJoueur1, (xJoueur1, yJoueur1))

    imgJoueur2 = pygame.image.load('fichiers/images/joueur2.png')
    gameDisplay.blit(imgJoueur2, (xJoueur2, yJoueur2))

    # Les plateformes, il y en a 5
    imgPlateforme = pygame.image.load('fichiers/images/plateforme.png')

    gameDisplay.blit(imgPlateforme, (xPlateforme1, yPlateforme1))

    gameDisplay.blit(imgPlateforme, (xPlateforme2, yPlateforme2))

    gameDisplay.blit(imgPlateforme, (xPlateforme3, yPlateforme3))

    gameDisplay.blit(imgPlateforme, (xPlateforme4, yPlateforme4))

    gameDisplay.blit(imgPlateforme, (xPlateforme5, yPlateforme5))
    # boucle de jeu
    print("[*]: Partie initialisée")
    while scoreJoueur1 < 3 and scoreJoueur2 < 3:  # tant que personne n'a gagné
        # Prendre les inputs et Mettre à jour les positions contrôlées
        print("[*]: Itération de la boucle")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # déplacement des joueurs
                if event.key == pygame.K_q:
                    sensJoueur1 = 0  # Le joueur se tourne vers la gauche.
                    xJoueur1 -= 25
                if event.key == pygame.K_k:
                    sensJoueur2 = 0  # Le joueur se tourne vers la gauche.
                    xJoueur2 -= 25
                if event.key == pygame.K_d:
                    sensJoueur1 = 1  # Le joueur se tourne vers la droite.
                    xJoueur1 += 25
                if event.key == pygame.K_m:
                    sensJoueur2 = 1  # Le joueur se tourne vers la droite.
                    xJoueur2 += 25
                if event.key == pygame.K_z and nbSautJoueur1 < 2:
                    vitXJoueur1 = -1  # Le joueur saute.
                    nbSautJoueur1 += 1
                if event.key == pygame.K_o and nbSautJoueur2 < 2:
                    vitXJoueur2 = -1  # Le joueur saute
                    nbSautJoueur2 += 1

                # attaques à l'épée
                if event.key == pygame.K_e:  # Joueur 1 frappe
                    if yJoueur1 == yJoueur2:  # si les joueurs sont à la même hauteur
                        # Et à portée
                        if sensJoueur1 == 1:
                            if xJoueur2 == (xJoueur1 + 5):
                                xJoueur2, yJoueur2 = respawnX, respawnY  # Remise à 0 du joueur 2
                                scoreJoueur1 += 1
                        else:
                            if xJoueur2 == (xJoueur1 - 5):
                                xJoueur2, yJoueur2 = respawnX, respawnY  # Remise à 0 du joueur 2
                                scoreJoueur1 += 1

                if event.key == pygame.K_p:  # Joueur 1 frappe
                    if yJoueur1 == yJoueur2:  # si les joueurs sont à la même hauteur
                        # Et à portée
                        if sensJoueur2 == 1:
                            if xJoueur1 == (xJoueur2 + 5):
                                xJoueur1 = respawnX
                                yJoueur1 = respawnY # Remise à 0 du joueur 1
                                scoreJoueur2 += 1
                        else:
                            if xJoueur1 == (xJoueur2 - 5):
                                xJoueur1 = respawnX
                                yJoueur1 = respawnY # Remise à 0 du joueur 1
                                scoreJoueur2 += 1

        # Gérer les chutes et les positions
        # Les plateformes
        if xPlateforme1 < 0:  # si la plateforme est sortie par la gauche
            yPlateforme1 = random.randrange(150, 600)  # on change sa hauteur au hasard
            xPlateforme1 = 800  # et on la renvoie à droite
        else:
            xPlateforme1 -= vitessePlateforme  # sinon on la fait avancer

        if xPlateforme2 < 0:  # si la plateforme est sortie par la gauche
            yPlateforme2 = random.randrange(150, 600)  # on change sa hauteur au hasard
            xPlateforme2 = 800  # et on la renvoie à droite
        else:
            xPlateforme2 -= vitessePlateforme # sinon on la fait avancer

        if xPlateforme3 < 0:  # si la plateforme est sortie par la gauche
            yPlateforme3 = random.randrange(150, 600)  # on change sa hauteur au hasard
            xPlateforme3 = 800  # et on la renvoie à droite
        else:
            xPlateforme3 -= vitessePlateforme  # sinon on la fait avancer

        if xPlateforme4 < 0:  # si la plateforme est sortie par la gauche
            yPlateforme4 = random.randrange(150, 600)  # on change sa hauteur au hasard
            xPlateforme4 = 800  # et on la renvoie à droite
        else:
            xPlateforme4 -= vitessePlateforme  # sinon on la fait avancer

        if xPlateforme5 < 0:  # si la plateforme est sortie par la gauche
            yPlateforme5 = random.randrange(150, 600)  # on change sa hauteur au hasard
            xPlateforme5 = 800  # et on la renvoie à droite
        else:
            xPlateforme5 -= vitessePlateforme  # sinon on la fait avancer

        # Les personnages
        # On checke d'abord si ils sont sortis de l'écran
        if xJoueur1 < 0:
            scoreJoueur1 -= 1
            yJoueur1 = respawnX
            xJoueur1 = respawnY

        if yJoueur2 > 800 or xJoueur2 < 0:
            scoreJoueur2 -= 1
            yJoueur2 = respawnX
            xJoueur2 = respawnY

        if yJoueur1 > 800:
            yJoueur1 = 0

        if yJoueur2 > 800:
            yJoueur2 = 0

        # Puis si ils sont sur une plateforme. sinon, ils chutent
        plateformesXmin = [xPlateforme1, xPlateforme2, xPlateforme3, xPlateforme4, xPlateforme5]
        plateformesYmin = [yPlateforme1, yPlateforme2, yPlateforme3, yPlateforme4, yPlateforme5]

        for i in range(len(plateformesYmin)):
            if not (plateformesYmin[i] >= yJoueur1 + largeurJoueur or yJoueur1 >= plateformesYmin[i] + longueurPlateforme) and xJoueur1 + hauteurJoueur <= plateformesXmin[i] <= xJoueur1 + hauteurJoueur + vitXJoueur1 :
                # si le joueur est sur une Plateforme
                if vitXJoueur1 > 0 :
                    vitXJoueur1 = 0    # On enlève sa vitesse verticale lors de son arrivée
                if xJoueur1 + hauteurJoueur <= plateformesXmin[i] :
                    hauteurJoueur1 = plateformesXmin[i] - hauteurJoueur    # On plaque le joueur sur la plateforme
                xJoueur1 -= vitessePlateforme    # On déplace le joueur avec la plateforme
                nbSautJoueur1 = 0 # On réinitialise son compteur de saut

            else :
                # si le joueur n'est pas sur une Plateforme
                if vitXJoueur1 < 2 :
                    vitXJoueur1 += 0.05    # On définit une accélération verticale
                if nbSautJoueur1 == 0 :
                    nbSautJoueur1 = 1    #On empêche le triple saut
            yJoueur1 += vitXJoueur1

        for i in range(len(plateformesYmin)):
            if not (plateformesYmin[i] >= yJoueur2 + largeurJoueur or yJoueur2 >= plateformesYmin[i] + longueurPlateforme) and xJoueur2 + hauteurJoueur <= plateformesXmin[i] <= xJoueur2 + hauteurJoueur + vitXJoueur2 :
                # si le joueur est sur une Plateforme
                if vitXJoueur2 > 0 :
                    vitXJoueur2 = 0    # On enlève sa vitesse verticale lors de son arrivée
                if xJoueur2 + hauteurJoueur <= plateformesXmin[i] :
                    hauteurJoueur2 = plateformesXmin[i] - hauteurJoueur    # On plaque le joueur sur la plateforme
                xJoueur2 -= vitessePlateforme    # On déplace le joueur avec la plateforme
                nbSautJoueur2 = 0 # On réinitialise son compteur de saut

            else :
                # si le joueur n'est pas sur une Plateforme
                if vitXJoueur2 < 2 :
                    vitXJoueur2 += 0.05    # On définit une accélération verticale
                if nbSautJoueur2 == 0 :
                    nbSautJoueur2 = 1    #On empêche le triple saut
            yJoueur2 += vitXJoueur2

        # Mettre à jour les images
        gameDisplay.blit(arrierePlan, (0, 0))
        gameDisplay.blit(imgJoueur1, (xJoueur1, yJoueur1))
        gameDisplay.blit(imgJoueur2, (xJoueur2, yJoueur2))
        gameDisplay.blit(imgPlateforme, (xPlateforme1, yPlateforme1))
        gameDisplay.blit(imgPlateforme, (xPlateforme2, yPlateforme2))
        gameDisplay.blit(imgPlateforme, (xPlateforme3, yPlateforme3))
        gameDisplay.blit(imgPlateforme, (xPlateforme4, yPlateforme4))
        gameDisplay.blit(imgPlateforme, (xPlateforme5, yPlateforme5))
        pygame.display.update()

        print("Score :", scoreJoueur1, " à ",scoreJoueur2)

    print("Endgame")



# Du test
print("""
 _____          _ _                  ___
|  ___|        | | |                / _ \
| |__ _ __   __| | | ___  ___ ___  / /_\ \_ __ ___ _ __   __ _
|  __| '_ \ / _` | |/ _ \/ __/ __| |  _  | '__/ _ \ '_ \ / _` |
| |__| | | | (_| | |  __/\__ \__ \ | | | | | |  __/ | | | (_| |
\____/_| |_|\__,_|_|\___||___/___/ \_| |_/_|  \___|_| |_|\__,_|


""")
print("[*]: Initialisation du programme")
menu()
# Du test
