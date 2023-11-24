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


testing = bool({"pytest", "test"}.intersection(sys.argv))

setup(
    name="tt-time-tracker",
    version="1.0.10",
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
    install_requires=["colorama", "pyyaml", 'tzlocal==2.1', 'pytz', 'mock', 'lark-parser'],
    setup_requires=["pytest-runner"] if testing else [],
    tests_require=["pytest", "cram", "pytest-cram"],
    extras_require={
        "docs": ["ghp-import", "pygreen"],
    },
    python_requires='>=3.6'
)
