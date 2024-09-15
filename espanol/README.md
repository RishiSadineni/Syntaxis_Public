# Traductor de Python Español

## Descripción

Este proyecto contiene un traductor que convierte código Python escrito con palabras clave en español a Python estándar. Permite a los programadores hispanohablantes escribir código Python usando palabras clave en su idioma nativo.

## Características

- **Traducción automática**: Convierte palabras clave españolas a inglés
- **Preserva comentarios**: Los comentarios y estructura del código se mantienen intactos
- **Fácil de usar**: Interfaz simple de línea de comandos
- **Compatible**: Genera código Python estándar ejecutable

## Palabras Clave Soportadas

### Control de Flujo
- `si` → `if`
- `sino` → `else`
- `sino_si` → `elif`
- `para` → `for`
- `mientras` → `while`
- `en` → `in`
- `range` → `range`

### Funciones
- `definir` → `def`
- `retornar` → `return`
- `imprimir` → `print`

### Tipos de Datos
- `verdadero` → `True`
- `falso` → `False`
- `nada` → `None`

### Lógica
- `y` → `and`
- `o` → `or`
- `no` → `not`

### Funciones Integradas
- `longitud` → `len`
- `tipo` → `type`
- `entrada` → `input`
- `entero` → `int`
- `flotante` → `float`
- `cadena` → `str`
- `lista` → `list`
- `diccionario` → `dict`

## Instalación

1. Asegúrate de tener Python 3.6+ instalado
2. Clona o descarga este repositorio
3. Navega al directorio `espanol/`

## Uso

### Uso Básico

```bash
python translator.py archivo_entrada.synt archivo_salida.py
```

### Ejemplos

**Entrada** (`programa_espanol.synt`):
```python
definir saludar(nombre):
    si nombre:
        imprimir(f"Hola {nombre}!")
    sino:
        imprimir("Hola desconocido!")

para i en range(5):
    imprimir(f"Número: {i}")

lista_numeros = [1, 2, 3, 4, 5]
longitud_lista = longitud(lista_numeros)
imprimir(f"La lista tiene {longitud_lista} elementos")
```

**Salida** (`programa_python.py`):
```python
def saludar(nombre):
    if nombre:
        print(f"Hola {nombre}!")
    else:
        print("Hola desconocido!")

for i in range(5):
    print(f"Número: {i}")

lista_numeros = [1, 2, 3, 4, 5]
longitud_lista = len(lista_numeros)
print(f"La lista tiene {longitud_lista} elementos")
```

### Uso Interactivo

```bash
python translator.py archivo_entrada.synt
```

Esto mostrará el código traducido en la consola sin crear un archivo de salida.

## Programas de Ejemplo

El directorio `programas/` contiene varios ejemplos de código Python en español:

1. **01_hola_mundo_maria_gonzalez_2024_07_15.synt** - Programa básico de saludo
2. **02_calculadora_carlos_rodriguez_2024_08_03.synt** - Calculadora simple
3. **03_lista_tareas_ana_martinez_2024_09_12.synt** - Gestor de tareas
4. **04_conversor_monedas_luis_hernandez_2024_10_05.synt** - Conversor de monedas
5. **05_juego_adivinanza_sofia_lopez_2024_11_20.synt** - Juego de adivinanzas
6. **06_gestor_contactos_diego_ramirez_2024_12_08.synt** - Gestor de contactos
7. **07_conversor_temperatura_jimena_sanchez_2025_01_10.synt** - Conversor de temperatura
8. **08_gestor_notas_soraya_morales_2025_02_14.synt** - Gestor de notas

## Cómo Funciona

El traductor utiliza expresiones regulares para identificar y reemplazar palabras clave españolas con sus equivalentes en inglés. El proceso es:

1. **Lectura**: Lee el archivo `.synt` línea por línea
2. **Análisis**: Identifica palabras clave españolas usando límites de palabra
3. **Traducción**: Reemplaza cada palabra clave con su equivalente en inglés
4. **Preservación**: Mantiene comentarios, espacios y estructura original
5. **Salida**: Genera código Python estándar ejecutable

## Estructura del Proyecto

```
espanol/
├── README.md              # Este archivo
├── translator.py          # Traductor principal
├── run_syntaxis.py        # Ejecutor de programas .synt
└── programas/             # Programas de ejemplo
    ├── 01_hola_mundo_maria_gonzalez_2024_07_15.synt
    ├── 02_calculadora_carlos_rodriguez_2024_08_03.synt
    └── ...
```

## Limitaciones

- Solo traduce palabras clave, no sintaxis completa
- No maneja traducciones de librerías personalizadas
- Las variables y nombres de funciones deben seguir las convenciones de Python
- No traduce strings literales (texto entre comillas)

## Contribuir

Para agregar nuevas palabras clave:

1. Abre `translator.py`
2. Agrega la nueva entrada al diccionario `keyword_map`
3. Prueba con un programa de ejemplo
4. Actualiza esta documentación

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Autor

Desarrollado para facilitar el aprendizaje de Python para hispanohablantes.

---

**Nota**: Este traductor es una herramienta educativa diseñada para ayudar a los programadores hispanohablantes a aprender Python usando su idioma nativo como puente hacia el inglés.