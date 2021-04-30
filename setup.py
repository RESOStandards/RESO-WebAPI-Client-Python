import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='reso-api',
    version='0.1',
    description='SDK which provides easy OpenID authentication and authorization.'
                'Also executes needed API requests with possibility to store response in a file',
    url='https://github.com/RESOStandards/RESO-WebAPI-Client-Python',
    author='RESO',
    author_email='justinask7@gmail.com',
    license='MIT',
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=[
        'bs4==0.0.1',
        'urllib3==1.25.8',
        'requests==2.22.0',
    ],
)
