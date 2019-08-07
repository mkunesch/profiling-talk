import numpy as np

from profiling_demos.demo_1.image_utils import remove_edge, remove_edge_fast

mask = np.array(
    [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ],
    dtype=bool,
)

assert np.array_equal(remove_edge(mask), remove_edge_fast(mask))
print("Test passed.")
