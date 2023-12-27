import math

# Constantes de Error
ERROR_ZERO = "El denominador no puede ser 0"
ERROR_NO_SUPPORTED = "Operacion no soportada"
ERROR_FORMAT = "No tiene el formato adecuado"
ERROR_ARGS = "Numero incorrecto de argumentos para crear Rational"


class Rational:
    def __init__(self, n, d=1):
        if d == 0:
            raise ValueError(ERROR_ZERO)
        
        g = abs(math.gcd(n, d)) 
        
        # esto es para que numer y denom sean enteros.
        self.numer = n // g # // significa división entera
        self.denom = d // g
    
    # Representacion en string del Rational
    def __str__(self):
        #print(f"***metodo str*** num: {self.numer} denom: {self.denom}")
        match (self.numer, self.denom):
            case (0, _):
                return "0"
            case (_, 1):
                return f"{self.numer}"
            case (_, _) if self.numer < 0 and self.denom < 0:
                return f"{abs(self.numer)}/{abs(self.denom)}"
            case (_, _) if self.numer < 0 or self.denom < 0:
                return f"-{abs(self.numer)}/{abs(self.denom)}"
            case (_, _):
                return f"{self.numer}/{self.denom}"
    
    # Representacion para el interprete, esta funcion debe retornar un string
    def __repr__(self): 
        match (self.numer, self.denom):
            case (0, _):
                return "Rational(0)"
            case (_, 1):
                return f"Rational({self.numer})"
            case (_, _) if self.numer < 0 and self.denom < 0:
                return f"Rational({abs(self.numer)}, {abs(self.denom)})"
            case (_, _) if self.numer < 0 or self.denom < 0:
                return f"Rational(-{abs(self.numer)}, {abs(self.denom)})"
            case (_, _):
                return f"Rational({self.numer}, {self.denom})"
    

    # Suma
    def __add__(self, other):
        match other:
            case Rational(): 
                # Rational() significa que es una instancia de la clase Rational
                return Rational(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)
            case int():
                return Rational(self.numer + other * self.denom, self.denom)
            case _:
                raise TypeError(ERROR_NO_SUPPORTED)
    
    # Suma con el operador +
    def __radd__(self, other):
        # este es el caso de que el operador + este a la izquierda del Rational, ejemplo 2 + r1
        return self + other 
    
    # Resta
    def __sub__(self, other):
        match other:
            case Rational():
                # se usa el operador + sobrecargado para sumar el negativo de other
                return self + (-other) 
            case int():
                return self + (-other)
            case _:
                raise TypeError(ERROR_NO_SUPPORTED)

    # Resta con el operador -
    def __rsub__(self, other): 
        return -(self - other)
    
    # Multiplicación
    def __mul__(self, other): 
        match other:
            case Rational():
                return Rational(self.numer * other.numer, self.denom * other.denom)
            case int():
                return Rational(self.numer * other, self.denom)
            case _:
                raise TypeError(ERROR_NO_SUPPORTED)
    
    # Multiplicación con el operador *
    def __rmul__(self, other): 
        return self * other
    

    # División
    def __truediv__(self, other):
        match other:
            case Rational() if other.numer != 0:
                return Rational(self.numer * other.denom, self.denom * other.numer)
            case int() if other != 0:
                return Rational(self.numer, self.denom * other)
            case int() if other == 0:
                raise ValueError(ERROR_ZERO)
            case _:
                raise TypeError(ERROR_NO_SUPPORTED)
            
    # División con el operador /
    def __rtruediv__(self, other): # other es el numerador
        return Rational(self.denom * other, self.numer) # se usa el operador / sobrecargado para dividir el racional por other, ejemplo 2 / r1
    
    # Negación (-)
    def __neg__(self): 
        return Rational(-self.numer, self.denom)
    
    # Inverso (~)
    def __invert__(self): 
        return Rational(self.denom, self.numer)
    
    # Igualdad (==)
    def __eq__(self, other):
        match other:
            case Rational():
                return self.numer == other.numer and self.denom == other.denom
            case int():
                return self.denom == 1 and self.numer == other
            case _:
                return False

    # metodo de comparacion
    def compare(self, other):
        num = self.numer * other.denom
        den = self.denom * other.numer
        if num < den:
            return -1
        elif num > den:
            return 1
        else:
            return 0

    # Potencia (**)
    def __pow__(self, n): 
        if not isinstance(n, int):
            raise TypeError(ERROR_NO_SUPPORTED)
        match n:
            case 0:
                return Rational(1)
            case -1:
                return self.__invert__()
            case x if x > 0:
                return Rational(self.numer ** x, self.denom ** x)
            case x if x < 0 and self.numer != 0:
                return Rational(self.denom ** -x, self.numer ** -x)
            case _:
                raise ValueError(ERROR_ZERO)

    # Hash (para poder usar Rational como clave de un diccionario)
    def __hash__(self): 
        return hash((self.numer, self.denom))
    


#*********** Factoria de Racionales ********************

    @classmethod # este decorador indica que el metodo es un metodo de clase, no de instancia
    def apply(cls, *args):
        
        # funcion interna para manejar los argumentos de tipo int
        def handle_int_args(n):
            return cls(n)
            # cls es la clase que llama al metodo apply (Rational)

        # funcion interna para manejar los argumentos de tipo string
        def handle_string_args(s):
            if '/' in s:
                try:
                    numer, denom = map(int, s.split('/')) # aplico la funcion int a cada elemento de la lista que retorna split
                except ValueError:
                    raise ValueError(ERROR_FORMAT)
                parts = s.split('/')
                if len(parts) != 2:
                    raise ValueError(ERROR_FORMAT)
                # aplico la funcion int a cada elemento de parts
                numer, denom = map(int, parts) 
                if denom == 0:
                    raise ValueError(ERROR_ZERO)
                return cls(numer, denom)
            else:
                return cls(int(s))

        match args:
            case (int(),): # si args es una tupla de un solo elemento
                return handle_int_args(args[0])
            case (str(),):
                return handle_string_args(args[0]) 
            case (int(), int()):
                return cls(*args)
            case _:
                raise ValueError(ERROR_ARGS)