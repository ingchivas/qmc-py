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
| ```_intconv(num)```               | Intenta convertir números a enteros. Auxiliar en el algoritmo de reconocimiento de fórmulas químicas. |

---

## Gases

| Métodos                        | Utilidad                                                                               |
|--------------------------------|----------------------------------------------------------------------------------------|
| ```Boyle{DATO A OBTENER}({DATOS QUE SE TIENEN} unidadesvol = 'L', unidadespres = 'atm')```  | Obtiene el valor faltante del problema de Boyle. Regresa un float.                           |
| ```Lussac{DATO A OBTENER}({DATOS QUE SE TIENEN} unidadesvol = 'L', unidadespres = 'atm')``` | Obtiene el valor faltante del problema de Lussac. Regresa un float.             |

