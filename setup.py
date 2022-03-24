from setuptools import setup, find_packages

setup(
    name='pre_commit_dummy_package',
    version='0.0.0',
    install_requires=['openapi-spec-validator==0.4.0'],
    scripts=['bin/check-many-openapi'],
)
