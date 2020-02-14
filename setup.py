from setuptools import setup, find_packages

setup(
    name='analyse_package',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/kopano-m/analyse-package.git',
    author='EDSA Group 6 (Analyase Sprint) Joburg Cohort 2020',
    author_email='<Your Email>'
)
