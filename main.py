
import datetime
from Ccannon import CCannon
from Csavemanager import CSaveManager
from visualizer import show_visualization

print("=== SIMULATEUR ===")

cannon = CCannon()
save = CSaveManager()

nb = int(input("Nombre de tirs : "))
date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
shots = []

for i in range(nb):

    print("\nTir", i + 1)

    vitesse = float(input("Vitesse : "))
    angle = float(input("Angle : "))

    tir = cannon.fire(vitesse, angle)

    p = tir.portee()
    t = tir.temps_vol()
    h = tir.hauteur_max()

    print("Portte :", round(p, 2))
    print("Temps :", round(t, 2))
    print("Hauteur :", round(h, 2))

    save.add(date, vitesse, angle, p, t, h)
    shots.append({"vitesse": vitesse, "angle": angle, "portee": p, "temps": t, "hauteur": h})

save.save()

print("\nResultats exportes")
show_visualization(shots)
