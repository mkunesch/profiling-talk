from setuptools import setup, find_packages


setup(
    name="profiling_demos",
    description="Demo examples for a profiling talk.",
    author="Markus Kunesch",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "click",
        "opencv-python",
        "line_profiler",
        "memory_profiler",
    ],
)
