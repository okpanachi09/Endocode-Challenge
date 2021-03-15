from setuptools import setup, find_packages

requires = [
    'flask'
]

setup(
    name='flask_todo',
    version='0.1',
    description='A Simple python http server that serves as a realization of the endocode programming challenge',
    author='Abel Yakubu',
    # author_email='<Your actual e-mail address here>',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
