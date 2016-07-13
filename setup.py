# I've never done this before - testing it out!!!

import os
from setuptools import setup

readme = os.path.join(os.path.dirname(__file__), 'README.md')
setup(
    name='bottomline',
    description='an accountants toolbox',
    long_description=read_md(readme) if os.path.exists(readme) else '',
    version='0.0',
    packages=['bottomline'],
    license='The MIT License',
    author='Daniel Shorstein',
    author_email='dshorstein@gmail.com',
    url='https://github.com/dtiz/bottomline',
    install_requires=['pandas'],
    entry_points=dict(
        console_scripts=[
            'bottomline = bottomline:main',
        ],
    ),
)
