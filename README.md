# sokoban

# 0.objetos

# Sokoban

## 0. Objetivo

Programar el juego Sokoban en una versión retro para consola.

## 1. Reglas del juego

El juego sokoban consiste en acomodar cajas en puntos determinados por las metas.

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja en cualquier sentido.
3. El personaje se moverá en un mapa predefinido.
4. Para terminar el nivel se tienen que acomodar totas las cajas sobre las metas.

## 2. Elementos del juego

### 2.0 Mapa de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando numeros para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

mapa = [
            [3,3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,2,2,4,4,4,4,3],
            [3,4,4,2,2,2,4,1,4,4,3],
            [3,4,4,4,2,4,4,4,4,4,3],
            [3,4,4,2,4,2,4,4,4,4,3],
            [3,4,4,1,4,4,0,2,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3,3,3]
        ]

### 2.1 Lista de elementos

- 0 - Personaje
- 1 - Cajas
- 2 - Metas
- 3 - Paredes
- 4 - Piso
- 5 - Pesonaje meta
- 6 - Caja meta

## 3. Controles

Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover.

- a -> Izquierda
- s -> Derecha
- w -> Arriba
- s -> Abajo

## 4. Función a implementar

| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | hecho | - | |  07/04/24 |
| 1. | Repetir el juego hasta terminar el nivel. | Por hacer | - | | - |
| 2. | Imprimir mapa.| hecho |  Mar 5, 2024 |
| 3. | Leer el movimiento. | hecho |  Mar 5, 2024 |
| 4. | Evaluar el movimiento del usuario. | Por hacer | - |

## Derecha

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, pasillo  | hecho | [0,4] | [4,0] | Mar 25, 2024 |
| 6. | Personaje, meta  | hecho | [0,2] | [4,5] | Mar 25, 2024 |
| 7. | Personaje, caja, pasillo | hecho | [0,1,4] | [4,0,1] | Mar 25, 2024 |
| 8. | Personaje, caja,  meta | hecho | [0,1,2] | [4,0,6] | Mar 25, 2024 |
| 9. | Personaje, caja_meta, pasillo | hecho | [0,6,4] | [4,5,1] | Mar 25, 2024 |
| 10. |Personaje, caja_meta, meta | hecho | [0,6,2] | [4,5,6] | Mar 25, 2024 |
| 11. | Personaje_meta, pasillo | hecho | [5,4] | [2,0] | Mar 25, 2024 |
| 12. | Personaje_meta, meta | hecho | [5,2] | [2,5] | Mar 25, 2024 |
| 13. | Personaje_meta, caja, pasillo | hecho | [5,1,4] | [2,0,1] | Mar 25, 2024 |
| 14. | Personaje_meta, caja, meta | hecho | [5,1,2] | [2,0,6] | Mar 25, 2024 |
| 15. | Personaje_meta, caja_meta, pasillo | hecho | [5,6,4] | [2,5,1] | Mar 25, 2024 |
| 16. | Personaje_meta, caja_meta, meta | hecho | [5,6,2] | [2,5,6] | Mar 25, 2024 |

## Izquierda

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 17. | Personaje y espacio | hecho  | [4,0] | [0,4] |  Mar 25, 2024 |
| 18. | Personaje y meta | hecho  | [2,0] | [5,4] |  Mar 25, 2024 |
| 19. | Personaje, caja y espacio | hecho  | [4,1,0] | [1,0,4] |  Mar 25, 2024 |
| 20. | Personaje, caja y meta | hecho  | [2,1,0] | [6,0,4] |  Mar 25, 2024 |
| 21. | Personaje, caja_meta y espacio | hecho  | [4,6,0] | [1,5,4] | - | 
| 22. | Personaje, caja_meta y meta | hecho  | [2,6,0] | [6,5,4] | - |
| 23. | Personaje_meta y espacio | hecho  | [4,5] | [0,2] | - |
| 24. | Personaje_meta y meta | hecho  | [2,5] | [5,2] | - |
| 25. | Personaje_meta, caja y espacio | hecho  | [4,1,5] | [1,0,2] | - |
| 26. | Personaje_meta, caja y meta | hecho  | [2,1,5] | [6,0,2] | - |
| 27. | Personaje_meta, caja_meta y espacio | hecho  | [4,6,5] | [1,5,2] |  Mar 25, 2024 |
| 28. | Personaje_meta, caja_meta y meta | hecho  | [2,6,5] | [6,5,2] |  Mar 25, 2024 |

## Arriba
| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, pasillo  | hecho | [0,4] | [4,0] | Mar 25, 2024 |
| 6. | Personaje, meta  | hecho | [0,2] | [4,5] |Mar 25, 2024 |
| 7. | Personaje, caja, pasillo | hecho | [0,1,4] | [4,0,1] | - |
| 8. | Personaje, caja,  meta | hecho | [0,1,2] | [4,0,6] | - |
| 9. | Personaje, caja_meta, pasillo | hecho | [0,6,4] | [4,5,1] | - |
| 10. |Personaje, caja_meta, meta | hecho | [0,6,2] | [4,5,6] | - |
| 11. | Personaje_meta, pasillo | hecho | [5,4] | [2,0] | - |
| 12. | Personaje_meta, meta | hecho | [5,2] | [2,5] | Mar 25, 2024 |
| 13. | Personaje_meta, caja, pasillo | hecho | [5,1,4] | [2,0,1] | - |
| 14. | Personaje_meta, caja, meta | hecho | [5,1,2] | [2,0,6] | - |
| 15. | Personaje_meta, caja_meta, pasillo | hecho | [5,6,4] | [2,5,1] | - |
| 16. | Personaje_meta, caja_meta, meta | hecho | [5,6,2] | [2,5,6] | Mar 25, 2024 |

## Abajo
| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 41. | Personaje y espacio | hecho  | [4,0] | [0,4] | Mar 25, 2024 |
| 42. | Personaje y meta | hecho  | [2,0] | [5,4] | Mar 25, 2024 |
| 43. | Personaje, caja y espacio | hecho  | [4,1,0] | [1,0,4] | Mar 25, 2024 |
| 44. | Personaje, caja y meta | hecho  | [2,1,0] | [6,0,4] | Mar 25, 2024 |
| 45. | Personaje, caja_meta y espacio | hecho  | [4,6,0] | [1,5,4] | Mar 25, 2024 | 
| 46. | Personaje, caja_meta y meta | hecho  | [2,6,0] | [6,5,4] | Mar 25, 2024 |
| 47. | Personaje_meta y espacio | hecho  | [4,5] | [0,2] | Mar 25, 2024 |
| 48. | Personaje_meta y meta | hecho  | [2,5] | [5,2] | Mar 25, 2024 |
| 49. | Personaje_meta, caja y espacio | hecho  | [4,1,5] | [1,0,2] | Mar 25, 2024 |
| 50. | Personaje_meta, caja y meta | hecho  | [2,1,5] | [6,0,2] | Mar 25, 2024 |
| 51. | Personaje_meta, caja_meta y espacio | hecho  | [4,6,5] | [1,5,2] | Mar 25, 2024 |
| 52. | Personaje_meta, caja_meta y meta | hecho  | [2,6,5] | [6,5,2] | Mar 25, 2024 |


## Determina si se completo el nivel o no

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 53. | Evaluar si el nivel esta terminado.  | Por hacer | - |
| 54. | Si el nivel esta terminado cargar el siguiente nivel.  | hecho | 07/04/24 |

## Función extra

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 55. | Función adicional o powerup (descripción). | Por hacer | - |
