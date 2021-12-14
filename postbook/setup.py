from setuptools import setup, find_packages

setup(
    name='plogger',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'my_start=my_package.start:main',
        ]
    }
)