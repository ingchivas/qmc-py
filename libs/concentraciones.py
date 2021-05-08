import numpy as np
from .gases import _convervol

def _getpeq(m_molecular, carga):
    peso_eq = m_molecular / carga
    return peso_eq

def _convermasa(masa, u_masa = 'g', u_masaout = 'g'):
    if u_masa == 'g' and u_masaout == 'g':
        pass
    elif u_masa != 'g' and u_masaout == 'mg':
        masa /= 1 * (10**3)
    elif u_masa != 'g' and u_masaout == 'kg':
        masa *= 1000
    return masa

def _convermasaKG(masa, u_masa):
    if u_masa == 'g':
        masa /= 1000
    elif u_masa == 'mg':
        masa /= 1 * (10**6)
    elif u_masa == 'kg':
        pass
    
    return masa

def masa_masasolucion(m_soluto, m_solvente, u_masa = 'g'):
    m_soluto = _convermasa(m_soluto,u_masa)
    m_solvente = _convermasa(m_solvente,u_masa)

    m_solucion = m_soluto + m_solvente

    return m_solucion

def masa_masasolucionp(p_masa,m_soluto,u_masa='g'):
    m_soluto = _convermasa(m_soluto,u_masa)
    m_solucion = (m_soluto / p_masa) * 100

    return m_solucion

def masa_msoluto(p_masa, m_solucion,u_masa='g'):
    m_solucion = _convermasa(m_solucion,u_masa)

    msoluto = (m_solucion * p_masa) / 100

    return msoluto

def masa_msolvente(p_masa,m_soluto, u_masa = 'g'):
    m_soluto = _convermasa(m_soluto, u_masa)

    m_solvente = ((m_soluto * 100) - (p_masa * m_soluto)) / p_masa

    return m_solvente

def masa_pmasaS(m_soluto,m_solucion, u_masa = 'g'):#Si sabemos m_solucion
    m_solucion = _convermasa(m_solucion, u_masa)
    m_soluto = _convermasa(m_soluto, u_masa)

    porcenmasa = (m_soluto / m_solucion) * 100
    
    return porcenmasa

def masa_pmasa(m_soluto, m_solvente, u_masa = 'g'):
    m_soluto = _convermasa(m_soluto,u_masa)
    m_solvente = _convermasa(m_solvente,u_masa)

    porcenmasa = (m_soluto / (m_soluto + m_solvente)) * 100
    return porcenmasa

def vol_vsolucion(v_soluto, v_solvente, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto, u_volumen)
    v_solvente = _convervol(v_solvente, u_volumen)

    v_solucion = v_soluto + v_solvente
    return v_solucion

def vol_vsolucionP(v_soluto, p_volumen, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto, u_volumen)
    v_solucion = (v_soluto / p_volumen) * 100

    return v_solucion

def vol_vsoluto(v_solucion, p_volumen, u_volumen = 'L'):
    v_solucion = _convervol(v_solucion, u_volumen)

    v_soluto = (v_solucion * p_volumen) / 100
    return v_soluto

def vol_vsolvente(v_soluto,p_volumen, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto,u_volumen)

    v_solvente = ((v_soluto * 100) - (p_volumen * v_soluto)) / p_volumen

    return v_solvente

def vol_pvolumenS(v_solucion, v_soluto, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto,u_volumen)
    v_solucion = _convervol(v_solucion,u_volumen)

    porcenvolumen = (v_soluto / v_solucion) * 100
    return porcenvolumen

def vol_pvolumen(v_soluto, v_solvente, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto,u_volumen)
    v_solvente = _convervol(v_solvente,u_volumen)

    porcenvolumen = (v_soluto / (v_soluto + v_solvente)) * 100
    return porcenvolumen

def pl_msoluto(c_pesolitro, v_solucion, u_volumen = 'L'):
    v_solucion = _convervol(v_solucion, u_volumen)
    m_soluto = c_pesolitro * v_solucion
    return m_soluto

def pl_litros(m_soluto, c_pesolitro, u_masa = 'g'):
    m_soluto = _convermasa(m_soluto, u_masa)

    l_solucion = m_soluto / c_pesolitro
    return l_solucion

def pl_gl(m_soluto, v_solucion, u_masa = 'g', u_volumen = 'L'):
    v_solucion = _convervol(v_solucion, u_volumen)
    m_soluto = _convermasa(m_soluto,u_masa)

    gramolitro = m_soluto/v_solucion
    return gramolitro

def molaridad_msoluto(m_molecular,v, molaridad, u_volumen = 'L' ):
    v = _convervol(v, u_volumen)
    m_soluto = molaridad * m_molecular * v
    return m_soluto

def molaridad_mmolecular(m_soluto, v, molaridad, u_masa = 'g', u_volumen = 'L'):
    v = _convervol(v, u_volumen)
    m_soluto=_convermasa(m_soluto, u_masa)
    m_molecular = m_soluto / (molaridad * v)

    return m_molecular

def molaridad_volumenM(moles, molaridad):
    v = moles * molaridad
    return v

def molaridad_volumen(m_soluto, molaridad, m_molecular, u_masa = 'g'):
    m_soluto=_convermasa(m_soluto, u_masa)

    v = m_soluto/(m_molecular*molaridad)
    return v

def molaridad_moles(v, molaridad, u_volumen = 'L'):
    v = _convervol(v, u_volumen)
    moles = molaridad*v
    return moles

def molaridad_molesM(moles, v , u_volumen='L'):
    v=_convervol(v, u_volumen)
    molaridad = v*moles

    return molaridad

def normal_msolutoPEQ(peso_eq, v,normal, u_volumen = 'L' ):
    v = _convervol(v, u_volumen)

    m_soluto = normal*peso_eq*v
    return m_soluto

def normal_msoluto(m_molecular, carga, v,normal, u_volumen = 'L'):
    v = _convervol(v, u_volumen)
    peso_eq = _getpeq(m_molecular, carga)
    m_soluto = normal*peso_eq*v

    return m_soluto

def normal_peq(m_soluto, v, normal, u_masa = 'g', u_volumen = 'L'):
    v = _convervol(v, u_volumen)
    m_soluto = _convermasa(m_soluto, u_masa)

    peso_eq = m_soluto/(normal*v)
    return peso_eq

def normal_normalPEQ(peso_eq, m_soluto, v, u_masa = 'g', u_volumen = 'L'):
    v = _convervol(v, u_volumen)
    m_soluto = _convermasa(m_soluto, u_masa)

    normal = m_soluto / (peso_eq*v)
    return normal

def normal_normal(m_molecular, m_soluto,carga, v, u_masa = 'g', u_volumen = 'L'):
    v = _convervol(v, u_volumen)
    m_soluto = _convermasa(m_soluto, u_masa)
    peso_eq = _getpeq(m_molecular, carga)

    normal = m_soluto / (peso_eq*v)
    return normal

def molal_msoluto(m_molecular, m_solvente, molal, u_masa = 'g'):
    m_solvente = _convermasaKG(m_solvente, u_masa)
    m_soluto = molal * m_molecular * m_solvente

    return m_soluto

def molal_msolvente(m_molecular, m_soluto, molal, u_masa = 'g'):
    m_soluto = _convermasa(m_soluto, u_masa)

    m_solvente = m_soluto/(molal*m_molecular)
    return m_solvente

def molal_mmolecular(m_soluto, m_solvente, molal, u_masasoluto = 'g', u_masasolvente = 'kg'):
    m_soluto=_convermasa(m_soluto, u_masasoluto)
    m_solvente = _convermasaKG(m_solvente, u_masasolvente)

    m_molecular = m_soluto/(molal * m_solvente)
    return m_molecular

def molal_molal(m_soluto, m_solvente, m_molecular, u_masasoluto = 'g', u_masasolvente = 'kg'):
    m_soluto=_convermasa(m_soluto, u_masasoluto)
    m_solvente = _convermasaKG(m_solvente, u_masasolvente)

    molal = m_soluto/(m_molecular*m_solvente)
    return molal

def frac_molal(*concentraciones):
    try:
        mol_total = sum(float(i) for i in concentraciones)
        res = {}
        for k in range(len(concentraciones)):
            res['C{}'.format(k+1)] = np.round(concentraciones[k]/mol_total,3)
        return res

    except:
        return 'Revisa los datos, deben ser tipo int o float'

def ppm_msoluto(v, ppm, u_volumen = 'L'):#regresa mg
    v = _convervol(v, u_volumen)

    m_soluto = (ppm * v)/ (1 * (10**6))
    return m_soluto

def ppm_vol(m_soluto, ppm, u_masa = 'mg'):
    m_soluto = _convermasa(m_soluto, u_masa, u_masaout = 'mg')
    vol = (m_soluto* 1000000) / ppm
    return vol

def ppm_ppm(m_soluto, v, u_volumen = 'L', u_masa = 'mg'):
    m_soluto = _convermasa(m_soluto, u_masa, u_masaout = 'mg')
    v = _convervol(v, u_volumen)

    ppm = (m_soluto / v) * 1000000
    return ppm
