from setuptools import setup, find_packages

setup(
    name='touch-the-grass',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'anthropic',
        'beautifulsoup4',
        'PyExifTool==0.5.6',
        'tk==0.1.0',
    ],
    entry_points={
        'console_scripts': [
            'ttg=ttg:main',
        ],
    },
    author='Onuralp',
    #author_email='your.email@example.com',
    description='A tool to generate location & mood history and make suggestions based on it',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cx0/touch-the-grass',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
