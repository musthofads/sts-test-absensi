#!/usr/bin/env python

import os
from setuptools import setup, find_packages


here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here, 'README.rst'))
long_description = f.read().strip()
f.close()

requires = [
    'django',
    'djangorestframework',
    'djangorestframework_simplejwt',
    'django-cors-headers',
    'dj-database-url',
    'requests',
    'responses',
    'psycopg2',
    'whitenoise',
]
dev_requires = [
    'pytest',
]

setup(
    name='absensi',
    version='0.0.1',
    author='Musthofa DS',
    author_email='musthofads@gmail.com',
    url='',
    description='Aplikasi Absensi',
    packages=find_packages(),
    long_description=long_description,
    keywords='django project absensi',
    zip_safe=False,
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    tests_require=requires,
    test_suite='manage.main',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
