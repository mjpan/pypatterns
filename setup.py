from setuptools import setup, find_packages

setup(
    name='pypatterns',
    version='0.1',
    packages=find_packages(
        'src',exclude=["*.test", "*.test.*", "test.*", "test"]),
    package_dir={'':'src'}
)
