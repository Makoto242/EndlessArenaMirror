#   -*- coding: utf-8 -*-

# Les imports
import pygame
import random
pygame.init()
# Les variables et fonctions globales

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

gameDisplay = pygame.display.set_mode((display_width, display_height))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, display, action=None):
    pygame.display.set_caption('Endless Arena')
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


#   Les classes
class Univers(object):
    """La classe générale, qui gère l'initialisation, les autres objets et les
    contrôleurs"""
    #   Attributs
    jeu = []  # la seule variable qui va voyager, contient la position de
    # chaque objet sous la forme {nom, x, y}

    #   Méthodes
    def __init__(self):
        """ Initialisation """
        # l'initialisation est déjà faite au début lol

    def checkChutePersos(self):
        joueurs = [joueur1, joueur2]
        for test in joueurs:
            if test.position_perso['y'] > tailleFenetreY:
                Univers.compteurDePoints(joueurs.index(test), -1)
                test.position_perso['y'] = positionInitialeY
                test.position_perso['x'] = positionInitialeX

    def jouer(self):
        "Jouer une partie"
        # initialisation des variables de partie
        scoreJoueur1 = 0
        scoreJoueur2 = 0

        sensJoueur1 = 1  # bool, 1 tourné vers la droite,
        sensJoueur2 = 1  # 0 tourné vers la gauche

        xJoueur1 = 0
        yJoueur1 = 0
        xJoueur2 = 0
        yJoueur2 = 0

        xPlateforme1 = 0
        yPlateforme1 = 0

        xPlateforme2 = 0
        yPlateforme2 = 0

        xPlateforme3 = 0
        yPlateforme3 = 0

        xPlateforme4 = 0
        yPlateforme4 = 0

        xPlateforme5 = 0
        yPlateforme5 = 0

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
        while scoreJoueur1 < 3 and scoreJoueur2 < 3:  # tant que personne n'a gagné
            # Prendre les inputs et Mettre à jour les positions contrôlées
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    # déplacement des joueurs
                    if event.key == pygame.K_q:
                        sensJoueur1 = 0  # Le joueur se tourne vers la gauche.
                        xJoueur1 -= 5
                    if event.key == pygame.K_k:
                        sensJoueur2 = 0  # Le joueur se tourne vers la gauche.
                        xJoueur2 -= 5
                    if event.key == pygame.K_d:
                        sensJoueur1 = 1  # Le joueur se tourne vers la droite.
                        xJoueur1 += 5
                    if event.key == pygame.K_m:
                        sensJoueur2 = 1  # Le joueur se tourne vers la droite.
                        xJoueur2 += 5
                    if event.key == pygame.K_z:
                        sensJoueur1 = 1  # Le joueur se tourne vers la droite.
                        yJoueur1 += 15
                    if event.key == pygame.K_o:
                        sensJoueur2 = 1  # Le joueur se tourne vers la droite.
                        yJoueur2 += 15

                    # attaques à l'épée ########PANICCCCC Positions Initiales à changer !!!!!!!!!!
                    if event.key == pygame.K_e:  # Joueur 1 frappe
                        if yJoueur1 == yJoueur2:  # si les joueurs sont à la même hauteur
                            # Et à portée
                            if sensJoueur1 == 1:
                                if xJoueur2 == (xJoueur1 + 5):
                                    xJoueur2, yJoueur2 = 0  # Remise à 0 du joueur 2
                                    scoreJoueur1 += 1
                            else:
                                if xJoueur2 == (xJoueur1 - 5):
                                    xJoueur2, yJoueur2 = 0  # Remise à 0 du joueur 2
                                    scoreJoueur1 += 1

                    if event.key == pygame.K_p:  # Joueur 1 frappe
                        if yJoueur1 == yJoueur2:  # si les joueurs sont à la même hauteur
                            # Et à portée
                            if sensJoueur2 == 1:
                                if xJoueur1 == (xJoueur2 + 5):
                                    xJoueur1, yJoueur1 = 0  # Remise à 0 du joueur 1
                                    scoreJoueur2 += 1
                            else:
                                if xJoueur1 == (xJoueur2 - 5):
                                    xJoueur1, yJoueur1 = 0  # Remise à 0 du joueur 1
                                    scoreJoueur2 += 1

            # Gérer les chutes et les positions
            # Les plateformes
            if xPlateforme1 < 0:  # si la plateforme est sortie par la gauche
                yPlateforme1 = random.randrange(0, 600)  # on change sa hauteur au hasard
                xPlateforme1 = 800  # et on la renvoie à droite
            else:
                xPlateforme1 += 5  # sinon on la fait avancer

            if xPlateforme2 < 0:  # si la plateforme est sortie par la gauche
                yPlateforme2 = random.randrange(0, 600)  # on change sa hauteur au hasard
                xPlateforme2 = 800  # et on la renvoie à droite
            else:
                xPlateforme2 += 5  # sinon on la fait avancer

            if xPlateforme3 < 0:  # si la plateforme est sortie par la gauche
                yPlateforme3 = random.randrange(0, 600)  # on change sa hauteur au hasard
                xPlateforme3 = 800  # et on la renvoie à droite
            else:
                xPlateforme3 += 5  # sinon on la fait avancer

            if xPlateforme4 < 0:  # si la plateforme est sortie par la gauche
                yPlateforme4 = random.randrange(0, 600)  # on change sa hauteur au hasard
                xPlateforme4 = 800  # et on la renvoie à droite
            else:
                xPlateforme4 += 5  # sinon on la fait avancer

            if xPlateforme2 < 0:  # si la plateforme est sortie par la gauche
                yPlateforme5 = random.randrange(0, 600)  # on change sa hauteur au hasard
                xPlateforme5 = 800  # et on la renvoie à droite
            else:
                xPlateforme5 += 5  # sinon on la fait avancer

            # Les personnages
            # On checke d'abord si ils sont sortis de l'écran
            if yJoueur1 > 800 or xJoueur1 < 0:
                scoreJoueur1 -= 1
                yJoueur1 = 0
                xJoueur1 = 0

            if yJoueur2 > 800 or xJoueur2 < 0:
                scoreJoueur2 -= 1
                yJoueur2 = 0
                xJoueur2 = 0

            plateformesX = [xPlateforme1, xJoueur2, xPlateforme3, xPlateforme4, xPlateforme5]
            plateformesY = [yPlateforme1, yJoueur2, yPlateforme3, yPlateforme4, yPlateforme5]


            # Mettre à jour les images
            gameDisplay.blit(imgJoueur1, (xJoueur1, yJoueur1))
            gameDisplay.blit(imgJoueur2, (xJoueur2, yJoueur2))
            gameDisplay.blit(imgPlateforme, (xPlateforme1, yPlateforme1))
            gameDisplay.blit(imgPlateforme, (xPlateforme2, yPlateforme2))
            gameDisplay.blit(imgPlateforme, (xPlateforme3, yPlateforme3))
            gameDisplay.blit(imgPlateforme, (xPlateforme4, yPlateforme4))
            gameDisplay.blit(imgPlateforme, (xPlateforme5, yPlateforme5))

    def menu(self):
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

            button("Jouer", 150, 450, 100, 50, green, bright_green, gameDisplay, action=self.jouer())
            button("Quitter", 550, 450, 100, 50, red, bright_red, gameDisplay, pygame.QUIT)

            pygame.display.update()
            clock.tick(15)

    def checkMeurtrePersos(self):
        pass

    def compteurDePoints(self, joueur, increment):
        joueur.position_perso['points'] += increment


class Plateforme(object):
    """La classe qui gère les plateformes"""
    # Attributs
    positionX = 0  # La position en X
    positionY = 0  # La position en Y
    vitesse = 0  # La vitesse

    # Méthodes
    def __init__(self, name, posX, posY):
        self.nom = name
        self.position_perso = {'x': posX, 'y': posY}

    def deplacement(self, deplacement):
        """Pour déplacer les plateformes, deplacement en pixel.
        deplacement > 0 ==> vers la droite ; deplacement < 0
        ==> vers la gauche"""
        self.position_plateforme['y'] += deplacement

    def jeu(self):
        pass


class Personnage(object):
    """La classe qui gère les personnages"""
    #  Méthodes

    def __init__(self, name):
        self.nom = name
        self.position_perso = {'nom': self.nom, 'x': 1, 'y': 0, 'sens': 1}

    def deplacementDroite(self):
        self.position_perso['sens'] = 1
        self.position_perso['x'] += 1

    def deplacementGauche(self):
        self.position_perso['sens'] = 0
        self.position_perso['x'] -= 1

    def saut(self):
        self.position_perso['y'] += 5   # très mauvais, à améliorer


class Epee(object):
    """La classe qui gère les épées"""
    #  Attributs

    #  Méthodes
    def __init__(self, name):
        self.nom = name
        self.position_epee = {'nom': self.nom, 'x': maitre.get('x'), 'y': maitre.get('y')}

    def coup(self):
        if maitre.sens == 1:  # si le maître est tourné vers la droite
            self.position_epee['x'] += 1
        else:
            self.position_epee['x'] += 1


class Grappin(object):
    """La classe qui gère les grappins"""

    #  Attributs
    maitre = 0  # Le personnage auquel l'épée est attachée

    def initialisation(self, name, joueur, direction):
        self.nom = name
        self.joueur = joueur
        self.direction = direction
        self.etat = 0
        self.position_grappin = {'x': largeurPerso/2, 'y': hauteurPerso/2}

    def principale(self):
        if self.etat == 0:
            self.lance()

        if self.etat == 1:
            self.tracte()

    def changement(self):
        self.direction = random.randint(0, 8)
        self.position_grappin = {'x': largeurPerso/2, 'y': hauteurPerso/2}

    def principale(self):
        if self.etat == 0:
            self.lance()

        if self.etat == 1:
            self.tracte()

    def changement(self):
        self.direction = random.randint(0, 8)

    def lance(self):
        if self.direction == 0:
            self.position_grappin['y'] += -5
        if self.direction == 1:
            self.position_grappin['y'] += -3
            self.position_grappin['x'] += 3
        if self.direction == 2:
            self.position_grappin['x'] += 5
        if self.direction == 3:
            self.position_grappin['y'] += 3
            self.position_grappin['x'] += 3
        if self.direction == 4:
            self.position_grappin['y'] += 5
        if self.direction == 5:
            self.position_grappin['y'] += 3
            self.position_grappin['x'] += -3
        if self.direction == 6:
            self.position_grappin['x'] += -5
        if self.direction == 5:
            self.position_grappin['y'] += -3
            self.position_grappin['x'] += -3

    def tracte(self):
        distance = math.hypot(self.pisition_grappin['x'], self.pisition_grappin['y']) - 5
        if self.pisition_grappin['y'] - joueur.position_perso['y'] != 0 and self.pisition_grappin['x'] - joueur.position_perso['x'] != 0:
            angle = math.atan(self.pisition_grappin['y'] - joueur.position_perso['y']/self.pisition_grappin['x'] - joueur.position_perso['x'])
        else:
            if self.pisition_grappin['y'] - joueur.position_perso['y'] > 0:
                joueur.position_perso['x'] = distance * math.cos(angle)
                joueur.position_perso['y'] = distance * math.sin(angle)

    def tranche(self):
        self.destroy


# Du test
test = Univers()
test.menu()
# Du test
