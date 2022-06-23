#!/usr/bin/env python
""" Setup the py-pip-install-test package """

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = ["pytest==7.1.1"]

test_requirements = [
    "pandas",
    "matplotlib",
    "pdal"
    "sql",
    "pytest",
]

setup(
    author="Rafaa",
    email="rafaesam0@gmail.com",
    python_requires=">=3.6",
    description ="AgriTech_USGS_LIDAR",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='agritech, pytest, lidar',
    name="USGS_LIDAR",
    packages=find_packages(include=['scripts', 'scripts.*']),
    test_suite="tests",
    tests_requires=test_requirements,
    url="https://github.com/rafaesam/AgriTech-USGS-LIDAR",
    zip_safe=False,
)
