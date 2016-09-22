from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='django_video_frame',
    version='1.0',
    author='Vladimir Gosha',
    author_email='vladimir.gosha.mail@gmail.com',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'Django',
        'moviepy==0.2.2.11',
    ],
)
