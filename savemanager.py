import csv

class CSaveManager:
    def __init__(self, filename="resultats.csv"):
        self.filename = filename
        self.data = []

    def add(self, date, vitesse, angle, portee, temps, hauteur):
        self.data.append([date, vitesse, angle, portee, temps, hauteur])

    def save(self):
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date","vitesse", "angle", "portee", "temps", "hauteur"])
            writer.writerows(self.data)

# Gestionnaire de sauvegarde pour les resultats.
