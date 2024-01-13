"""
    using Enum class present in enum module
"""

from enum import Enum


""" we have to create a class """
class Constants(Enum):
    PI = 3.14159

# we have to access it like this
print('Constants.PI.value --> ',Constants.PI.value)