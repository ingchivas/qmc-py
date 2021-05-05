import math
import numpy as np

def _convervol(v, unidadesvol):
    if unidadesvol == 'ml':
        v /= 1000
    elif unidadesvol == 'l':
        pass
    elif unidadesvol == 'm3':
        v *= 1000
    elif unidadesvol == 'cm3':
        v /= 1000

    return v

def _converpres(p, unidadespres):
    if unidadespres == 'pa':
        p /= 101, 300

    elif unidadespres == 'atm':
        pass
    elif unidadespres == 'mmhg':
        p /= 760

    return p

def _convertemp(t, unidadestemp):
    if unidadestemp == 'C':
        t += 273
    elif unidadestemp == 'F':
        t = (((t - 32) * (5 / 9)) + 273)
    elif unidadestemp == 'k':
        pass

    return t

def _cumpleBoyle(p1,p2,v1,v2):
    p1v1 = p1 * v1
    p2v2 = p2 * v2

    return p1v1==p2v2

def _cumpleLussac(p1,p2,t1,t2):
    p1_t1 = float(p1) / float(t1)
    p2_t2 = float(p2) / float(t2)

    return p1_t1==p2_t2


def BoyleP1(v1,v2,p2, unidadesvol = 'L', unidadespres = 'atm'):
    v1 = _convervol(v1,unidadesvol)
    v2 = _convervol(v2,unidadesvol)
    p2 = _converpres(p2,unidadespres)

    p1 = (p2 * v2) / v1

    resultado = {}
    resultado['p1']=p1
    resultado['CumpleLey'] = _cumpleBoyle(p1,p2,v1,v2)

    return resultado

def BoyleP2(v1,v2,p1, unidadesvol = 'L', unidadespres = 'atm'):
    v1 = _convervol(v1,unidadesvol)
    v2 = _convervol(v2,unidadesvol)
    p1 = _converpres(p1,unidadespres)

    p2 = (p1 * v1) / v2

    resultado = {}
    resultado['p2']=p2
    resultado['CumpleLey'] = _cumpleBoyle(p1,p2,v1,v2)

    return resultado

def BoyleV1(v2,p1,p2, unidadesvol = 'L', unidadespres = 'atm'):
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)
    v2 = _convervol(v2,unidadesvol)

    v1 = (p2 * v2) / p1

    resultado = {}
    resultado['v1']=v1
    resultado['CumpleLey'] = _cumpleBoyle(p1,p2,v1,v2)

    return resultado

def BoyleV2(v1,p1,p2, unidadesvol = 'L', unidadespres = 'atm'):
    v1 = _convervol(v1,unidadesvol)
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)

    v2 = (p1 * v1) / p2

    resultado = {}
    resultado['v2']=v2
    resultado['CumpleLey'] = _cumpleBoyle(p1,p2,v1,v2)

    return resultado

def LussacP1(t1,t2,p2, unidadespres = 'atm', unidadestemp = 'k'):
    t1 = _convertemp(t1,unidadestemp)
    t1 = _convertemp(t1,unidadestemp)
    p2 = _converpres(p2,unidadespres)

    p1 = (p2 / t2) * t1

    resultado = {}
    resultado['p1']=p1
    resultado['CumpleLey'] = _cumpleLussac(p1,p2,t1,t2)

    return resultado

def LussacP2(t1,t2,p1, unidadespres = 'atm', unidadestemp = 'k'):
    t1 = _convertemp(t1,unidadestemp)
    t1 = _convertemp(t1,unidadestemp)
    p1 = _converpres(p1,unidadespres)

    p2 = (p1 * t2) / t1

    resultado = {}
    resultado['p2']=p2
    resultado['CumpleLey'] = _cumpleLussac(p1,p2,t1,t2)

    return resultado

def LussacT1(t2,p1,p2, unidadespres = 'atm', unidadestemp = 'k'):
    t2 = _convertemp(t2,unidadestemp)
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)

    t1 = (p1 * t2) / p2

    resultado = {}
    resultado['t1']=t1
    resultado['CumpleLey'] = _cumpleLussac(p1,p2,t1,t2)

    return resultado

def LussacT2(t1,p1,p2, unidadespres = 'atm', unidadestemp = 'k'):
    t1 = _convertemp(t1,unidadestemp)
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)

    t2 = (p2 * t1) / p1

    resultado = {}
    resultado['t2']=t2
    resultado['CumpleLey'] = _cumpleLussac(p1,p2,t1,t2)

    return resultado


# print(BoyleP2(28,15,12, unidadespres='atm'))
# print(LussacP1(18686532121100,1070,108768680))

