import pytest
from geometria import (
    area_rectangulo,
    area_circulo,
    area_triangulo,
    volumen_cilindro,
)

def test_area_rectangulo():
    assert area_rectangulo(4, 5) == 20

def test_area_triangulo():
    assert area_triangulo(10, 6) == 30
