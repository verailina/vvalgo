from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup_params = dict(
    name="vvalgo",
    version="1.0.0",
    description="CS algorithms",
    long_description="Implementations of basic computer science algorithms",
    url="https://github.com/vvegorova/vvalgo",
    author="Vera Ilina",
    author_email="vvegorova@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Algorithms",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="algorithms",
    package_dir={"": "src"},
    packages=find_packages("src"),
    # python_requires=[],
    install_requires=[],  # Optional
    extras_require={
        "test": ["pytest"],
    }
)

if __name__ == "__main__":
    setup(**setup_params)
