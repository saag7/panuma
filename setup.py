# setup.py

from setuptools import setup, find_packages

setup(
    name='panuma',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/saag7/panuma',
    license='MIT',
    author='saag7',
    author_email='salomon.agboto7@gmail.com',
    description='A convenience package for importing pandas, numpy, and matplotlib.pyplot',
    long_description=open('README.md').read() if open(
        'README.md').readable() else '',
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib'
    ]
)
