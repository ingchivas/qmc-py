import math
import numpy as np

UMA = {
    "H": 1,
    "He": 4,
    "Li": 7,
    "Be": 9,
    "B": 11,
    "C": 12,
    "N": 14,
    "O": 16,
    "F": 19,
    "Ne": 20,
    "Na": 23,
    "Mg": 24,
    "Al": 27,
    "Si": 28,
    "P": 31,
    "S": 32,
    "Cl": 35,
    "Ar": 40,
    "K": 39,
    "Ca": 40,
    "Sc": 45,
    "Ti": 75,
    "V": 51,
    "Cr": 52,
    "Mn": 55,
    "Fe": 56,
    "Co": 59,
    "Ni": 59,
    "Cu": 64,
    "Zn": 65,
    "Ga": 70,
    "Ge": 73,
    "As": 75,
    "Se": 79,
    "Br": 80,
    "Kr": 84,
    "Rb": 85,
    "Sr": 88,
    "Y": 89,
    "Zr": 91,
    "Nb": 93,
    "Mo": 96,
    "Tc": 98,
    "Ru": 101,
    "Rh": 102,
    "Pd": 106,
    "Ag": 108,
    "Cd": 112,
    "In": 115,
    "Sn": 119,
    "Sb": 122,
    "Te": 128,
    "I": 127,
    "Xe": 131,
    "Cs": 133,
    "Ba": 137,
    "La": 139,
    "Ce": 140,
    "Pr": 141,
    "Nd": 144,
    "Pm": 147,
    "Sm": 150,
    "Eu": 152,
    "Gd": 157,
    "Tb": 159,
    "Dy": 163,
    "Ho": 165,
    "Er": 167,
    "Tm": 169,
    "Yb": 173,
    "Lu": 175,
    "Hf": 179,
    "Ta": 181,
    "W": 184,
    "Re": 186,
    "Os": 190,
    "Ir": 192,
    "Pt": 195,
    "Au": 197,
    "Hg": 201,
    "Tl": 204,
    "Pb": 207,
    "Bi": 209,
    "Po": 210,
    "At": 210,
    "Rn": 222,
    "Fr": 223,
    "Ra": 226,
    "Ac": 227,
    "Th": 232,
    "Pa": 231,
    "U": 238,
    "Np": 237,
    "Pu": 242,
    "Am": 293,
    "Cm": 247,
    "Bk": 247,
    "Cf": 251,
    "Es": 254,
    "Fm": 257,
    "Md": 258,
    "No": 259,
    "Lr": 262,
    "Rf": 261,
    "Ha": 262,
    "Nt": 263,
    "Gp": 264,
    "Hr": 265,
    "Wl": 266,
    "Mv": 269,
    "Pl": 272,
    "Da": 270,
    "Tf": 272,
    "Eo": 276,
    "Me": 279,
    "Nc": 282,
    "El": 286,
    "On": 288
}
Z = {
    "H": 1,
    "He": 2,
    "Li": 3,
    "Be": 4,
    "B": 5,
    "C": 6,
    "N": 7,
    "O": 8,
    "F": 9,
    "Ne": 10,
    "Na": 11,
    "Mg": 12,
    "Al": 13,
    "Si": 14,
    "P": 15,
    "S": 16,
    "Cl": 17,
    "Ar": 18,
    "K": 19,
    "Ca": 20,
    "Sc": 21,
    "Ti": 22,
    "V": 23,
    "Cr": 24,
    "Mn": 25,
    "Fe": 26,
    "Co": 27,
    "Ni": 28,
    "Cu": 29,
    "Zn": 30,
    "Ga": 31,
    "Ge": 32,
    "As": 33,
    "Se": 34,
    "Br": 35,
    "Kr": 36,
    "Rb": 37,
    "Sr": 38,
    "Y": 39,
    "Zr": 40,
    "Nb": 41,
    "Mo": 42,
    "Tc": 43,
    "Ru": 44,
    "Rh": 45,
    "Pd": 46,
    "Ag": 47,
    "Cd": 48,
    "In": 49,
    "Sn": 50,
    "Sb": 51,
    "Te": 52,
    "I": 53,
    "Xe": 54,
    "Cs": 55,
    "Ba": 56,
    "La": 57,
    "Ce": 58,
    "Pr": 59,
    "Nd": 60,
    "Pm": 61,
    "Sm": 62,
    "Eu": 63,
    "Gd": 64,
    "Tb": 65,
    "Dy": 66,
    "Ho": 67,
    "Er": 68,
    "Tm": 69,
    "Yb": 70,
    "Lu": 71,
    "Hf": 72,
    "Ta": 73,
    "W": 74,
    "Re": 75,
    "Os": 76,
    "Ir": 77,
    "Pt": 78,
    "Au": 79,
    "Hg": 80,
    "Tl": 81,
    "Pb": 82,
    "Bi": 83,
    "Po": 84,
    "At": 85,
    "Rn": 86,
    "Fr": 87,
    "Ra": 88,
    "Ac": 89,
    "Th": 90,
    "Pa": 91,
    "U": 92,
    "Np": 93,
    "Pu": 94,
    "Am": 95,
    "Cm": 96,
    "Bk": 97,
    "Cf": 98,
    "Es": 99,
    "Fm": 100,
    "Md": 101,
    "No": 102,
    "Lr": 103,
    "Rf": 104,
    "Ha": 105,
    "Nt": 106,
    "Gp": 107,
    "Hr": 108,
    "Wl": 109,
    "Mv": 110,
    "Pl": 111,
    "Da": 112,
    "Tf": 113,
    "Eo": 114,
    "Me": 115,
    "Nc": 116,
    "El": 117,
    "On": 118
}
ELEMENTOS = {}
COMPUESTOS = {}
reactivos = []
productos = []

GrupoA = [
    "H", "Li", "Na", "K", "Rb", "Cs", "Fr", "Be", "Mg", "Ca", "Sr", "Ba", "Ra",
    "B", "Al", "Ga", "In", "Tl", "Tf", "C", "Si", "Ge", "Sn", "Pb", "Eo", "N",
    "P", "As", "Sb", "Bi", "Me", "O", "S", "Se", "Te", "Po", "Nc", "F", "Cl",
    "Br", "I", "At", "El", "He", "Ne", "Ar", "Kr", "Xe", "Rn", "On"
]
GrupoB = [
    "Sc", "Y", "La", "Ac", "Ti", "Zr", "Hf", "Rf", "V", "Nb", "Ta", "Ha", "Cr",
    "Mo", "W", "Nt", "Mn", "Tc", "Re", "Gp", "Fe", "Ru", "Os", "Hr", "Co",
    "Rh", "Ir", "Wl", "Ni", "Pd", "Pt", "Mv", "Cu", "Ag", "Au", "Pl", "Zn",
    "Cd", "Hg", "Da", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy",
    "Ho", "Er", "Tm", "Yb", "Lu", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm",
    "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"
]

fam1 = ["H", "Li", "Na", "K", "Rb", "Cs", "Fr"]
fam2 = ["Be", "Mg", "Ca", "Sr", "Ba", "Ra"]
fam3 = ["B", "Al", "Ga", "In", "Tl", "Tf"]
fam4 = ["C", "Si", "Ge", "Sn", "Pb", "Eo"]
fam5 = ["N", "P", "As", "Sb", "Bi", "Me"]
fam6 = ["O", "S", "Se", "Te", "Po", "Nc"]
fam7 = ["F", "Cl", "Br", "I", "At", "El"]
fam8 = ["He", "Ne", "Ar", "Kr", "Xe", "Rn", "On"]
fam3B = ["Sc", "Y", "La", "Ac"]
fam4B = ["Ti", "Zr", "Hf", "Rf"]
fam5B = ["V", "Nb", "Ta", "Ha"]
fam6B = ["Cr", "Mo", "W", "Nt"]
fam7B = ["Mn", "Tc", "Re", "Gp"]
fam8B = ["Fe", "Ru", "Os", "Hr"]
fam9B = ["Co", "Rh", "Ir", "Wl"]
fam10B = ["Ni", "Pd", "Pt", "Mv"]
fam11B = ["Cu", "Ag", "Au", "Pl"]
fam12B = ["Zn", "Cd", "Hg", "Da"]
Lantanidos = [
    "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm",
    "Yb", "Lu"
]
Actanidos = [
    "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md",
    "No", "Lr"
]
Metales = ["Al", "Ga", "In", "Sn", "Tl", "Pb", "Bi", "Tf", "Eo", "Me", "Nc"]
Metaloides = ["B", "Si", "Ge", "As", "Sb", "Te", "Po", "At"]
Nometales = [
    "C", "N", "O", "F", "P", "S", "Cl", "Se", "Br", "I", "He", "Ne", "Ar",
    "Kr", "Xe", "Rn", "On"
]

moleslist = []
compuestolist = []
molesdicionario = {}
semejante = []
semejante2 = []


def UMA_percentual():
    var = 0
    while var == 0:
        resfinal = []
        resfinal2 = []
        resfinal3 = []
        compuesto = ""
        print(
            "desea conocer el UMA de un elemento (e), de un compuesto(c) o deseas regresar (ex)?"
        )
        x = input()
        if x == "e":
            var1 = 0
            while var1 == 0:
                check = input("Elemento: ")
                res = [i for i in UMA if i == check]
                res1 = res.pop(0)
                res2 = UMA[res1]
                print(res2, "uma")
                ELEMENTOS[res1] = res2
                print("Quieres conocer la uma de otro elemento?")
                w = input()
                if w == "si":
                    resfinal.clear()
                    compuesto = ""
                    pass
                else:
                    print(ELEMENTOS)
                    ELEMENTOS.clear()
                    var1 += 1

        elif x == "c":
            var1 = 0
            while var1 == 0:
                resfinal = []
                resfinal2 = []
                resfinal3 = []
                porcentual = {}
                print("Cuantos elementos tiene tu compuesto?")
                y = int(input())
                if y < 3:
                    for i in range(y):
                        check = input("ingresa el elemento: ")
                        res = [i for i in UMA if i == check]
                        res1 = res.pop()
                        print("¿Cuantos atomos de ese elemento hay?")
                        z = int(input())
                        res2 = UMA[res1] * z
                        resfinal.append(res2)
                        resfinal2.append(check)
                        if z != 1:
                            compuesto = compuesto + check + str(z)
                        else:
                            compuesto += check
                    Mm = sum(resfinal)
                    COMPUESTOS[compuesto] = Mm
                    print("Mm", compuesto, "=", Mm, "g/mol")
                    if y == 2:
                        for i in resfinal:
                            reporcentual = (i / Mm) * 100
                            reporcentual = "%.3f" % reporcentual
                            reporcentual = str(reporcentual) + "%"
                            resfinal3.append(reporcentual)
                        for i in resfinal2:
                            x = resfinal3.pop(0)
                            porcentual[i] = x
                        print(porcentual)

                else:
                    resfinal = []
                    resfinal2 = []
                    resfinal3 = []
                    check = input("ingresa el elemento: ")
                    primer_elemento = [i for i in UMA if i == check]
                    primer_elemento = primer_elemento.pop()
                    primer_valor = UMA[primer_elemento]
                    print("¿Cuantos atomos de ese elemento hay?")
                    n = int(input())
                    primer_valor *= n
                    resfinal2.append(check)
                    resfinal.append(primer_valor)
                    compuesto1 = ""
                    if n != 1:
                        compuesto1 = check + str(n)
                    else:
                        compuesto1 += check
                    print(
                        "Los siguientes elementos se ven afectados por un subindice?"
                    )
                    xa = input()
                    if xa == "no":
                        for i in range(y - 1):
                            check = input("ingresa el siguiente elemento: ")
                            res = [i for i in UMA if i == check]
                            resfinal2.append(check)
                            res1 = res.pop()
                            print("¿Cuantos atomos de ese elemento hay?")
                            z = int(input())
                            res2 = UMA[res1] * z
                            resfinal.append(res2)
                            if z != 1:
                                compuesto = compuesto + check + str(z)
                            else:
                                compuesto += check
                        compuesto3 = compuesto1 + compuesto
                        Mm = sum(resfinal)
                        COMPUESTOS[compuesto3] = Mm
                        print("Mm", compuesto3, "=", Mm, "g/mol")
                        for i in resfinal:
                            reporcentual = (i / Mm) * 100
                            reporcentual = "%.3f" % reporcentual
                            reporcentual = str(reporcentual) + "%"
                            resfinal3.append(reporcentual)
                        for i in resfinal2:
                            x = resfinal3.pop(0)
                            porcentual[i] = x
                        print(porcentual)

                    else:
                        xb = int(input("ingresa el valor del subindice: "))
                        for i in range(y - 1):
                            check = input("ingresa el siguiente elemento: ")
                            res = [i for i in UMA if i == check]
                            res1 = res.pop()
                            resfinal2.append(check)
                            print("¿Cuantos atomos de ese elemento hay?")
                            z = int(input())
                            res2 = UMA[res1] * z * xb
                            resfinal.append(res2)
                            if z != 1:
                                compuesto = compuesto + check + str(z)
                            else:
                                compuesto += check
                        compuesto3 = compuesto1 + "(" + compuesto + ")" + str(
                            xb)
                        Mm = sum(resfinal)
                        COMPUESTOS[compuesto3] = Mm
                        print("Mm", compuesto3, "=", Mm, "g/mol")
                        for i in resfinal:
                            reporcentual = (i / Mm) * 100
                            reporcentual = "%.3f" % reporcentual
                            reporcentual = str(reporcentual) + "%"
                            resfinal3.append(reporcentual)
                        for i in resfinal2:
                            x = resfinal3.pop(0)
                            porcentual[i] = x
                        print(porcentual)
                resfinal.clear()
                print("Quieres conocer la uma de otro compuesto?")
                w = input()
                if w == "si":
                    compuesto = ""
                    pass
                else:
                    print(COMPUESTOS)
                    COMPUESTOS.clear()
                    var1 += 1

        elif x == "ex":
            var += 1


def conservacion_materia():
    var1 = 0
    while var1 == 0:
        resfinal = []
        compuesto = ""
        var = 0
        while var == 0:
            print("Cuantos elementos tiene tu compuesto?")
            y = int(input())
            if y < 3:
                for i in range(y):
                    check = input("ingresa el elemento: ")
                    res = [i for i in UMA if i == check]
                    res1 = res.pop()
                    print("¿Cuantos atomos de ese elemento hay?")
                    z = int(input())
                    res2 = UMA[res1] * z
                    resfinal.append(res2)
                    if z != 1:
                        compuesto = compuesto + check + str(z)
                    else:
                        compuesto += check
                Mm = sum(resfinal)
                COMPUESTOS[compuesto] = Mm
                print("Mm", compuesto, "=", Mm, "g/mol")
                print("Quieres conocer la UMA de otro compuesto?")
                w = input()
                if w == "si":
                    resfinal.clear()
                    compuesto = ""
                    pass
                else:
                    var += 1
            else:
                check = input("ingresa el elemento: ")
                primer_elemento = [i for i in UMA if i == check]
                primer_elemento = primer_elemento.pop()
                primer_valor = UMA[primer_elemento]
                print("¿Cuantos atomos de ese elemento hay?")
                n = int(input())
                primer_valor *= n
                compuesto1 = ""
                if n != 1:
                    compuesto1 = check + str(n)
                else:
                    compuesto1 += check
                print(
                    "Los siguientes elementos se ven afectados por un subindice?"
                )
                xa = input()
                if xa == "no":
                    for i in range(y - 1):
                        check = input("ingresa el siguiente elemento: ")
                        res = [i for i in UMA if i == check]
                        res1 = res.pop()
                        print("¿Cuantos atomos de ese elemento hay?")
                        z = int(input())
                        res2 = UMA[res1] * z
                        resfinal.append(res2)
                        if z != 1:
                            compuesto = compuesto + check + str(z)
                        else:
                            compuesto += check
                    compuesto3 = compuesto1 + compuesto
                    Mm = sum(resfinal) + primer_valor
                    COMPUESTOS[compuesto3] = Mm
                    print("Mm", compuesto3, "=", Mm, "g/mol")
                    print("Quieres conocer la UMA de otro compuesto?")
                    w = input()
                    if w == "si":
                        resfinal.clear()
                        compuesto = ""
                        pass
                    else:
                        var += 1
                else:
                    xb = int(input("ingresa el valor del subindice: "))
                    for i in range(y - 1):
                        check = input("ingresa el siguiente elemento: ")
                        res = [i for i in UMA if i == check]
                        res1 = res.pop()
                        print("¿Cuantos atomos de ese elemento hay?")
                        z = int(input())
                        res2 = UMA[res1] * z * xb
                        resfinal.append(res2)
                        if z != 1:
                            compuesto = compuesto + check + str(z)
                        else:
                            compuesto += check
                    compuesto3 = compuesto1 + "(" + compuesto + ")" + str(xb)
                    Mm = sum(resfinal) + primer_valor
                    COMPUESTOS[compuesto3] = Mm
                    print("Mm", compuesto3, "=", Mm, "g/mol")
                    print("Quieres conocer la UMA de otro compuesto?")
                    w = input()
                    if w == "si":
                        resfinal.clear()
                        compuesto = ""
                        pass
                    else:
                        var += 1

        print(COMPUESTOS)
        print("Cuantos reactivos tienes?")
        r = int(input())
        print("por favor ingresar el reactivo tal cual se ve en la pantalla")
        for i in range(r):
            check = input("ingresa el reactivo: ")
            reac = [i for i in COMPUESTOS if i == check]
            reac2 = reac.pop()
            mol = float(input("Ingresa el numero de moles: "))
            reac3 = COMPUESTOS[reac2] * mol
            reactivos.append(reac3)

        print(COMPUESTOS)
        print("Cuantos productos tienes?")
        p = int(input())
        print("por favor ingresar el producto tal cual se ve en la pantalla")
        for i in range(p):
            check = input("ingresa el producto: ")
            reac = [i for i in COMPUESTOS if i == check]
            reac2 = reac.pop()
            mol = float(input("Ingresa el numero de moles: "))
            reac3 = COMPUESTOS[reac2] * mol
            productos.append(reac3)

        reactives = sum(reactivos)
        products = sum(productos)
        conservacion = reactives == products
        if conservacion == True:
            print(reactives, "g", "=", products, "g")
            print("Se cumple la ley de la conservacion de la materia")
        else:
            print(reactives, "g", "!=", products, "g")
            print("No se cumple la ley de la conservacion de la materia")

        COMPUESTOS.clear()
        productos.clear()
        reactivos.clear()

        print("Quieres comprobar otra reaccion?")
        ax = input()
        if ax == "si":
            pass
        else:
            var += 1
            var1 += 1


def g_to_mol():
    var = 0
    while var == 0:
        resfinal = []
        compuesto = ""
        print("Cuantos elementos tiene tu compuesto?")
        y = int(input())
        if y < 3:
            for i in range(y):
                check = input("ingresa el elemento: ")
                res = [i for i in UMA if i == check]
                res1 = res.pop()
                print("¿Cuantos atomos de ese elemento hay?")
                z = int(input())
                res2 = UMA[res1] * z
                resfinal.append(res2)
                if z != 1:
                    compuesto = compuesto + check + str(z)
                else:
                    compuesto += check
            Mm = sum(resfinal)
            COMPUESTOS[compuesto] = Mm
            print(
                "Quieres conocer los moles (m) o los gramos del compuesto (g)?"
            )
            ax = input()
            if ax == "m":
                print("Cuantos gramos tienes de ese compuesto?")
                m = float(input())
                mol = m / Mm
                mol = "%.3f" % mol
                print("Mm", compuesto, "=", Mm, "g/mol")
                print(mol, "mol", compuesto)
            elif ax == "g":
                print("Cuantos moles tienes del compuesto?")
                mol = float(input())
                m = mol * Mm
                m = "%.3f" % m
                print("Mm", compuesto, "=", Mm, "g/mol")
                print(m, "g", compuesto)

        else:
            resfinal = []
            check = input("ingresa el elemento: ")
            primer_elemento = [i for i in UMA if i == check]
            primer_elemento = primer_elemento.pop()
            primer_valor = UMA[primer_elemento]
            print("¿Cuantos atomos de ese elemento hay?")
            n = int(input())
            primer_valor *= n
            resfinal.append(primer_valor)
            compuesto1 = ""
            if n != 1:
                compuesto1 = check + str(n)
            else:
                compuesto1 += check
            print(
                "Los siguientes elementos se ven afectados por un subindice?")
            xa = input()
            if xa == "no":
                for i in range(y - 1):
                    check = input("ingresa el siguiente elemento: ")
                    res = [i for i in UMA if i == check]
                    res1 = res.pop()
                    print("¿Cuantos atomos de ese elemento hay?")
                    z = int(input())
                    res2 = UMA[res1] * z
                    resfinal.append(res2)
                    if z != 1:
                        compuesto = compuesto + check + str(z)
                    else:
                        compuesto += check
                    compuesto3 = compuesto1 + compuesto
                Mm = sum(resfinal)
                COMPUESTOS[compuesto3] = Mm
                print(
                    "Quieres conocer los moles (m) o los gramos del compuesto (g)?"
                )
                ax = input()
                if ax == "m":
                    print("Cuantos gramos tienes de ese compuesto?")
                    m = float(input())
                    mol = m / Mm
                    mol = "%.3f" % mol
                    print("Mm", compuesto3, "=", Mm, "g/mol")
                    print(mol, "mol", compuesto3)
                elif ax == "g":
                    print("Cuantos moles tienes del compuesto?")
                    mol = float(input())
                    m = mol * Mm
                    m = "%.3f" % m
                    print("Mm", compuesto3, "=", Mm, "g/mol")
                    print(m, "g", compuesto3)

            else:
                xb = int(input("ingresa el valor del subindice: "))
                for i in range(y - 1):
                    check = input("ingresa el siguiente elemento: ")
                    res = [i for i in UMA if i == check]
                    res1 = res.pop()
                    print("¿Cuantos atomos de ese elemento hay?")
                    z = int(input())
                    res2 = UMA[res1] * z * xb
                    resfinal.append(res2)
                    if z != 1:
                        compuesto = compuesto + check + str(z)
                    else:
                        compuesto += check
                compuesto3 = compuesto1 + "(" + compuesto + ")" + str(xb)
                Mm = sum(resfinal)
                COMPUESTOS[compuesto3] = Mm
                print(
                    "Quieres conocer los moles (m) o los gramos del compuesto (g)?"
                )
                ax = input()
                if ax == "m":
                    print("Cuantos gramos tienes de ese compuesto?")
                    m = float(input())
                    mol = m / Mm
                    mol = "%.3f" % mol
                    print("Mm", compuesto3, "=", Mm, "g/mol")
                    print(mol, "mol", compuesto3)
                elif ax == "g":
                    print("Cuantos moles tienes del compuesto?")
                    mol = float(input())
                    m = mol * Mm
                    m = "%.3f" % m
                    print("Mm", compuesto3, "=", Mm, "g/mol")
                    print(m, "g", compuesto3)

        resfinal.clear()
        print("Quieres conocer los moles de otro compuesto?")
        w = input()
        if w == "si":
            compuesto = ""
            pass
        else:
            print(COMPUESTOS)
            COMPUESTOS.clear()
            var += 1


def conf_electric():
    var1 = 0
    confi = ""
    while var1 == 0:
        niveles = [
            1, 2, 2, 3, 3, 4, 3, 4, 5, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 6, 7, 7
        ]
        orbitales = [
            "s", "s", "p", "s", "p", "s", "d", "p", "s", "d", "p", "s", "f",
            "d", "p", "s", "f", "d", "p", "f", "d", "f"
        ]
        orden = [
            2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6, 14,
            10, 14
        ]
        check = input("Elemento: ")
        res = [i for i in Z if i == check]
        res1 = res.pop(0)
        res2 = Z[res1]
        res2a = res2
        res3 = UMA[res1]
        protones = res2
        electrones = protones
        neutrones = res3 - protones
        if check in fam1:
            while res2 >= 2:
                x = orden.pop(0)
                res2 -= x
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(x) + ","
            n = niveles.pop(0)
            y = orbitales.pop(0)
            confi = confi + str(n) + y + str(1)
            orbitals = "s"
            valencia = 1
            numo = "+1"
            fam = "I"
            nombrefam = "Metales alcalinos"
            clase = "Metal"

        if check in fam2:
            while res2 > 2:
                x = orden.pop(0)
                res2 -= x
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(x) + ","
            n = niveles.pop(0)
            y = orbitales.pop(0)
            confi = confi + str(n) + y + str(2)
            orbitals = "s"
            valencia = 2
            numo = "+2"
            fam = "II"
            nombrefam = "Metal alcalino-terreo"
            clase = "Metal"

        if check in fam3:
            while res2 >= 2:
                x = orden.pop(0)
                res2 -= x
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(x) + ","
            n = niveles.pop(0)
            y = orbitales.pop(0)
            confi = confi + str(n) + y + str(1)
            orbitals = "s,p"
            valencia = 3
            numo = "+3"
            if res2a > 80:
                numo = "+1,+3"
            else:
                pass
            fam = "III"
            nombrefam = "Familia del Boro o Terreos"

        if check in fam4:
            while res2 >= 3:
                x = orden.pop(0)
                res2 -= x
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(x) + ","
            n = niveles.pop(0)
            y = orbitales.pop(0)
            confi = confi + str(n) + y + str(2)
            orbitals = "s,p"
            valencia = 4
            if res2a == 6 or res2a == 14:
                numo = "+2,+-2"
            elif res2a > 14 and res2a < 114:
                numo = "+2,+4"
            else:
                numo = "+2,+4,+6"
            fam = "IV"
            nombrefam = "Familia del carbono o Carbonoides"

        if check in fam5:
            while res2 >= 4:
                x = orden.pop(0)
                res2 -= x
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(x) + ","
            n = niveles.pop(0)
            y = orbitales.pop(0)
            confi = confi + str(n) + y + str(3)
            orbitals = "s,p"
            valencia = 5
            if res2a == 7:
                numo = "+-1,+-2,+-3,+4,+5"
            elif res2a == 15:
                numo = "+-3,+4,+-5"
            elif res2a == 33 or res2a == 51:
                numo = "+-3,+5"
            elif res2a == 83:
                numo = "-3,+5"
            else:
                numo = "+1,+4,+5"
            fam = "V"
            nombrefam = "Familia del Nitrogeno o Nitrogenoides"

        if check in fam6:
            while res2 >= 5:
                x = orden.pop(0)
                res2 -= x
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(x) + ","
            n = niveles.pop(0)
            y = orbitales.pop(0)
            confi = confi + str(n) + y + str(4)
            orbitals = "s,p"
            valencia = 6

            if res2a == 8:
                numo = "-1,-2"
            elif res2a == 16 or res2a == 52:
                numo = "+-2,+4,+6"
            elif res2a == 34:
                numo = "-2,+-4,+6"
            elif res2a == 84:
                numo = "+-2,+4,+6"
            else:
                numo = "+3,+4,+5"
            fam = "VI"
            nombrefam = "Familia del Oxigeno o Calcogenos"

        if check in fam7:
            while res2 >= 6:
                x = orden.pop(0)
                res2 -= x
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(x) + ","
            n = niveles.pop(0)
            y = orbitales.pop(0)
            confi = confi + str(n) + y + str(5)
            orbitals = "s,p"
            valencia = 7
            if res2a == 9:
                numo = "-1"
            elif res2a < 85:
                numo = "+-1,+3,+5,+7"
            elif res2a == 85:
                numo = "+-1,+5"
            else:
                numo == "+1,+2,+3"
            fam = "VII"
            nombrefam = "Halogenos"

        if check == "He":
            confi = confi + "1s2"
            n = 1
            orbitals = "s"
            valencia = 2
            numo = "no tiene"
            fam = "VIII"
            nombrefam = "Gases nobles"

        if check in fam8 and check != "He":
            while res2 >= 8:
                x = orden.pop(0)
                res2 -= x
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(x) + ","
            n = niveles.pop(0)
            y = orbitales.pop(0)
            confi = confi + str(n) + y + str(6)
            orbitals = "s,p"
            valencia = 8
            numo = "no tiene"
            fam = "VIII"
            nombrefam = "Gases nobles"

        if check in fam3B:
            if res2 < 57:
                while res2 >= 3:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(1)

            else:
                while res2 >= 3:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                n += 1
                y = orbitales.pop(0)
                confi = confi + str(n) + "d" + str(1)
            orbitals = "s"
            n += 1
            valencia = 2
            numo = "+3"
            fam = "III"
            nombrefam = "Familia del Escandio (tierras raras y actinidos)"

        if check in fam4B:
            if res2 < 104:
                while res2 >= 3:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + "d" + str(2)

            elif res2 == 104:
                while res2 >= 3:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + "d" + str(1)
            n += 1
            orbitals = "s"
            valencia = 2
            if check == "Ti":
                numo = "+3"
            else:
                numo = "+3,+4"
            fam = "IV"
            nombrefam = "Famillia del Titanio"

        if check in fam5B:
            while res2 >= 5:
                x = orden.pop(0)
                res2 -= x
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(x) + ","
            if res2a == 23 or res2a == 73:
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + "d" + str(3)
            elif res2a == 41:
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + "d" + str(4)
            elif res2a == 105:
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + "d" + str(1)
            n += 1
            orbitals = "s"
            valencia = 2
            if res2a < 73:
                numo = "+2,+3,+4,+5"
            elif res2a == 73:
                numo = "+3,+4,+5"
            else:
                numo = "?"
            fam = "V"
            nombrefam = "Famillia del Vanadio"

        if check in fam6B:
            while res2 >= 7:
                x = orden.pop(0)
                res2 -= x
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(x) + ","
            if res2a == 24 or res2a == 42:
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + "s" + str(1) + "," + str(
                    n - 1) + "d" + str(5)
                orbitals = "s"
                valencia = 1
            if res2a == 74 or res2a == 106:
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(4)
                n += 1
                orbitals = "s"
                valencia = 2

            if res2a < 106 and res2a > 24:
                numo = "+2,+3,+4,+5,+6"
            elif res2a == 24:
                numo = "+2,+3,+6"
            else:
                numo = "?"
            fam = "VI"
            nombrefam = "Famillia del Cromo"

        if check in fam7B:
            if check != "Gp":
                while res2 >= 7:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","

                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(5)

            elif check == "Gp":
                while res2 >= 20:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","

                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(10) + "," + str(
                    n + 1) + "d" + str(2)

            n += 1
            orbitals = "s"
            valencia = 2
            if check == "Mn":
                numo = "+2,+3,+4,+6,+7"
            elif check == "Tc":
                numo = "+4,+5,+6,+7"
            elif check == "Re":
                numo = "+2,+3,(+4,+6,+7)"
            fam = "VII"
            nombrefam = "Famillia del Manganeso"

        if check in fam8B:
            if res2a == 26 or res2a == 76:
                while res2 >= 7:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","

                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(6)

                n += 1
                orbitals = "s"
                valencia = 2

            elif res2a == 44:
                while res2 >= 12:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","

                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(1) + "," + str(
                    n - 1) + "d" + str(7)
                orbitals = "s"
                valencia = 1

            elif res2a == 108:
                while res2 >= 12:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","

                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(6)
                orbitals = "s"
                valencia = 2
                n = 7

            if res2a == 26:
                numo = "+2,+3"
            elif res2a > 26 and res2a < 108:
                numo = "+2,+3,+4,+5,+6,+7"
            elif res2a == 108:
                numo = "?"
            fam = "VIII"
            nombrefam = "Famillia del Hierro"

        if check in fam9B:
            if res2a == 27 or res2a == 77:
                while res2 >= 8:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(7)
                n += 1
                valencia = 2

            if res2a == 45:
                while res2 >= 12:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(1) + "," + str(
                    n - 1) + "d" + str(8)
                n = 5
                valencia = 1

            if res2a == 109:
                while res2 >= 12:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(6)
                n = 7
                valencia = 2
                numo = "?"
                fam = "VIII"

            if res2a == 27:
                numo = "+2,+3"
            elif res2a == 45 or res2a == 77:
                numo = "+2,+3,+4,+5,+6"
            else:
                pass
            nombrefam = "Famillia del Cobalto"

        if check in fam10B:
            if res2a == 28:
                while res2 >= 10:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(8)
                n += 1
                valencia = 2
                orbitals = "s"

            if res2a == 46:
                while res2 >= 16:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(0) + "," + str(
                    n - 1) + "d" + str(10)
                n = 5
                valencia = 18
                orbitals = "s,p,d"

            if res2a == 78:
                while res2 >= 28:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(1) + "," + str(
                    n - 2) + "f" + str(14) + "," + str(5) + "d" + str(9)
                n = 6
                valencia = 1
                orbitals = "s"

            if res2a == 110:
                while res2 >= 20:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(8)
                n = 7
                valencia = 2
                orbitals = "s"
                numo = "?"

            if res2a == 28:
                numo = "+2,+3"
            elif res2a == 46 or res2a == 78:
                numo = "+2,+4"
            else:
                pass
            fam = "VIII"
            nombrefam = "Famillia del Niquel"

        if check in fam11B:
            if res2a == 29 or res2a == 47:
                while res2 >= 14:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(1) + "," + str(
                    n - 1) + "d" + str(10)

            elif res2a == 79:
                while res2 >= 28:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(1) + "," + str(
                    n - 2) + "f" + str(14) + "," + str(n - 1) + "d" + str(10)
            valencia = 1
            orbitals = "s"

            if res2a == 111:
                while res2 >= 12:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(9)
                valencia = 2
                n += 1
                orbitals = "s"

            if res2a == 29:
                numo = "+1,+2"
            elif res2a == 46:
                numo = "+1"
            elif res2a == 79:
                numo = "+1,+3"
            else:
                numo = "?"
            fam = "I"
            nombrefam = "Famillia del Cobre"

        if check in fam12B:
            while res2 >= 12:
                x = orden.pop(0)
                res2 -= x
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(x) + ","
            n = niveles.pop(0)
            y = orbitales.pop(0)
            confi = confi + str(n) + y + str(10)
            valencia = 2
            n += 1
            orbitals = "s"
            if res2a == 30:
                numo = "+2"
            elif res2a == 47:
                numo = "+2"
            elif res2a == 80:
                numo = "+1,+2"
            else:
                numo = "?"
            fam = "II"
            nombrefam = "Famillia del Zinc"

        if check in Lantanidos:
            numo = "?"
            if res2a == 58:
                while res2 >= 3:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(1) + "," + str(
                    n + 1) + "d" + str(1)

            elif res2a == 59 or res2a == 60:
                while res2 >= 5:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 59:
                    x = 3
                elif res2a == 60:
                    x = 4
                confi = confi + str(n) + y + str(x)

            elif res2a == 61 or res2a == 62:
                while res2 >= 7:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 61:
                    x = 5
                if res2a == 62:
                    x = 6
                confi = confi + str(n) + y + str(x)

            elif res2a == 63:
                while res2 >= 8:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                confi = confi + str(n) + y + str(7)

            elif res2a == 64 or res2a == 65:
                while res2 >= 10:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 64:
                    confi = confi + str(n) + y + str(7) + "," + str(
                        n + 1) + "d" + str(1)
                elif res2a == 65:
                    confi = confi + str(n) + y + str(9)

            elif res2a == 66 or res2a == 67:
                while res2 >= 12:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 66:
                    confi = confi + str(n) + y + str(10)
                elif res2a == 67:
                    confi = confi + str(n) + y + str(11)

            elif res2a == 68 or res2a == 69:
                while res2 >= 14:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 68:
                    confi = confi + str(n) + y + str(12)
                elif res2a == 69:
                    confi = confi + str(n) + y + str(13)

            elif res2a == 70 or res2a == 71:
                while res2 >= 16:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 70:
                    confi = confi + str(n) + y + str(14)
                elif res2a == 71:
                    confi = confi + str(n) + y + str(14) + "," + str(
                        5) + "d" + str(1)
            valencia = 2
            n = 6
            orbitals = "s"
            fam = "Lantanidos"

        if check in Actanidos:
            numo = "?"
            if res2a == 90:
                while res2 >= 4:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                confi = confi + str(6) + "d" + str(2)

            elif res2a == 91:
                while res2 >= 4:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 91:
                    confi = confi + str(n) + y + str(2) + "," + str(
                        6) + "d" + str(1)

            elif res2a == 92 or res2a == 93:
                while res2 >= 6:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 92:
                    confi = confi + str(n) + y + str(3) + "," + str(
                        6) + "d" + str(1)
                elif res2a == 93:
                    confi = confi + str(n) + y + str(4) + "," + str(
                        6) + "d" + str(1)

            elif res2a == 94 or res2a == 95:
                while res2 >= 8:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 94:
                    confi = confi + str(n) + y + str(6)
                elif res2a == 95:
                    confi = confi + str(n) + y + str(7)

            elif res2a == 96 or res2a == 97:
                while res2 >= 10:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 96:
                    confi = confi + str(n) + y + str(7) + "," + str(
                        6) + "d" + str(1)
                elif res2a == 97:
                    confi = confi + str(n) + y + str(9)

            elif res2a == 98 or res2a == 99:
                while res2 >= 12:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 98:
                    confi = confi + str(n) + y + str(10)
                elif res2a == 99:
                    confi = confi + str(n) + y + str(11)

            elif res2a == 100 or res2a == 101:
                while res2 >= 14:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 100:
                    confi = confi + str(n) + y + str(12)
                elif res2a == 101:
                    confi = confi + str(n) + y + str(13)

            valencia = 2
            orbitals = "s"
            if res2a == 102 or res2a == 103:
                while res2 >= 16:
                    x = orden.pop(0)
                    res2 -= x
                    n = niveles.pop(0)
                    y = orbitales.pop(0)
                    confi = confi + str(n) + y + str(x) + ","
                n = niveles.pop(0)
                y = orbitales.pop(0)
                if res2a == 102:
                    confi = confi + str(n) + y + str(14)
                elif res2a == 103:
                    confi = confi + str(n) + y + str(14) + "," + str(
                        7) + "p" + str(1)
                valencia = 3
                orbitals = "s,p"

            n = 7
            fam = "Actinidos"

        if check in GrupoA:
            grupo = "Grupo: A"
        elif check in GrupoB:
            grupo = "Grupo: B"
            clase = "metales de transicion"

        if orbitals == "s":
            l = 0
            forma = "esferica"
        elif orbitals == "s,p":
            l = "0,1"
            forma = "esferica,dilobular"

        if l == 0:
            m = "0"
        elif l == "0,1":
            m = "0", "-1,0,1"

        if check in Metales:
            clase = "Metal"
        elif check in GrupoB:
            clase = "Metal de transicion"
        elif check in Nometales or check == "H":
            clase = "No metal"
        elif check in Metaloides:
            clase = "Metaloide"
        elif check == "El" or check == "On":
            clase = " "

        if check in Lantanidos or check in Actanidos:
            print("Z =", res2a, "|", res3, "uma", "|", "e- =", electrones, "|",
                  "p+ =", protones, "|", "n+- =", neutrones, "|", fam)
        if check == "On" or check == "El":
            print("Z =", res2a, "|", res3, "uma", "|", "e- =", electrones, "|",
                  "p+ =", protones, "|", "n+- =", neutrones, "|", grupo, "|",
                  "familia :", fam, "|", nombrefam)
        else:
            print("Z =", res2a, "|", res3, "uma", "|", "e- =", electrones, "|",
                  "p+ =", protones, "|", "n+- =", neutrones, "|", grupo, "|",
                  "familia :", fam, "|", nombrefam, "|", clase)
        print(protones, "+", neutrones, "=", res3, "uma")
        print(confi)
        print("n =", n, "|", "l =", l, "|", "ultimo orbital =", orbitals, "|",
              "forma:", forma, "|", "v =", valencia, "|", "num oxidacion =",
              numo)
        print("m =", m)
        print("Quieres conocer las caracteristicas quimicas de otro elemento?")
        w = input()
        if w == "si":
            confi = ""
            pass
        else:
            var1 += 1


def Ley_Boyle():
    print(
        "La ley de Boyle situa un gas a temperatura constante, pero un cambio en la presion-volumen"
    )
    var = 0
    while var == 0:
        print(
            "Quieres conocer la presion1 (p1), el volumen1 (v1), la presion (p2) o el volumen (v2)?"
        )
        x = input()
        if x == "p1":
            v1 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v1 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v1 *= 1000
            elif z == 4:
                v1 /= 1000
            p2 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p2 /= 101, 300
            elif y == 2:
                pass
            else:
                p2 /= 760
            v2 = float(input("ingresa el valor del volumen2: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v2 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v2 *= 1000
            elif z == 4:
                v2 /= 1000
            p1 = (p2 * v2) / v1
            p1v1 = p1 * v1
            p2v2 = p2 * v2
            print(p1, "atm")
            print(p1v1, "atm*L", "=", p2v2, "atm*L")

        elif x == "v1":
            p1 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p1 /= 101, 300
            elif y == 2:
                pass
            else:
                p1 /= 760
            p2 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p2 /= 101, 300
            elif y == 2:
                pass
            else:
                p2 /= 760
            v2 = float(input("ingresa el valor del volumen2: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v2 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v2 *= 1000
            elif z == 4:
                v2 /= 1000
            v1 = (p2 * v2) / p1
            p1v1 = p1 * v1
            p2v2 = p2 * v2
            print(v1, "L")
            print(p1v1, "atm*L", "=", p2v2, "atm*L")

        elif x == "v2":
            p1 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p1 /= 101, 300
            elif y == 2:
                pass
            else:
                p1 /= 760
            v1 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v1 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v1 *= 1000
            elif z == 4:
                v1 /= 1000
            p2 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p2 /= 101, 300
            elif y == 2:
                pass
            else:
                p2 /= 760
            v2 = (p1 * v1) / p2
            p1v1 = p1 * v1
            p2v2 = p2 * v2
            print(v2, "L")
            print(p1v1, "atm*L", "=", p2v2, "atm*L")

        else:
            p1 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p1 /= 101, 300
            elif y == 2:
                pass
            else:
                p1 /= 760
            v1 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v1 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v1 *= 1000
            elif z == 4:
                v1 /= 1000
            v2 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v2 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v2 *= 1000
            elif z == 4:
                v2 /= 1000
            p2 = (p1 * v1) / v2
            p1v1 = p1 * v1
            p2v2 = p2 * v2
            print(p2, "atm")
            print(p1v1, "atm*L", "=", p2v2, "atm*L")

        print("¿Quieres conocer otra presion o volumen?")
        ax = input()
        if ax == "si":
            pass
        else:
            var += 1


def Ley_Lussac():
    print(
        "La ley de Lussac situa un gas a volumen constante, pero un cambio en la presion-temperatura"
    )
    var = 0
    while var == 0:
        print(
            "Quieres conocer la presion1 (p1), la temperatura1 (t1), la presion2 (p2) o la temperaura2 (t2)?"
        )
        x = input()
        if x == "p1":
            t1 = float(input("ingresa el valor de la temperatura1: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t1 += 273
            elif zz == 2:
                t1 = (((t1 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            p2 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p2 /= 101, 300
            elif y == 2:
                pass
            else:
                p2 /= 760
            t2 = float(input("ingresa el valor de la temperatura2: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t2 += 273
            elif zz == 2:
                t2 = (((t2 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            p1 = (p2 / t2) * t1
            p1 = "%.3f" % p1
            print(p1, "atm")

        elif x == "t1":
            p1 = float(input("ingresa el valor de la presion1: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p1 /= 101, 300
            elif y == 2:
                pass
            else:
                p1 /= 760
            p2 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p2 /= 101, 300
            elif y == 2:
                pass
            else:
                p2 /= 760
            t2 = float(input("ingresa el valor de la temperatura2: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t2 += 273
            elif zz == 2:
                t2 = (((t2 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            t1 = (p1 * t2) / p2
            t1 = "%.3f" % t1
            print(t1, "K")

        elif x == "p2":
            p1 = float(input("ingresa el valor de la presion1: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p1 /= 101, 300
            elif y == 2:
                pass
            else:
                p1 /= 760
            t1 = float(input("ingresa el valor de la temperatura1: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t1 += 273
            elif zz == 2:
                t1 = (((t1 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            t2 = float(input("ingresa el valor de la temperatura2: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t2 += 273
            elif zz == 2:
                t2 = (((t2 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            p2 = (p1 * t2) / t1
            p2 = "%.3f" % p2
            print(p2, "atm")

        elif x == "t2":
            p1 = float(input("ingresa el valor de la presion1: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p1 /= 101, 300
            elif y == 2:
                pass
            else:
                p1 /= 760
            t1 = float(input("ingresa el valor de la temperatura1: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t1 += 273
            elif zz == 2:
                t1 = (((t1 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            p2 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p2 /= 101, 300
            elif y == 2:
                pass
            else:
                p2 /= 760
            t2 = (p2 * t1) / p1
            t2 = "%.3f" % t2
            print(t2, "K")

        p1entret1 = float(p1) / float(t1)
        p2entret2 = float(p2) / float(t2)
        p1entret1 = "%.4f" % p1entret1
        p2entret2 = "%.4f" % p2entret2
        print(p1entret1, "atm/K", "=", p2entret2, "atm/K")
        print("Quieres conocer otra presion o temperatura?")
        ax = input()
        if ax == "si":
            pass
        else:
            var += 1


def Ley_Charles():
    print(
        "La ley de Charles situa un gas a presion constante, pero un cambio en el volumen-temperatura"
    )
    var = 0
    while var == 0:
        print(
            "Quieres conocer el  volumen1 (v1), la temperatura1 (t1), el volumen2 (v2) o la temperaura2 (t2)?"
        )
        x = input()
        if x == "v1":
            t1 = float(input("ingresa el valor de la temperatura1: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t1 += 273
            elif zz == 2:
                t1 = (((t1 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            v2 = float(input("ingresa el valor del volumen2: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v2 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v2 *= 1000
            elif z == 4:
                v2 /= 1000
            t2 = float(input("ingresa el valor de la temperatura2: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t2 += 273
            elif zz == 2:
                t2 = (((t2 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            v1 = (v2 / t2) * t1
            v1 = "%.3f" % v1
            print(v1, "L")

        elif x == "t1":
            v1 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v1 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v1 *= 1000
            elif z == 4:
                v1 /= 1000
            v2 = float(input("ingresa el valor del volumen2: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v2 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v2 *= 1000
            elif z == 4:
                v2 /= 1000
            t2 = float(input("ingresa el valor de la temperatura2: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t2 += 273
            elif zz == 2:
                t2 = (((t2 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            t1 = (v1 * t2) / v2
            t1 = "%.3f" % t1
            print(t1, "K")

        elif x == "v2":
            v1 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v1 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v1 *= 1000
            elif z == 4:
                v1 /= 1000
            t1 = float(input("ingresa el valor de la temperatura1: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t1 += 273
            elif zz == 2:
                t1 = (((t1 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            t2 = float(input("ingresa el valor de la temperatura2: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t2 += 273
            elif zz == 2:
                t2 = (((t2 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            v2 = (v1 * t2) / t1
            v2 = "%.3f" % v2
            print(v2, "L")

        elif x == "t2":
            v1 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v1 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v1 *= 1000
            elif z == 4:
                v1 /= 1000
            t1 = float(input("ingresa el valor de la temperatura1: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t1 += 273
            elif zz == 2:
                t1 = (((t1 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            v2 = float(input("ingresa el valor del volumen2: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v2 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v2 *= 1000
            elif z == 4:
                v2 /= 1000
            t2 = (v2 * t1) / v1
            t2 = "%.3f" % t2
            print(t2, "K")

        v1entret1 = float(v1) / float(t1)
        v2entret2 = float(v2) / float(t2)
        v1entret1 = "%.4f" % v1entret1
        v2entret2 = "%.4f" % v2entret2
        print(v1entret1, "L/K", "=", v2entret2, "L/K")
        print("Quieres conocer otra presion o temperatura?")
        ax = input()
        if ax == "si":
            pass
        else:
            var += 1


def Ley_Combinada_Gases():
    print("En esta ley ninguna variable permanece constante")
    var = 0
    while var == 0:
        print(
            "¿Quieres conocer la presion1 (p1), el volumen1 (v1), la temperatura1 (t1), la presion (p2), el volumen2 (v2) o la temperatura2 (t2)?"
        )
        x = input()
        if x == "p1":
            v1 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v1 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v1 *= 1000
            elif z == 4:
                v1 /= 1000
            t1 = float(input("ingresa el valor de la temperatura1: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t1 += 273
            elif zz == 2:
                t1 = (((t1 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            p2 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p2 /= 101, 300
            elif y == 2:
                pass
            else:
                p2 /= 760
            v2 = float(input("ingresa el valor del volumen2: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v2 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v2 *= 1000
            elif z == 4:
                v2 /= 1000
            t2 = float(input("ingresa el valor de la temperatura2: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t2 += 273
            elif zz == 2:
                t2 = (((t2 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            p1 = ((p2 * v2 * t1) / (t2 * v1))
            p1 = "%.3f" % p1
            print(p1, "atm")

        elif x == "v1":
            p1 = float(input("ingresa el valor de la presion1: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p1 /= 101, 300
            elif y == 2:
                pass
            else:
                p1 /= 760
            t1 = float(input("ingresa el valor de la temperatura1: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t1 += 273
            elif zz == 2:
                t1 = (((t1 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            p2 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p2 /= 101, 300
            elif y == 2:
                pass
            else:
                p2 /= 760
            v2 = float(input("ingresa el valor del volumen2: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v2 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v2 *= 1000
            elif z == 4:
                v2 /= 1000
            t2 = float(input("ingresa el valor de la temperatura2: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t2 += 273
            elif zz == 2:
                t2 = (((t2 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            v1 = (p2 * v2 * t1) / (p1 * t2)
            v1 = "%.3f" % v1
            print(v1, "L")
        elif x == "t1":
            p1 = float(input("ingresa el valor de la presion1: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p1 /= 101, 300
            elif y == 2:
                pass
            else:
                p1 /= 760
            v1 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v1 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v1 *= 1000
            elif z == 4:
                v1 /= 1000
            p2 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p2 /= 101, 300
            elif y == 2:
                pass
            else:
                p2 /= 760
            v2 = float(input("ingresa el valor del volumen2: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v2 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v2 *= 1000
            elif z == 4:
                v2 /= 1000
            t2 = float(input("ingresa el valor de la temperatura2: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t2 += 273
            elif zz == 2:
                t2 = (((t2 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            t1 = (p1 * v1 * t2) / (p2 * v2)
            t1 = "%.3f" % t1
            print(t1, "K")
        elif x == "p2":
            p1 = float(input("ingresa el valor de la presion1: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p1 /= 101, 300
            elif y == 2:
                pass
            else:
                p1 /= 760
            v1 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v1 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v1 *= 1000
            elif z == 4:
                v1 /= 1000
            t1 = float(input("ingresa el valor de la temperatura1: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t1 += 273
            elif zz == 2:
                t1 = (((t1 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            v2 = float(input("ingresa el valor del volumen2: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v2 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v2 *= 1000
            elif z == 4:
                v2 /= 1000
            t2 = float(input("ingresa el valor de la temperatura2: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t2 += 273
            elif zz == 2:
                t2 = (((t2 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            p2 = (p1 * v1 * t2) / (t1 * v2)
            p2 = "%.3f" % p2
            print(p2, "atm")
        elif x == "v2":
            p1 = float(input("ingresa el valor de la presion1: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p1 /= 101, 300
            elif y == 2:
                pass
            else:
                p1 /= 760
            v1 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v1 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v1 *= 1000
            elif z == 4:
                v1 /= 1000
            t1 = float(input("ingresa el valor de la temperatura1: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t1 += 273
            elif zz == 2:
                t1 = (((t1 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            p2 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p2 /= 101, 300
            elif y == 2:
                pass
            else:
                p2 /= 760
            t2 = float(input("ingresa el valor de la temperatura2: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t2 += 273
            elif zz == 2:
                t2 = (((t2 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            v2 = (p1 * v1 * t2) / (t1 * p2)
            v2 = "%.3f" % v2
            print(v2, "L")
        elif x == "t2":
            p1 = float(input("ingresa el valor de la presion1: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p1 /= 101, 300
            elif y == 2:
                pass
            else:
                p1 /= 760
            v1 = float(input("ingresa el valor del volumen1: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v1 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v1 *= 1000
            elif z == 4:
                v1 /= 1000
            t1 = float(input("ingresa el valor de la temperatura1: "))
            print("Esta en Celsius [1], en Fahrenheit [2] o en Kelvin [3]?")
            zz = int(input())
            if zz == 1:
                t1 += 273
            elif zz == 2:
                t1 = (((t1 - 32) * (5 / 9)) + 273)
            elif zz == 3:
                pass
            p2 = float(input("ingresa el valor de la presion2: "))
            print("Esta en Pa (1), en atm (2) o en mmHg (3)?")
            y = int(input())
            if y == 1:
                p2 /= 101, 300
            elif y == 2:
                pass
            else:
                p2 /= 760
            v2 = float(input("ingresa el valor del volumen2: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v2 /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v2 *= 1000
            elif z == 4:
                v2 /= 1000
            t2 = (p2 * v2 * t1) / (p1 * v1)
            t2 = "%.3f" % t2
            print(t2, "K")
        p1v1entret1 = (float(p1) * float(v1)) / float(t1)
        p2v2entret2 = (float(p2) * float(v2)) / float(t2)
        p1v1entret1 = "%.4f" % p1v1entret1
        p2v2entret2 = "%.4f" % p2v2entret2
        print(p1v1entret1, "atm*L/K", "=", p2v2entret2, "atm*L/K")

        print("Quieres conocer otro dato?")
        y = input()
        if y == "si":
            pass
        else:
            var += 1


def conc_masa():
    var = 0
    while var == 0:
        print(
            "¿Quieres conocer la masa de la solucion (ms), la masa del soluto (msol), la masa del solvente (msolv) o la porcentaje masa(%m)?"
        )
        x = input()
        if x == "ms":
            print("Conoces la masa del soluto y del solvente?")
            x = input()
            if x == "si":
                msoluto = float(input("ingresa la masa del soluto: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    msoluto /= 1 * (10**3)
                elif y == 3:
                    msoluto *= 1000
                msolvente = float(input("ingresa la masa del solvente: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    msolvente /= 1 * (10**3)
                elif y == 3:
                    msolvente *= 1000
                msolucion = msoluto + msolvente
                msolucion = "%.2f" % msolucion

            else:
                porcenmasa = float(input("ingresa el porciento masa: "))
                msoluto = float(input("ingresa la masa del soluto: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    msoluto /= 1 * (10**3)
                elif y == 3:
                    msoluto *= 1000
                msolucion = (msoluto / porcenmasa) * 100
                msolucion = "%.3f" % msolucion
            print(msolucion, "g")

        elif x == "msol":
            porcenmasa = float(input("ingresa el porciento masa: "))
            msolucion = float(input("ingresa la masa la solucion: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                pass
            elif y == 2:
                msolucion /= 1 * (10**3)
            elif y == 3:
                msolucion *= 1000
            msoluto = (msolucion * porcenmasa) / 100
            msoluto = "%.3f" % msoluto
            print(msoluto, "g")

        elif x == "msolv":
            porcenmasa = float(input("ingresa el porciento masa: "))
            msoluto = float(input("ingresa la masa del soluto: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                pass
            elif y == 2:
                msoluto /= 1 * (10**3)
            elif y == 3:
                msoluto *= 1000
            msolvente = ((msoluto * 100) - (porcenmasa * msoluto)) / porcenmasa
            msolvente = "%.2f" % msolvente
            print(msolvente, "g")

        elif x == "%m":
            print("Conoces la masa de la solucion?")
            z = input()
            if z == "si":
                msoluto = float(input("ingresa la masa del soluto: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    msoluto /= 1 * (10**3)
                elif y == 3:
                    msoluto *= 1000
                msolucion = float(input("ingresa la masa la solucion: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    msolucion /= 1 * (10**3)
                elif y == 3:
                    msolucion *= 1000
                porcenmasa = (msoluto / msolucion) * 100
                porcenmasa = "%.2f" % porcenmasa
            else:
                msoluto = float(input("ingresa la masa del soluto: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    msoluto /= 1 * (10**3)
                elif y == 3:
                    msoluto *= 1000
                msolvente = float(input("ingresa la masa del solvente: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    msolvente /= 1 * (10**3)
                elif y == 3:
                    msolvente *= 1000
                porcenmasa = (msoluto / (msoluto + msolvente)) * 100
                porcenmasa = "%.2f" % porcenmasa
            print(porcenmasa, "%m")

        print("Quieres conocer otro dato?")
        z = input()
        if z == "si":
            pass
        else:
            var += 1


def conc_volumen():
    var = 0
    while var == 0:
        print(
            "¿Quieres conocer el volumen de la solucion (vs), el volumen del soluto (vsol), el volumen del solvente (vsolv) o el porcentaje volumen(%v)?"
        )
        x = input()
        if x == "vs":
            print("Conoces el volumen del soluto y del solvente?")
            x = input()
            if x == "si":
                vsoluto = float(input("ingresa el vollumen del soluto: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    vsoluto /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    vsoluto *= 1000
                elif z == 4:
                    vsoluto /= 1000
                vsolvente = float(input("ingresa el volumen del solvente: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    vsolvente /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    vsolvente *= 1000
                elif z == 4:
                    vsolvente /= 1000
                vsolucion = vsoluto + vsolvente
                vsolucion = "%.2f" % vsolucion

            else:
                porcenvolumen = float(input("ingresa el porciento volumen: "))
                vsoluto = float(input("ingresa el volumen del soluto: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    vsoluto /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    vsoluto *= 1000
                elif z == 4:
                    vsoluto /= 1000
                vsolucion = (vsoluto / porcenvolumen) * 100
                vsolucion = "%.3f" % vsolucion
            print(vsolucion, "L")

        elif x == "vsol":
            porcenvolumen = float(input("ingresa el porciento volumen: "))
            vsolucion = float(input("ingresa el volumen la solucion: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                vsolucion /= 1000
            elif z == 2:
                pass
            elif z == 3:
                vsolucion *= 1000
            elif z == 4:
                vsolucion /= 1000
            vsoluto = (vsolucion * porcenvolumen) / 100
            vsoluto = "%.3f" % vsoluto
            print(vsoluto, "L")

        elif x == "vsolv":
            porcenvolumen = float(input("ingresa el porciento volumen: "))
            vsoluto = float(input("ingresa el volumen del soluto: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                vsoluto /= 1000
            elif z == 2:
                pass
            elif z == 3:
                vsoluto *= 1000
            elif z == 4:
                vsoluto /= 1000
            vsolvente = (
                (vsoluto * 100) - (porcenvolumen * vsoluto)) / porcenvolumen
            vsolvente = "%.2f" % vsolvente
            print(vsolvente, "L")

        elif x == "%v":
            print("Conoces el volumen de la solucion?")
            z = input()
            if z == "si":
                vsoluto = float(input("ingresa el volumen del soluto: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    vsoluto /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    vsoluto *= 1000
                elif z == 4:
                    vsoluto /= 1000
                vsolucion = float(input("ingresa el volumen de la solucion: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    vsolucion /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    vsolucion *= 1000
                elif z == 4:
                    vsolucion /= 1000
                porcenvolumen = (vsoluto / vsolucion) * 100
                porcenvolumen = "%.2f" % porcenvolumen
            else:
                vsoluto = float(input("ingresa el volumen del soluto: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    vsoluto /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    vsoluto *= 1000
                elif z == 4:
                    vsoluto /= 1000
                vsolvente = float(input("ingresa el volumen del solvente: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    v1 /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    v1 *= 1000
                elif z == 4:
                    v1 /= 1000
                porcenvolumen = (vsoluto / (vsoluto + vsolvente)) * 100
                porcenvolumen = "%.2f" % porcenvolumen
            print(porcenvolumen, "%v")

        print("Quieres conocer otro dato?")
        z = input()
        if z == "si":
            pass
        else:
            var += 1


def peso_litros():
    var = 0
    while var == 0:
        print(
            "Quieres conocer la masa del soluto (msol), los litros de la solucion (l), o la concentracion peso/litros (g/l)?"
        )
        x = input()
        if x == "msol":
            l = float(input("ingresa el volumen de la solucion: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                l /= 1000
            elif z == 2:
                pass
            elif z == 3:
                l *= 1000
            elif z == 4:
                l /= 1000
            porcengel = float(input("ingresa la concentracion peso/litros: "))
            gr = porcengel * l
            gr = "%.2f" % gr
            print(gr, "g")
        elif x == "l":
            gr = float(input("ingresa la masa del soluto: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                pass
            elif y == 2:
                gr /= 1 * (10**3)
            elif y == 3:
                gr *= 1000
            porcengel = float(input("ingresa la concentracion peso/litros: "))
            l = gr / porcengel
            l = "%.2f" % l
            print(l, "L")
        elif x == "g/l":
            gr = float(input("ingresa la masa del soluto: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                pass
            elif y == 2:
                gr /= 1 * (10**3)
            elif y == 3:
                gr *= 1000
            l = float(input("ingresa el volumen de la solucion: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                l /= 1000
            elif z == 2:
                pass
            elif z == 3:
                l *= 1000
            elif z == 4:
                l /= 1000
            porcengel = (gr / l)
            porcengel = "%.2f" % porcengel
            print(porcengel, "g/L")

            print("Quieres conocer otro dato?")
            xx = input()
            if xx == "si":
                pass
            else:
                var += 1


def Molaridad():
    var = 0
    while var == 0:
        print(
            "Quieres conocer la masa del soluto (m), la masa molecular(Mm), el volumen (v), los moles (n), la molaridad (M)?"
        )
        x = input()
        if x == "m":
            Mm = float(input("ingresa la masa molecular: "))
            v = float(input("ingresa el volumen: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v *= 1000
            elif z == 4:
                v /= 1000
            M = float(input("ingresa la Molaridad: "))
            gr = M * Mm * v
            gr = "%.4f" % gr
            print(gr, "g")
        elif x == "Mm":
            gr = float(input("ingresa la masa del soluto: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                pass
            elif y == 2:
                gr /= 1 * (10**3)
            elif y == 3:
                gr *= 1000
            v = float(input("ingresa el volumen: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v *= 1000
            elif z == 4:
                v /= 1000
            M = float(input("ingresa la Molaridad: "))
            Mm = gr / (M * v)
            Mm = "%.4f" % Mm
            print(Mm, "g/mol")
        elif x == "v":
            print("Conoces los moles?")
            xx = input()
            if xx == "si":
                n = float(input("ingresa los moles: "))
                M = float(input("ingresa la Molaridad: "))
                v = n * M
            else:
                gr = float(input("ingresa la masa del soluto: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    gr /= 1 * (10**3)
                elif y == 3:
                    gr *= 1000
                M = float(input("ingresa la Molaridad: "))
                Mm = float(input("ingresa la masa molecular: "))
                v = gr / (Mm * M)
            v = "%.4f" % v
            print(v, "L")
        elif x == "n":
            v = float(input("ingresa el volumen: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v *= 1000
            elif z == 4:
                v /= 1000
            M = float(input("ingresa la Molaridad: "))
            n = M * v
            n = "%.4f" % n
            print(n, "mol")
        elif x == "M":
            print("Conoces el numero de moles?")
            xx = input()
            if xx == "si":
                n = float(input("ingresa los moles: "))
                v = float(input("ingresa el volumen: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    v /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    v *= 1000
                elif z == 4:
                    v /= 1000
                M = n / v
            else:
                gr = float(input("ingresa la masa del soluto: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    gr /= 1 * (10**3)
                elif y == 3:
                    gr *= 1000
                v = float(input("ingresa el volumen: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    v /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    v *= 1000
                elif z == 4:
                    v /= 1000
                Mm = float(input("ingresa la masa molecular: "))
                M = gr / (Mm * v)
            M = "%.5f" % M
            print(M, "mol/L")
        print("Quieres conocer otra variable?")
        xxy = input()
        if xxy == "si":
            pass
        else:
            var += 1


def Normal():
    var = 0
    while var == 0:
        print(
            "Quieres conocer la masa del soluto (g), el peso equivalente (peq), el volumen (v), la concentracion Normal (N)?"
        )
        x = input()
        if x == "g":
            print("Conoces el peso equivalente?")
            xx = input()
            if xx == "si":
                peq = float(input("ingresa el peso equivalente: "))
                v = float(input("ingresa el volumen: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    v /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    v *= 1000
                elif z == 4:
                    v /= 1000
                N = float(input("ingresa la concentracion Normal: "))
            else:
                Mm = float(input("ingresa la masa molecular del compuesto: "))
                print(
                    "Tu compuesto es un acido (h), una base (oh) o una sal(s)?"
                )
                xxx = input()
                if xxx == "h":
                    print("Cuantos hidrogenos tienes?")
                    carga = float(input())
                elif xxx == "oh":
                    print("Cuantos oxhidrilos tienes?")
                    carga = float(input())
                else:
                    print("Cuantos atomos tienes de tu primer elemento?")
                    carga = float(input())
                peq = Mm / carga
                v = float(input("ingresa el volumen: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    v /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    v *= 1000
                elif z == 4:
                    v /= 1000
                N = float(input("ingresa la concentracion Normal: "))
            gr = N * peq * v
            gr = "%.3f" % gr
            print(gr, "g")

        elif x == "v":
            print("Conoces el peso equivalente?")
            xx = input()
            if xx == "si":
                peq = float(input("ingresa el peso equivalente: "))
                gr = float(input("ingresa la masa del soluto: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    gr /= 1 * (10**3)
                elif y == 3:
                    gr *= 1000
                N = float(input("ingresa la concentracion Normal: "))
            else:
                Mm = float(input("ingresa la masa molecular del compuesto: "))
                print(
                    "Tu compuesto es un acido (h), una base (oh) o una sal(s)?"
                )
                xxx = input()
                if xxx == "h":
                    print("Cuantos hidrogenos tienes?")
                    carga = float(input())
                elif xxx == "oh":
                    print("Cuantos oxhidrilos tienes?")
                    carga = float(input())
                else:
                    print("Cuantos atomos tienes de tu primer elemento?")
                    carga = float(input())
                peq = Mm / carga
                gr = float(input("ingresa la masa del soluto: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    gr /= 1 * (10**3)
                elif y == 3:
                    gr *= 1000
                N = float(input("ingresa la concentracion Normal: "))
            v = gr / (peq * N)
            v = "%.3f" % v
            print(v, "L")

        elif x == "peq":
            gr = float(input("ingresa la masa del soluto: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                pass
            elif y == 2:
                gr /= 1 * (10**3)
            elif y == 3:
                gr *= 1000
            v = float(input("ingresa el volumen: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v *= 1000
            elif z == 4:
                v /= 1000
            N = float(input("ingresa la concentracion Normal: "))
            peq = gr / (N * v)
            peq = "%.3f" % peq
            print(peq, "g/mol")

        elif x == "N":
            print("Conoces el peso equivalente?")
            xx = input()
            if xx == "si":
                peq = float(input("ingresa el peso equivalente: "))
                gr = float(input("ingresa la masa del soluto: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    gr /= 1 * (10**3)
                elif y == 3:
                    gr *= 1000
                v = float(input("ingresa el volumen: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    v /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    v *= 1000
                elif z == 4:
                    v /= 1000
            else:
                Mm = float(input("ingresa la masa molecular del compuesto: "))
                print(
                    "Tu compuesto es un acido (h), una base (oh) o una sal(s)?"
                )
                xxx = input()
                if xxx == "h":
                    print("Cuantos hidrogenos tienes?")
                    carga = float(input())
                elif xxx == "oh":
                    print("Cuantos oxhidrilos tienes?")
                    carga = float(input())
                else:
                    print("Cuantos atomos tienes de tu primer elemento?")
                    carga = float(input())
                peq = Mm / carga
                gr = float(input("ingresa la masa del soluto: "))
                print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
                y = int(input())
                if y == 1:
                    pass
                elif y == 2:
                    gr /= 1 * (10**3)
                elif y == 3:
                    gr *= 1000
                v = float(input("ingresa el volumen: "))
                print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
                z = int(input())
                if z == 1:
                    v /= 1000
                elif z == 2:
                    pass
                elif z == 3:
                    v *= 1000
                elif z == 4:
                    v /= 1000
            N = gr / (peq * v)
            N = "%.3f" % N
            print(N, "mol/L")

        print("Quieres conocer otro dato?")
        xxx = input()
        if xxx == "si":
            pass
        else:
            var += 1


def molal():
    var = 0
    while var == 0:
        print(
            "Quieres conocer la masa del soluto(g), masa molecular (Mm), la masa del solvente(kg) o la concentracion molal(m)?"
        )
        x = input()
        if x == "g":
            Mm = float(input("ingresa la masa molecular: "))
            kg = float(input("ingresa la masa del solvente: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                kg /= 1000
            elif y == 2:
                kg /= 1 * (10**6)
            elif y == 3:
                pass
            m = float(input("ingresa la concentracion molal: "))
            gr = m * Mm * kg
            gr = "%.3f" % gr
            print(gr, "g")

        elif x == "kg":
            Mm = float(input("ingresa la masa molecular: "))
            gr = float(input("ingresa la masa del soluto: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                pass
            elif y == 2:
                gr /= 1 * (10**3)
            elif y == 3:
                gr *= 1000
            m = float(input("ingresa la concentracion molal: "))
            kg = gr / (m * Mm)
            kg = "%.3f" % kg
            print(kg, "kg")

        elif x == "Mm":
            gr = float(input("ingresa la masa del soluto: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                pass
            elif y == 2:
                gr /= 1 * (10**3)
            elif y == 3:
                gr *= 1000
            kg = float(input("ingresa la masa del solvente: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                kg /= 1000
            elif y == 2:
                kg /= 1 * (10**6)
            elif y == 3:
                pass
            m = float(input("ingresa la concentracion molal: "))
            Mm = gr / (m * kg)
            Mm = "%.3f" % Mm
            print(Mm, "mol/g")

        elif x == "m":
            gr = float(input("ingresa la masa del soluto: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                pass
            elif y == 2:
                gr /= 1 * (10**3)
            elif y == 3:
                gr *= 1000
            kg = float(input("ingresa la masa del solvente: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                kg /= 1000
            elif y == 2:
                kg /= 1 * (10**6)
            elif y == 3:
                pass
            Mm = float(input("ingresa la masa molecular: "))
            m = gr / (Mm * kg)
            m = "%.3f" % m
            print(m, "mol/kg")

        print("Quieres conocer otro dato?")
        xx = input()
        if xx == "si":
            pass
        else:
            var += 1


def fraccion_mol():
    var = 0
    while var == 0:
        print("Cuantos compuestos tienes?")
        xx = int(input())
        for i in range(xx):
            compuesto = str(input("ingresa el compuesto: "))
            compuestolist.append(compuesto)
            mol = float(input("ingresa el numero de moles: "))
            moleslist.append(mol)
        moles = sum(moleslist)
        for i in range(xx):
            x = moleslist.pop(0)
            y = compuestolist.pop(0)
            z = x / moles
            semejante2.append(z)
            z = "%.3f" % z
            molesdicionario[y] = z
            semejante.append(z)
        xx = sum(semejante2)
        xx = int(xx)
        print(molesdicionario)
        print(semejante)
        print(xx, "=", "1")

        print("Quieres conocer otro dato?")
        x = input()
        if x == "si":
            pass
        else:
            var += 1


def partesxmillon():
    var = 0
    while var == 0:
        print(
            "Quieres conocer la masa del soluto (m), el volumen de la solucion(l) o la concentracion por partes de millon (ppm)?"
        )
        x = input()
        if x == "m":
            v = float(input("ingresa el volumen de la solucion: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v *= 1000
            elif z == 4:
                v /= 1000
            ppm = float(
                input("ingresa la concentracion por partes por millon: "))
            mg = (ppm * v) / (1 * (10**6))
            print(mg, "mg")
        elif x == "l":
            mg = float(input("ingresa la masa del soluto: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                mg *= 1000
            elif y == 2:
                pass
            elif y == 3:
                mg *= 1000000
            ppm = float(
                input("ingresa la concentracion por partes por millon: "))
            v = (mg * 1000000) / ppm
            print(v, "L")
        else:
            mg = float(input("ingresa la masa del soluto: "))
            print("Esta en gramos(1), en miligramos(2) o en kilogramos(3)")
            y = int(input())
            if y == 1:
                mg *= 1000
            elif y == 2:
                pass
            elif y == 3:
                mg *= 1000000
            v = float(input("ingresa el volumen de la solucion: "))
            print("Esta en mL (1), L (2), m^3 (3) o cm^3 (4)?")
            z = int(input())
            if z == 1:
                v /= 1000
            elif z == 2:
                pass
            elif z == 3:
                v *= 1000
            elif z == 4:
                v /= 1000
            ppm = (mg / v) * 1000000
            print(ppm, "mg/L")

        print("Quieres conocer otro dato?")
        xxx = input()
        if xxx == "si":
            pass
        else:
            var += 1


def pH_pOH():
    var = 0
    while var == 0:
        print(
            "Tienes el pH(1), el pOH(2), la concentracion de hidronios(H+) o la concentracion de oxhidrilos(OH-)?"
        )
        x = input()
        if x == "1":
            pH = float(input("ingresa el pH: "))
            pOH = 14 - pH
            H = 10**(-pH)
            OH = 10**(-pOH)

        elif x == "2":
            pOH = float(input("ingresa el pOH: "))
            pH = 14 - pOH
            H = 10**(-pH)
            OH = 10**(-pOH)

        elif x == "H+":
            H = float(input("ingresa la concentracion de hidronios: "))
            pH = math.log10(H) * -1
            pOH = 14 - pH
            OH = (1e-14) / H

        elif x == "OH-":
            OH = float(input("ingresa la concentracion de oxhidrilos: "))
            pOH = math.log10(OH) * -1
            pH = 14 - pOH
            H = (1e-14) / OH

        if (pH < 7 and pOH > 7) and (H > OH) == True:
            print("La sustancia es un acido")
        elif pH == 7 or pOH == 7:
            print("La sustancia es neutra")
        else:
            print("La sustancia es una base")

        completo = H * OH
        print("pH =", pH, "|", "pOH =", pOH, "|", "[H+] =", H, "mol/L", "|",
              "[OH-] =", OH, "mol/L", "|", "[H+][OH-] =", completo,
              "mol^2/L^2")

        print("Quieres conocer otro dato?")
        xx = input()
        if xx == "si":
            pass
        else:
            var += 1


def Atomos():
    var = 0
    while var == 0:

        print("Bienvenido a la UNIDAD 1: Clasificacion de la Materia")
        print("""
        Obtencion de uma-masa molecular [1],
        comprobacion de la conservacion de la materia [2],
        obtencion de gramos o moles [3],
        propiedades quimicas de los elementos [4],
        exit[5]
        """)
        x = int(input())
        if x == 1:
            UMA_percentual()
        elif x == 2:
            conservacion_materia()
        elif x == 3:
            g_to_mol()
        elif x == 4:
            conf_electric()
        else:
            var += 1


def Leyes_gases():
    var = 0
    while var == 0:
        print("Bienvenido a la UNIDAD 2: Leyes de los gases")
        print("""
        Ley de Boyle [1],
        Ley de Gauss-Lussac [2],
        Ley de Charles [3],
        Ley combinada de los gases [4],
        exit[5]
        """)
        x = int(input())
        if x == 1:
            Ley_Boyle()
        elif x == 2:
            Ley_Lussac()
        elif x == 3:
            Ley_Charles()
        elif x == 4:
            Ley_Combinada_Gases()
        else:
            var += 1


def concentaciones():
    var = 0
    while var == 0:

        print("Bienvenido a la UNIDAD 3: Concentraciones")
        print("""
        Porcantaje masa [1],
        Porcentaje volumen [2],
        Peso/litros [3],
        Molaridad [4],
        Normalidad [5],
        Molal [6],
        Fraccion mol [7],
        Partes por millon [8]
        exit [9]
        """)
        x = int(input())
        if x == 1:
            conc_masa()
        elif x == 2:
            conc_volumen()
        elif x == 3:
            peso_litros()
        elif x == 4:
            Molaridad()
        elif x == 5:
            Normal()
        elif x == 6:
            molal()
        elif x == 7:
            fraccion_mol()
        elif x == 8:
            partesxmillon()
        else:
            var += 1


def Potencial_Hidrogeno():
    var = 0
    while var == 0:
        print("Bienvenido a la UNIDAD 4: PH y POH")
        print("""
        PH y POH [1],
        exit [2]
        """)
        x = int(input())
        if x == 1:
            pH_pOH()
        elif x == 2:
            var += 1


def temario():
    var2 = 0
    while var2 == 0:
        print("""
        UNIDAD1: Clasificacion de la Materia[1],
        UNIDAD2: Leyes de los gases[2],
        UNIDAD3: Concentraciones[3],
        UNIDAD4: PH y POH[4],
        exit[5]
        """)
        axz = int(input())
        if axz == 1:
            Atomos()
        elif axz == 2:
            Leyes_gases()
        elif axz == 3:
            concentaciones()
        elif axz == 4:
            Potencial_Hidrogeno()
        else:
            var2 += 1


temario()
