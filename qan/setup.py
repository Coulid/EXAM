from distutils.core import setup
from Cython.Build import cythonize

setup(name  = "analyzer",
        ext_modules = cythonize("source/analyzer.py"))

