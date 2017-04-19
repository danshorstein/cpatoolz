import os
from setuptools import setup

readme = os.path.join(os.path.dirname(__file__), 'README.md')
setup(
    name='simple_ledger',
    description='an accountants toolbox',
    version='0.0',
    packages=['simple_ledger'],
    license='The MIT License',
    author='Daniel Shorstein',
    author_email='dshorstein@gmail.com',
    url='https://github.com/danshorstein/simple_ledger',
    install_requires=['pandas'],
    entry_points=dict(
        console_scripts=[
            'cpatoolz = cpztoolz.cpztoolz:main',
        ],
    ),
)
