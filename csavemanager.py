import csv

class CSaveManager:
    def __init__(self, filename="resultats.csv"):
        self.__filename = filename
        self.__data = []

    def add(self, date, vitesse, angle, portee, temps, hauteur):
        self.__data.append([date, vitesse, angle, portee, temps, hauteur])

    def save(self):
        with open(self.__filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date","vitesse", "angle", "portee", "temps", "hauteur"])
            writer.writerows(self.__data)
