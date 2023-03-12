"""Setup file."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()


setup(
    name="ml-random-utils",
    version="0.1.0",
    license="MIT",
    description="Utilities I use in ML projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Machine Learning :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.10",
    author="Marco Podda",
    author_email="marco.podda@di.unipi.it",
    url="https://github.com/marcopodda/ml-utils",
    install_requires=[
        "numpy>=1.24.2",
        "pandas>=1.5.3",
        "scikit-learn>=1.2.2",
        "pytest>=7.2.2",
    ],
    packages=find_packages(),
)
