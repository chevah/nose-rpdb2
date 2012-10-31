from setuptools import setup

VERSION = '0.1.7'

setup(
    name='nose-rpdb2',
    version=VERSION,
    maintainer="Adi Roiban",
    maintainer_email="adi.roiban@chevah.com",
    license='BSD (3 clause) License',
    platforms='any',
    description='Nose plugin to use rpdb2 when tests fail.',
    long_description=open('README').read(),
    url='https://github.com/chevah/nose-rpdb2',
    install_requires=['nose', 'winpdb'],
    keywords = 'test unittest nose nosetests plugin debug winpdb rpdb2',
    py_modules = ['nose_plugin_rpdb2'],
    entry_points = {
        'nose.plugins.0.10': [
            'rpdb2 = nose_plugin_rpdb2:RPDB2Plugin'
        ]
    }
)
