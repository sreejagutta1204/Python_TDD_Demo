
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

