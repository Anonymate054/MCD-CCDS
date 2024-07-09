from setuptools import setup, find_packages

setup(
    name='main_modules',
    version='0.1',
    packages=find_packages(include=['scripts']),
    install_requires=[
        'fs'
    ],
    include_package_data=True,
)