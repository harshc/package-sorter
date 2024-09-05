# Package Sorter

## Description

Package Sorter is a Python application that sorts packages into different categories based on their dimensions and mass. It's designed to help logistics companies efficiently categorize packages for appropriate handling and shipping.

## Features

- Sorts packages into three categories: STANDARD, SPECIAL, and REJECTED
- Handles precise calculations using Python's Decimal class to avoid floating-point errors
- Includes a comprehensive test suite to ensure accuracy

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/harshc/package-sorter.git
   ```
2. Navigate to the project directory:
   ```
   cd package-sorter
   ```

## Usage

The main functionality is provided by the `sort` function in the `package_sorter.py` file. You can import and use this function in your Python code as follows:

```python
from package_sorter import sort

result = sort(width, height, length, mass)
print(result)  # Will print "STANDARD", "SPECIAL", or "REJECTED"
```

Where:

- `width`, `height`, and `length` are the dimensions of the package in centimeters
- `mass` is the weight of the package in kilograms

## Sorting Rules

- A package is considered **bulky** if:
  - Its volume (width x height x length) is greater than or equal to 1,000,000 cm³, OR
  - Any of its dimensions is greater than or equal to 150 cm
- A package is considered **heavy** if its mass is greater than or equal to 20 kg
- Sorting categories:
  - **STANDARD**: Neither bulky nor heavy
  - **SPECIAL**: Either bulky or heavy (but not both)
  - **REJECTED**: Both bulky and heavy

## Running Tests

To run the test suite:

```
python -m unittest test_package_sorter.py
```

## Contributing

Contributions to improve Package Sorter are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
