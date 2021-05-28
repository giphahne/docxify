from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='docxify',
    version='0.1.1',
    description='docxify and dedocxify files for fun and profit',
    url='https://danhahne.com/projects/docxify',
    author='Dan Hahne',
    author_email='contact@danhahne.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=['base58', 'python-docx', 'argcomplete'],
    packages=['docxify'],
    entry_points={
        'console_scripts': [
            'docxify=docxify:docxify',
            'dedocxify=docxify:dedocxify',
        ],
    },
)
