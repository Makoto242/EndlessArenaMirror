# -*- coding: utf-8 -*-

# Les imports


# Les variables globales


# Les classes
class Univers:
    """La classe générale, qui gère l'initialisation, les autres objets et les contrôleurs"""
    # Attributs
    jeu = [] #la seule variable qui va voyager, contient la position de chaque objet sous la forme {nom, x, y}
    
    # Méthodes
    def __init__(self):
        """ Initialisation """
        pass
    
    def affichage(self):
        pass
    
    def menus(self):
        pass
    
    def checkChutePersos(self):
        joueurs = [joueur1; joueur2]
        for test in joueurs :
            if test.position_perso['y'] > tailleFenetreY:
                Univers.compteurDePoints(joueurs.index(test), -1)
                test.position_perso['y'] = positionInitialeY
                test.position_perso['x'] = positionInitialeX
    
    def checkMeurtrePersos(self):
        pass
    
    def compteurDePoints(self, joueur, increment):
        joueur.position_perso['points'] += increment

class Plateforme:
    """La classe qui gère les plateformes"""
    
    #Méthodes
    def __init__(self, name, posX, posY):
        self.nom = name
        self.position_perso = {'x': posX, 'y': posY}
    
    def deplacement(self, deplacement):
        """Pour déplacer les plateformes, deplacement en pixel. deplacement > 0 ==> vers la droite ; deplacement < 0 ==> vers la gauche"""
        self.position_plateforme['y'] += deplacement
    

class Personnage:
    """La classe qui gère les personnages"""
    #Attributs
    contrôleur = 0 #le contrôleur auquel il est relié
    positionX = 0 #La position en X
    positionY = 0 #La position en Y
    
    #Méthodes
    def deplacement(self):
        pass
    
    def saut(self):
        pass
    
    def mort(self):
        pass
    

class Epee:
    """La classe qui gère les personnages"""
    #Attributs
    maitre =  0 #Le personnage auquel l'épée est attachée
    
    #Méthodes    
    def coup(self):
        pass
    
    def donneCaseFrappee(self):
        pass

class Grappin:
    """La classe qui gère les personnages"""
    #Attributs
    maitre =  0 #Le personnage auquel l'épée est attachée
    
    #Méthodes
    def __init__(self, name, joueur, direction):
        self.nom = name
        self.joueur = joueur
        self.direction = direction
        self.etat = 0
        self.position_grappin = {'x':largeurPerso/2;,'y':hauteurPerso/2}
    
    def principale (self):
        if self.etat = 0 :
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


#Univers(lesArguments)

