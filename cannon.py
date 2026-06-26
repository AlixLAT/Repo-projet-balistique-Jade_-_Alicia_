from projectile import Projectile
from tir import Tir

class Cannon:
    def __init__(self):
        pass

    def fire(self, vitesse, angle):
        projectile = Projectile(vitesse, angle)
        return Tir(projectile)