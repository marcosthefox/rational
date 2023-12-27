from rational import Rational, ERROR_ZERO, ERROR_FORMAT, ERROR_ARGS, ERROR_NO_SUPPORTED
import pytest

# Constantes Rational
ZERO = Rational(0)
ONE = Rational(1)
R1 = Rational(3, 4)
R2 = Rational(1, 2)
R3 = Rational(3, 4)
R4 = Rational(0, 3)
R5 = Rational(5, 1)
R6 = Rational(2, -3)
R7 = Rational(-2, -3)
R8 = Rational(-2, 3)


class TestRational:

    def test_str_representation(self):
        assert str(R1) == "3/4"
        assert str(R2) == "1/2"
        assert str(R3) == "3/4"
        assert str(ZERO) == "0"
        assert str(ONE) == "1"
        assert str(R4) == "0"
        assert str(R5) == "5"
        assert str(R6) == "-2/3"
        assert str(R7) == "2/3"
        assert str(R8) == "-2/3"
        with pytest.raises(ValueError) as context:
            Rational(1, 0)
        assert str(context.value) == ERROR_ZERO
        

    def test_repr_representation(self):
        assert repr(R1) == "Rational(3, 4)"
        assert repr(R2) == "Rational(1, 2)"
        assert repr(R3) == "Rational(3, 4)"
        assert repr(ZERO) == "Rational(0)"
        assert repr(ONE) == "Rational(1)"
        assert repr(R4) == "Rational(0)"
        assert repr(R5) == "Rational(5)"
        assert repr(R6) == "Rational(-2, 3)"
        assert repr(R7) == "Rational(2, 3)"
        assert repr(R8) == "Rational(-2, 3)"
        with pytest.raises(ValueError) as context:
            Rational(1, 0)
        assert str(context.value) == ERROR_ZERO
        
    def test_addition(self):
        assert str(R1 + R2) == "5/4"
        assert str(R1 + 2) == "11/4" # suma con entero a la derecha
        assert str(2 + R1) == "11/4" # suma con entero a la izquierda
        with pytest.raises(TypeError) as context:
            R1 + "3" # sumo un string
        assert str(context.value) == ERROR_NO_SUPPORTED

    def test_subtraction(self):
        assert str(R1 - R2) == "1/4"
        assert str(R1 - R3) == "0"
        assert str(R1 - 2) == "-5/4" # resta con entero a la derecha
        assert str(2 - R1) == "5/4" # resta con entero a la izquierda
        with pytest.raises(TypeError) as context:
            R1 - "3"
        assert str(context.value) == ERROR_NO_SUPPORTED

    def test_multiplication(self):
        assert str(R1 * R2) == "3/8"
        assert str(R1 * R3) == "9/16"
        assert str(R1 * 2) == "3/2" # multiplicación con entero a la derecha
        assert str(2 * R1) == "3/2" # multiplicación con entero a la izquierda
        with pytest.raises(TypeError) as context:
            R1 * "3"
        assert str(context.value) == ERROR_NO_SUPPORTED

    def test_division(self):
        assert str(R1 / R2) == "3/2"
        assert str(R1 / R3) == "1"
        assert str(R1 / 2) == "3/8" # división con entero a la derecha
        assert str(2 / R1) == "8/3" # división con entero a la izquierda
        assert str(ZERO / R1) == "0"
        with pytest.raises(ValueError) as context:
            R1 / 0
        assert str(context.value) == ERROR_ZERO
        with pytest.raises(TypeError) as context:
            R1 / "3"
        assert str(context.value) == ERROR_NO_SUPPORTED

    def test_negation(self):
        assert str(-R1) == "-3/4"
        assert str(-R2) == "-1/2"
        assert str(-R3) == "-3/4"
        assert str(-ZERO) == "0"
        assert str(-ONE) == "-1"
        assert str(-R4) == "0"
        assert str(-R5) == "-5"
        assert str(-R6) == "2/3"
        assert str(-R7) == "-2/3"
        assert str(-R8) == "2/3"

    def test_inversion(self):
        assert str(~R1) == "4/3"
        assert str(~R2) == "2"
        assert str(~R3) == "4/3"
        assert str(~ONE) == "1"
        assert str(~R5) == "1/5"
        assert str(~R6) == "-3/2"
        assert str(~R7) == "3/2"
        assert str(~R8) == "-3/2"
        with pytest.raises(ValueError) as context:
            ~Rational(0, 3)
        assert str(context.value) == ERROR_ZERO

    def test_equality(self):
        assert R1 == R3
        assert R1 != R2
        assert R1 != 2

    def test_compare(self):
        assert ONE.compare(Rational(2,2)) == 0
        assert R1.compare(R2) == 1
        assert R2.compare(R1) == -1
        assert R1.compare(R3) == 0
    
    def test_power(self):
        assert str(R1 ** 3) == "27/64"
        assert str(R1 ** 0) == "1"
        assert str(R1 ** -1) == "4/3"
        assert str(R1 ** -2) == "16/9"
        assert str(R1 ** -3) == "64/27"
        with pytest.raises(ValueError) as context:
            Rational(0,2) ** -2
        assert str(context.value) == ERROR_ZERO

    def test_hasing(self):
        assert hash(R1) == hash(R3)
        assert hash(R1) != hash(R2)
        assert hash(R1) != hash(2)

    def test_rational_dict(self):
        d = {R1: "R1", 
            R2: "R2", 
            R4: "R4"}
        
        assert d[R1] == "R1"
        assert d[R2] == "R2"
        assert d[R4] == "R4"

    def test_rational_set(self):
        s = {R1, R2, R3}

        assert len(s) == 2
        assert R1 in s
        assert R2 in s
        assert R4 not in s


    # Test Factory methods
    def test_factory_apply(self):
        assert str(Rational.apply(3, 5)) == "3/5"
        assert str(Rational.apply("3/5")) == "3/5"
        assert str(Rational.apply(3)) == "3"
        assert str(Rational.apply("3")) == "3"
        assert str(Rational.apply(0, 3)) == "0"
        assert str(Rational.apply(5, 1)) == "5"
        assert str(Rational.apply(2, -3)) == "-2/3"
        assert str(Rational.apply(-2, -3)) == "2/3"
        assert str(Rational.apply(-2, 3)) == "-2/3"
        assert str(Rational.apply(4, 2)) == "2"

        # Error
        with pytest.raises(ValueError) as context:
            Rational.apply("1/0")
        assert str(context.value) == ERROR_ZERO
        with pytest.raises(ValueError) as context:
            Rational.apply("1/2/3")
        assert str(context.value) == ERROR_FORMAT
        with pytest.raises(ValueError) as context:
            Rational.apply("1//2")
        assert str(context.value) == ERROR_FORMAT
        with pytest.raises(ValueError) as context:
            Rational.apply("1/a")
        assert str(context.value) == ERROR_FORMAT
        with pytest.raises(ValueError) as context:
            Rational.apply("/2")
        assert str(context.value) == ERROR_FORMAT 

        # Error de argumentos
        with pytest.raises(ValueError) as context:
            Rational.apply(3, 5, 7)
        assert str(context.value) == ERROR_ARGS
        with pytest.raises(ValueError) as context:
            Rational.apply("3/5", 7)
        assert str(context.value) == ERROR_ARGS
        with pytest.raises(ValueError) as context:
            Rational.apply("3/5", "7/9")
        assert str(context.value) == ERROR_ARGS

    def test_zero_denominator_init(self):
        with pytest.raises(ValueError) as e:
            Rational(3, 0)
        assert str(e.value) == ERROR_ZERO

    def test_zero_denominator_division(self):
        rat = Rational(1, 3)
        with pytest.raises(ValueError) as e:
            rat / 0
        assert str(e.value) == ERROR_ZERO
