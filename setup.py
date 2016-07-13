# I've never done this before - testing it out!!!

import os
from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

readme = os.path.join(os.path.dirname(__file__), 'README.md')
setup(
    name='bottomline',
    description='an accountant\'s toolbox',
    long_description=read_md(readme) if os.path.exists(readme) else '',
    version='0.0',
    packages=['bottomline'],
    license='The MIT License',
    author='Daniel Shorstein',
    author_email='dshorstein@gmail.com',
    url='https://github.com/dtiz/bottomline',
    install_requires=[],
    entry_points=dict(
        console_scripts=[
            'bottomline = bottomline:main',
        ],
    ),
)
