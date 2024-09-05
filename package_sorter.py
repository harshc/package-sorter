# File: package_sorter.py

from decimal import Decimal, getcontext

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort packages based on their dimensions and mass.
    
    Args:
    width (float): Width of the package in centimeters.
    height (float): Height of the package in centimeters.
    length (float): Length of the package in centimeters.
    mass (float): Mass of the package in kilograms.
    
    Returns:
    str: The name of the stack where the package should go.
    
    Raises:
    ValueError: If any input is negative or not a number.
    """
    # Input validation
    for param in [width, height, length, mass]:
        if not isinstance(param, (int, float)) or param < 0:
            raise ValueError("All inputs must be non-negative numbers.")
    
    # Set decimal precision
    getcontext().prec = 10
    
    # Convert all inputs to Decimal
    width, height, length, mass = map(lambda x: Decimal(str(x)), [width, height, length, mass])
    
    # Calculate volume
    volume = width * height * length
    
    # Check if the package is bulky
    is_bulky = volume >= Decimal('1000000') or width >= Decimal('150') or height >= Decimal('150') or length >= Decimal('150')
    
    # Check if the package is heavy
    is_heavy = mass >= Decimal('20')
    
    # Determine the appropriate stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"