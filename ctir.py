import math

class CTir:
    def __init__(self, projectile):
        self.__projectile = projectile

    def portee(self):
        a = math.radians(self.__projectile.angle)
        return (self.__projectile.vitesse ** 2 * math.sin(2 * a)) / 9.81

    def temps_vol(self):
        a = math.radians(self.__projectile.angle)
        return (2 * self.__projectile.vitesse * math.sin(a)) / 9.81

    def hauteur_max(self):
        a = math.radians(self.__projectile.angle)
        return (self.__projectile.vitesse ** 2 * (math.sin(a) ** 2)) / (2 * 9.81)

# Calcul de la trajectoire et de la porte.
