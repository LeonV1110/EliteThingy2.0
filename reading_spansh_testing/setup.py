from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('F:\Elite shit\EliteThingy2.0\reading_spansh_testing\cythondatajsonconversion.pyx'))