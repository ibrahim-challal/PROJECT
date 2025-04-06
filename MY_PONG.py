import turtle as t
# Création de la fenêtre graphique
fenêtre= t.Screen() #screen() => utilisée pour créer une fenêtre graphique (fenêtre d'affichage) où les dessins de la tortue seront affichés
fenêtre.title("PING PONG BY IBRAHIM CHALLAL")
#Configure les dimensions de la fenêtre graphique
fenêtre.setup(width=800,height=600)
fenêtre.tracer(0) #tracer() => pour contrôler la vitesse 
fenêtre.bgcolor("black")
#La création du balle
balle=t.Turtle() #turtle() => pour créer une nouvelle instance
balle.speed(1000000 )
balle.shape("circle") #shape() => pour définir la forme de la tortue lorsqu'elle est affichée sur le canevas graphique. 
balle.color("white") 
balle.shapesize(2) #shapesize() => pour définir la taille de la forme de la tortue
balle.penup() # penup() => pour relever le stylo de la tortue
balle.goto(0,0) #goto() => pour déplacer la tortue à une position spécifique
balle_dx=1
balle_dy= 1
vitesse_balle=0.5



# La création de le ligne au centre
ligne=t.Turtle()
ligne.speed(2)
ligne.shape("square")
ligne.color("white")
ligne.shapesize(24,0.01)
ligne.goto(0,0)


#La création de la première raquette
joueur1=t.Turtle()
joueur1.speed(2)
joueur1.shape("square")
joueur1.shapesize(7,1.2)
joueur1.color("blue")
joueur1.penup()
joueur1.goto(376,10)


#La création de la deuxième raquette
joueur2=t.Turtle()
joueur2.speed(2)
joueur2.shape("square")
joueur2.shapesize(7,1.2)
joueur2.color("red")
joueur2.penup()
joueur2.goto(-383,-10)


#La création du score
score=t.Turtle()
score.speed(2)
score.color("white")
score.penup()
score.goto(0,273)
score.write(" JOUEUR1: 0 & JOUEUR2: 0 ", align="center", font=("courier",14,"normal"))
score.shapesize(100,300)
score.hideturtle() 
J1_score=0
J2_score=0

vitesse_de_jeu=20
en_jeu = False
def demarrer_jeu():
    global en_jeu
    en_jeu = True
#déplacement de la première raquette vers le haut
def J1_dvhaut():
    joueur1.sety(joueur1.ycor()+ vitesse_de_jeu)
#déplacement de la première raquette vers le bas
def J1_dvbas():
    joueur1.sety(joueur1.ycor()- vitesse_de_jeu)   





#déplacement de la deuxième raquette vers le haut
def J2_dvhaut():
    joueur2.sety(joueur2.ycor()+ vitesse_de_jeu)
#déplacement de la deuxième raquette vers le bas
def J2_dvbas():
    joueur2.sety(joueur2.ycor()- vitesse_de_jeu)



fenêtre.onkeypress(demarrer_jeu, "space")
fenêtre.listen() #listen => pour activer l'écoute des événements clavier sur la fenêtre graphique
fenêtre.onkeypress(J1_dvhaut,"w") # onkeypress => pour définir une fonction de rappel qui sera exécutée lorsqu'une touche du clavier est enfoncée
fenêtre.onkeypress(J1_dvbas,"s")
fenêtre.onkeypress(J2_dvhaut,"Up")
fenêtre.onkeypress(J2_dvbas,"Down")





while True:
    fenêtre.update() # update =>  pour mettre à jour l'affichage de la fenêtre graphique
    if not en_jeu:
        continue  # le jeu ne commencera que lorsque l'utilisateur appuiera sur la touche "ESPACE"
    balle.setx(balle.xcor()+ (balle_dx * vitesse_balle)) #setx => pour déplacer la tortue horizontalement
    balle.sety(balle.ycor()+ (balle_dy * vitesse_balle)) #sety => pour déplacer la tortue verticalement

    if (balle.ycor()> 290): #ycor=> pour obtenir les coordonnées y (ORDONNE) 
        balle.sety(290)
        balle_dy*=-1
    if (balle.ycor()< -290):
        balle.sety(-290)
        balle_dy*=-1

    son = "16476.mp3"
    if (balle.xcor() > 370 and balle.xcor() < 380) and (balle.ycor() < joueur1.ycor() + 60 and balle.ycor() > joueur1.ycor() - 60): #xcor=> pour obtenir les coordonnées X (ABSCISSE) 
        balle.setx(370)
        balle_dx *= -1
        winsound.PlaySound(son, winsound.SND_FILENAME)
    if (balle.xcor() < -370 and balle.xcor() > -380) and (balle.ycor() < joueur2.ycor() + 60 and balle.ycor() > joueur2.ycor() - 60):
        balle.setx(-370)
        balle_dx *= -1
        winsound.PlaySound(son, winsound.SND_FILENAME)


    if(balle.xcor()>390):
        balle.goto(0,0)
        balle_dx*=-1
        score.clear()  
        J1_score+=1
        score.write(f" JOUEUR1: {J1_score} & JOUEUR2: {J2_score} ", align="center", font=("courier",14,"normal"))


    if(balle.xcor()<-390):
        balle.goto(0,0)
        balle_dx*=-1   
        score.clear()  #cler() => pour effacer tout ce qui est effectués par la tortue
        J2_score+=1
        score.write(f" JOUEUR1: {J1_score} & JOUEUR2: {J2_score} ", align="center", font=("courier",14,"normal"))