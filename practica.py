from cv2 import circle
from manim import *
class ExmaplesScene(Scene):
    def construct(self):
        triangulo=Triangle(color=RED)
        circle=Circle(color=GREEN)
        triangulo.add(circle)
        triangulo.generate_target()
        triangulo.target.set_height(2)
        self.play(Create(triangulo))
        self.play(
            triangulo.animate.scale(0.5)
        )
        self.play(triangulo.animate.move_to(3*RIGHT))
        self.play(MoveToTarget(triangulo))
        self.wait()