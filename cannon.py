from projectile import CProjectile
from tir import CTir

class CCannon:
    def __init__(self):
        pass

    def fire(self, vitesse, angle):
        projectile = CProjectile(vitesse, angle)
        return CTir(projectile)

# C'est un canon tres simplle, mais pafaitement fonctionnel.
