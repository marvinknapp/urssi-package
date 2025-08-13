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
