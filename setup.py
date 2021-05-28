import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="landscapy",
    version="0.0.1",
    author="Jiří Podivín",
    author_email="jpodivin@gmail.com",
    description="Library of various test functions for benchmarking optimization algorithms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jpodivin/landscapy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy"
    ]
)
