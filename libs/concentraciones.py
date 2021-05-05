import numpy as np
from gases import _convervol

def _convermasa(masa, u_masa):
    if u_masa == 'g':
        pass
    elif u_masa == 'mg':
        masa /= 1 * (10**3)
    elif u_masa == 'kg':
        masa *= 1000
    
    return masa

def get_masa(m_soluto, m_solvente, u_masa = 'g'):
    m_soluto = _convermasa(m_soluto,u_masa)
    m_solvente = _convermasa(m_solvente,u_masa)

    msolucion = m_soluto + m_solvente

    return msolucion

def get_masap(p_masa,m_soluto,u_masa='g'):
    m_soluto = _convermasa(m_soluto,u_masa)
    msolucion = (m_soluto / p_masa) * 100

    return msolucion

def get_msoluto(p_masa, m_solucion,u_masa='g'):
    m_solucion = _convermasa(m_solucion)

    msoluto = (msolucion * porcenmasa) / 100

    return msoluto

def get_msolvente(p_masa,m_solucion, u_masa = 'g'):
    m_solucion = _convermasa(m_solucion)

    msolvente = ((msoluto * 100) - (porcenmasa * msoluto)) / porcenmasa

    return msolvente

def get_pmasa(m_soluto,m_solucion, u_masa = 'g'):#Si sabemos m_solucion
    m_solucion = _convermasa(m_solucion)
    m_soluto = _convermasa(m_soluto)

    porcenmasa = (msoluto / msolucion) * 100
    
    return porcenmasa

def get_pmasas(m_soluto, m_solvente, u_masa = 'g'):
    m_soluto = _convermasa(m_soluto,u_masa)
    m_solvente = _convermasa(m_solvente,u_masa)

    porcenmasa = (msoluto / (msoluto + msolvente)) * 100
    return porcenmasa

def get_volumen(v_soluto, v_solvente, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto, u_volumen)
    v_solvente = _convervol(v_solvente, u_volumen)

    vsolucion = v_soluto + v_solvente
    return vsolucion

def get_volumenP(v_soluto, p_volumen, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto, u_volumen)
    vsolucion = (v_soluto / p_volumen) * 100

    return vsolucion

def get_vsoluto(v_solucion, p_volumen, u_volumen = 'L'):
    v_solucion = _convervol(v_solucion, u_volumen)

    vsoluto = (v_solucion * p_volumen) / 100
    return vsoluto

def get_vsolvente(v_soluto,p_volumen, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto,u_volumen)

    vsolvente = ((v_soluto * 100) - (p_volumen * v_soluto)) / p_volumen

    return vsolvente

def get_pvolumen(v_solucion, v_soluto, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto,u_volumen)
    v_solucion = _convervol(v_solucion,u_volumen)

    porcenvolumen = (v_soluto / v_solucion) * 100
    return porcenvolumen

def get_pvolumen(v_soluto, v_solvente, u_volumen = 'L'):
    v_soluto = _convervol(v_soluto,u_volumen)
    v_solvente = _convervol(v_solvente,u_volumen)

    porcenvolumen = (v_soluto / (v_soluto + v_solvente)) * 100
    return porcenvolumen

    