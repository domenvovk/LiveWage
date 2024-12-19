import sys
from cx_Freeze import setup, Executable


setup(
    name='Wage Counter Live',
    version='1.0',
    description='Does stuff noone needs.',
    executables=[Executable('main.py', base='gui')]
)