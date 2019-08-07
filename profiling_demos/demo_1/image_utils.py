import numpy as np
from scipy.ndimage.morphology import binary_erosion

from profiling_demos.demo_1.api_simulator import get_api_prediction


def remove_edge(mask):
    """Remove the edge of a masked region.

    The image border is left untouched.

    Parameters
    ----------
    mask: np.array(bool)
        Array of bools of masked pixels.

    Returns
    -------
    The mask with edges removed.
    """
    out = mask.copy()
    # This is very bad implementation - it represents one of the biggest
    # performance mistakes one can make with numpy
    for i in range(1, out.shape[0] - 1):
        for j in range(1, out.shape[1] - 1):
            out[i, j] = np.all(mask[i - 1 : i + 2, j - 1 : j + 2])

    return out


def remove_edge_fast(mask):
    """Remove the edge of a masked region.

    The image border is left untouched.

    Parameters
    ----------
    mask: np.array(bool)
        Array of bools of masked pixels.

    Returns
    -------
    The mask with edges removed.
    """
    # A faster implementation using scipy.binary_erosion
    # A huge improvement ... but can we do even better?
    is_interior = np.full(mask.shape, True)
    is_interior[[0, -1], :] = False  # Boundary must be left untouched
    is_interior[:, [0, -1]] = False
    erosion_structure = np.ones((3, 3))
    return binary_erosion(mask, mask=is_interior, structure=erosion_structure)


def get_masked_fraction(mask):
    """Calculate the fraction of pixels that are masked."""
    return np.count_nonzero(mask) / mask.size
