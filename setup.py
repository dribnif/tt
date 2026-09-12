#!/usr/bin/env python
import io
import sys
from setuptools import find_packages, setup

def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

setup(
    name="tt-time-tracker",
    version="1.1.2", # Bumped version!
    author="Bogdan Maxim",
    author_email="bogdan.maxim@metamorphant.de",
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    url="https://github.com/dribnif/tt",
    description="A simple, precise command-line based time tracker",
    long_description=read("README.md", "CHANGES.md"),
    long_description_content_type='text/markdown',
    entry_points={
        "console_scripts": [
            "tt = tt.tt:main",
        ]
    },
    # tzlocal pinned strictly below 3.0 to prevent pytz compatibility breaks
    install_requires=[
        "colorama>=0.4.0",
        "pyyaml>=5.0",
        "tzlocal>=2.1,<3.0",
        "pytz"
    ],
    extras_require={
        "docs": ["ghp-import", "pygreen"],
        # Modern way to define test dependencies
        "test": ["pytest", "cram", "mock"]
    },
    python_requires='>=3.6'
)