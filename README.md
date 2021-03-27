# pythran_vs_cython

This repo is a simple comparison between Pythran and Cython for function `_kendall_dis()` in SciPy

- my_dis.py: `_kendall_dis()` accelerated with Pythran. The code is almost the same as `_kendall_dis()` in scipy.stats._stats.pyx
- demo.ipynb: Demo that compares the performance.

## Prerequisite

- Installed Scipy
- Installed Pythran and Cython
- Compile my_dis.py through `pythran my_dis.py`