import numpy as np


def compute_statistics(data: np.ndarray) -> dict:
    """ Compute basic statistics of a numpy array.

    Args:
        data (np.ndarray): Input numpy array containing numerical data.

    Raises:
        ValueError: If the input is not a numpy ndarray.

    Returns:
        dict: A dictionary containing mean, median, standard deviation,
              minimum, and maximum of the input data.
    """
    if not isinstance(data, np.ndarray):
        raise ValueError("Input must be a numpy ndarray.")

    stats = {
        'mean': np.mean(data),
        'median': np.median(data),
        'std_dev': np.std(data),
        'min': np.min(data),
        'max': np.max(data)
    }
    
    return stats


def hypot(a ,b):
    return (a**2 + b**2)**0.5


def better_hypot(a: float, b: float) -> float:
    """ Compute the hypotenuse of a right triangle given sides a and b.

    Args:
        a (float): Length of one side of the triangle.
        b (float): Length of the other side of the triangle.

    Returns:
        float: Length of the hypotenuse.
    """
    assert a >= 0 and b >= 0, "Sides must be non-negative."
    return np.sqrt(a**2 + b**2)


def example_doctest_usage(a: int, b: int) -> int:
    """
    Example function to demonstrate doctest usage and simple arithmetic.
    Test with `python -m doctest src/urssi_package/example.py -v`

    Note: You need to use "Examples" **not** "Example" in the docstring for mkdocs to render it nicely.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The sum of a and b, or 42 if both are zero.

    Examples:
        >>> example_doctest_usage(2, 3)
        5
        >>> example_doctest_usage(0, 0)
        42
        >>> example_doctest_usage(-1, 1)
        0
    """
    if a == 0 and b == 0:
        return 42
    return a + b
