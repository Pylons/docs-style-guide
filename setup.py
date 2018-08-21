##############################################################################
#
# Copyright (c) 2018 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################
from setuptools import find_packages, setup

def readfile(name):
    with open(name) as f:
        return f.read()


README = readfile('README.rst')


install_requires = [
    'Sphinx >= 1.7.7',
    'docutils',
    'pylons-sphinx-themes',
]


setup(name='docs-style-guide',
      version='1.0',
      description='Documentation Style Guide for all projects under the '
                  'Pylons Project',
      long_description=README,
      classifiers=[
          "Development Status :: 6 - Mature",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Framework :: Sphinx",
          "Topic :: Documentation",
          "Topic :: Documentation :: Sphinx",
          "License :: Repoze Public License",
      ],
      keywords='Documentation, Pylons Project, Sphinx',
      author="Steve Piercy",
      author_email="pylons-discuss@googlegroups.com",
      url="https://pylonsproject.org",
      license="BSD-derived (http://repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
      install_requires=install_requires,
      )
