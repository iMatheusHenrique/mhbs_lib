"""
This is the setup module for the mhbs_lib project.
It uses setuptools to package the project and manage dependencies.
"""

from setuptools import setup, find_packages

DESCRIPTION = "Python Template"

# Load requirements from the requirements.txt file
REQUIREMENTS_FILE_PATH = "requirements.txt"
with open(REQUIREMENTS_FILE_PATH, encoding='utf-8') as requirements_file:
    requires = [
        line.split("#", 1)[0].strip()
        for line in requirements_file
        if line.split("#", 1)[0].strip() and not line.startswith("--")
    ]

# Define the project name pattern
PROJECT_NAME_PATTERN = "mhbs_lib"

setup(
    name=PROJECT_NAME_PATTERN,
    version="0.1.0",
    author="Matheus Henrique Borges dos Santos",
    description=DESCRIPTION,
    packages=find_packages(
        where=PROJECT_NAME_PATTERN, exclude=["*tests"]
    ),
    install_requires=requires,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)
