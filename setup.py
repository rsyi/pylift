from setuptools import find_packages, setup

# Read the contents of README file.
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pylift',
      version='0.1.3',
      description='Python implementation of uplift modeling.',
      author='Robert Yi, Will Frost',
      author_email='robert@ryi.me',
      url='https://github.com/pylift/pylift',
      install_requires=[
            'numpy',
            'matplotlib',
            'scikit-learn',
            'scipy',
            'scikit-optimize',
            'xgboost'
          ],
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(),
      zip_safe=False)
