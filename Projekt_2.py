"""
Projekt_2.py: druhý projekt do Engeto Online Python Akademie.

Author: Petr Podolinský
Email: podolinsky.petr@gmail.com
Discord: Petr P. (podolinsky.petr)

BULLS & COWS (Býci a Krávy)
==============================================================
Tento program simuluje hru Bulls and Cows, ve které uživatel
hádá čtyřciferná čísla a podle úspěšnosti (uhádnutí správné
číslice nebo její pozice) dostává zpětnou vazbu ve formě
bodového ohodnocení "bulls" (býci), pokud uživatel uhodne jak
číslo, tak jeho umístění a/nebo "cows" (krávy), pokud uživatel
uhodne pouze číslo, ale ne jeho umístění.

Na základě celkového počtu pokusů vedoucích k úspěšnému řešení
se uživateli nakonec zobrazí posouzení jeho výkonu včetně
časové náročnosti správného řešení.

Výstupy hry jsou realizovány v češtině, kromě označení
"bulls" a "cows".

"""

import random
import time


def generator_cisla():
    """Vygeneruje čtyřmísné číslo.

    Toto číslo nezačíná nulou a neobsahuje
    duplicitní číslice (použití "set")

    Vstupy - číslice 0-9
    Výstupy - čtyřmístné číslo
    """
    cislice = '0123456789'
    while True:
        cisla = random.sample(cislice, 4)
        if cisla[0] != '0' and len(cisla) == len(set(cisla)):
            cislo = ''.join(cisla)
            return cislo


def odezva(nezname, tip):
    """Hodnocení úspěšnosti během hry.

    Tato funkce počítá 'BULLS and COWS'
    Proměnné:
    nezname - neznámé číslo
    tip - tip uživatele
    """
    bulls = sum(1 for n, t in zip(nezname, tip) if n == t)
    cows = sum(1 for n in nezname if n in tip) - bulls
    return bulls, cows


# Nastavení proměnných
tajne_cislo = generator_cisla()
pokusy = 0
bulls = 0

# Oddělovač ve formě pomlček
oddelovac = 49 * "-"

# Začátek časování
start_time = time.time()

# Přivítání ve hře
print("\nVítejte ve hře!")
print(oddelovac)
print("Vygeneroval jsem pro Tebe náhodné 4místné číslo.")
print("Zahrejme si hru BULLS & COWS (Býci a krávy).")
print(oddelovac)

while True:
    tip_uzivatele = input("Zadejte hádané čtyřmístné číslo: ")
    print(oddelovac)

    # Vyhodnocení požadavků na číslo zadané uživatelem
    if tip_uzivatele[0] == '0':
        print("Číslo nesmí začínat nulou.\n")
    elif len(tip_uzivatele) != 4:
        print("Číslo musí být čtyřmístné.\n")
    elif not tip_uzivatele.isdigit():
        print("Číslo nesmí obsahovat nečíselné znaky.\n")
    elif len(set(tip_uzivatele)) != len(tip_uzivatele):
        print("Číslo nesmí obsahovat duplicity (stejné číslice).\n")
    else:
        pokusy += 1
        bulls, cows = odezva(tajne_cislo, tip_uzivatele)
        print(
            f"Zpětná vazba: {bulls} {'bull' if bulls == 1 else 'bulls'},"
            f"{cows} {'cow' if cows == 1 else 'cows'}."
            )

        # (testovací část kódu - pouze pro účely testování)
        # print(tajne_cislo)

    hodnoceni = {
        "výborně": (
            "Uhádl/a jsi číslo {} v {} pokusu za celkový čas {} sekund. "
            "Úžasný výkon!"
        ),
        "velmi dobře": (
            "Uhádl/a jsi číslo {} ve {} pokusech za celkový čas {} sekund. "
            "Nebylo to vůbec špatné!"
        ),
        "dobře": (
            "Uhádl/a jsi číslo {} v {} pokusech za celkový čas {} sekund. "
            "Je zde stále velký prostor pro zlepšování."
        )
    }

    if bulls == 4:
        end_time = time.time()  # Konec časování
        cas_hry = round(end_time - start_time, 2)  # Výpočet délky hry
        if pokusy == 1:
            print(
                hodnoceni["výborně"].format(tajne_cislo, pokusy, cas_hry)
                )
        elif pokusy <= 4:
            print(
                hodnoceni["velmi dobře"].format(tajne_cislo, pokusy, cas_hry)
                )
        else:
            print(
                hodnoceni["dobře"].format(tajne_cislo, pokusy, cas_hry)
                )
        break

print()
