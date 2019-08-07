import click

import profiling_demos.demo_1.api_simulator
from profiling_demos.demo_1.image_utils import (
    get_masked_fraction,
    remove_edge,
    remove_edge_fast,
)
from profiling_demos.demo_1.video_utils import split_video


def classify_frame(frame):
    mask = api_simulator.get_api_prediction(frame)
    mask = remove_edge(mask)

    return get_masked_fraction(mask)


def classify_video(video, threshold=0.2):
    api_simulator.setup_api()
    frames = split_video(video)

    mean_masked_fraction = 0
    for frame in frames:
        mean_masked_fraction += classify_frame(frame)

    return mean_masked_fraction > threshold


@click.command()
@click.argument("file_paths", nargs=-1, type=click.Path(exists=True))
@click.option("-t", "--threshold", type=float, default=0.3)
def main(file_paths, threshold):
    for video in file_paths:
        result = classify_video(video, threshold)
        print(f"Result on {video}: {result}.")


if __name__ == "__main__":
    main()
