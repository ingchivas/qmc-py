# qmc-py

## Miscellaneous chemistry package for Pyhton3

### Paquete misceláneo de química para Python3

## Descripción:

Este paquete contiene diferentes módulos orientados a resolver diferentes problemas de química.  

## Estructura del paquete:
El paquete se divide en los siguientes módulos:

| Nombre          | Utilidad                                                                                                         |
|-----------------|------------------------------------------------------------------------------------------------------------------|
| elementos       | Contiene los elementos de la tabla periódica instanciados en la clase Elemento.                                  |
| materia         | Contiene módulos para resolver problemas de UMA, de compuestos y elementos, incluyendo la UMA percentual.        |
| gases           | Módulos para resolver problemas de Ley de Boyle, Ley de Lussac, Ley de Charles, Ley Combinada de los Gases,      |
| concentraciones | Módulos para resolver problemas de concentración. [MASA,VOLUMEN,PESO,MOLARIDAD, NORMAL, MOLAL, FRACCIONMOL, PPM] |
| ph              | Módulos para resolver problemas de pH.                                                                           |

### Elementos

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

Ejemplo de uso:

```python
from libs import elementos
elementos.He.nombre
```

Nos daría: ```Helio```
