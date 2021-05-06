# quimpy

## Miscellaneous chemistry package for Pyhton3

### Paquete misceláneo de química para Python3

## Tabla de contenidos

1. [Descripción](#descripción)
2. [Dependencias](#dependencias)
3. [Estructura del paquete](#estructura-del-paquete)
4. [Elementos](#elementos)
5. [Materia](#materia)
6. [Gases](#gases)
7. [Concentraciones](#concentraciones)

## Descripción

Este paquete contiene diferentes módulos orientados a resolver diferentes problemas de química.  

---

### Dependencias

- math
- re
- numpy

Para el InstanciadorMAX [Instanciador que creamos para instanciar los elementos de la tabla periódica]:

- pandas

---

## Estructura del paquete

El paquete se divide en los siguientes módulos:

| Nombre          | Utilidad                                                                                                         |
|-----------------|------------------------------------------------------------------------------------------------------------------|
| elementos       | Contiene los elementos de la tabla periódica instanciados en la clase Elemento.                                  |
| materia         | Contiene módulos para resolver problemas de UMA, de compuestos y elementos, incluyendo la UMA percentual.        |
| gases           | Módulos para resolver problemas de Ley de Boyle, Ley de Lussac, Ley de Charles, Ley Combinada de los Gases,      |
| concentraciones | Módulos para resolver problemas de concentración. [MASA,VOLUMEN,PESO_LITRO,MOLARIDAD, NORMAL, MOLAL, FRACCIONMOL, PPM] |
| pH              | Módulos para resolver problemas de pH.                                                                           |

---

## Elementos

Cada elemento tiene los siguientes atributos:

| Nombre del Atributo       | Uso
|---------------------------|---------------------|
| Elemento                  | ```.elemento```     |
| Nombre                    | ```.nombre```       |
| Número Atómico            | ````.z````          |
| UMA                       | ````.uma````        |
| Periodo                   | ````.periodo````    |
| Grupo                     | ````.grp````        |
| Configuración Electrónica | ````.c_electron```` |
| Protones                  | ````.protones````   |
| Electrones                | ````.electrones```` |
| Neutrones                 | ```.neutrones```    |

Llamamos al elemento por su símbolo.

Ejemplo de uso:

```python
from libs import elementos
elementos.He.nombre
```

Nos daría: ```Helio```

La clase elementos tiene los siguientes métodos:
```imprimirElemento()``` - Imprime un resumen del elemento

Ejemplo:

```python
from libs import elementos
elementos.He.imprimirElemento()
```

```python
Elemento: He
Nombre: Helio
Número Atómico: 2
UMA: 4.002
Periodo: 1
Grupo: 18
Configuración Electrónica:  1s2
Protones: 2
Electrones 2
Neutrones: 2.0
```

```getElemento()``` - Regresa un diccionario conteniendo todos los atributos del elemento.

```python
from libs import elementos
elementos.He.getElemento()
```

```python
{'Elemento': 'He', 'Nombre': 'Helio', 'Z': 2, 'UMA': 4.002, 'Periodo': 1, 'Grupo': '18', 'C_Electronica': ' 1s2', 'Protones': 2, 'Electrones': 2, 'Neutrones': 2.0}   
```

Además de un método adicional fuera de la clase:
```imprimirTabla()``` - Imprime la tabla periódica a la consola.

```python
      -----                                                               -----
        1 | H |                                                               |He |
        |---+----                                       --------------------+---|
        2 |Li |Be |                                       | B | C | N | O | F |Ne |
        |---+---|                                       |---+---+---+---+---+---|
        3 |Na |Mg |3B  4B  5B  6B  7B |    8B     |1B  2B |Al |Si | P | S |Cl |Ar |
        |---+---+---------------------------------------+---+---+---+---+---+---|
        4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |
        |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
        5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |
        |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
        6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |
        |---+---+---+------------------------------------------------------------
        7 |Fr |Ra |ACT|
        -------------
                    -------------------------------------------------------------
        Lanthanide |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |
                    |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
        Actinide   |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |
                    -------------------------------------------------------------
```

---

## Materia

Materia tiene los siguientes métodos.

| Métodos                        | Utilidad                                                                               |
|--------------------------------|----------------------------------------------------------------------------------------|
| ```umacompuesto(compuesto)```  | Obtiene la UMA de un compuesto o elemento. Regresa un float.                           |
| ```umapercentual(compuesto)``` | Obtiene la relación porcentual de la UMA de un compuesto. Regresa un dict.             |
| ```gmol(gramos, compuesto)```  | Obtiene la cantidad de moles de un compuesto a partir de los gramos. Regresa un float. |
| ```molg(moles,compuesto)```    | Obtiene la cantidad de gramos de un compuesto a partir de la cantidad de moles.        |

### umacompuesto(compuesto)

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

### umapercentual(compuesto)

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

### gmol(gramos, compuesto)

Convierte gramos de un compuesto a moles. Utiliza el mismo parser y regresa un valor float.

```python
from libs import materia

materia.gmol(18.01528,'H2 O') 
```

Regresa:

```python
1.000015542603386
```

### molg(gramos, compuesto)

Convierte moles de un compuesto a gramos. Utiliza el mismo parser y regresa un valor float.

```python
materia.molg(1, 'H2 O')
```

Regresa:

```python
18.015
```

### Métodos encapsulados

| Métodos                      | Utilidad                                                                                               |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| ```_umaelemento(elemento)``` | Checa la UMA de un elemento en el contenedor.                                                          |
| ```_cosplit(compuesto)```    | Parser de ecuaciones químicas basado en regex.                                                         |
| ```_intconv(num)```          | Intenta convertir números a enteros. Auxiliar en el algoritmo de reconocimiento de fórmulas químicas.  |

---

## Gases

| Métodos                 | Utilidad                                                                                               |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| ```Boyle{DO}({DP})```   | Obtiene el dato faltante en un problema de gases de la Ley de Boyle.                                   |
| ```Llusac{DO}({DP})```  | Obtiene el dato faltante en un problema de gases de la Ley de Llusac.                                  |
| ```Charles{DO}({DP})``` | Obtiene el dato faltante en un problema de gases de la Ley de Charles.                                 |
| ```Combinada{{DO}}```   | Obtiene el dato faltante en un problema de gases de la Ley Combinada de los Gases.                     |

Donde {DO} es nuestro dato a obtener en mayúscula y {DP} son los datos del problema.

Las funciones regresan un diccionario conteniendo el valor float que se busca y un booleano que indica si la ley se cumple o no.

NOTA: **Los valores por defecto para unidades son los siguientes:**

### Unidades por defecto

| Métrica     | Unidad por defecto    | Unidades alternativas disponibles |
|-------------|-----------------------|-----------------------------------|
| Volúmen     | ```"L"``` Litro       | ```"ml","cm3","m3"```             |
| Presión     | ```"atm"``` Atmósfera | ```"pa","mmhg"```                 |
| Temperatura | ```"k"``` Kelvin      | ```"C","F"```                     |

NOTA: **Los resultados siempre se darán en las unidades por defecto**

### Boyle

> La ley de Boyle situa un gas a temperatura constante, pero un cambio en la presion-volumen.
> $$P_1V_1=P_2V_2$$

| Parámetros para {DO} en Boyle | Dato que obtiene | Datos que necesita {DP}                 |
|-------------------------------|------------------|-----------------------------------------|
| P1   ```BoyleP1({DP})```      | Presión inicial  | ```v1,v2,p2,unidadesvol,unidadespres``` |
| P2   ```BoyleP2({DP})```      | Presión final    | ```v1,v2,p1,unidadesvol,unidadespres``` |
| V1   ```BoyleV1({DP})```      | Volumen inicial  | ```v2,p1,p2,unidadesvol,unidadespres``` |
| V2   ```BoyleV2({DP})```      | Volumen final    | ```v1,p1,p2,unidadesvol,unidadespres``` |

#### Ejemplo de uso de ```BoyleP2(v1,v2,p1,unidadesvol,unidadespres)```

> Un gas ocupa 1.5 litros a una presión de 2.5 atm. Si la temperatura permanece constante, ¿Cuál es la presión en mm de Hg, si se pasa a un recipiente de 3 litros?

```python
from libs import gases

'''
 Como mi problema tiene los datos en sus unidades por defecto, no es necesario asignar esos argumentos.
'''
gases.BoyleP2(1.5,3,2.5)

```

Regresa:

```python
{'p2': 1.25, 'CumpleLey': True}
```

Recordemos que la unidad es **atmósfera**, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

#### Ejemplo de uso de ```BoyleV1(v2,p1,p2,unidadesvol,unidadespres)```

> Calcular el volumen de un gas a una temperatura constante al recibir una presión de 5 atm, si su volumen es de 3.4 litros a una presión de 2.5 atmósferas.

```python
from libs import gases

'''
 Como mi problema tiene los datos en sus unidades por defecto, no es necesario asignar esos argumentos.
'''
gases.BoyleV1(3.4,5,2.5)

```

Regresa:

```python
{'v1': 1.7, 'CumpleLey': True}
```

Recordemos que la unidad es **litro**, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

#### Ejemplo de uso de ```BoyleV2(v1,p1,p2,unidadesvol,unidadespres)```

> Una muestra de oxígeno ocupa 4.2 litros a 760 mmHg. ¿Cuál será el volumen del oxígeno a 415 mmHg, si la temperatura permanece constante?

```python
from libs import gases

'''
Como mi problema tiene la unidad de presión en mmhg y esta unidad está soportada
asignamos el parámetro a mmhg.
'''
gases.BoyleV2(4.2,760,415,unidadespres = "mmhg")

```

Regresa:

```python
{'v2': 7.691566265060241, 'CumpleLey': True}
```

### Llusac

> La ley de Lussac situa un gas a volumen constante, pero un cambio en la presion-temperatura.
> $$\frac{P_1}{T_1} = \frac{P_2}{T_2}$$

| Parámetros para {DO} en Lussac | Dato que obtiene    | Datos que necesita {DP}                  |
|--------------------------------|---------------------|------------------------------------------|
| P1   ```LussacP1({DP})```      | Presión inicial     | ```t1,t2,p2,unidadespres,unidadestemp``` |
| P2   ```LussacP2({DP})```      | Presión final       | ```t1,t2,p1,unidadespres,unidadestemp``` |
| T1   ```LussacT1({DP})```      | Temperatura inicial | ```t2,p1,p2,unidadespres,unidadestemp``` |
| T2   ```LussacT2({DP})```      | Temperatura final   | ```t1,p1,p2,unidadespres,unidadestemp``` |

#### Ejemplo de uso de ```LussacP2(t1,t2,p1,unidadespres,unidadestemp)```

> La presión del aire en un matraz cerrado es de 460 mm de Hg a 45°C. ¿Cuál es la presión del gas si se calienta hasta 125°C y el volumen permanece constante.

```python
from libs import gases

gases.LussacP2(45, 125, 460, unidadespres = 'mmhg', unidadestemp = 'C')

```

Regresa:

```python
{'p2': 0.757530619000331, 'CumpleLey': True}
```

Recordemos que la unidad es **atmósfera**, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

#### Ejemplo de uso de ```LussacT2(t1,p1,p2,unidadespres,unidadestemp)```

> Cierto volumen de un gas se encuentra a una presión de 970 mmHg cuando su temperatura es de 25.0°C. ¿A qué temperatura deberá estar para que su presión sea 760 mmHg?

```python
from libs import gases

gases.LussacT2(25, 970, 760, unidadespres = 'mmhg', unidadestemp = 'C')

```

Regresa:

```python
{'t2': 233.48453608247422, 'CumpleLey': True}
```

Recordemos que la unidad es **Kelvin**, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

### Charles

> La ley de Charles situa un gas a presion constante, pero un cambio en el volumen-temperatura.
> $$\frac{V_1}{T_1} = \frac{V_2}{T_2}$$

| Parámetros para {DO} en Charles | Dato que obtiene    | Datos que necesita {DP}                  |
|---------------------------------|---------------------|------------------------------------------|
| V1   ```CharlesV1({DP})```      | Volumen inicial     | ```t1,t2,v2,unidadesvol,unidadestemp```  |
| V2   ```CharlesV2({DP})```      | Volumen final       | ```t1,t2,v1,unidadesvol,unidadestemp```  |
| T1   ```CharlesT1({DP})```      | Temperatura inicial | ```t2,v1,v2,unidadesvol,unidadestemp```  |
| T2   ```CharlesT2({DP})```      | Temperatura final   | ```t1,v1,v2,unidadesvol,unidadestemp```  |

#### Ejemplo de uso de ```CharlesV2(t1,t2,v1,unidadesvol,unidadestemp)```

> Se tiene un gas a una presión constante de 560 mm de Hg, el gas ocupa un volumen de 23 cm³ a una temperatura que está en 69°C . ¿Qué volumen ocupará el gas a una temperatura de 13°C?

```python
from libs import gases

gases.CharlesV2(69,13,23, unidadesvol = 'cm3', unidadestemp = 'C')

```

Obtenemos:

```python
{'v2': 0.01923391812865497, 'CumpleLey': True}
```

Recordemos que la unidad es **Litros**, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

#### Ejemplo de uso de ```CharlesT1(t2,v1,v2,unidadesvol,unidadestemp)```

> Calcular la temperatura absoluta a la cual se encuentra un gas que ocupa un volumen de 0.4 litros a una presión de una atmósfera, si a una temperatura de 45°C ocupa un volumen de 1.2 litros a la misma presión.

```python
from libs import gases

gases.CharlesT1(45,0.4,1.2, unidadestemp = 'C')

```

Obtenemos:

```python
{'t1': 106.0, 'CumpleLey': True}
```

Recordemos que la unidad es **Kelvin**, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

#### Ejemplo de uso de ```CharlesT2(t1,v1,v2,unidadesvol,unidadestemp)```

> Una masa determinada de nitrógeno gaseoso ocupa un volumen de 4 litros a una temperatura de 31°C y a una presión de una atmósfera, calcular su temperatura absoluta si el volumen que ocupa es de 1.2 litros a la misma presión

```python
from libs import gases

gases.CharlesT2(31,4,1.2, unidadestemp = 'C')

```

Obtenemos:

```python
{'t2': 91.2, 'CumpleLey': True}
```

Recordemos que la unidad es **Kelvin**, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

### Ley combinada de los gases

> En esta ley ninguna variable permanece constante.
> $$\frac{P_1V_1}{T_1}=\frac{P_2V_2}{T_2}

| Parámetros para {DO} en LeyComb | Dato que obtiene    | Datos que necesita {DP}                                     |
|---------------------------------|---------------------|-------------------------------------------------------------|
| V1   ```LeyCombV1({DP})```      | Volumen inicial     | ```t1,t2,v2,p1,p2,unidadesvol,unidadestemp,unidadespres```  |
| V2   ```LeyCombV2({DP})```      | Volumen final       | ```t1,t2,v1,p1,p2,unidadesvol,unidadestemp,unidadespres```  |
| T1   ```LeyCombT1({DP})```      | Temperatura inicial | ```t2,v1,v2,p1,p2,unidadesvol,unidadestemp,unidadespres```  |
| T2   ```LeyCombT2({DP})```      | Temperatura final   | ```t1,v1,v2,p1,p2,unidadesvol,unidadestemp,unidadespres```  |
| P1   ```LeyCombP1({DP})```      | Presión inicial     | ```t1,t2,v1,v2,p2,unidadesvol,unidadestemp,unidadespres```  |
| P2   ```LeyCombP2({DP})```      | Presión final       | ```t1,t2,v1,v2,p1,unidadesvol,unidadestemp,unidadespres```  |

#### Ejemplo de uso de ```LeyCombP2(t1,t2,v1,v2,p1,unidadesvol,unidadestemp,unidadespres)```

> Los neumáticos de un coche deben estar a una presión de 1,8 atm,
> a 20 ºC. Con el movimiento se calientan hasta 50 ºC, pasando su volumen de 50 a 50,5 litros.
> ¿Cuál será la presión del neumático tras la marcha?

```python
from libs import gases

gases.LeyCombP2(20,50,50,50.5,1.8, unidadestemp = 'C')
```

Devuelve:

```python
{'p2': 1.9645604335292814, 'CumpleLey': False}
```

Recordemos que la unidad es **atmósfera**, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

#### Ejemplo de uso de ```LeyCombV2(t1,t2,v1,p1,p2,unidadesvol,unidadestemp,unidadespres)```

> Una muestra de neón ocupa 105 L a 27 °C bajo una presión de 985mmhg . ¿Cuál es el volumen que debería ocupar el gas
> a temperatura y y presión estándar (0°C - 760mmhg).

```python
from libs import gases

gases.LeyCombV2(27,0,105,985,760, unidadestemp = 'C', unidadespres = 'mmhg')
```

Devuelve:

```python
{'v2': 123.84394973565848, 'CumpleLey': False}
```

Recordemos que la unidad es **litro**, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

#### Ejemplo de uso de ```t1,v1,v2,p1,p2,unidadesvol,unidadestemp,unidadespres```

> Una muestra de 4L de nitrógeno se recoge a 1.5 atm y 288 K. Si la presión se
> incrementa a 2.5 atm y el volumen se reduce a 2L, ¿qué temperatura posee el
> nitrógeno?

```python
gases.LeyCombT2(288,4,2,1.5,2.5)
```

Devuelve:

```python
{'t2': 240.0, 'CumpleLey': True}
```

Recordemos que la unidad es **kelvin**, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

### Métodos encapsulados [gases]

| Métodos                            | Utilidad                                                                                       |
|------------------------------------|------------------------------------------------------------------------------------------------|
| ```_convervol(v, unidadesvol)```   | Método auxiliar que convierte un valor de volumen de la unidad argumento a ```Litros```.       |
| ```_converpres(p, unidadespres)``` | Método auxiliar que convierte un valor de presión de la unidad argumento a ```atmósferas```.   |
| ```_convertemp(t, unidadestemp)``` | Método auxiliar que convierte un valor de temperatura de la unidad argumento a ```kelvin```.   |
| ```_cumple{LEY}```({ADP})          | Método auxiliar que indica si se cumple la ley en cuestión. Toma todos los datos del problema. |

#### ```_convervol(v, unidadesvol)```

Método auxiliar que convierte un valor de volumen de la unidad argumento a Litros.
Regresa un float.

Uso:

```python
gases._convervol(1000,'ml')
```
  
Regresa:

```python
1.0
```

#### ```_converpres(p, unidadespres)```

Método auxiliar que convierte un valor de presión de la unidad argumento a atmósferas.

Regresa un float.
Uso:

```python
gases._converpres(760,'mmhg')

```

Regresa:

```python
1.0
```

#### ```_convertemp(t, unidadestemp)```

Método auxiliar que convierte un valor de temperatura de la unidad argumento a kelvin.

Regresa un float.

Uso:

```python
gases._convertemp(0,'C')

```

Regresa:

```python
273.15
```

---

## Concentraciones
