#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from pathlib import Path

from Cython.Build import cythonize
from setuptools import Extension, find_packages, setup
from setuptools.command.build_ext import build_ext

with open("README.md") as readme_file:
    readme = readme_file.read()

test_requirements = [
    "codecov",
    "flake8",
    "black",
    "pytest",
    "pytest-cov",
    "pytest-raises",
]

setup_requirements = [
    "pytest-runner",
]

dev_requirements = [
    "bumpversion>=0.5.3",
    "coverage>=5.0a4",
    "Cython",
    "flake8>=3.7.7",
    "ipython>=7.5.0",
    "m2r>=0.2.1",
    "pytest>=4.3.0",
    "pytest-cov==2.6.1",
    "pytest-raises>=0.10",
    "pytest-runner>=4.4",
    "Sphinx>=2.0.0b1,<3",
    "sphinx_rtd_theme>=0.1.2",
    "tox>=3.5.2",
    "twine>=1.13.0",
    "wheel>=0.33.1",
]

interactive_requirements = [
    "altair",
    "jupyterlab",
    "matplotlib",
]

requirements = []

extra_requirements = {
    "test": test_requirements,
    "setup": setup_requirements,
    "dev": dev_requirements,
    "interactive": interactive_requirements,
    "all": [
        *requirements,
        *test_requirements,
        *setup_requirements,
        *dev_requirements,
        *interactive_requirements
    ]
}

saxon_c_extension = [Extension("saxon_c",
                               ["py_saxon_c/saxonc.pyx",
                                "saxon_c/SaxonProcessor.cpp",
                                "saxon_c/SaxonCGlue.c",
                                "saxon_c/SaxonCXPath.c",
                                "saxon_c/XdmValue.cpp",
                                "saxon_c/XdmItem.cpp",
                                "saxon_c/XdmNode.cpp",
                                "saxon_c/XdmAtomicValue.cpp",
                                "saxon_c/XsltProcessor.cpp",
                                "saxon_c/Xslt30Processor.cpp",
                                "saxon_c/XQueryProcessor.cpp",
                                "saxon_c/XPathProcessor.cpp",
                                "saxon_c/SchemaValidator.cpp"],
                               language="c++",
                               )
                     ]

setup(
    author="Jamie Sherman",
    author_email="jamies@alleninstitute.org",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Pip installable version of saxons python library",
    entry_points={
        "console_scripts": [
            "my_example=py_saxon_c.bin.my_example:main"
        ],
    },
    ext_modules=cythonize(saxon_c_extension,
                          cmdclass={'build_ext': build_ext},
                          include_dirs=['jni', "jni/unix"]),
    install_requires=requirements,
    license="BSD license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="py_saxon_c",
    name="py_saxon_c",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*"]),
    python_requires=">=3.6",
    setup_requires=setup_requirements,
    test_suite="py_saxon_c/tests",
    tests_require=test_requirements,
    extras_require=extra_requirements,
    url="https://github.com/AllenCellModeling/py_saxon_c",
    # Do not edit this string manually, always use bumpversion
    # Details in CONTRIBUTING.rst
    version="0.1.0",
    zip_safe=False,
)
