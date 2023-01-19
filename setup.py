from setuptools import setup
from setuptools import find_packages
import os

setup(
    name='hinge_high_speed',
    version='0.0.1',
    description='Code for analyzing high speed video of wing hinge during motion.',
    long_description=__doc__,
    author='Sam Whitehead',
    author_email='swhitehe@caltech',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],

    packages=find_packages(exclude=['examples', 'scratch']),
)
