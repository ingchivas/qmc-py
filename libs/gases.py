# Importamos las librerías que vamos a utilizar
import math
import numpy as np

# Esta función se utiliza para convertir los volumenes. 
def _convervol(v, unidadesvol):
    '''
    ```_convervol(v, unidadesvol)```

    Método auxiliar que convierte un valor de volumen de la unidad argumento a Litros.
    Las unidades soportadas se encuentran en los docs.


    Regresa un float.

    Uso:

    ```python
    gases._convervol(1000,'ml')

    ```
    Regresa:

    ```python
    1.0
    ```

    '''
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
    '''
    ```_converpres(p, unidadespres)```

    Método auxiliar que convierte un valor de presión de la unidad argumento a atmósferas.
    Las unidades soportadas se encuentran en los docs.

    Regresa un float.

    Uso:

    ```python
    gases._converpres(760,'mmhg')

    ```
    Regresa:

    ```python
    1.0
    ```

    '''
    if unidadespres == 'pa': # Se convierte la presión de pascales a atmósferas
        p /= 101, 300

    elif unidadespres == 'atm': # Se deja la presión en atmósferas
        pass
    elif unidadespres == 'mmhg': # Se convierte la presión de milímetros de mercurio a atmósferas
        p /= 760

    return p # Se regresa el valor asignado

# Esta función se utiliza para la conversión de temperaturas
def _convertemp(t, unidadestemp): 
    '''
    ```_convertemp(t, unidadestemp)```

    Método auxiliar que convierte un valor de temperatura de la unidad argumento a kelvin.
    Las unidades soportadas se encuentran en los docs.

    Regresa un float.

    Uso:

    ```python
    gases._convertemp(0,'C')

    ```
    Regresa:

    ```python
    273.15
    ```

    '''
    if unidadestemp == 'C': # Se convierte la temperatura de celsius a Kelvin
        t += 273.15
    elif unidadestemp == 'F': # Se convierte la temperatura de Farenheit a Kelvin
        t = (((t - 32) * (5 / 9)) + 273)
    elif unidadestemp == 'k': # Se deja la temperatura en Kelvin
        pass

    return t # Se regresa el valor asignado

# Esta función sirve para hacer asignaciones de valores que se ocuparán posteriormente
def _cumpleBoyle(p1,p2,v1,v2):
    '''
    Método auxiliar que indica si se cumple la ley 
    '''
    p1v1 = p1 * v1
    p2v2 = p2 * v2

    return p1v1==p2v2 # Regresa un valor booleano indicando si es falso o verdadero

# Esta función sirve para hacer asignaciones de valores que se ocuparán posteriormente
def _cumpleLussac(p1,p2,t1,t2):
    '''
    Método auxiliar que indica si se cumple la ley 
    '''
    p1_t1 = float(p1) / float(t1)
    p2_t2 = float(p2) / float(t2)

    return p1_t1==p2_t2 # Regresa un valor booleano indicando si es falso o verdadero

# Esta función sirve para hacer asignaciones de valores que se ocuparán posteriormente
def _cumpleCharles(t1,t2,v1,v2):
    '''
    Método auxiliar que indica si se cumple la ley 
    '''
    v1_t1 = float(v1) / float(t1)
    v2_t2 = float(v2) / float(t2)

    return v1_t1 == v2_t2 # Regresa un valor booleano indicando si es falso o verdadero
    
# Esta función sirve para hacer asignaciones de valores que se ocuparán posteriormente
def _cumpleComb(t1,t2,v1,v2,p1,p2):
    '''
    Método auxiliar que indica si se cumple la ley 
    '''
    p1v1_t1 = (float(p1) * float(v1)) / float(t1)
    p2v2_t2 = (float(p2) * float(v2)) / float(t2)

    return p1v1_t1	== p2v2_t2 # Regresa un valor booleano indicando si es falso o verdadero

# Esta función sirve para asignar los resultados de funciones anteriores relacionado con Boyle [p1]
def BoyleP1(v1,v2,p2, unidadesvol = 'L', unidadespres = 'atm'):
    '''
    Boyle: Presión inicial
    Revisar docstring de BoyleP2 para información detallada.
    '''
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
    '''
    Ejemplo de uso de ```BoyleP2(v1,v2,p1,unidadesvol,unidadespres)```

    > Un gas ocupa 1.5 litros a una presión de 2.5 atm. Si la temperatura permanece constante, ¿Cuál es la presión en mm de Hg, si se pasa a un recipiente de 3 litros?

    ```python
    from libs import gases

    
    # Como mi problema tiene los datos en sus unidades por defecto, no es necesario asignar esos argumentos.
    
    gases.BoyleP2(1.5,3,2.5)

    ```

    Regresa:

    ```python
    {'p2': 1.25, 'CumpleLey': True}
    ```
    '''
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
    '''
    Ejemplo de uso de ```BoyleV1(v2,p1,p2,unidadesvol,unidadespres)```

    > Calcular el volumen de un gas a una temperatura constante al recibir una presión de 5 atm, si su volumen es de 3.4 litros a una presión de 2.5 atmósferas.

    ```python
    from libs import gases

    
    #Como mi problema tiene los datos en sus unidades por defecto, no es necesario asignar esos argumentos.
    
    gases.BoyleV1(3.4,5,2.5)

    ```

    Regresa:

    ```python
    {'v1': 1.7, 'CumpleLey': True}
    ```
    '''
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
    '''
    Ejemplo de uso de ```BoyleV2(v1,p1,p2,unidadesvol,unidadespres)```

    > Una muestra de oxígeno ocupa 4.2 litros a 760 mmHg. ¿Cuál será el volumen del oxígeno a 415 mmHg, si la temperatura permanece constante?

    ```python
    from libs import gases

    
    # Como mi problema tiene la unidad de presión en mmhg y esta unidad está soportada asignamos el parámetro a mmhg.
    
    gases.BoyleV2(4.2,760,415,unidadespres = "mmhg")

    ```

    Regresa:

    ```python
    {'v2': 7.691566265060241, 'CumpleLey': True}
    ```
    '''
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
    '''
    ```LussacP1(t1,t2,p2, unidadespres = 'atm', unidadestemp = 'k')```

    Toma como argumentos la temperatura inicial, temperatura final y presión  final, regresa un diccionario
    que contiene la presión inicial en atmósferas y un booleano que indica si se cumple la ley o no.

    Para mayor información y caso de uso similar, revisar docstring de ```LussacP2()```.

    '''
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
    '''
    Ejemplo de uso de ```LussacP2(t1,t2,p1,unidadespres,unidadestemp)```

    > La presión del aire en un matraz cerrado es de 460 mm de Hg a 45°C. ¿Cuál es la presión del gas si se calienta hasta 125°C y el volumen permanece constante.

    ```python
    from libs import gases

    gases.LussacP2(45, 125, 460, unidadespres = 'mmhg', unidadestemp = 'C')

    ```

    Regresa:

    ```python
    {'p2': 0.757530619000331, 'CumpleLey': True}
    ```

    Recordemos que la unidad es atmósfera, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)
    '''
    t1 = _convertemp(t1,unidadestemp)
    t2 = _convertemp(t2,unidadestemp)
    p1 = _converpres(p1,unidadespres)

    p2 = (p1 * t2) / t1

    # Se crean los resultados y se guardan en un diccionario
    resultado = {}
    resultado['p2']=p2
    resultado['CumpleLey'] = _cumpleLussac(p1,p2,t1,t2)

    return resultado # Se regresa el resultado

# Esta función sirve para asginar los resultados de funciones anteriores relacionado con Lussac [t1]
def LussacT1(t2,p1,p2, unidadespres = 'atm', unidadestemp = 'k'):
    '''
    ```LussacT1(t2,p1,p2,unidadespres,unidadestemp)```

    Toma como argumentos la temperatura final, temperatura inicial y presión final, regresa un diccionario
    que contiene la temperatura inicial en Kelvin y un booleano que indica si se cumple la ley o no.

    Para mayor información y caso de uso similar, revisar docstring de ```LussacT2()```.

    '''
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
    '''
    Ejemplo de uso de ```LussacT2(t1,p1,p2,unidadespres,unidadestemp)```

    > Cierto volumen de un gas se encuentra a una presión de 970 mmHg cuando su temperatura es de 25.0°C. ¿A qué temperatura deberá estar para que su presión sea 760 mmHg?

    ```python
    from libs import gases

    gases.LussacT2(25, 970, 760, unidadespres = 'mmhg', unidadestemp = 'C')

    ```

    Regresa:

    ```python
    {'t2': 233.48453608247422, 'CumpleLey': True}
    ```

    Recordemos que la unidad es Kelvin, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

    '''
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

