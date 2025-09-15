
"""
Core math utilities for TDD practice.

All functions use basic `float` types only.
"""

from typing import List


def add(num1: float, num2: float) -> float:
    return num1+num2


def safe_divide(num1: float, num2: float) -> float:
    
    if(num2 == 0):
        raise ValueError("denominator must not be zero")
    return num1/num2

def average(xs: List[float]) -> float:
    
    if(xs == []):
        raise ValueError("xs must not be empty")
    return(sum(xs)/len(xs))

def sqrt_approx(x: float, tolerance: float = 1e-7) -> float:
    """Approximate square root using Newton's method."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")

    guess = x / 2 if x > 1 else 1.0
    while abs(guess * guess - x) > tolerance:
        guess = (guess + x / guess) / 2
    return guess
