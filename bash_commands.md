# Demo bash commands
This file contains the bash commands that we used during the talk, together
with some explanations.

## Demo 0
The first part of demo 0 is a quick demonstration of what profiling is.
In the folder `profiling_demos/demo_0`, we create a profile using
`cProfile`:

```
python -m cProfile -o profile demo_0.py --sleep 2 --work 3
```

and visualise the profile e.g. using `gprof2dot`

```
gprof2dot -f pstats profile | dot -Tpng -Gdpi=200 -o profile.png
```

This produces a png image with a very helpful graph view of the profile.

The second part of demo 0 demonstrates other simple tools that can be
used for timing and profiling:


```
# Timing of whole program
time python demo_0.py --sleep 2 --work 3

# Line-by-line timing of work function
# (note: this requires @profile decorator before work function)
# Run line_profiler (creates file demo_0.py.lprof)
kernprof -l demo_0.py
# Display output
python -m line_profiler demo_0.py.lprof
```

The remainder of the demo uses the notebook `demo_0.ipynb`.


## Demo 1
In the folder `profiling_demos/demo_1` there is a mock-up of a video
classification code that splits up the video into frames, calls an API to create
a mask for each frame, and then does some trivial post-processing to that mask.

Pretending that the code is very long and complicated, we profile the code
without reading it first (we'll use the profile to show us where to start
reading).  Since it takes ages to run, we attached `pyflame` to the running
process

```
# Run the video classifier in the background
# Here VIDEO_NAME.mp4 has to be replaced the path to some mp4 video.
python classify_videos.py VIDEO_NAME.mp4 &

# Now attach pyflame to the process and profile for 5 seconds
# PROCESS_ID has to be replaced by the ID (found using htop)
pyflame -p PROCESS_ID -s 5 > pyflame_profile
# Visualise using FlameGraph, (replace PATH_TO_FLAMEGRAPH as appropriate)
PATH_TO_FLAMEGRAPH/flamegraph.pl pyflame_profile > pyflame_profile.svg

# Remember to kill the execution again
kill PROCESS_ID
```

The profile immediately points us to the culprit: a terribly implemented
function (`remove_edge`) that loops over a 2D-numpy array. After fixing this
terrible implementation (e.g. by replacing it with `remove_edge_fast`), the
code is much faster and can be profiled directly with `pyflame` or `cProfile`:

```
pyflame -t python classify_videos.py VIDEO_NAME.mp4 > pyflame_profile1
PATH_TO_FLAMEGRAPH/flamegraph.pl pyflame_profile1 > pyflame_profile1.svg

python -m cProfile -o cprofile classify_videos.py VIDEO_NAME.mp4
gprof2dot -f pstats cprofile | dot -Tpng -Gdpi=200 cprofile.png
```

## Profiling with threading
In the folder `profiling_demos/demo_0` there is also a threaded version of the
work and sleep script. First let us look at what goes wrong with `cProfile`:

```
python -m cProfile -o profile_threaded demo_0_threaded.py --sleep 3 --work 3
gprof2dot -f pstats profile_threaded | dot -Tpng -o demo_0_threaded.png
```

Since `cProfile` clearly is not helpful in this case, let us use `pyflame`.
In addition to the standard mode, there is `-x` which only shows instructions
that hold the GIL
```
pyflame -x -t python demo_0_threaded.py --sleep 3 --work 3 > pyflame_gil_only
PATH_TO_FLAMEGRAPH/flamegraph.pl pyflame_gil_only > pyflame_gil_only.svg
```

and `--threads` which shows real time for each thread

```
pyflame --threads -t python demo_0_threaded.py --sleep 3 --work 3 > pyflame_threads
PATH_TO_FLAMEGRAPH/flamegraph.pl pyflame_threads > pyflame_threads.svg
```



