from distutils.core import setup
import os
  
setup(name = 'pycse',
      version='1.25.1',
      description='python computations in science and engineering',
      url='http://github.com/jkitchin/pycse',
      maintainer='John Kitchin',
      maintainer_email='jkitchin@andrew.cmu.edu',
      license='GPL',
      platforms=['linux'],
      packages=['pycse'],
      scripts=['pycse/publish.py'],
      long_description='''\
python computations in science and engineering
===============================================

This package provides some utilities to perform:
1. linear and nonlinear regression with confidence intervals
2. Solve some boundary value problems.

See http://jkitchin.github.io/pycse for documentation.

      ''')

# to push to pypi - python setup.py sdist upload
