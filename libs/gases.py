# Importamos las librerías que vamos a utilizar
import math
import numpy as np

# Esta función se utiliza para convertir los volumenes. 
def _convervol(v, unidadesvol):
    if unidadesvol == 'ml': # Se convierte el volumen de mililitros a litros
        v /= 1000
    elif unidadesvol == 'L': # Se deja el volumen de litros
        pass
    elif unidadesvol == 'm3': # Se convierte el volumen de metros cúbicos a litros
        v *= 1000
    elif unidadesvol == 'cm3': # Se convierte el volumen de centímetros cúbicos a litros
        v /= 1000

    return v # Se regresa el valor asignado

# Esta función se utiliza para la conversión de presión
def _converpres(p, unidadespres): 
    if unidadespres == 'pa': # Se convierte la presión de pascales a atmósferas
        p /= 101, 300

    elif unidadespres == 'atm': # Se deja la presión en atmósferas
        pass
    elif unidadespres == 'mmhg': # Se convierte la presión de milímetros de mercurio a atmósferas
        p /= 760

    return p # Se regresa el valor asignado

# Esta función se utiliza para la conversión de temperaturas
def _convertemp(t, unidadestemp): 
    if unidadestemp == 'C': # Se convierte la temperatura de celsius a Kelvin
        t += 273
    elif unidadestemp == 'F': # Se convierte la temperatura de Farenheit a Kelvin
        t = (((t - 32) * (5 / 9)) + 273)
    elif unidadestemp == 'k': # Se deja la temperatura en Kelvin
        pass

    return t # Se regresa el valor asignado

# Esta función sirve para hacer asignaciones de valores que se ocuparán posteriormente
def _cumpleBoyle(p1,p2,v1,v2):
    p1v1 = p1 * v1
    p2v2 = p2 * v2

    return p1v1==p2v2 # Regresa un valor booleano indicando si es falso o verdadero

# Esta función sirve para hacer asignaciones de valores que se ocuparán posteriormente
def _cumpleLussac(p1,p2,t1,t2):
    p1_t1 = float(p1) / float(t1)
    p2_t2 = float(p2) / float(t2)

    return p1_t1==p2_t2 # Regresa un valor booleano indicando si es falso o verdadero

# Esta función sirve para hacer asignaciones de valores que se ocuparán posteriormente
def _cumpleCharles(t1,t2,v1,v2):
    v1_t1 = float(v1) / float(t1)
    v2_t2 = float(v2) / float(t2)

    return v1_t1 == v2_t2 # Regresa un valor booleano indicando si es falso o verdadero
    
# Esta función sirve para hacer asignaciones de valores que se ocuparán posteriormente
def _cumpleComb(t1,t2,v1,v2,p1,p2):
    p1v1_t1 = (float(p1) * float(v1)) / float(t1)
    p2v2_t2 = (float(p2) * float(v2)) / float(t2)

    return p1v1_t1	== p2v2_t2 # Regresa un valor booleano indicando si es falso o verdadero

# Esta función sirve para asignar los resultados de funciones anteriores relacionado con Boyle [p1]
def BoyleP1(v1,v2,p2, unidadesvol = 'L', unidadespres = 'atm'):
    v1 = _convervol(v1,unidadesvol) 
    v2 = _convervol(v2,unidadesvol)
    p2 = _converpres(p2,unidadespres)

    p1 = (p2 * v2) / v1 
 
    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['p1']=p1
    resultado['CumpleLey'] = _cumpleBoyle(p1,p2,v1,v2)

    return resultado # Regresa el resultado


# Esta función sirve para asginar los resultado de funciones anteriores relacionado con Boyle [p2]
def BoyleP2(v1,v2,p1, unidadesvol = 'L', unidadespres = 'atm'):
    v1 = _convervol(v1,unidadesvol)
    v2 = _convervol(v2,unidadesvol)
    p1 = _converpres(p1,unidadespres)

    p2 = (p1 * v1) / v2

    # Se crean de igual forma los resultados correspondientes y se guardan en un diccionario
    resultado = {}
    resultado['p2']=p2
    resultado['CumpleLey'] = _cumpleBoyle(p1,p2,v1,v2)

    return resultado # Regresa el resultado


# Esta funcion sirve para asignar los resultados de funciones anteriores relacionado con Boyle [v1]
def BoyleV1(v2,p1,p2, unidadesvol = 'L', unidadespres = 'atm'):
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)
    v2 = _convervol(v2,unidadesvol)

    v1 = (p2 * v2) / p1

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['v1']=v1
    resultado['CumpleLey'] = _cumpleBoyle(p1,p2,v1,v2)

    return resultado # Se regresa el resultado

# Esta funcion sirve para asignar los resultados de funciones anteriores relacionado con Boyle[v2]
def BoyleV2(v1,p1,p2, unidadesvol = 'L', unidadespres = 'atm'):
    v1 = _convervol(v1,unidadesvol)
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)

    v2 = (p1 * v1) / p2

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['v2']=v2
    resultado['CumpleLey'] = _cumpleBoyle(p1,p2,v1,v2)

    return resultado # Se regresa el resultado


# Esta función sirve para asginar los resultado de funciones anteriores relacionado con Lussac [p1]
def LussacP1(t1,t2,p2, unidadespres = 'atm', unidadestemp = 'k'):
    t1 = _convertemp(t1,unidadestemp)
    t1 = _convertemp(t1,unidadestemp)
    p2 = _converpres(p2,unidadespres)

    p1 = (p2 / t2) * t1

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['p1']=p1
    resultado['CumpleLey'] = _cumpleLussac(p1,p2,t1,t2)

    return resultado # Se regresa el resultado

# Esta función sirve para asignar los resultados de funciones anteriores relacionado con Lussac [p2]
def LussacP2(t1,t2,p1, unidadespres = 'atm', unidadestemp = 'k'):
    t1 = _convertemp(t1,unidadestemp)
    t1 = _convertemp(t1,unidadestemp)
    p1 = _converpres(p1,unidadespres)

    p2 = (p1 * t2) / t1

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['p2']=p2
    resultado['CumpleLey'] = _cumpleLussac(p1,p2,t1,t2)

    return resultado # Se regresa el resultado

# Esta función sirve para asginar los resultados de funciones anteriores relacionado con Lussac [t1]
def LussacT1(t2,p1,p2, unidadespres = 'atm', unidadestemp = 'k'):
    t2 = _convertemp(t2,unidadestemp)
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)

    t1 = (p1 * t2) / p2

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['t1']=t1
    resultado['CumpleLey'] = _cumpleLussac(p1,p2,t1,t2)

    return resultado # Se regresa el resultado


# Esta función sirve para asignar los resultados de funciones anteriores relacionado con Lussac [t2]
def LussacT2(t1,p1,p2, unidadespres = 'atm', unidadestemp = 'k'):
    t1 = _convertemp(t1,unidadestemp)
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)

    t2 = (p2 * t1) / p1

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['t2']=t2
    resultado['CumpleLey'] = _cumpleLussac(p1,p2,t1,t2)

    return resultado # Se regresa el resultado

# Esta función sirve para asignar los resultados de funciones anteriores relacionado con Charles [v1]
def CharlesV1(t1,t2,v2, unidadesvol = 'L', unidadestemp = 'k'):
    t1 = _convertemp(t1,unidadestemp)
    t2 = _convertemp(t2,unidadestemp)
    v2 = _convervol(v2, unidadesvol)

    v1 = (v2 / t2) * t1

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['v1']=v1
    resultado['CumpleLey'] = _cumpleCharles(t1,t2,v1,v2)

    return resultado # Se regresa el resultado


# Esta función sirve para asignar los resultados de funciones anteriores relacionado con Charles [v2]
def CharlesV2(t1,t2,v1, unidadesvol = 'L', unidadestemp = 'k'):
    t1 = _convertemp(t1,unidadestemp)
    t2 = _convertemp(t2,unidadestemp)
    v1 = _convervol(v1, unidadesvol)

    v2 = (v1 * t2) / t1

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['v2']=v2
    resultado['CumpleLey'] = _cumpleCharles(t1,t2,v1,v2)

    return resultado # Se regresa el resultado


# Esta función sirve para asignar los resultado de funciones anteriores relacionado con Charles [t1]
def CharlesT1(t2,v1,v2, unidadesvol = 'L', unidadestemp = 'k'):
    t2 = _convertemp(t2,unidadestemp)
    v1 = _convervol(v1,unidadesvol)
    v2 = _convervol(v2, unidadesvol)

    t1 = (v1 * t2) / v2

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['t1']=t1
    resultado['CumpleLey'] = _cumpleCharles(t1,t2,v1,v2)

    return resultado # Se regresa el resultado

# Esta función sirve para asignar los resultados de funciones anteriores relacionado con Charles [t2]
def CharlesT2(t1,v1,v2, unidadesvol = 'L', unidadestemp = 'k'):
    t1 = _convertemp(t1,unidadestemp)
    v1 = _convervol(v1,unidadesvol)
    v2 = _convervol(v2, unidadesvol)

    t2 = (v2 * t1) / v1

    # Se crean los resultados y se guardan en un diccionario 
    resultado = {}
    resultado['t2']=t2
    resultado['CumpleLey'] = _cumpleCharles(t1,t2,v1,v2)

    return resultado # Se regresa el resultado

# Esta función sirve para asignar los resultados de funciones anteriores relacionado con LeyComb [p1]
def LeyCombP1(t1,t2,v1,v2,p2, unidadesvol = 'L', unidadestemp = 'k', unidadespres = 'atm'):
    t1 = _convertemp(t1,unidadestemp)
    t2 = _convertemp(t2,unidadestemp)
    v1 = _convervol(v1,unidadesvol)
    v2 = _convervol(v2, unidadesvol)
    p2 = _converpres(p2,unidadespres)

    p1 = ((p2 * v2 * t1) / (t2 * v1))
    
    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['p1'] = p1
    resultado['CumpleLey'] = _cumpleComb(t1,t2,v1,v2,p1,p2)

    return resultado # Se regresa el resultado

# Esta función sirve para asignar los resultados de funciones anteriores relacionado con LeyComb [p2]
def LeyCombP2(t1,t2,v1,v2,p1, unidadesvol = 'L', unidadestemp = 'k', unidadespres = 'atm'):
    t1 = _convertemp(t1,unidadestemp)
    t2 = _convertemp(t2,unidadestemp)
    v1 = _convervol(v1,unidadesvol)
    v2 = _convervol(v2, unidadesvol)
    p1 = _converpres(p1,unidadespres)

    p2 = (p1 * v1 * t2) / (t1 * v2)

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['p2'] = p2
    resultado['CumpleLey'] = _cumpleComb(t1,t2,v1,v2,p1,p2)

    return resultado # Se regresa el resultado

# Esta función sirve para asignar los resultados de funciones anteriores relacionado con LeyComb [v1]
def LeyCombV1(t1,t2,v2,p1,p2, unidadesvol = 'L', unidadestemp = 'k', unidadespres = 'atm'):
    t1 = _convertemp(t1,unidadestemp)
    t2 = _convertemp(t2,unidadestemp)
    v2 = _convervol(v2, unidadesvol)
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)

    v1 = (p2 * v2 * t1) / (p1 * t2)

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['v1'] = v1
    resultado['CumpleLey'] = _cumpleComb(t1,t2,v1,v2,p1,p2)

    return resultado # Se regresa el resultado

# Esta función sirve para asignar los resultados de funciones anteriores relacionado con LeyComb [v2]
def LeyCombV2(t1,t2,v1,p1,p2, unidadesvol = 'L', unidadestemp = 'k', unidadespres = 'atm'):
    t1 = _convertemp(t1,unidadestemp)
    t2 = _convertemp(t2,unidadestemp)
    v1 = _convervol(v1, unidadesvol)
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)

    v2 = (p1 * v1 * t2) / (t1 * p2)

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['v2'] = v2
    resultado['CumpleLey'] = _cumpleComb(t1,t2,v1,v2,p1,p2)

    return resultado # Se regresa el resultado

# Esta función sirve para asignar los resultados de funciones anteriores relacionado con LeyComb [t1]
def LeyCombT1(t2,v1,v2,p1,p2, unidadesvol = 'L', unidadestemp = 'k', unidadespres = 'atm'):
    t2 = _convertemp(t2,unidadestemp)
    v1 = _convervol(v1, unidadesvol)
    v2 = _convervol(v2, unidadesvol)
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)

    t1 = (p1 * v1 * t2) / (p2 * v2)
    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['t1'] = t1
    resultado['CumpleLey'] = _cumpleComb(t1,t2,v1,v2,p1,p2)

    return resultado # Se regresa el resultado

# Esta función sirve para asignar los resultados de funciones anteriores relacionado con LeyComb [t2]
def LeyCombT2(t1,v1,v2,p1,p2, unidadesvol = 'L', unidadestemp = 'k', unidadespres = 'atm'):
    t1 = _convertemp(t1,unidadestemp)
    v1 = _convervol(v1, unidadesvol)
    v2 = _convervol(v2, unidadesvol)
    p1 = _converpres(p1,unidadespres)
    p2 = _converpres(p2,unidadespres)

    t2 = (p2 * v2 * t1) / (p1 * v1)

    # Se crean los resultado y se guardan en un diccionario 
    resultado = {}
    resultado['t2'] = t2
    resultado['CumpleLey'] = _cumpleComb(t1,t2,v1,v2,p1,p2)

    return resultado # Se regresa el resultado

# print(BoyleP2(28,15,12, unidadespres='atm'))
# print(LussacP1(18686532121100,1070,108768680))

