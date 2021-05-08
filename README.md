# quimpy

## Miscellaneous chemistry package for Python3

### Paquete misceláneo de química para Python3

> Desarrollado por:
>
> Alberto L. Figueroa
>
> José Emilio Kuri
>
> Sebastiám Jácome
>
> Carlos A. Durán
>
> Universidad Panamericana CDMX

![IUP](data:image/png;base64,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)


## Tabla de contenidos

1. [Descripción](#descripción)
2. [Dependencias](#dependencias)
3. [Estructura del paquete](#estructura-del-paquete)
4. [Elementos](#elementos)
5. [Materia](#materia)
6. [Gases](#gases)
7. [pH](#ph)
8. [Concentraciones](#concentraciones)

## Descripción

Este paquete contiene diferentes módulos orientados a resolver diferentes problemas de química.  

---

## Dependencias

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
| gases           | Módulos para resolver problemas de Ley de Boyle, Ley de Lussac, Ley de Charles, Ley Combinada de los Gases.      |
| pH              | Módulos para resolver problemas de pH.                                                                           |
| concentraciones | Módulos para resolver problemas de concentración. [MASA,VOLUMEN,PESO_LITRO,MOLARIDAD, NORMAL, MOLAL, FRACCIONMOL, PPM] |

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
| ```_cumple{LEY}({ADP})```          | Método auxiliar que indica si se cumple la ley en cuestión. Toma todos los datos del problema. |

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

## pH

| Métodos                                            | Utilidad                                                                                                 |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ```get_pH(valorH)```                               | Método que, al recibir un valor en específico (pH), calcula los restantes (pOH, H, OH). Regresa un dict. |
| ```get_pOH(valorOH)```                             | Método que mediante la obtención de el valor de pOH, calcula los demás (pH, H, OH). Regresa un dict.     |
| ```get_H(valorH)```                                | Método que se encarga de calcular valores de (pH, pOH, OH) al obtener el valor de H. Regresa un dict.    |
| ```get_OH(valorOH)```                              | Método que calcula los valores de (pH, pOH, H) al tener el valor OH. Regresa un dict.                    |  

### _tipoPH(valorpH, valorpOH, valorH, valorOH)

Los valores se tienen que pasar en el orden indicado para que se pueda hacer una comparación correcta y no suelte ningún error.
Por ejemplo, para la fórmula química del cloro sería ```_tipoPH(13, 1, 1e-13, 0.1)```.

Ejemplo:

```python
from libs import ph

_tipoPH(7, 7, 1e-7, 1e-7)
```

Regresa:

```python
'neutra'
```

### _getConcentración(valorH, valorOH)

Los valores se tienen que pasar por medio de comas, y se realizará la operación indicada.
Por ejemplo, para la fórmula química del cloro sería ```_getConcentración(1e-13, 0.1)```.

Ejemplo:

```python
from libs import ph

_getConcentración(1e-7, 1e-7)
```

Regresa:

```python
1e-14
```

### get_pH(pH)

El único valor que se tiene que pasar como argumento es el valor de pH de la solución. Se harán un cierto número de operaciones y regresará un diccionario con lo restante.
Por ejemplo, para la fórmula química del cloro sería ```get_pH(13)```.

Ejemplo:

```python
from libs import ph

get_pH(7)
```

Regresa:

```python
{'pH':7,'pOH':7,'H+':1e-7,'OH-':1e-7, 'Tipo':'neutra', 'Concentración':1e-14}
```

### get_pOH(pOH)

El único valor que se tiene que pasar como argumento es el valor de pOH de la solución. Se harán un cierto número de operaciones y regresará un diccionario con lo faltante.
Por ejemplo, para la fórmula química del cloro sería ```get_pOH(1)```.

Ejemplo:

```python
from libs import ph

get_pOH(7)
```

Regresa:

```python
{'pH':7,'pOH':7,'H+':1e-7,'OH-':1e-7, 'Tipo':'neutra', 'Concentración':1e-14}
```

### get_H(H)

El único valor que se tiene que pasar como argumento es el valor de H de la solución. Se harán un cierto número de operaciones y regresará un diccionario con lo faltante.
Por ejemplo, para la fórmula química del cloro sería ```get_H(1e-13)```.

Ejemplo:

```python
from libs import ph

get_H(1e-7)
```

Regresa:

```python
{'pH':7,'pOH':7,'H+':1e-7,'OH-':1e-7, 'Tipo':'neutra', 'Concentración':1e-14}
```

### get_OH(OH)

El único valor que se tiene que pasar como argumento es el valor de OH de la solución. Se harán un cierto número de operaciones y regresará un diccionario con lo faltante.
Por ejemplo, para la fórmula química del cloro sería ```get_OH(1e-13)```.

Ejemplo:

```python
from libs import ph

get_OH(1e-7)
```

Regresa:

```python
{'pH':7,'pOH':7,'H+':1e-7,'OH-':1e-7, 'Tipo':'neutra', 'Concentración':1e-14}
```

### Métodos encapsulados [pH]

| Métodos                                            | Utilidad                                                                          |
|----------------------------------------------------|-----------------------------------------------------------------------------------|
| ```_tipoPH(valorpH, valorpOH, valorH, valorOH)```  | Método encapsulado que comprueba el tipo de solución. Regresa un string.          |
| ```_getConcentración(valorH, valorOH)```           | Método encapsulado que calcula la concentración de una solución. Regresa un int.  |

---

## Concentraciones

| Métodos                   | Utilidad                                                                    |
|---------------------------|-----------------------------------------------------------------------------|
| ```masa{DO}({DP})```      | Obtiene el dato faltante en un problema de concentración de masa.           |
| ```vol{DO}({DP})```       | Obtiene el dato faltante en un problema de concentración de volumen.        |
| ```pl{DO}({DP})```        | Obtiene el dato faltante en un problema de concentración peso-litro.        |
| ```normal{DO}({DP})```    | Obtiene el dato faltante en un problema de concentración normal.            |
| ```molaridad{DO}({DP})``` | Obtiene el dato faltante en un problema de concentración molaridad.         |
| ```frac_molal(*c)```      | Obtiene el dato faltante en un problema de concentración fracción molal.    |
| ```ppm{{DO}}```           | Obtiene el dato faltante en un problema de concentración partes por millón. |

### Unidades por defecto [Concentraciones]

| Métrica     | Unidad por defecto    | Unidades alternativas disponibles |
|-------------|-----------------------|-----------------------------------|
| Volumen     | ```"L"``` Litro       | ```"ml","cm3","m3"```             |
| Masa        | ```"g"``` Gramo       | ```"kg","mg"```                   |

NOTA: En ppm, el valor de la unidad de masa por defecto según la fórmula debe ser **mg**.
Igualmente para la concentración molal la unidad defaul de la masa del solvente es **kg**

#### Concentración porciento masa

| Parámetros para {DO} en masa   | Dato que obtiene | Datos que necesita {DP}            |
|--------------------------------|------------------|------------------------------------|
| ```masa_masasolucion({DP})```  | Masa solución    | ```m_soluto, m_solvente, u_masa``` |
| ```masa_masasolucionp({DP})``` | Masa solución    | ```p_masa,m_soluto,u_masa```       |
| ```masa_msoluto({DP})```       | Masa soluto      | ```p_masa, m_solucion,u_masa```    |
| ```masa_msolvente({DP})```     | Masa solvente    | ```p_masa,m_soluto,u_masa```       |
| ```masa_pmasaS({DP})```        | %masa            | ```m_soluto,m_solucion,u_masa```   |
| ```masa_pmasa({DP})```         | %masa            | ```m_soluto,m_solvente,u_masa```   |

Ejemplo para ```masa_msoluto(p_masa, m_solucion, u_masa = 'g')```

> Algunos refrescos contienen 11% en masa de azúcar, determinar cuántos
> gramos contendrá una botella de refresco de coca- cola con 600 gramos de refresco.

```python
from libs import concentraciones

concentraciones.masa_msoluto(11, 600)

```

Regresa

```python
66.0
```

La unidad es **gramos** según la tabla de [unidades por defecto.](#unidades-por-defecto-concentraciones)

Ejemplo para ```masa_pmasaS(m_soluto, m_solucion, u_masa = 'g')```

> Determinar el porciento en masa de un suero que contiene 45 gramos de sal en
> 225 gramos de disolución.

```python
from libs import concentraciones

concentraciones.masa_pmasa(45,225)

```

Regresa:

```python
20.0
```

Ejemplo para ```masa_pmasa(m_soluto, m_solvente, u_masa = 'g')```

> Un acuario debe mantener la concentración de sal similar a la del agua de mar,
> esto es, 1.8 gramos de sal disueltos en 50 gramos de agua.
> ¿Cuál es el porcentaje en masa de la sal en la disolución?

```python
from libs import concentraciones

concentraciones.masa_pmasa(1.8,50)

```

Regresa:

```python
3.6000000000000005
```

#### Concentración %volumen

| Parámetros para {DO} en %vol | Dato que obtiene    | Datos que necesita {DP}              |
|------------------------------|---------------------|--------------------------------------|
| ```vol_vsolucion({DP})```    | Volumen solución    | ```v_soluto,v_solvente,u_volumen```  |
| ```vol_vsolucionP({DP})```   | Volumen solución    | ```v_soluto,p_volumen,u_volumen```   |
| ```vol_vsoluto({DP})```      | Volumen soluto      | ```v_solucion,p_volumen,u_volumen``` |
| ```vol_vsolvente({DP})```    | Volumen solvente    | ```v_soluto,p_volumen,u_volumen```   |
| ```vol_pvolumenS({DP})```    | %volumen            | ```v_solucion,v_soluto,u_volumen```  |
| ```vol_pvolumen({DP})```     | %volumen            | ```v_soluto,v_solvente,u_volumen```  |

#### Concentración Peso-Litro

| Parámetros para {DO} en pl | Dato que obtiene    | Datos que necesita {DP}              |
|----------------------------|---------------------|--------------------------------------|
| ```pl_msoluto({DP})```     | Masa soluto         | ```v_soluto,v_solvente,u_volumen```  |
| ```pl_litros({DP})```      | Volumen solución    | ```v_soluto,p_volumen,u_volumen```   |
| ```pl_gl({DP})```          | Conc. Gramo/Litro   | ```v_solucion,p_volumen,u_volumen``` |

#### Concentración molaridad

| Parámetros para {DO} en molaridad | Dato que obtiene    | Datos que necesita {DP}         |
|------------------------------|---------------------|--------------------------------------|
| ```molaridad_msoluto({DP})```    | Masa soluto    | ```m_molecular,v,molaridad,u_volumen``` |
| ```molaridad_mmolecular({DP})``` | Masa molecular | ```m_soluto,v,molaridad, u_masa```   |
| ```molaridad_volumenM({DP})```   | Volumen        | ```moles,molaridad``` |
| ```molaridad_volumen({DP})```    | Volumen        | ```m_soluto,molaridad,m_molecular,u_masa``` |
| ```molaridad_moles({DP})```      | moles          | ```v,molaridad,u_volumen```  |
| ```molaridad_molesM({DP})```     | moles          | ```moles,v,u_volumen```  |

#### Concentración normal

| Parámetros para {DO} en normal | Dato que obtiene    | Datos que necesita {DP}              |
|-------------------------------|---------------------|--------------------------------------|
| ```normal_msolutoPEQ({DP})``` | Masa soluto    | ```peso_eq,v,normal,u_volumen```  |
| ```normal_msoluto({DP})```    | Masa soluto    | ```m_molecular,carga,v,normal,u_volumen```  |
| ```normal_peq({DP})```        | Peso equivalente | ```m_soluto,v,normal,u_masa, u_volumen``` |
| ```normal_normalPEQ({DP})```  | Normal   | ```peso_eq,m_soluto,v,u_masa```   |
| ```normal_normal({DP})```     | Normal            | ```m_molecular,m_soluto,carga,v, u_masa, u_volumen```|

#### Concentración molal

| Parámetros para {DO} en molal | Dato que obtiene  | Datos que necesita {DP}              |
|-------------------------------|-------------------|--------------------------------------|
| ```molal_msoluto({DP})```    | Masa soluto        | ```m_molecular,m_solvente,molal, u_masa```  |
| ```molal_msolvente({DP})```  | Masa solvente (KG) | ```m_molecular,m_soluto,molal, u_masa```   |
| ```molal_mmolecular({DP})``` | Masa molecular     | ```m_soluto,m_solvente,molal, u_masasoluto, u_masasolvente``` |
| ```molal_molal({DP})```      | Conc. Gramo/Litro  | ```m_soluto,m_solvente,m_molecular, u_masasoluto,u_masasolvente``` |

#### Concentración fracción molar

Método ```frac_molal(*concentraciones)```:

Los argumentos que toma son n número de concentraciones que se tienen, calcula la fracción en el orden de los argumentos.

Regresa un diccionario.

Ejemplo de uso:

>Calcular la fracción molar de cada una de las sustancias de la disolución de:
> 10 moles de metanol, 1 mol de etanol y 8 moles de agua.

```python
from libs import concentraciones
concentraciones.frac_molar(10,1,8)

```

Regresa:

```python
{'C1': 0.526, 'C2': 0.053, 'C3': 0.421}

```

#### Concentración PPM (PartesXmillón)

| Parámetros para {DO} en ppm | Dato que obtiene    | Datos que necesita {DP}              |
|----------------------------|---------------------|--------------------------------------|
| ```pl_msoluto({DP})```     | Masa soluto (mg)        | ```v,ppm,u_volumen```  |
| ```pl_litros({DP})```      | Volumen     | ```m_soluto,ppm,u_masa```   |
| ```pl_gl({DP})```          | ppm  | ```m_soluto,v,u_volumen,u_masa``` |

#### Métodos encapsulados [Concentraciones]

| Métodos                                            | Utilidad                      |
|----------------------------------------------------|-------------------------------------|
| ```_getpeq(m_molecular, carga)```  | Método encapsulado que regresa peso equivalente .          |
| ```_convermasa(masa, u_masa = 'g', u_masaout = 'g')```           | Método encapsulado que calcula la conversión entre unidades de masa, regresa un float. Soprta las unidades de la tabla de unidades. |
