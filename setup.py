from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='podfox',
    version='0.1.1',
    description='Podcatcher for the terminal',
    url='http://github.com/brtmr/podfox',
    author='Bastian Reitemeier',
    author_email='mail@brtmr.de',
    license='GPLv3',
    packages=['podfox'],
    zip_safe=False,
    entry_points={
        'console_scripts' : [
            'podfox = podfox.__init__:main'
        ]
    },
    install_requires=[
        'colorama==0.4.6',
        'docopt==0.6.2',
        'feedparser==6.0.11',
        'requests==2.20.0',
        ],
    )
