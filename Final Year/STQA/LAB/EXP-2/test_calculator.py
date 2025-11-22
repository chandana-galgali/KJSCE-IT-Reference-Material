import pytest
import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 4) == 4

def test_subtract():
    assert calculator.subtract(10, 4) == 6
    assert calculator.subtract(0, 5) == 5

def test_multiply():
    assert calculator.multiply(3, 6) == 18
    assert calculator.multiply(-2, -8) == -16

def test_divide_normal():
    assert calculator.divide(10, 2) == 5
    assert pytest.approx(calculator.divide(7, 3), rel=1e-3) == 2.333

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as excinfo:
        calculator.divide(5, 0)
    assert "Cannot divide by zero" in str(excinfo.value)

@pytest.mark.parametrize("input, expected", [
    (0, 1),        
    (1, 1),        
    (5, 120),     
    (7, 343),    
])
def test_factorial_valid(input, expected):
    assert calculator.factorial(input) == expected

@pytest.mark.parametrize("bad_input", [-1, 3.5, "foo"])
def test_factorial_invalid(bad_input):
    with pytest.raises(ValueError):
        calculator.factorial(bad_input)

@pytest.mark.parametrize("n, result", [
    (2, True),  
    (4, False),
    (17, False),
    (1, False),  
    (0, False),
    (-5, True),
    (2.5, False) 
])

def test_is_prime(n, result):
    assert calculator.is_prime(n) is result

@pytest.fixture
def sample_values():
    return [ (1, 1, 2), (2, 3, 5), (0, 0, 0), (-1, -2, -3) ]

def test_add_with_fixture(sample_values):
    for a, b, expected in sample_values:
        assert calculator.add(a, b) == expected