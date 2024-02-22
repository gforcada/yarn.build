# -*- coding: utf-8 -*-
from setuptools import setup
from pathlib import Path


version = '1.0.1.dev0'
long_description = f"""
{Path('README.md').read_text()}

{Path('CHANGES.md').read_text()}
"""

setup(
    name='yarn.build',
    version=version,
    description='Build JS artifacts with yarn',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',  # noqa
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='yarn javascript compile build release zest.releaser',
    author='Gil Forcada Codinachs',
    author_email='gil.gnome@gmail.com',
    url='https://github.com/gforcada/yarn.build',
    license='GPL version 3',
    py_modules=['build', ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zest.releaser',
        'six',
    ],
    entry_points={
        'zest.releaser.releaser.after_checkout': [
            'yarn_build = build:build_project',
        ],
    },
)
