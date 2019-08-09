# Profiling talk
This repository contains the material ([slides](slides.pdf), demo code, [bash
commands](bash_commands.md)) for a public profiling talk I gave as part of the
tech talk series at [Faculty](https://faculty.ai).

## Tools covered in this talk
This talk covered the profiling tools

* [cProfile](https://docs.python.org/2/library/profile.html#module-cProfile)
* [pyflame](https://github.com/uber/pyflame) (really good with threading,
  only for Linux unfortunately)
* [line_profiler](https://github.com/rkern/line_profiler)
* [memory_profiler](https://github.com/pythonprofilers/memory_profiler)

and the following tools for visualising the profiles

* [gprof2dot](https://github.com/jrfonseca/gprof2dot)
* [snakeviz](https://jiffyclub.github.io/snakeviz/)
* [FlameGraph](https://github.com/brendangregg/FlameGraph)


## Installation instructions
To install the code for the demos and all its dependencies run

```
pip install .
```

In addition, you need to install `pyflame` and the visualisation tools
`FlameGraph` and `gprof2dot` to follow the commands I used in the demos.

## Feedback and contributing
Comments, corrections, and issue reports are very welcome!
