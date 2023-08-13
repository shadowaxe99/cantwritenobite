from setuptools import setup, find_packages

setup(
    name='cantwritenobite',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # add your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'cantwritenobite = src.main:main',
        ],
    },
)