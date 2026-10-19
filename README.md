# Mi árbol binario — Árbol binario de búsqueda en Python

Programa desarrollado para la actividad **MA Evaluación 8 – Reporte académico «Mi árbol binario»**
(Corporación Universitaria Minuto de Dios – UNIMINUTO · Curso: Estructuras de datos ·
Docente: Carmen Emilia Rubio Vanegas · Estudiante: Luis Felipe Díaz).

## Descripción

Permite ingresar una serie de elementos numéricos, almacenarlos en un **árbol binario de
búsqueda (ABB)** y realizar los recorridos en profundidad **inorder, preorder y posorder**.
Adicionalmente implementa búsqueda, eliminación de elementos (con los tres casos: hoja,
un solo hijo y dos hijos mediante sucesor inorder), visualización de la estructura del
árbol y estadísticas básicas (total de nodos y altura).

## Características

- Inserción recursiva sin duplicados, conservando el invariante del ABB
- Recorridos en profundidad: **inorder**, **preorder** y **posorder**
- Eliminación con manejo de los 3 casos (hoja, un hijo, dos hijos con sucesor inorder)
- Búsqueda iterativa en O(log n) promedio
- Visualización del árbol girado 90°, total de nodos y altura en niveles
- Menú de consola con validación de entradas (manejo de excepciones)

## Ejecución

```bash
python arbol_binario.py
```

Requiere Python 3.x. No utiliza librerías externas.

## Ejemplo

Insertando, en este orden, los valores `50, 30, 70, 20, 40, 60, 80`:

| Recorrido | Resultado |
|---|---|
| Inorder   | 20, 30, 40, 50, 60, 70, 80 |
| Preorder  | 50, 30, 20, 40, 70, 60, 80 |
| Posorder  | 20, 40, 30, 60, 80, 70, 50 |

Tras eliminar `20` (hoja), `30` (un hijo) y `50` (dos hijos), la nueva raíz es `60`,
sucesor inorder del nodo eliminado, y el invariante del árbol se conserva.

## Estructura del código

| Componente | Responsabilidad |
|---|---|
| `class Nodo` | Unidad mínima de la estructura: dato + referencias a hijos izquierdo y derecho |
| `class ArbolBinarioBusqueda` | Encapsula la raíz y las operaciones: insertar, buscar, eliminar, recorridos y visualización |
| `main()` | Menú de consola, captura y validación de entradas del usuario |
