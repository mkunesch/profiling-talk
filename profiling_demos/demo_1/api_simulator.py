import random
import time

import numpy as np


def setup_api(setup_time=5):
    """Simulates some start-up/setup time of the API.

    Only needs to be done once to get the API running.
    """
    time.sleep(setup_time)


def get_api_prediction(image, prediction_time=0.1):
    """Simulates an API that returns a mask for an image.

    The API takes some wallclock time (but no CPU time) to process the image
    and provide the mask. This simulator just sleeps for a specified amount of
    time and then returns a random mask.
    """
    time.sleep(prediction_time)

    # The model this API simulates isn't great: it just puts a random
    # rectangular mask somewhere.
    mask = np.full((image.shape[0], image.shape[1]), False)
    num_rows = random.randint(0, mask.shape[0] // 5)
    num_cols = random.randint(0, mask.shape[1] // 5)
    row = np.random.randint(num_rows, mask.shape[0] - num_rows)
    col = np.random.randint(num_cols, mask.shape[1] - num_cols)

    mask[
        row - num_rows // 2 : row + num_rows // 2,
        col - num_cols // 2 : col + num_cols // 2,
    ] = True

    return mask
