#   -*- coding: utf-8 -*-

# Les imports
import pygame
import random
pygame.init()
# Les variables et fonctions globales
longueurPlateforme = 160
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

def text_fin(text, font):
    textSurface = font.render(text, True, red)
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
    print("[0] Fermeture de la fenêtre")
    pygame.quit()

def menu():
    print("[0]: Lancement du menu")
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

def endgame(scoreJoueur1, scoreJoueur2):
    print("[0]: Écran de fin de jeu")
    pasdechoix = True

    while pasdechoix:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        bgEndgame = pygame.image.load('fichiers/images/bgEndgame.png')
        gameDisplay.blit(bgEndgame, (0, 0))
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_fin("%s à %s" %(scoreJoueur1, scoreJoueur2), largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Quitter", 550, 450, 100, 50, red, bright_red, gameDisplay, quitter)
        button("Rejouer?", 150, 450, 100, 50, green, bright_green, gameDisplay, jouer)

        pygame.display.update()
        clock.tick(15)


def jouer():
    "Jouer une partie"
    print("[0]: Début d'une partie")
    # initialisation des variables de partie
    scoreJoueur1 = 0
    scoreJoueur2 = 0

    # variables de personnages
    hauteurJoueur = 92
    largeurJoueur = 66

    sensJoueur1 = 1  # bool, 1 tourné vers la droite,
    sensJoueur2 = 0  # 0 tourné vers la gauche

    xJoueur1 = 15
    yJoueur1 = 380
    xJoueur2 = 785
    yJoueur2 = 380

    vitXJoueur1 = 0
    vitXJoueur2 = 0
    vitYJoueur1 = 0
    vitYJoueur2 = 0
    nbSautJoueur1 = 0
    nbSautJoueur2 = 0

    respawnX = (800 - largeurJoueur) / 2
    respawnY = 15

    # variables de plateformes
    vitessePlateforme = 1
    vitesseJoueur = vitessePlateforme * 3

    xPlateforme1 = 0
    yPlateforme1 = random.randrange(150, 550)

    xPlateforme2 = 160
    yPlateforme2 = random.randrange(150, 550)

    xPlateforme3 = 320
    yPlateforme3 = random.randrange(150, 550)

    xPlateforme4 = 480
    yPlateforme4 = random.randrange(150, 550)

    xPlateforme5 = 640
    yPlateforme5 = random.randrange(150, 600)

    xPlateforme6 = 800
    yPlateforme6 = random.randrange(150, 600)


    #création des sons
    pygame.mixer.pre_init(44100, -16, 2, 4096) # réglage du mixer pour éviter des bugs audio
    pygame.mixer.init()
    #charger la musique et la jouer en boucle
    pygame.mixer.music.load("fichiers/son/musique.mp3")
    pygame.mixer.music.play(-1)

    # charger les autres sons
    fichierCoup = 'fichiers/son/coup.ogg'
    fichierSaut = 'fichiers/son/saut.ogg'

    sonCoup = pygame.mixer.Sound(fichierCoup)
    sonSaut = pygame.mixer.Sound(fichierSaut)

    # création des sprites et objets
    # L'arrière plan
    arrierePlan = pygame.image.load('fichiers/images/bgPartie.png')
    gameDisplay.blit(arrierePlan, (0, 0))

    # Les joueurs
    imgJoueur1D = pygame.image.load('fichiers/images/joueur1D.png')
    imgJoueur1G = pygame.image.load('fichiers/images/joueur1G.png')
    gameDisplay.blit(imgJoueur1D, (xJoueur1, yJoueur1))

    imgJoueur2D = pygame.image.load('fichiers/images/joueur2D.png')
    imgJoueur2G = pygame.image.load('fichiers/images/joueur2G.png')
    gameDisplay.blit(imgJoueur2G, (xJoueur2, yJoueur2))

    # Les plateformes, il y en a 6
    imgPlateforme = pygame.image.load('fichiers/images/plateforme.png')
    gameDisplay.blit(imgPlateforme, (xPlateforme1, yPlateforme1))
    gameDisplay.blit(imgPlateforme, (xPlateforme2, yPlateforme2))
    gameDisplay.blit(imgPlateforme, (xPlateforme3, yPlateforme3))
    gameDisplay.blit(imgPlateforme, (xPlateforme4, yPlateforme4))
    gameDisplay.blit(imgPlateforme, (xPlateforme5, yPlateforme5))
    gameDisplay.blit(imgPlateforme, (xPlateforme6, yPlateforme6))
    # boucle de jeu
    print("[0]: Partie initialisée")
    while scoreJoueur1 < 3 and scoreJoueur2 < 3:  # tant que personne n'a gagné
        print("[0]: Itération de la boucle")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            print("    [1]: Récupération des inputs")
            if event.type == pygame.KEYDOWN:
                # déplacement des joueurs
                if event.key == pygame.K_a:
                    sensJoueur1 = 0  # Le joueur se tourne vers la gauche.
                    vitXJoueur1 = -vitesseJoueur
                if event.key == pygame.K_j:
                    sensJoueur2 = 0  # Le joueur se tourne vers la gauche.
                    vitXJoueur2 = -vitesseJoueur
                if event.key == pygame.K_d:
                    sensJoueur1 = 1  # Le joueur se tourne vers la droite.
                    vitXJoueur1 = vitesseJoueur
                if event.key == pygame.K_l:
                    sensJoueur2 = 1  # Le joueur se tourne vers la droite.
                    vitXJoueur2 = vitesseJoueur
                if event.key == pygame.K_w and nbSautJoueur1 < 2:
                    vitYJoueur1 = -5  # Le joueur saute.
                    nbSautJoueur1 += 1
                if event.key == pygame.K_i and nbSautJoueur2 < 2:
                    vitYJoueur2 = -5  # Le joueur saute
                    nbSautJoueur2 += 1


                # attaques à l'épée
                if event.key == pygame.K_e:  # Joueur 1 frappe
                    if not(yJoueur1 >= yJoueur2 + hauteurJoueur or yJoueur1 + hauteurJoueur <= yJoueur2):  # si les joueurs sont à la même hauteur
                        if sensJoueur1:
                            if not(xJoueur1 >= xJoueur2 or xJoueur1 + 3*largeurJoueur <= xJoueur2):
                                scoreJoueur1 += 1
                                xJoueur2, yJoueur2 = respawnX, respawnY
                        else:
                            if not(xJoueur1 - 3 * largeurJoueur >= xJoueur2 or xJoueur1 <= xJoueur2):
                                scoreJoueur1 += 1
                                xJoueur2, yJoueur2 = respawnX, respawnY

                if event.key == pygame.K_o:  # Joueur 1 frappe
                    if not(yJoueur2 >= yJoueur1 + hauteurJoueur or yJoueur2 + hauteurJoueur <= yJoueur1):  # si les joueurs sont à la même hauteur
                        if sensJoueur2:
                            if not(xJoueur2 >= xJoueur1 or xJoueur2 + 3*largeurJoueur <= xJoueur1):
                                scoreJoueur2 += 1
                                xJoueur1, yJoueur1 = respawnX, respawnY
                        else:
                            if not(xJoueur2 - 3 * largeurJoueur >= xJoueur1 or xJoueur2 <= xJoueur1):
                                scoreJoueur2 += 1
                                xJoueur1, yJoueur1 = respawnX, respawnY



        xJoueur1 += vitXJoueur1
        xJoueur2 += vitXJoueur2

        print("    [1]: Gestion du déplacement des plateformes")
        plateformesXY = [[xPlateforme1, yPlateforme1], [xPlateforme2, yPlateforme2], [xPlateforme3, yPlateforme3], [xPlateforme4, yPlateforme4], [xPlateforme5, yPlateforme5], [xPlateforme6, yPlateforme6]]
        plateformesX = [xPlateforme1,xPlateforme2,xPlateforme3,xPlateforme4,xPlateforme5,xPlateforme6]
        plateformesY = [yPlateforme1,yPlateforme2,yPlateforme3,yPlateforme4,yPlateforme5,yPlateforme6]

        # Gérer les chutes et les positions
        # Les plateformes
        if xPlateforme1 < -160:  # si la plateforme est sortie par la gauche
            yPlateforme1 = random.randrange(150, 550)  # on change sa hauteur au hasard
            xPlateforme1 = 800  # et on la renvoie à droite
        else:
            xPlateforme1 -= vitessePlateforme  # sinon on la fait avancer

        if xPlateforme2 < -160:  # si la plateforme est sortie par la gauche
            yPlateforme2 = random.randrange(150, 550)  # on change sa hauteur au hasard
            xPlateforme2 = 800  # et on la renvoie à droite
        else:
            xPlateforme2 -= vitessePlateforme  # sinon on la fait avancer

        if xPlateforme3 < -160:  # si la plateforme est sortie par la gauche
            yPlateforme3 = random.randrange(150, 550)  # on change sa hauteur au hasard
            xPlateforme3 = 800  # et on la renvoie à droite
        else:
            xPlateforme3 -= vitessePlateforme  # sinon on la fait avancer

        if xPlateforme4 < -160:  # si la plateforme est sortie par la gauche
            yPlateforme4 = random.randrange(150, 550)  # on change sa hauteur au hasard
            xPlateforme4 = 800  # et on la renvoie à droite
        else:
            xPlateforme4 -= vitessePlateforme  # sinon on la fait avancer

        if xPlateforme5 < -160:  # si la plateforme est sortie par la gauche
            yPlateforme5 = random.randrange(150, 550)  # on change sa hauteur au hasard
            xPlateforme5 = 800  # et on la renvoie à droite
        else:
            xPlateforme5 -= vitessePlateforme  # sinon on la fait avancer

        if xPlateforme6 < -160:  # si la plateforme est sortie par la gauche
            yPlateforme6 = random.randrange(150, 550)  # on change sa hauteur au hasard
            xPlateforme6 = 800  # et on la renvoie à droite
        else:
            xPlateforme6 -= vitessePlateforme  # sinon on la fait avancer

        print("    [1]: Gestion des chutes")

        # Les personnages
        # On checke d'abord si ils sont sortis de l'écran
        if xJoueur1 < -(2 * largeurJoueur) or xJoueur1 > 800 + largeurJoueur:
            scoreJoueur1 -= 1
            yJoueur1 = respawnX
            xJoueur1 = respawnY

        if yJoueur1 > 600:
            yJoueur1 -= 800 + hauteurJoueur

        if xJoueur2 < -(2 * largeurJoueur) or xJoueur2 > 800 + largeurJoueur:
            scoreJoueur2 -= 1
            yJoueur2 = respawnX
            xJoueur2 = respawnY

        if yJoueur2 > 600:
            yJoueur2 -= 800 + hauteurJoueur

        # Puis si ils sont sur une plateforme. sinon, ils chutent

        joueur1Soutenu = False
        for plateforme in plateformesXY:  # on teste si il est sur une plateforme
            testX = not(xJoueur1 + largeurJoueur <= plateforme[0] or plateforme[0] + longueurPlateforme <= xJoueur1)
            testY = (yJoueur1 + hauteurJoueur <= plateforme[1] and plateforme[1] <= yJoueur1 + hauteurJoueur + vitYJoueur1+1)
            if testX and testY :
                Joueur1Soutenu = True
                yJoueur1 = plateforme[1] - hauteurJoueur - 1

        if joueur1Soutenu:
            nbSautJoueur1 = 0
            if vitYJoueur1 > 0 :
                vitYJoueur1 = 0
            xJoueur1 -= vitessePlateforme

        else:
            if vitYJoueur1 < 5 :
                vitYJoueur1 += 0.1
            if nbSautJoueur1 == 0:
                nbSautJoueur1 = 1       # Pour ne permettre qu'un seul saut mid-air

        yJoueur1 += vitYJoueur1

        Joueur2Soutenu = False
        for plateforme in plateformesXY:  # on teste si il est sur une plateforme
            testX = not(xJoueur2 + largeurJoueur <= plateforme[0] or plateforme[0] + longueurPlateforme <= xJoueur2)
            testY = (yJoueur2 + hauteurJoueur <= plateforme[1] and plateforme[1] <= yJoueur2 + hauteurJoueur + vitYJoueur2+1)
            if testX and testY :
                Joueur2Soutenu = True
                yJoueur2 = plateforme[1] - hauteurJoueur - 1

        if Joueur2Soutenu:
            nbSautJoueur2 = 0
            if vitYJoueur2 > 0 :
                vitYJoueur2 = 0
            xJoueur2 -= vitessePlateforme

        else:
            if vitYJoueur2 < 5 :
                vitYJoueur2 += 0.1
            if nbSautJoueur2 == 0:
                nbSautJoueur2 = 1       # Pour ne permettre qu'un seul saut mid-air
        yJoueur2 += vitYJoueur2
        print("    [1]: Mise à jour du score (%s:%s)" %(scoreJoueur1, scoreJoueur2))
        largeText = pygame.font.SysFont("comicsansms", 50)
        TextSurf, TextRect = text_objects("%s : %s" % (scoreJoueur1, scoreJoueur2), largeText)
        TextRect.center = ((display_width/2), (display_height/9))

        print("    [1]: Mise à jour de l'affichage")
        # Mettre à jour les images
        gameDisplay.blit(arrierePlan, (0, 0))
        if sensJoueur1 :
            gameDisplay.blit(imgJoueur1D, (xJoueur1, yJoueur1))
        else :
            gameDisplay.blit(imgJoueur1G, (xJoueur1, yJoueur1))
        if sensJoueur2 :
            gameDisplay.blit(imgJoueur2D, (xJoueur2, yJoueur2))
        else :
            gameDisplay.blit(imgJoueur2G, (xJoueur2, yJoueur2))
        gameDisplay.blit(imgPlateforme, (xPlateforme1, yPlateforme1))
        gameDisplay.blit(imgPlateforme, (xPlateforme2, yPlateforme2))
        gameDisplay.blit(imgPlateforme, (xPlateforme3, yPlateforme3))
        gameDisplay.blit(imgPlateforme, (xPlateforme4, yPlateforme4))
        gameDisplay.blit(imgPlateforme, (xPlateforme5, yPlateforme5))
        gameDisplay.blit(imgPlateforme, (xPlateforme6, yPlateforme6))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()


    endgame(scoreJoueur1,scoreJoueur2)


# Du test
print(
"""
 _____          _ _                  ___
|  ___|        | | |                / _ \
| |__ _ __   __| | | ___  ___ ___  / /_\ \_ __ ___ _ __   __ _
|  __| '_ \ / _` | |/ _ \/ __/ __| |  _  | '__/ _ \ '_ \ / _` |
| |__| | | | (_| | |  __/\__ \__ \ | | | | | |  __/ | | | (_| |
\____/_| |_|\__,_|_|\___||___/___/ \_| |_/_|  \___|_| |_|\__,_|


"""
)
print("[0]: Initialisation du programme")
menu()
# Du test
