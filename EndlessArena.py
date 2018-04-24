# -*- coding: utf-8 -*-

# Les imports
import pygame
pygame.init()
# Les variables et fonctions globales

display_width, display_height = 800, 600
#couleurs
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)
pygame.display.set_caption('Endless Arena')
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width,display_height))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac, display, action=None):
    pygame.display.set_caption('Endless Arena')
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        smallText = pygame.font.SysFont("comicsansms",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)

# Les classes
class Univers(object):
    """La classe générale, qui gère l'initialisation, les autres objets et les contrôleurs"""
    # Attributs
    jeu = [] #la seule variable qui va voyager, contient la position de chaque objet sous la forme {nom, x, y}

    # Méthodes
    def __init__(self):
        """ Initialisation """
        pass

    def jouer(self):
        "Jouer une partie"
        pass

    def menu(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            carImg = pygame.image.load('fichiers/images/bg.png')
            gameDisplay.blit(carImg, (0,0))
            largeText = pygame.font.SysFont("comicsansms",115)
            TextSurf, TextRect = text_objects("Endless Arena", largeText)
            TextRect.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)

            button("Jouer",150,450,100,50,green,bright_green, gameDisplay, action=self.jouer())
            button("Quitter",550,450,100,50,red,bright_red, gameDisplay, pygame.QUIT)

            pygame.display.update()
            clock.tick(15)

    def checkChutePersos(self):
        pass

    def checkMeurtrePersos(self):
        pass

    def compteurDePoints(self):
        pass


class Plateforme(object):
    """La classe qui gère les plateformes"""
    #Attributs
    positionX = 0 #La position en X
    positionY = 0 #La position en Y
    vitesse = 0 #La vitesse

    #Méthodes
    def __init__(self, name, posX, posY):
        self.nom = name
        self.position_perso = {'x': posX, 'y': posY}

    def deplacement(self, deplacement):
        """Pour déplacer les plateformes, deplacement en pixel. deplacement > 0 ==> vers la droite ; deplacement < 0 ==> vers la gauche"""
        self.position_plateforme['y'] += deplacement


    def jeu(self):
        pass

class Personnage(object):
    """La classe qui gère les personnages"""
    #Méthodes

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
        self.position_perso['y'] += 5 ##trés mauvais, à améliorer


class Epee(object):
    """La classe qui gère les épées"""
    #Attributs

    #Méthodes
    def __init__(self, name):
        self.nom = name
        self.position_epee = {'nom': self.nom, 'x': maitre.get('x'), 'y': maitre.get('y')}


    def coup(self):
        if maitre.sens == 1 : #si le maître est tourné vers la droite
            self.position_epee['x'] += 1
        else :
            self.position_epee['x'] += 1

class Grappin(object):
    """La classe qui gère les grappins"""

    #Attributs
    maitre =  0 #Le personnage auquel l'épée est attachée


    #Méthodes
    def __init__(self, name, joueur, direction):
        self.nom = name
        self.joueur = joueur
        self.direction = direction
        self.etat = 0
        self.position_grappin = {'x':largeurPerso/2 ,'y':hauteurPerso/2}

    def principale (self):
        if self.etat == 0 :
            self.lance()

        if self.etat = 1 :
            self.tracte()

    def changement(self) :
        self.direction = random.randint(0,8)

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
        if self.pisition_grappin['y'] - joueur.position_perso['y'] != 0 and self.pisition_grappin['x'] - joueur.position_perso['x'] != 0 :
            angle = math.atan(self.pisition_grappin['y'] - joueur.position_perso['y']/ self.pisition_grappin['x'] - joueur.position_perso['x'])
        else :
            if self.pisition_grappin['y'] - joueur.position_perso['y'] > 0 :

        joueur.position_perso['x'] = distance * math.cos(angle)
        joueur.position_perso['y'] = distance * math.sin(angle)

    def tranche(self):
        self.destroy
# Le programme principal


###Du test !!!! branche ajout-menu, gérée par Olivier
#initialisation





test = Univers()
test.menu()
###Du test !!!! branche ajout-menu, gérée par Olivier

#Univers(lesArguments)
