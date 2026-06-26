import math

class CTir:
    def __init__(self, projectile):
        self.projectile = projectile

    def portee(self):
        a = math.radians(self.projectile.angle)
        return (self.projectile.vitesse ** 2 * math.sin(2 * a)) / 9.81

    def temps_vol(self):
        a = math.radians(self.projectile.angle)
        return (2 * self.projectile.vitesse * math.sin(a)) / 9.81

    def hauteur_max(self):
        a = math.radians(self.projectile.angle)
        return (self.projectile.vitesse ** 2 * (math.sin(a) ** 2)) / (2 * 9.81)

# Calcul de la trajectoire et de la porte.
