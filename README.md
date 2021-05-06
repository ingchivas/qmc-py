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
| concentraciones | Módulos para resolver problemas de concentración. [MASA,VOLUMEN,PESO,MOLARIDAD, NORMAL, MOLAL, FRACCIONMOL, PPM] |
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

> La ley de Boyle situa un gas a temperatura constante, pero un cambio en la presion-volumen. $$P_1V_1=P_2V_2$$.

| Parámetros para {DO} en Boyle | Dato que obtiene | Datos que necesita {DP}                 |
|-------------------------------|------------------|-----------------------------------------|
| P1   ```BoyleP1({DP})```      | Presión inicial  | ```v1,v2,p2,unidadesvol,unidadespres``` |
| P2   ```BoyleP2({DP})```      | Presión final    | ```v1,v2,p1,unidadesvol,unidadespres``` |
| V1   ```BoyleV1({DP})```      | Volumen inicial  | ```v2,p1,p2,unidadesvol,unidadespres``` |
| V2   ```BoyleV2({DP})```      | Volumen final    | ```v1,p1,p2,unidadesvol,unidadespres``` |

Ejemplo de uso de ```BoyleP2(v1,v2,p1,unidadesvol,unidadespres)```

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

Recordemos que la unidad es atmósfera, siempre se utilizarán las unidades contenidas en la tabla de [unidades por defecto.](#unidades-por-defecto)

Ejemplo de uso de ```BoyleV1(v2,p1,p2,unidadesvol,unidadespres)```

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

Ejemplo de uso de ```BoyleV2(v1,p1,p2,unidadesvol,unidadespres)```

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

> La ley de Lussac situa un gas a volumen constante, pero un cambio en la presion-temperatura. $$\frac{P_1}{T_1} = \frac{P_2}{T_2}$$

| Parámetros para {DO} en Lussac | Dato que obtiene    | Datos que necesita {DP}                 |
|--------------------------------|---------------------|-----------------------------------------|
| P1   ```LussacP1({DP})```      | Presión inicial     | ```v1,v2,p2,unidadesvol,unidadespres``` |
| P2   ```LussacP2({DP})```      | Presión final       | ```v1,v2,p1,unidadesvol,unidadespres``` |
| T1   ```LussacT1({DP})```      | Temperatura inicial | ```v2,p1,p2,unidadesvol,unidadespres``` |
| T2   ```LussacT2({DP})```      | Temperatura final   | ```v1,p1,p2,unidadesvol,unidadespres``` |
