cena_paliwa = 6.50
droga = float(input("Podaj pokonaną drogę w km:"))
spalanie = float(input("Podaj średnie spalanie w litrach na 100km"))

zużycie_paliwa =(droga * spalanie /100)
koszty = (cena_paliwa * zużycie_paliwa)

print("Zużycie paliwa wynosi:", round(zużycie_paliwa, 2), "litry")
print("Szacowane koszty za tą drogę:", round(koszty, 2), "zł")
