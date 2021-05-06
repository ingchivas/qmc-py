import numpy as np
from .gases import _convervol

def _convermasa(masa, u_masa):
    if u_masa == 'g':
        pass
    elif u_masa == 'mg':
        masa /= 1 * (10**3)
    elif u_masa == 'kg':
        masa *= 1000
    
    return masa

def masa_masasolucion(m_soluto, m_solvente, u_masa = 'g'):
    m_soluto = _convermasa(m_soluto,u_masa)
    m_solvente = _convermasa(m_solvente,u_masa)

    msolucion = m_soluto + m_solvente

    return msolucion

def masa_masasolucionp(p_masa,m_soluto,u_masa='g'):
    m_soluto = _convermasa(m_soluto,u_masa)
    msolucion = (m_soluto / p_masa) * 100

    return msolucion

def masa_msoluto(p_masa, m_solucion,u_masa='g'):
    m_solucion = _convermasa(m_solucion)

    msoluto = (m_solucion * p_masa) / 100

    return msoluto

def masa_msolvente(p_masa,m_soluto, u_masa = 'g'):
    m_soluto = _convermasa(m_soluto)

    msolvente = ((m_soluto * 100) - (p_masa * m_soluto)) / p_masa

    return msolvente

def masa_pmasa(m_soluto,m_solucion, u_masa = 'g'):#Si sabemos m_solucion
    m_solucion = _convermasa(m_solucion)
    m_soluto = _convermasa(m_soluto)

    porcenmasa = (m_soluto / m_solucion) * 100
    
    return porcenmasa

def masa_pmasas(m_soluto, m_solvente, u_masa = 'g'):
    m_soluto = _convermasa(m_soluto,u_masa)
    m_solvente = _convermasa(m_solvente,u_masa)

    porcenmasa = (m_soluto / (m_soluto + m_solvente)) * 100
    return porcenmasa

def vol_vsolucion(v_soluto, v_solvente, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto, u_volumen)
    v_solvente = _convervol(v_solvente, u_volumen)

    vsolucion = v_soluto + v_solvente
    return vsolucion

def vol_vsolucionP(v_soluto, p_volumen, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto, u_volumen)
    vsolucion = (v_soluto / p_volumen) * 100

    return vsolucion

def vol_vsoluto(v_solucion, p_volumen, u_volumen = 'L'):
    v_solucion = _convervol(v_solucion, u_volumen)

    vsoluto = (v_solucion * p_volumen) / 100
    return vsoluto

def vol_vsolvente(v_soluto,p_volumen, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto,u_volumen)

    vsolvente = ((v_soluto * 100) - (p_volumen * v_soluto)) / p_volumen

    return vsolvente

def vol_pvolumen(v_solucion, v_soluto, u_volumen = 'L'):
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
    gr = c_pesolitro * v_solucion
    return gr

def pl_litros(m_soluto, c_pesolitro, u_masa = 'g'):
    m_soluto = _convermasa(m_soluto, u_masa)

    l = m_soluto / c_pesolitro
    return l

def pl_gl(m_soluto, v_solucion, u_masa = 'g', u_volumen = 'L'):
    v_solucion = _convervol(v_solucion, u_volumen)
    m_soluto = _convermasa(m_soluto,u_masa)

    gramolitro = m_soluto/v_solucion
    return gramolitro

def molaridad_msoluto(m_molecular,v, molaridad, u_volumen = 'L' ):
    v = _convervol(v, u_volumen)
    gr = molaridad * m_molecular * v
    return gr

def molaridad_mmolecular(m_soluto, v, molaridad, u_masa = 'g', u_volumen = 'L'):
    v = _convervol(v, u_volumen)
    m_soluto=_convermasa(m_soluto, u_masa)
    Mm = m_soluto / (molaridad * v)

    return Mm

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

def moles_molaridadM(moles, v , u_volumen='L'):
    v=_convervol(v, u_volumen)
    molaridad = v*moles

    return molaridad

