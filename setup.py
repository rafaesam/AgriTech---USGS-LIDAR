""" Setup the py-pip-install-test package """

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

# requirement = pip install -r /path/to/requirements.txt  

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
    title ="AgriTech_USGS_LIDAR",
    python_version=">=3.6",
    install_requirement=requirements,
    description=readme,
    include_package_data=True,
    name="USGS_LIDAR",
    packages=find_packages(include=["src", "src.*"]),
    test_suite="Tests",
    tests=test_requirements,
    url="https://github.com/rafaesam/AgriTech-USGS-LIDAR",
    zip_safe=False,
)
