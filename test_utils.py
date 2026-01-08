import pytest
from utils import calculate_average


def test_calculate_average_basic():
    """Test avec des valeurs basiques"""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0


def test_calculate_average_single_value():
    """Test avec une seule valeur"""
    assert calculate_average([5]) == 5.0


def test_calculate_average_empty_list():
    """Test avec une liste vide"""
    assert calculate_average([]) == 0


def test_calculate_average_negative_values():
    """Test avec des valeurs négatives"""
    assert calculate_average([-1, -2, -3]) == -2.0


def test_calculate_average_decimals():
    """Test avec des décimales"""
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5
