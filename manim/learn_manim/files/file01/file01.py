from manim import *

class MathEquation(Scene):
    def construct(self):
        # Création de l'équation
        equation1 = MathTex(r" \text{Mq} \quad a^2+b^2+c^2+d^2=ab+bc+cd+da \implies a=b=c=d").shift(UP * 2)
        
        # Écriture de l'équation
        self.play(Write(equation1))
        self.wait(1)
        
        # Déplacement vers le bas
        self.play(equation1.animate.shift(DOWN * 4))
        self.wait(1)
        
        # Remontée de moitié
        self.play(equation1.animate.shift(UP * 2))

        # Déplacement vers la gauche
        self.play(equation1.animate.shift(LEFT * 2))
        self.wait(1)
        
        # Agrandir l'équation avec animation
        self.play(equation1.animate.scale(1.5))
        self.wait(1)
        
        # Déplacement vers la droite
        self.play(equation1.animate.shift(RIGHT * 4))
        self.wait(1)
        
        # Revenir à la taille normale (1/3 pour compenser l'agrandissement ×3)
        self.play(equation1.animate.scale(1/3))
        self.wait(1)
