# Importamos la librería que usaremos
import numpy as np

# Esta función realiza la distinción de si una solución es un ácido, neutra o base
def _tipoPH(pH, pOH, H, OH):
    # Se comprueba que los requerimientos se cumplan para cada uno de los casos
    if (pH < 7 and pOH > 7) and (H > OH) == True: 
        return ("ácido") # Regresa el valor respectivo
    elif pH == 7 or pOH == 7:
        return ("neutra") # Regresa el valor respectivo
    else:
        return ("base") # Regresa el valor respectivo

# Esta función regresa la concentración de la solución
def _getConcentracion(H, OH):
    return (H*OH) # Regresa la operación

# Se usa esta función si lo que se tiene es el PH de la solución
def get_pH(pH): 
    # Se usan diccionarios para guardar toda la información correspondiente 
    res = {}
    res['pH'] = pH
    res['pOH'] = 14 - pH
    res['H+'] = 10**(-pH)
    res['OH-'] = 10**(-res['pOH'])
    res['Tipo'] = _tipoPH(res['pH'], res['pOH'],res['H+'] ,res['OH-'])
    res['Concentración'] = _getConcentracion(res['H+'], res['OH-'])

    return res # Se regresa el valor 

# Se usa esta función si lo que se tiene es el PH de la solución
def get_pOH(pOH):
    # Se usan diccionarios para guardar toda la información correspondiente 
    res = {}
    res['pH'] = 14 - pOH
    res['pOH'] = pOH
    res['H+'] = 10**(-res['pH'])
    res['OH-'] = 10**(-res['pOH'])
    res['Tipo'] = _tipoPH(res['pH'], res['pOH'],res['H+'] ,res['OH-'])
    res['Concentración'] = _getConcentracion(res['H+'], res['OH-'])

    return res # Se regresa el valor 

# Se usa esta función si lo que se tiene es el PH de la solución
def get_H(H):
    # Se usan diccionarios para guardar toda la información correspondiente 
    res = {}
    res['pH'] = np.log10(H)
    res['pOH'] = 14 - res['pH']
    res['H+'] = H
    res['OH-'] = (1e-14) / H
    res['Tipo'] = _tipoPH(res['pH'], res['pOH'],res['H+'] ,res['OH-'])
    res['Concentración'] = _getConcentracion(res['H+'], res['OH-'])

    return res # Se regresa el valor 

# Se usa esta función si lo que se tiene es el PH de la solución
def get_OH(OH):
    # Se usan diccionarios para guardar toda la información correspondiente 
    res = {}
    pOH = np.log10(OH) * -1
    res['pH'] = 14 - pOH
    res['pOH'] = np.log10(OH) * -1
    res['H+'] = (1e-14) / OH
    res['OH-'] = OH
    res['Tipo'] = _tipoPH(res['pH'], res['pOH'],res['H+'] ,res['OH-'])
    res['Concentración'] = _getConcentracion(res['H+'], res['OH-'])

    return res # Se regresa el valor 