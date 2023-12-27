# Clase Rational

## Descripción

Este archivo contiene la implementación de la clase `Rational`, que representa un número racional.

## Métodos disponibles

### `init`

Este es el constructor de la clase e inicializa un numero racional. 

- **Entrada:**
  - `n` (int): El numerador del número racional. Debe ser un entero.
  - `d` (int): El denominador del número racional. Debe ser un entero distinto de cero. Por defecto es 1.

- **Salida:**
  - No devuelve nada.

- **Errores:**
  - `ValueError`: Se lanza si `d` es 0, con el mensaje de error `ERROR_ZERO`.

### `str`

Este método devuelve una representación en string del número racional.

- **Entrada:**
  - self: numero al cual se quiere obtener una representacion string. Puede ser Rational o int.

- **Salida:**
  - Devuelve una cadena que representa el número racional en el formato "numerador/denominador".

- **Errores:**
  - No genera mensajes de error.

### `repr`

Este método devuelve una representación en string del número racional que puede ser utilizada por el intérprete de Python.

- **Entrada:**
  - self: numero al cual se quiere obtener una representacion string. Puede ser Rational o int.

- **Salida:**
  - Devuelve una cadena en el formato "Rational(numerador, denominador)".

- **Errores:**
  - No genera mensajes de error.


### `add (+)`

Este metodo implementa la suma de dos numeros racionales.
Tambien implementa la suma de un numero racional con un entero.

- **Entrada:**
  - self: numero al cual se le quiere aplicar la suma. Puede ser Rational o int.
  - other: numero que se quiere sumar. Puede ser Rational o int.

- **Salida:**
  - retorna un racional.

- **Errores:**
  - `TypeError` si se intenta sumar un tipo de dato no compatible.
  con el mensaje de error `ERROR_NO_SUPPORTED`.

```python
r1 = Rational(3, 4)
r2 = Rational(1, 2)
print("Suma:", r1 + r2) # Imprime 5/4
print("Suma con entero a la derecha:", r1 + 2) # Imprime 11/4
print("Suma con entero a la izquierda:", 2 + r1) # Imprime 11/4
```

### `sub (-)`

Este metodo implementa la diferencia de dos numeros racionales.
Tambien implementa la resta de un numero racional con un entero.

- **Entrada:**
  - self: numero al cual se le quiere aplicar la diferencia. Puede ser Rational o int.
  - other: numero que se quiere restar. Puede ser Rational o int.

- **Salida:**
  - retorna un racional.

- **Errores:**
  - `TypeError` si se intenta sumar un tipo de dato no compatible.
  con el mensaje de error `ERROR_NO_SUPPORTED`.

```python
r1 = Rational(3, 4)
r2 = Rational(1, 2)
print("Resta:", r1 - r2) # Imprime 1/4
print("Resta con entero a la derecha:", r1 - 2) # Imprime -5/4
print("Resta con entero a la izquierda:", 2 - r1) # Imprime 5/4
```

### `mul (*)`

Este metodo implementa el producto de dos numeros racionales.
Tambien implementa el producto de un numero racional con un entero.

- **Entrada:**
  - self: numero al cual se le quiere aplicar la multiplicacion. Puede ser Rational o int.
  - other: numero que se quiere multiplicar. Puede ser Rational o int.

- **Salida:**
  - retorna un racional.

- **Errores:**
  - `TypeError` si se intenta sumar un tipo de dato no compatible.
  con el mensaje de error `ERROR_NO_SUPPORTED`.

```python
r1 = Rational(3, 4)
r2 = Rational(1, 2)
print("Multiplicación:", r1 * r2) # Imprime 3/8
print("Multiplicación con entero a la derecha:", r1 * 2) # Imprime 3/2
print("Multiplicación con entero a la izquierda:", 2 * r1) # Imprime 3/2
```

### `truediv (/)`

Este metodo implementa la division de dos numeros racionales.
Tambien implementa la division de un numero racional con un entero.

- **Entrada:**
  - self: numero al cual se le quiere aplicar la division. Puede ser Rational o int.
  - other: numero que se quiere dividir. Puede ser Rational o int.

- **Salida:**
  - retorna un racional.

- **Errores:**
  - `TypeError` si se intenta dividir por un tipo de dato no compatible, con el mensaje de error `ERROR_NO_SUPPORTED`. 
  - `ValueError` si se intenta dividir por cero, con el mensaje de error `ERROR_ZERO`.

```python
r1 = Rational(3, 4)
r2 = Rational(1, 2)
print("División:", r1 / r2) # Imprime 3/2
print("División con entero a la derecha:", r1 / 2) # Imprime 3/8
print("División con entero a la izquierda:", 2 / r1) # Imprime 8/3
```

### `neg (-)`

Este metodo implementa la negacion de un racional.

- **Entrada:**
  - self: numero que se quiere negar. Puede ser Rational o int.

- **Salida:**
  - retorna un objeto de la clase Rational.

- **Errores:**
  - No genera mensajes de error. 

```python
r1 = Rational(3, 4)
print("Negación:", -r1) # Imprime -3/4
```

### `invert (~)`

Este metodo implementa el inverso de un racional.

- **Entrada:**
  - self: numero que se quiere invertir. Puede ser Rational o int.

- **Salida:**
  - retorna un objeto de la clase Rational.

- **Errores:**
  - No genera mensajes de error. 

```python
r1 = Rational(3, 4)
print("Inverso:", ~r1) # Imprime 4/3
```

### `eq (==)`

Este metodo sirve para comparar dos objetos de la clase Rational.

- **Entrada:**
  - self: numero al cual se quiere comparar. Puede ser Rational o int.
  - other: otro numero a comparar. Puede ser Rational o int.

- **Salida:**
  - `True`: si los racionales son iguales.
  - `False`: si los racionales son distintos.

- **Errores:**
  - No genera mensajes de error. 

```python
r1 = Rational(3, 4)
r2 = Rational(1, 2)
print("Igualdad:", r1 == r2) # Imprime False
print("Igualdad con entero a la derecha:", r1 == 3) # Imprime False
print("Igualdad con entero a la izquierda:", 3 == r1) # Imprime False
```

### `compare`

Este metodo sirve para comparar dos objetos de la clase Rational.

- **Entrada:**
  - self: numero al cual se quiere comparar. Puede ser Rational o int.
  - other: otro numero a comparar. Puede ser Rational o int.

- **Salida:**
  - `-1`: si el self < other
  - `0`: si self = other.
  - `1`: si el self > other.

- **Errores:**
  - No genera mensajes de error. 

```python
print("Comparación:", Rational(1,4).compare(Rational(1,2))) # Imprime -1
print("Comparación:", Rational(1).compare(Rational(2,2))) # Imprime 0
print("Comparación:", Rational(3,4).compare(Rational(1,2))) # Imprime 1
```

### `pow (**)`

Devuelve la potencia enésima de un racional.

- **Entrada:**
  - self: numero que se quiere potenciar. Puede ser Rational o int.
  - n (int): potencia.

- **Salida:**
  - retorna un Rational.

- **Errores:**
  - `ValueError` si se intenta elevar 0 a una potencia negativa, con el mensaje de error ERROR_ZERO.

```python
r1 = Rational(3, 4)
print("Potencia:", r1 ** -1) # Imprime 4/3
print("Potencia:", r1 ** 0) # Imprime 1
```

### `hash`

Calcula un código hash para el racional.
Este metodo sirve para poder usar un objeto de la clase Rational como clave de un diccionario de Python.
Si dos numero son iguales deben retornar el mismo numero entero.

- **Entrada:**
  - self: numero al que se quiere calcular el hash. Puede ser Rational o int.

- **Salida:**
  - retorna un entero.

- **Errores:**
  - No genera mensajes de error.

```python
r1 = Rational(3, 4)
r2 = Rational(1, 2)
print("Hash r1:", hash(r1)) # Imprime 1079245023883434373
print("Hash r2:", hash(r2)) # Imprime -3550055125485641917
```

## Instanciación
Para crear un objeto `Rational`, puedes utilizar diferentes métodos de factoría:

## Métodos de Factoría

### `Método apply`

Este metodo sirve para crear un objeto de la clase Rational.
Puede recibir un numero variable de argumentos y los almacena en una tupla.
Crea un Rational a partir de una cadena que representa un número racional en el formato "a/b" o "a".
Crea un Rational a partir de un número entero.

- **Entrada:**
  - cls: es la clase que llama al metodo apply (Rational)
  - *args: tupla de argumentos. Puede ser un entero, dos enteros o un String con dos numeros separados por `/`.

- **Salida:**
  - retorna un objeto de la clase Rational.

- **Errores:**
  - `ValueError` si la cadena no tiene los elementos adecuados, con el mensaje de error `ERROR_FORMAT`. 
  - `ValueError` si la cadena no tiene el formato adecuado, con el mensaje `ERROR_FORMAT`.
  - `ValueError` si el denominador es cero, con el mensaje `ERROR_ZERO`.
  - `ValueError` si se proporciona un número incorrecto de argumentos, con el mensaje `ERROR_ARGS`.  

```python
print(Rational.apply("4/2")) # Imprime 2
print(Rational.apply(4, 2)) # Imprime 2
print(Rational.apply(10)) # Imprime 10
Rational.apply(3, 5)       # Crea un número racional 3/5
```

## Uso

Para crear un número racional, simplemente instancie la clase `Rational` con el numerador y el denominador como argumentos. Por ejemplo:

```python
r = Rational(6, 8)
print(r)  # Imprime: "3/4"
```

Para obtener la representación del intérprete de un número racional, utilice la función `repr()`. Por ejemplo:

```python
r = Rational(6, 8)
print(repr(r))  # Imprime: "Rational(3, 4)"
```

## Mensajes de error

- **ERROR_ZERO:** "El denominador no puede ser 0"
- **ERROR_NO_SUPPORTED:** "Operacion no soportada"
- **ERROR_FORMAT:** "No tiene el formato adecuado"
- **ERROR_ARGS:** "Numero incorrecto de argumentos para crear Rational"

## Requerimientos de ejecucion.

Los requerimientos para ejecutar el proyecto se encuentran en el archivo [requirements](./requirements.txt).

## Casos de prueba

Las pruebas unitarias fueron escritas sobre el framework Pytest de Python.
Para ejecutar los test:
```python
pytest
```