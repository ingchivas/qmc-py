# Importando las librerías auxiliares
import math
import re
import numpy as np

# En esta sección, se va a incluir un diccionario con todas las unidades de masa atómica de todos los elementos de la tabla
uma_dc = {"H": 1.008,"He": 4.003,"Li": 6.94 ,"Be": 9.012,"B": 10.81,"C": 12.011,"N": 14.007,"O": 15.999,"F": 18.998,
    "Ne": 20.180,"Na": 22.990,"Mg": 24.305,"Al": 26.982,"Si": 28.085,"P": 30.974,"S": 32.06,"Cl": 35.45,"Ar": 39.95,"K": 39.098,"Ca": 40.078,
    "Sc": 44.956 ,"Ti": 47.867,"V": 50.942,"Cr": 51.996,"Mn": 54.938,"Fe": 55.845,"Co": 58.933 ,"Ni": 58.693,"Cu": 63.546,
    "Zn": 65.38,"Ga": 69.723,"Ge": 72.630,"As": 74.922,"Se": 78.971,"Br": 79.904,"Kr": 83.798,"Rb": 85.468,"Sr": 87.62,"Y": 88.906,"Zr": 91.224,
    "Nb": 92.906,"Mo": 95.95,"Tc": 98,"Ru": 101.07,"Rh": 102.906,"Pd": 106.42,"Ag": 107.868,"Cd": 112.414,
    "In": 114.818,"Sn": 118.710,"Sb": 121.76,"Te": 127.6,"I": 126.904,"Xe": 131.293,"Cs": 132.905,"Ba": 137.327,"La": 138.905,
    "Ce": 140.116,"Pr": 140.908,"Nd": 144.242,"Pm": 147,"Sm": 150.36,"Eu": 151.964,"Gd": 157.25,"Tb": 158.925,"Dy": 163.5,
    "Ho": 164.93,"Er": 167.259,"Tm": 168.934,"Yb": 173.045,"Lu": 174.967,
    "Hf": 178.486,"Ta": 180.948,"W": 183.84,"Re": 186.207,"Os": 190.23,"Ir": 192.217 ,"Pt": 195,"Au": 197,
    "Hg": 201,"Tl": 204,"Pb": 207,"Bi": 209,"Po": 210,"At": 210,"Rn": 222,"Fr": 223,
    "Ra": 226,"Ac": 227,"Th": 232,"Pa": 231,"U": 238,"Np": 237,"Pu": 242,
    "Am": 293,"Cm": 247,"Bk": 247,"Cf": 251,"Es": 254,"Fm": 257,
    "Md": 258,"No": 259,"Lr": 262,"Rf": 261,"Ha": 262,"Nt": 263,"Gp": 264,"Hr": 265,"Wl": 266,
    "Mv": 269,"Pl": 272,"Da": 270,"Tf": 272,"Eo": 276,"Me": 279,"Nc": 282,"El": 286,"On": 288
}
# En esta variable, se almacena el diccionario de números atómicos de cada elemento de la tabla
Z = {
    "H": 1,"He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10, "Na": 11,
    "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20,"Sc": 21,"Ti": 22,"V": 23,"Cr": 24,"Mn": 25,
    "Fe": 26,"Co": 27,"Ni": 28,"Cu": 29,"Zn": 30,"Ga": 31,"Ge": 32,"As": 33,"Se": 34,"Br": 35,"Kr": 36, "Rb": 37,
    "Sr": 38,"Y": 39,"Zr": 40,"Nb": 41,"Mo": 42,"Tc": 43,"Ru": 44,"Rh": 45,"Pd": 46,"Ag": 47,"Cd": 48,"In": 49,"Sn": 50,
    "Sb": 51,"Te": 52,"I": 53,"Xe": 54,"Cs": 55,"Ba": 56,"La": 57,"Ce": 58,"Pr": 59,"Nd": 60,"Pm": 61,"Sm": 62,"Eu": 63,"Gd": 64,
    "Tb": 65,"Dy": 66,"Ho": 67,"Er": 68,"Tm": 69,"Yb": 70,"Lu": 71,"Hf": 72,"Ta": 73,"W": 74,"Re": 75,"Os": 76,
    "Ir": 77,"Pt": 78,"Au": 79,"Hg": 80,"Tl": 81,"Pb": 82,"Bi": 83,"Po": 84,"At": 85,"Rn": 86,"Fr": 87,"Ra": 88,"Ac": 89,
    "Th": 90,"Pa": 91,"U": 92,"Np": 93,"Pu": 94,"Am": 95,"Cm": 96,"Bk": 97,"Cf": 98,"Es": 99,
    "Fm": 100,"Md": 101,"No": 102,"Lr": 103,"Rf": 104,"Ha": 105,"Nt": 106,"Gp": 107,
    "Hr": 108,"Wl": 109,"Mv": 110,"Pl": 111,"Da": 112,"Tf": 113,"Eo": 114,"Me": 115,"Nc": 116,"El": 117,"On": 118
}

# En esta función, se toma un compuesto y se divide en sus elementos
def _cosplit(compuesto):
    '''
    Parser de ecuaciones químicas basado en regex. 
    '''
    com = compuesto.split(' ') # Separa el compuesto en secciones
    div = [] # Inicia una lista llamada 'div'
    for i in range(len(com)): # Por cada sección
        a = re.findall('[A-Z][a-z]?|[0-9]+', com[i]) # Obtiene el elemento y su cantidad de átomos en una lista
        div.append(a) # Añade la lista [elemento, número de átomos] a la lista div
    return div # Regresa la lista de divisiones

# Convierte números enteros para su uso dentro de las funciones químicas
def _intconv(num): 
    '''
    Intenta convertir números a enteros. Auxiliar en el algoritmo de reconocimiento de fórmulas químicas.
    '''
    try: # Intenta hacer la conversión
        n = int(num)
        return n
    except: # De lo contrario, continúa con el programa
        pass

# Obtiene la uma de un elemento determinado
def _umaelemento(elemento):
    '''
    Checa la UMA de un elemento en el contenedor.   
    '''
    check = elemento
    try: # Intenta utilizar el valor introducido
        if str(check) in uma_dc: # Revisa si el valor existe dentro del diccionario
            umaa = uma_dc.get(check) # Asigna el valor correspondiente
            return umaa # Regresa el valor
        else: # De no encontrarlo, el programa sigue
            print("Valor no encontrado")
    except: # De haber algun error, levanta un mensaje de error
        print("Revise su sintaxis")

# Obtiene la uma de un compuesto determinado
def umacompuesto(compuesto):
    '''
    El compuesto debe estar separado por elementos con espacios para que el parser de REGEX pueda interpretar el compuesto.
    Por ejemplo, para la fórmula química de la glucosa sería ```materia.umacompuesto('C6 H12 O 6')```.

    Este método igual puede devolver la UMA de solo un elemento: ```materia.umacompuesto(C)```.

    Ejemplo:

    ```python
    from libs import materia

    materia.umacompuesto('H2 O')
    ```

    Regresa:

    ```python
    18.015
    ```

    Para un elemento individual:

    ```python
    materia.umacompuesto('O')
    ```

    Regresa:

    ```python
    15.999
    ```
    '''
    div = _cosplit(compuesto) # Se apoya de la función _cosplit() para separar el compuesto en elementos
    acumcomp = 0
    # En la siguiente cadena de ifs se va a catalogar el tipo de compuesto y se harán los cálculos acorde
    for j in range(len(div)):
        for n in range(len(div[j])):
            if len(div[j]) == 3:
                aucompa = _umaelemento(str(div[j][1]))
                compa = aucompa * int(div[j][2])* int(div[j][0])
                acumcomp += int(compa)
                break
            
            elif len(div[j])==1:
                aucompb = _umaelemento(str(div[j][0]))
                acumcomp += aucompb
                break
            
            elif len(div[j]) == 2 and type(_intconv(div[j][1])==int):
                aucompc = _umaelemento(str(div[j][0]))
                compc = aucompc * int(div[j][1])
                acumcomp += compc
                break

            elif len(div[j]) == 2 and (type(_intconv(div[j][0]))== int):
                aucompd = _umaelemento(str(div[j][1]))
                compd = aucompd * int(div[j][0])

                acumcomp += compd
                break
    return acumcomp # Devuelve el valor

# Obtiene la uma percentual
def umapercentual(compuesto):
    '''
    Este método regresa la composición percentual de la UMA de un elemento o compuesto.
    El parser es el mismo, y se debe escribir de la misma forma que el método ```umacompuesto()```.

    ```python
    from libs import materia

    materia.umapercentual('H2 O')
    ```

    Regresa:

    ```python
    {'H': 11.19067443796836, 'O': 88.80932556203163}
    ```

    Funciona igual para elementos, solo que la relación siempre será 100%.

    ```python
    materia.umapercentual('O')
    ```

    Regresa:

    ```python
    {'O': 100.0}
    ```
    '''
    utotal = umacompuesto(compuesto) # Se apoya de la función umacompuesto() para obtener la uma
    div = _cosplit(compuesto) # Se apoya de la función _cosplit() para obtener el compuesto dividido
    
    upercentual = {}
    # Cataloga cada elemento con sus átomos y hace los cálculos acorde
    for j in range(len(div)):
        for n in range(len(div[j])):
            if len(div[j]) == 3:
                aucompa = _umaelemento(str(div[j][1]))
                compa = aucompa * int(div[j][2])* int(div[j][0])
                upercentual[str(div[j][1])] = (compa/utotal)*100
                break

            
            elif len(div[j])==1:
                aucompb = _umaelemento(str(div[j][0]))
                upercentual[str(div[j][0])] = (aucompb/utotal)*100
                break
            
            
            elif len(div[j]) == 2 and type(_intconv(div[j][1])==int):
                aucompc = _umaelemento(str(div[j][0]))
                compc = aucompc * int(div[j][1])
                upercentual[str(div[j][0])] = (compc/utotal)*100
                
                break

            elif len(div[j]) == 2 and (type(_intconv(div[j][0]))== int):
                aucompd = _umaelemento(str(div[j][1]))
                compd = aucompd * int(div[j][0])
                upercentual[str(div[j][1])] = (compd/utotal)*100
                break
    return upercentual # Devuelve el valor     

# Obtiene los gramos / mol del compuesto utilizando la función de umacompuesto()
def gmol(gramos, compuesto):
    '''
    Convierte gramos de un compuesto a moles. Utiliza el mismo parser y regresa un valor float.

    ```python
    from libs import materia

    materia.gmol(18.01528,'H2 O') 
    ```

    Regresa:

    ```python
    1.000015542603386
    ```
    '''
    return gramos/umacompuesto(compuesto)

# Obtiene los mol del compuesto utilizando la función de umacompuesto() 
def molg(moles, compuesto):
    '''
    Convierte moles de un compuesto a gramos. Utiliza el mismo parser y regresa un valor float.

    ```python
    materia.molg(1, 'H2 O')
    ```

    Regresa:

    ```python
    18.015
    ```
    '''
    return moles * umacompuesto(compuesto)