from Cprojectile import CProjectile
from Ctir import CTir

class CCannon:
    def __init__(self):
        pass

    def fire(self, vitesse, angle):
        projectile = CProjectile(vitesse, angle)
        return CTir(projectile)
