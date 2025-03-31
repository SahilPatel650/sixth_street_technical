from setuptools import setup, find_packages

setup(
    name="alpha_stock",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    author="Sahil Patel",
    description="A client for Alpha Vantage TIME_SERIES_DAILY",
    url="https://github.com/SahilPatel650/sixth_street_technical",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)