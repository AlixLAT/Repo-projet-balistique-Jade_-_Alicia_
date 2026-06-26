class CProjectile:
    def __init__(self, vitesse, angle):
        self.__vitesse = vitesse
        self.__angle = angle

    @property
    def vitesse(self):
        return self.__vitesse

    @property
    def angle(self):
        return self.__angle


