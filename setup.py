"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import find_packages
from cx_Freeze import setup, Executable
# To use a consistent encoding
from codecs import open
from os import path

import sys


here = path.abspath(path.dirname(__file__))

parent_dir = path.abspath(path.join(here, 'src'))
sys.path.append(parent_dir)

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    version = f.read().strip()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().splitlines()

build_exe_options = {
    # "icon": r"assets/favicon/favicon.ico",
    "includes": [
        "config",
        "sqlalchemy.sql.default_comparator",
        "faker.providers",
        "jinja2.ext",
    ],
    "include_files": [
        "src/static",
        "src/templates",
        "db",
        "imports",
        "log",
    ],
    # "path": [
    #     path.dirname(__file__),
    # ],
}

base = None
setup(
    name='privatisation',
    version=version,
    keywords='archive database flask privatisation',
    description='Privatisation database for archive',
    long_description=long_description,
    url='https://github.com/d2emon/privatisation-py',
    executables = [Executable(
        "src/run_server.py",
        base=base,
        icon=r"src/assets/favicon/favicon.ico",
    )],

    # Author details
    author='Dmitry Kutsenko',
    author_email='d2emon@gmail.com',

    # Choose your license
    license='GPL-3.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    package_dir={'': 'src'},
    packages=find_packages('./src', exclude=['tests']),
    py_modules=[
        "app",
        "config",
    ],
    install_requires=requirements,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'server=app:run',
        ],
    },

    options = {
        "build_exe": build_exe_options,
    },
)
