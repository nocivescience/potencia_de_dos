from cmath import rect
from tokenize import group
from manim import *
import itertools as it
class PowerTwoScene(Scene):
    CONFIG={
        'colors':[BLUE,RED,GREEN,YELLOW]
    }
    def construct(self):
        power_of_two=VGroup(*[
            MathTex('2^{%d}'%n,'=','{:,}'.format(2**n)) for n in range(0,10)
        ])
        power_of_two.to_edge(UP,buff=0.5)
        colors=it.cycle(self.CONFIG['colors'])
        mob=Dot()
        mob.move_to(np.array([0,0,0]))
        vects=it.cycle(4*[RIGHT]+4*[UP])
        self.play(Write(power_of_two[0]))
        for i,pow_2,vect in zip(it.count(),power_of_two[1:],vects):
            if i==8:
                rect=SurroundingRectangle(mob,color=next(colors))
                group=VGroup(rect,mob)
                two_to_ten=group.copy()
                group.generate_target()
                group.target.scale(0.1)
                group.target.set_fill(YELLOW,1)
                group.target[1].set_stroke(RED,1)
                self.play(Create(rect))
                self.play(MoveToTarget(group))
                self.remove(group)
                mob=rect
                self.add(rect)
            mob.set_color(next(colors))
            m1,m2=mob.copy(),mob.copy()
            group=VGroup(m1,m2)
            group.arrange(vect,buff=SMALL_BUFF)
            group.move_to(np.array([0,0,0]))
            if group.get_width()>12:
                group.set_width(12)
            self.play(
                ReplacementTransform(mob,m1),
                ReplacementTransform(mob.copy(),m2),
                Transform(power_of_two[0],pow_2)
            )
            mob=VGroup(*it.chain(m1,m2))
            
        self.wait()