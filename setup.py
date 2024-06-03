# -*- coding: utf-8 -*-


import sys

from setuptools import setup
from os import path


VERSION = '0.0.12'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

# Dirty hack to differentiate hosts in 22.04 & 24.04
ipython_max_version = '8.0' if sys.version_info < (3, 12) else '8.20'

setup(
    name='pylane',
    version=VERSION,
    author='valensc, Wu Xiao',
    author_email='weidong1312@gmail.com, notgiven@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NtesEyes/pylane',
    download_url='https://github.com/NtesEyes/pylane/archive/0.0.2.tar.gz',
    packages=[
        'pylane',
        'pylane.core',
        'pylane.shell',
    ],
    entry_points="""
          [console_scripts]
          pylane = pylane.entry:main
      """,
    # cmdclass={
        # 'build_py': build_py
    # },
    install_requires=[
        'ipython==5.8;python_version<"3.4"',
        f'ipython>=7.2,<={ipython_max_version};python_version>="3.4"',
        "Click==7.0",
    ],
    keywords=['debug', 'attach', 'gdb', 'shell']
)
