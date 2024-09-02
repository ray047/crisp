# setup.py

from setuptools import setup, find_packages

setup(
    name='crispsim',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'crispsim=main:main',
        ],
    },
)
