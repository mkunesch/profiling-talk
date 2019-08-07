import time
from threading import Thread

import click
from profiling_demos.demo_0.demo_0 import work


def sleep_and_work_threaded(sleep_amount, work_amount):
    """Let the CPU sleep and work concurrently.

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
    t1 = Thread(target=time.sleep, args=(sleep_amount,))
    t2 = Thread(target=work, args=(work_amount,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


@click.command()
@click.option("--sleep", default=3, type=int)
@click.option("--work", default=3, type=int)
def main(sleep, work):
    sleep_and_work_threaded(sleep, work)


if __name__ == "__main__":
    main()
