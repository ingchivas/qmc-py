import numpy as np

def _tipoPH(pH, pOH, H, OH):
    if (pH < 7 and pOH > 7) and (H > OH) == True:
        return ("ácido")
    elif pH == 7 or pOH == 7:
        return ("neutra")
    else:
        return ("base")

def _getConcentracion(H, OH):
    return (H*OH),3

def get_pH(pH):
    res = {}
    res['pH'] = pH
    res['pOH'] = 14 - pH
    res['H+'] = 10**(-pH)
    res['OH-'] = 10**(-res['pOH'])
    res['Tipo'] = _tipoPH(res['pH'], res['pOH'],res['H+'] ,res['OH-'])
    res['Concentración'] = _getConcentracion(res['H+'], res['OH-'])

    return res

def get_pOH(pOH):
    res = {}
    res['pH'] = 14 - pOH
    res['pOH'] = pOH
    res['H+'] = 10**(-res['pH'])
    res['OH-'] = 10**(-res['pOH'])
    res['Tipo'] = _tipoPH(res['pH'], res['pOH'],res['H+'] ,res['OH-'])
    res['Concentración'] = _getConcentracion(res['H+'], res['OH-'])

    return res

def get_H(H):
    res = {}
    res['pH'] = np.log10(H)
    res['pOH'] = 14 - res['pH']
    res['H+'] = H
    res['OH-'] = (1e-14) / H
    res['Tipo'] = _tipoPH(res['pH'], res['pOH'],res['H+'] ,res['OH-'])
    res['Concentración'] = _getConcentracion(res['H+'], res['OH-'])

    return res

def get_OH(OH):
    res = {}
    pOH = np.log10(OH) * -1
    res['pH'] = 14 - pOH
    res['pOH'] = np.log10(OH) * -1
    res['H+'] = (1e-14) / OH
    res['OH-'] = OH
    res['Tipo'] = _tipoPH(res['pH'], res['pOH'],res['H+'] ,res['OH-'])
    res['Concentración'] = _getConcentracion(res['H+'], res['OH-'])

    return res

print(get_H(10))
print(get_pH(10))
print(get_OH(10))
print(get_pOH(10))