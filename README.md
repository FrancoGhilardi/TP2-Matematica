# 🧮 Programa de Operaciones con DNIs y Años de Nacimiento

Este programa desarrollado en Python permite realizar múltiples operaciones con **números de DNI** y **años de nacimiento** ingresados por el usuario a través de un menú interactivo por consola. El objetivo es aplicar estructuras de datos, funciones, estructuras de control, lógica condicional y procesamiento de conjuntos de manera didáctica y visual.

---

## 📌 ¿Qué hace este programa?

El programa ofrece dos grandes bloques funcionales:

### A. Operaciones con DNIs

1. **Ingreso de DNIs** reales o ficticios.
2. **Generación de conjuntos únicos de dígitos** por cada DNI.
3. **Cálculos de teoría de conjuntos**:
   - Unión
   - Intersección
   - Diferencia
   - Diferencia simétrica
4. **Frecuencia de aparición de cada dígito** en cada DNI.
5. **Suma total de los dígitos** de cada DNI.
6. **Evaluación de condiciones lógicas**, por ejemplo:
   - Si un dígito aparece en todos los DNIs: se muestra `"Dígito compartido"`.
   - Si algún DNI tiene más de 6 dígitos únicos: se muestra `"Diversidad numérica alta"`.

---

### B. Operaciones con Años de Nacimiento

1. **Ingreso de años de nacimiento** de varias personas (reales o ficticios).
2. **Conteo de años pares e impares**.
3. **Identificación de generaciones**:
   - Si todos nacieron después del año 2000: se muestra `"Grupo Z"`.
4. **Detección de años bisiestos**.
5. **Cálculo del producto cartesiano** entre:
   - El conjunto de años ingresados.
   - Las edades actuales (calculadas automáticamente en base al año actual).

---

## 🧪 Librerías utilizadas

### `colorama`

- **¿Qué hace?** Permite aplicar colores al texto de la consola.
- **¿Por qué se usa?** Mejora la experiencia del usuario diferenciando:
  - Entradas (`amarillo`)
  - Títulos y secciones (`cyan`)
  - Resultados numéricos (`verde`)
  - Mensajes lógicos especiales (`magenta`)
  - Errores o advertencias (`rojo`)

```bash
pip install colorama
```

### `datetime`

- **¿Qué hace?** Proporciona herramientas para trabajar con fechas.
- **¿Por qué se usa?** Se utiliza para obtener el año actual y calcular edades automáticamente.

### `itertools.product`

- **¿Qué hace?** Permite calcular el producto cartesiano entre listas.
- **¿Por qué se usa?** Para combinar años de nacimiento con edades actuales en el bloque B del programa.

---

## 🚀 ¿Cómo ejecutar el programa?

1. Cloná o descargá este repositorio.
2. Asegurate de tener Python instalado (recomendado: Python 3.7 o superior).
3. Instalá la dependencia `colorama` si aún no lo hiciste:

```bash
pip install colorama
```

4. Ejecutá el archivo principal desde la terminal:

```bash
python programa.py
```

5. Seguí las instrucciones por consola y seleccioná la opción deseada desde el menú.

---

## 📋 Estructura del menú

Al iniciar el programa, verás un menú con las siguientes opciones:

- `1. Operaciones con DNIs`
- `2. Operaciones con Años de Nacimiento`
- `0. Salir del programa`

Cada sección te irá guiando paso a paso para completar los datos necesarios y visualizar los resultados en colores diferenciados para facilitar la comprensión.

---

## 👨‍🏫 Profesores

- Prof. Vanina Durrutty
- Tutor. Ana Maria Castro

---

## 👨‍🎓 Alumnos

- Franco Ghilardi
- Kevin Gastaldello

---
