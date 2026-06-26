import csv

class SaveManager:
    def __init__(self, filename="resultats.csv"):
        self.filename = filename
        self.data = []

    def add(self, vitesse, angle, portee, temps, hauteur):
        self.data.append([vitesse, angle, portee, temps, hauteur])

    def save(self):
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["vitesse", "angle", "portee", "temps", "hauteur"])
            writer.writerows(self.data)