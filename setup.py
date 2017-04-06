# I've never done this before - testing it out!!!

import os
from setuptools import setup

readme = os.path.join(os.path.dirname(__file__), 'README.md')
setup(
    name='cpatoolz',
    description='an accountants toolbox',
    version='0.0',
    packages=['cpatoolz'],
    license='The MIT License',
    author='Daniel Shorstein',
    author_email='dshorstein@gmail.com',
    url='https://github.com/danshorstein/cpatoolz',
    install_requires=['pandas'],
    entry_points=dict(
        console_scripts=[
            'bottomline = bottomline.bottomline:main',
        ],
    ),
)
