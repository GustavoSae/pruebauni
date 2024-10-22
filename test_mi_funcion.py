# test_resta.py

from resta import resta

def test_resta():
    # Afirmaciones de igualdad
    assert resta(10, 5) == 5
    assert resta(5, 10) == -5
    assert resta(0, 0) == 0
    assert resta(-1, -1) == 0
    assert resta(-5, 5) == -10
    assert resta(2.5, 1.5) == 1.0

    # Afirmaciones de desigualdad
    assert resta(10, 5) != 6
    assert resta(5, 10) != 5

    # Afirmaciones de verdad y falso
    assert (resta(1, 1) == 0)  # Verdadero
    assert not (resta(1, 1) == 1)  # Falso

    # Afirmaciones nulas y no nulas
    assert resta(0, 0) is not None  # No nulo
    # Elimina o modifica la siguiente línea
