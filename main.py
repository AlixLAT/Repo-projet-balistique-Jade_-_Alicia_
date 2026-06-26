from cannon import Cannon
from savemanager import SaveManager

print("=== SIMULATOR ===")

cannon = Cannon()
save = SaveManager()

nb = int(input("Nombre de tirs : "))

for i in range(nb):

    print("\nTir", i + 1)

    vitesse = float(input("Vitesse : "))
    angle = float(input("Angle : "))

    tir = cannon.fire(vitesse, angle)

    p = tir.portee()
    t = tir.temps_vol()
    h = tir.hauteur_max()

    print("Portee :", round(p, 2))
    print("Temps :", round(t, 2))
    print("Hauteur :", round(h, 2))

    save.add(vitesse, angle, p, t, h)

save.save()

print("\nResultats exportes")