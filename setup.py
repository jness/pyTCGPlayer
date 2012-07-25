from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='TCGPlayer',
      version=version,
      description="A tool for getting MTG Sets and Cards from TCGPlayer",
      long_description="",
      classifiers=[],
      keywords='',
      author='Jeffrey Ness',
      author_email='jness@flip-edesign.com',
      url='',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['BeautifulSoup'],
      test_suite='nose.collector',
      )