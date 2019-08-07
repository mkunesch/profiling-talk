import time

import click
import numpy as np


def work(amount):
    """Work on calculations for a specified amount of time.

    Parameters
    ----------
    amount: int
        The time in seconds to work.

    Returns
    -------
    None
    """
    start_time = time.time()
    while time.time() - start_time < amount:
        large_vector1 = np.random.uniform(size=5000)
        large_vector2 = np.random.uniform(size=5000)
        product = np.dot(large_vector1, large_vector2)

        # Uncomment the following line for code that uses more sys time.
        # outer_product = np.outer(large_vector1, large_vector2)


def sleep_and_work(sleep_amount, work_amount):
    """Let the CPU sleep then work.

    Parameters
    ----------
    sleep_amount: int
        The amount of time (in seconds) the CPU should sleep.
    work: int
        The amount of time (in seconds) the CPU should work.

    Returns
    -------
    None
    """
    time.sleep(sleep_amount)
    work(work_amount)


@click.command()
@click.option("--sleep", default=3, type=int)
@click.option("--work", default=3, type=int)
def main(sleep, work):
    sleep_and_work(sleep, work)


if __name__ == "__main__":
    main()
