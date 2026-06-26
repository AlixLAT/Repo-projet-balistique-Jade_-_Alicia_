
from cannon import CCannon
from savemanager import CSaveManager
print("=== SIMULATEUR ===")

cannon = CCannon()
save = CSaveManager()

nb = int(input("Nombre de tirs : "))
date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

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

save.save()

print("\nResultats exportes")
