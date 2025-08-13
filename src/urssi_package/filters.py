from __future__ import annotations

from typing import TYPE_CHECKING
from skimage.filters import threshold_otsu

if TYPE_CHECKING:
    import numpy as np

def threshold_otsu_or_minimum(
    img: np.ndarray,
    min_value: int | float | None = None
) -> int | float:
    """Get Otsu's threshold or a minimum of an image

    Parameters
    ----------
    img : np.ndarray
        Image-like array to threshold
    min_value : Optional
        Minimum return value for the threshold

    Returns
    -------
    threshold : int | float
        Threshold value
    """
    threshold = threshold_otsu(img)
    if min_value is not None and min_value > threshold:
        threshold = min_value
    return threshold
