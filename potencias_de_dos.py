from manim import *
class PowerTwoScene(Scene):
    def construct(self):
        power_of_two=VGroup(*[
            MathTex('2^{%d}'%n,'=','{:,}'.format(2**n)) for n in range(0,10)
        ])
        self.play(Write(power_of_two[0]))
        for t in power_of_two[1:]:
            self.play(Transform(power_of_two[0],t))
            self.wait(0.5)