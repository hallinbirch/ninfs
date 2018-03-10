#!/usr/bin/env python3

import sys

from setuptools import setup

if sys.hexversion < 0x030502f0:
    sys.exit('Python 3.5.2+ is required.')

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

install_requires = ['pycryptodomex']
# this should be removed once windows support is in the original fusepy.
if sys.platform not in {'win32', 'cygwin'}:
    install_requires.append('fusepy')

setup(
    name='fuse-3ds',
    version='0.1.dev0',
    packages=['fuse3ds', 'fuse3ds.pyctr', 'fuse3ds.mount'],
    url='https://github.com/ihaveamac/fuse-3ds',
    license='MIT',
    author='Ian Burgwin',
    author_email='',
    description='FUSE Filesystem Python scripts for Nintendo 3DS files',
    long_description=readme,
    classifiers=[
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=install_requires,
    entry_points={'console_scripts': ['mount_cci = fuse3ds.mount.cci:main',
                                      'mount_cdn = fuse3ds.mount.cdn:main',
                                      'mount_cia = fuse3ds.mount.cia:main',
                                      'mount_nand = fuse3ds.mount.nand:main',
                                      'mount_ncch = fuse3ds.mount.ncch:main',
                                      'mount_romfs = fuse3ds.mount.romfs:main',
                                      'mount_sd = fuse3ds.mount.sd:main']}
)
