from setuptools import setup, find_packages

setup(
    name='redactor',
    version='1.0.0',
    author='Rushit Varma Gadiraju',
    author_email='vgadiraju@ufl.edu',
    description='A text redaction tool for sensitive information',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cis6930fa24-project1',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'spacy==3.1.4',
        'pytest',
    ],
    dependency_links=[
        'https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.1.0/en_core_web_md-3.1.0-py3-none-any.whl'
    ]
)
