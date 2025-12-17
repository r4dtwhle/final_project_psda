"""
Recursive Algorithms Implementation
"""


def factorial(n):
    """Calculate factorial recursively"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Calculate fibonacci recursively"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_points(drivers, index=0):
    """Calculate total points recursively"""
    if index >= len(drivers):
        return 0
    return drivers[index]["points"] + sum_points(drivers, index + 1)


def get_recursion_tree_visual():
    """Return ASCII visualization of recursion tree"""
    return """fibonacci(5)
├── fibonacci(4)
│   ├── fibonacci(3)
│   │   ├── fibonacci(2)
│   │   │   ├── fibonacci(1) → 1
│   │   │   └── fibonacci(0) → 0
│   │   └── fibonacci(1) → 1
│   └── fibonacci(2)
│       ├── fibonacci(1) → 1
│       └── fibonacci(0) → 0
└── fibonacci(3)
    ├── fibonacci(2)
    │   ├── fibonacci(1) → 1
    │   └── fibonacci(0) → 0
    └── fibonacci(1) → 1

Result: 5"""